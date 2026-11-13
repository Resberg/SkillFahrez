# Working on SkillFahrez

Keep skills portable: use paths relative to the skill folder, discover available tools, and document dependencies rather than assuming a particular machine or connected account.

Put reusable agent instructions in `skills/`, human tutorials in `docs/`, and reusable production worksheets in `templates/`. A copied installed skill must work without this repository's docs; link outside the skill only for optional reading.

Preserve third-party attribution and license files. Do not add credentials, personal memory, user projects, generated media, or machine-specific configuration to the package.

Before publishing changes, run `python scripts/check_bundle.py`, exercise changed scripts on temporary files, and state which checks actually ran. Rendering a preview does not establish that a final video was exported.
