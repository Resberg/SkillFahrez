"""Inspect video metadata, full decoding, audio levels, and an optional contact sheet."""
import argparse
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys


def run(command):
    return subprocess.run(command, capture_output=True, text=True, errors='replace')


def positive(value):
    result = float(value)
    if not math.isfinite(result) or result <= 0:
        raise argparse.ArgumentTypeError('Expected a positive finite number')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', type=Path)
    parser.add_argument('--expect-duration', type=positive)
    parser.add_argument('--tolerance', type=positive, default=0.25, help='Duration tolerance in seconds')
    parser.add_argument('--require-audio', action='store_true')
    parser.add_argument('--contact-sheet', type=Path, help='New .jpg or .png path; will not overwrite')
    args = parser.parse_args()
    if not args.video.is_file():
        parser.error(f'Input file does not exist: {args.video}')
    for tool in ['ffmpeg', 'ffprobe']:
        if not shutil.which(tool):
            parser.error(f'{tool} is not on PATH; install it separately.')
    video = args.video.resolve()
    if args.contact_sheet:
        sheet = args.contact_sheet.resolve()
        if sheet.exists() or sheet.is_symlink():
            parser.error('Contact-sheet output already exists; choose a new path.')
        if sheet.suffix.lower() not in ['.jpg', '.png']:
            parser.error('Contact-sheet output must end in .jpg or .png')
    probe = run(['ffprobe', '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(video)])
    if probe.returncode:
        print(probe.stderr, file=sys.stderr)
        return 1
    metadata = json.loads(probe.stdout)
    streams = metadata.get('streams', [])
    pictures = [s for s in streams if s.get('codec_type') == 'video' and not s.get('disposition', {}).get('attached_pic')]
    audio = [s for s in streams if s.get('codec_type') == 'audio']
    failures = []
    duration = float(metadata.get('format', {}).get('duration', 0))
    if not math.isfinite(duration) or duration <= 0:
        failures.append('No valid positive duration')
    if not pictures:
        failures.append('No video stream')
    if args.require_audio and not audio:
        failures.append('Required audio stream missing')
    if args.expect_duration and abs(duration - args.expect_duration) > args.tolerance:
        failures.append(f'Duration differs from {args.expect_duration}s by more than {args.tolerance}s')
    decode = run(['ffmpeg', '-v', 'error', '-xerror', '-i', str(video),
                  '-map', '0:v?', '-map', '0:a?', '-f', 'null', '-'])
    if decode.returncode:
        failures.append('Full decode failed: ' + decode.stderr[-2000:])
    audio_levels = []
    for index, stream in enumerate(audio):
        volume = run(['ffmpeg', '-hide_banner', '-nostats', '-i', str(video),
                      '-map', f'0:a:{index}', '-af', 'volumedetect', '-vn', '-sn', '-dn', '-f', 'null', '-'])
        measurements = dict(re.findall(r'(mean_volume|max_volume):\s*(-?(?:inf|\d+(?:\.\d+)?)) dB', volume.stderr))
        audio_levels.append({'stream_index': stream['index'], **measurements})
        if volume.returncode or not measurements:
            failures.append(f'Audio level measurement failed for audio stream {index}')
        elif args.require_audio and float(measurements.get('max_volume', '-inf')) <= -90:
            failures.append(f'Required audio stream {index} is silent or near-silent (peak <= -90 dBFS)')
    if args.contact_sheet and pictures and math.isfinite(duration) and duration > 0:
        sheet.parent.mkdir(parents=True, exist_ok=True)
        # Sample twelve times across the clip; preserve aspect ratio inside each cell.
        interval = duration / 12
        graph = (f'fps=1/{interval:.9f},scale=320:180:force_original_aspect_ratio=decrease,'
                 'pad=320:180:(ow-iw)/2:(oh-ih)/2,setsar=1,tile=4x3')
        contact = run(['ffmpeg', '-v', 'error', '-n', '-i', str(video), '-map', f'0:{pictures[0]["index"]}',
                       '-vf', graph, '-frames:v', '1', str(sheet)])
        if contact.returncode or not sheet.is_file():
            failures.append('Contact-sheet generation failed: ' + contact.stderr[-1000:])
    report = {'file': str(video), 'duration_seconds': duration,
              'video': [{k: s.get(k) for k in ['codec_name', 'width', 'height', 'avg_frame_rate']} for s in pictures],
              'audio_streams': len(audio), 'audio_levels_dbfs': audio_levels,
              'decode_passed': decode.returncode == 0,
              'contact_sheet': str(args.contact_sheet.resolve()) if args.contact_sheet and not failures else None,
              'failures': failures,
              'manual_review_required': 'Watch the final file, inspect text/transitions, and listen to required sound.'}
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 1 if failures else 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as error:
        print(f'Inspection failed: {error}', file=sys.stderr)
        sys.exit(1)
