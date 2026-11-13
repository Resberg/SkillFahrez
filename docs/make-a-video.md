# Make a video from idea to inspected export

## 1. Write a production brief

Use the [video brief](../templates/video-brief.md). Decide the audience, message, language, aspect ratio, duration range, and sound. A 9:16 social explainer and a 16:9 product film need different framing and pacing. Start with a concrete example or question the audience understands.

For factual explainers, keep a claims-and-sources list before recording. Recheck current legal, political, medical, or financial claims against authoritative sources. Clearly mark reconstructions, diagrams, and generated footage.

## 2. Script against time

Draft spoken words and on-screen text separately. Read the script aloud; estimate timing from an actual recording where possible. Shorten sentences before speeding up speech. Captions support the voice; a headline can carry a different visual job without duplicating an entire paragraph.

Fill the [storyboard](../templates/storyboard.md). Each beat needs a purpose, picture, motion, transition, sound cue, and source. Include reading holds and transition time in the duration budget.

## 3. Pick the production route

| Material | Good starting route |
| --- | --- |
| UI demonstrations, animated diagrams, reusable scenes | Frame-driven Remotion or an explicit-time renderer |
| Layered titles, masks, composited objects and footage | EffectCraft or an available compositor |
| Interview clips, camera footage, assembled media | Shotcut or an available timeline editor |
| Missing illustration or atmospheric shot | Authorized image/video generation, then compositing |
| Voice, music, and effects | Supplied recordings, authorized TTS, SoundCraft or an available audio tool |

The [tool setup guide](tool-setup.md) explains what these routes require. Choose one main editable project rather than losing changes across several unsynchronized timelines.

## 4. Build for reproducible frames

For Remotion, animate from `useCurrentFrame()` and composition settings. Put media in the project's managed assets and use the documented loading components. Avoid `Date.now()`, unseeded randomness, and timer-driven scene progression. See the [component example](../examples/remotion/README.md).

For explicit-time HTML, expose a function that sets every visible property for time `t`. The renderer must seek, wait for assets/fonts, capture each frame, and encode the frames. Playing a browser animation or recording a screen is a different workflow and may introduce frame drops.

For editor tools, discover the current commands, use the actual saved project path, and verify output locations. Build the hardest scene first, render a short draft, and examine it before assembling everything.

## 5. Fit sound and picture

Use the actual narration cues. Keep speech clear above music, leave room before emphasis, and attach effects to meaningful actions. Listen on normal speakers or headphones. Check names, pronunciation, clipping, abrupt cuts, silence, and the ending. Do not assume a voice provider is available just because a skill mentions it.

## 6. Render and verify the final file

Render a draft, review stills and playback, fix problems, then export the final. Example after a Remotion project has been created and its dependencies installed:

```powershell
npx remotion render src/index.ts FahrezDemo out/final.mp4
python /path/to/SkillFahrez/scripts/inspect_video.py out/final.mp4 --expect-duration 6 --contact-sheet out/contact.jpg
```

For a narration-led video, also pass `--require-audio`. The silent component example deliberately has no audio.

The inspector checks metadata and decodes the video. If audio exists, it reports FFmpeg volume measurements, including detection of wholly silent audio. It can build a contact sheet for visual inspection. It does not determine whether the story is good, captions are readable, speech is intelligible, or music has appropriate rights. Watch and listen to the actual final file.

Deliver the editable project, final MP4, requested captions and thumbnail, sources, and [delivery note](../templates/delivery-note.md). State precisely if only a preview or project was completed.

Technical references: [Remotion's frame model](https://www.remotion.dev/docs/idea), [render CLI](https://www.remotion.dev/docs/cli/render), and [FFmpeg documentation](https://ffmpeg.org/documentation.html).
