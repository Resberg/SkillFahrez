# SkillFahrez

A portable toolkit for building interfaces and producing videos with an AI coding agent. Includes installable skills, practical production guides, reusable briefs, and small local utilities.

**Start here:** [Make a UI](docs/make-a-ui.md) · [Make a video](docs/make-a-video.md) · [Tool setup](docs/tool-setup.md) · [Prompt cookbook](prompts/cookbook.md)

## What's inside

| Skill | Use it for |
| --- | --- |
| `fahrez-ui-build` | Turn a brief into a responsive, working interface |
| `fahrez-ui-review` | Inspect an existing interface and fix evidenced usability problems |
| `fahrez-video-production` | Script, storyboard, build, render, and inspect a video |
| `fahrez-creative-tools` | Route work between code, image generation, compositing, audio, and editing tools |
| `frontend-design` | Additional visual direction from the bundled Apache-2.0 skill |

The first four skills are authored for this repository. `frontend-design` is an attributed local snapshot. See [provenance and licenses](THIRD_PARTY_NOTICES.md). More specialized UI/video skills are listed in the [optional catalog](docs/skill-catalog.md).

## UI design references

[Framer University Resources](https://framer.university/resources) is a reference library for components, animations, effects, interactions, and websites. Use it to study details such as hover feedback, text reveals, scroll animation, and form states, then adapt the relevant behavior to your product and existing stack.

The [UI guide](docs/make-a-ui.md#use-framer-university-as-a-reference) explains how to turn a selected reference into an implementation brief. These resources are linked for reference; their source files and assets are not bundled in this repository. Check each resource's terms before reuse.

## Install

Requires Git and Python 3.10+. The utilities use Python's standard library.

```powershell
git clone https://github.com/Resberg/SkillFahrez.git
cd SkillFahrez
python scripts/check_bundle.py
python scripts/install_skills.py --target codex --dry-run
python scripts/install_skills.py --target codex
```

The installer copies skills to `~/.agents/skills/`. Start a new Codex session afterward. [Official OpenAI installation guidance](https://developers.openai.com/api/reference/cli) documents this user-level directory. For older installations using `~/.codex/skills`, pass that path explicitly:

```powershell
python scripts/install_skills.py --destination "$env:USERPROFILE/.codex/skills"
```

Other destinations:

```powershell
# Current project's agent skills
python scripts/install_skills.py --destination ../my-project/.agents/skills
# Claude Code's user skills directory
python scripts/install_skills.py --target claude
# Only the two UI workflows
python scripts/install_skills.py --target codex --only fahrez-ui-build fahrez-ui-review
```

Existing skill folders cause the installer to stop before copying. It never replaces an existing installation; use a new destination or explicitly manage the older version yourself.

## Use

```text
Use $fahrez-ui-build to build a responsive portfolio for an electrical
engineering student. Use the existing stack. Make project demos the focus,
and inspect the finished desktop and mobile layouts.
```

```text
Use $fahrez-video-production to make a 30-second Indonesian vertical
explainer. Deliver the script, editable project, final MP4, subtitles,
thumbnail, and a report of what was actually checked.
```

Skills are instructions and resources. They do not install MCP servers, provide paid services, transfer account access, or grant an agent new tools. The [tool guide](docs/tool-setup.md) explains the dependencies and fallbacks.

## Useful files

- [UI brief](templates/ui-brief.md) and [UI review checklist](templates/ui-review.md)
- [Video brief](templates/video-brief.md), [storyboard](templates/storyboard.md), and [delivery note](templates/delivery-note.md)
- [Minimal Remotion component](examples/remotion/README.md)
- `scripts/inspect_video.py`: metadata, decode validation, audio-level analysis, and optional contact sheet
- [Validation record](docs/validation.md)

## Scope

This is a curated UI/video package, not a full export of an assistant environment. It contains no credentials, account configuration, personal memory, private projects, or plugin binaries. Tools and models change; consult their current documentation before setup. The original repository material is MIT licensed; bundled third-party material retains its own license.
