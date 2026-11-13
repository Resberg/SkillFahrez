---
name: fahrez-creative-tools
description: Select and coordinate available UI and video tools, including code, image generation, compositing, audio production, and timeline editing. Use when a creative task spans tools or a preferred tool is unavailable.
---

# Route creative work

Inspect the tools actually exposed in the session and the user's existing project. A skill does not prove that an application or MCP server is installed. Prefer the user's chosen tool; otherwise choose the simplest route that preserves editability and can produce the requested export.

| Need | Typical route | Verify |
| --- | --- | --- |
| Working interactive UI | Existing frontend stack and browser inspection | User journey, responsive layout, build |
| Editable Figma handoff | Connected Figma tools and their current required skill | Editable structure, components, fonts |
| Bitmap illustration or cutout | Available image-generation/editing tool | Composition, artifacts, transparency |
| Reproducible animated scenes | Remotion or explicit-time HTML/canvas renderer | Seeking, assets, exported frames |
| Layered titles, masks, effects | Available compositor, such as EffectCraft | Project save, preview, final export |
| Narration, music, mix | Supplied audio, authorized TTS, or a DAW such as SoundCraft | Speech timing, levels, audible export |
| Footage cuts and assembly | Timeline editor such as Shotcut | Saved timeline and rendered media |
| File inspection/transcoding | FFmpeg and FFprobe | Full decode, dimensions, duration, streams |

Discover current command names, parameters, and project state through each tool's own schema or command catalog. Do not hardcode guessed compositor or DAW commands. With Shotcut integrations that read disk, operate on the saved project and reconcile unsaved GUI edits first.

Keep source projects, intermediate media, and exports in distinct folders. Record file paths returned by tools rather than assuming output locations. A successful job submission is not a completed render: follow the job to its terminal result, then inspect the output.

If a tool is missing, explain the specific unavailable capability and continue with a usable authorized fallback. Do not represent a raster image as an editable interface or a web preview as a video export. Do not copy local credentials or account configuration into project deliverables.
