# Tools, dependencies, and fallback routes

## Basic package

Git and Python 3.10+ are enough to download, validate, and install the skills. Python utilities have no third-party dependencies. Browser inspection, image generation, MCP servers, and rendering are separate capabilities.

```powershell
git --version
python --version
python scripts/check_bundle.py
```

## Working UI

Use the target project's README and lockfile to install its existing dependencies. Start its preview server and use an available browser automation or computer-use tool. If only source inspection is possible, record that limitation. Editable Figma output requires a connected Figma integration and the corresponding current Figma skill; an HTML page alone is not a Figma file.

## Remotion route

Install a Node version supported by the current Remotion release. Follow the official [getting-started documentation](https://www.remotion.dev/docs). Create a project with `npx create-video@latest`, choosing a minimal TypeScript template. Keep the Remotion packages on matching versions and retain the generated lockfile.

Use `npx remotion studio` to preview and the documented render command to export. The repository's [sample component](../examples/remotion/README.md) is intended to be added to that initialized project; it is not a dependency-complete standalone application. Check [Remotion's license](https://www.remotion.dev/docs/license) for the intended use.

## FFmpeg / FFprobe

Install these separately from an appropriate distribution linked by the [FFmpeg project](https://ffmpeg.org/download.html), then confirm both are on PATH:

```powershell
ffmpeg -version
ffprobe -version
```

The video inspector uses these executables and fails clearly when they are missing. It does not install codecs or tools. Its contact sheet is diagnostic, not a thumbnail design.

## Connected creative tools

| Tool family | Role | Setup and session check |
| --- | --- | --- |
| EffectCraft | Compositing and motion graphics | Connect the separately installed app/server; discover commands through `command_list` before `command_run` |
| SoundCraft | Audio recording, editing, and mixing | Connect the separately installed app/server; discover supported commands through `list_commands` |
| Shotcut | Footage editing and timeline assembly | Supply the actual saved project path; disk-based MCP state may differ from unsaved GUI edits |
| ArtCraft or another generation provider | Missing visual/audio assets | Discover supported models and job parameters; use the user's authorized account and budget; follow jobs to completion |
| Image generation integration | Illustrations, backgrounds, cutouts | Check the session tool schema, reference-image support, and transparency requirements |
| Figma | Editable design handoff | Connect the account and load the skill required for the intended Figma operation |

These are capability routes, not universal installation instructions. Server availability, command schemas, paid access, and versions vary. No MCP config, tokens, application binaries, or paid credits are included. Do not paste a machine's entire agent configuration into a public repository.

Fallbacks: use supplied audio if TTS is unavailable; use existing licensed media if generation is unavailable; build a frame-driven project if a compositor is missing. Explain any resulting change in deliverable before calling the work complete.
