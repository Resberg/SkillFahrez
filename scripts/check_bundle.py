"""Validate skill manifests, local Markdown links, and vendored file digests."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def main():
    errors = []
    skills = sorted((ROOT / 'skills').glob('*/SKILL.md'))
    if not skills:
        errors.append('No skills found')
    for file in skills:
        source = file.read_text(encoding='utf-8-sig')
        match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', source, re.S)
        if not match:
            errors.append(f'{file.relative_to(ROOT)}: missing YAML frontmatter')
            continue
        fields = dict(re.findall(r'^([a-z_-]+):[ \t]*(.+)$', match.group(1), re.M))
        name = fields.get('name', '').strip('"\' ')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            errors.append(f'{file.relative_to(ROOT)}: invalid name')
        if name != file.parent.name:
            errors.append(f'{file.relative_to(ROOT)}: name/folder mismatch')
        if not fields.get('description', '').strip():
            errors.append(f'{file.relative_to(ROOT)}: missing description')
    for file in ROOT.rglob('*.md'):
        if any(part.startswith('.') for part in file.relative_to(ROOT).parts):
            continue
        source = file.read_text(encoding='utf-8-sig')
        # Ignore code fences so tutorial placeholders are not interpreted as links.
        source = re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', source, flags=re.M | re.S)
        for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', source):
            target = raw.split(' "', 1)[0].strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            path = (file.parent / unquote(parsed.path)).resolve()
            if not path.exists():
                errors.append(f'{file.relative_to(ROOT)}: missing link {target}')
    provenance = ROOT / 'catalog' / 'bundled-sources.json'
    if not provenance.exists():
        errors.append('Missing bundled-source manifest')
    else:
        for item in json.loads(provenance.read_text(encoding='utf-8'))['files']:
            path = ROOT / item['path']
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
                errors.append('Bundled file digest mismatch: ' + item['path'])
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'PASS: {len(skills)} skill manifests, local Markdown targets, bundled-source digests')
    print('This structural check does not validate agent behavior or external links.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
