"""Copy bundled skills to an agent directory without replacing existing files."""
import argparse
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group()
    choice.add_argument('--target', choices=['codex', 'claude'], default='codex')
    choice.add_argument('--destination', type=Path)
    parser.add_argument('--only', nargs='+', metavar='SKILL')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    destination = (args.destination.expanduser() if args.destination else
                   Path.home() / ('.agents' if args.target == 'codex' else '.claude') / 'skills')
    destination = destination.resolve()
    available = {p.name: p for p in sorted((ROOT / 'skills').iterdir())
                 if p.is_dir() and (p / 'SKILL.md').is_file()}
    names = list(dict.fromkeys(args.only or available))
    if not names:
        parser.error('No skills found in this package.')
    unknown = sorted(set(names) - set(available))
    if unknown:
        parser.error('Unknown skills: ' + ', '.join(unknown))
    if destination.exists() and not destination.is_dir():
        parser.error(f'Destination is not a directory: {destination}')
    # Refuse source-overlapping destinations before any filesystem mutation.
    source_root = (ROOT / 'skills').resolve()
    if destination == source_root or source_root in destination.parents or destination in source_root.parents:
        parser.error('Destination must not overlap the package skills directory.')
    conflicts = [name for name in names if (destination / name).exists() or (destination / name).is_symlink()]
    if conflicts:
        parser.error('Existing skill folders; nothing copied: ' + ', '.join(conflicts))
    for name in names:
        print(f'{"Would copy" if args.dry_run else "Copy"}: {name} -> {destination / name}')
    if args.dry_run:
        return 0
    destination.mkdir(parents=True, exist_ok=True)
    for name in names:
        shutil.copytree(available[name], destination / name)
    print('Installed. Start a new agent session to discover the skills.')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except OSError as error:
        print(f'Installation failed: {error}', file=sys.stderr)
        sys.exit(1)
