"""Check public Git candidates for private artifacts, secret tokens and local MD links.

No network or third-party dependencies. Only inspects files Git would publish;
does not claim to establish copyright clearance or comprehensive secret detection.
"""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def candidates():
    result = subprocess.run(
        ['git', '-c', 'core.quotepath=false', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
        cwd=ROOT, check=True, stdout=subprocess.PIPE,
    )
    return sorted({p for p in result.stdout.decode('utf-8').split('\0') if p and (ROOT / p).is_file()})


PRIVATE = re.compile(
    r'(?:^|/)(?:\.exam-data|\.readx-backup-stage-[^/]*)(?:/|$)'
    r'|(?:^|/)\.env(?:\.(?!example$)[^/]+)?$'
    r'|\.(?:sqlite(?:-wal|-shm)?|pem|key|p12|pfx|(?:mfa|audit|data|recovery|backup)-keys\.json|recovery\.ndjson|readxbackup|readxaudit)(?:\.partial-.*)?$',
    re.I,
)
SECRETS = [
    re.compile(rb'gh[pousr]_[A-Za-z0-9]{30,}'),
    re.compile(rb'github_pat_[A-Za-z0-9_]{40,}'),
    re.compile(rb'AKIA[0-9A-Z]{16}'),
    re.compile(rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
]
LINK = re.compile(r'(?<!!)\[[^\]\n]+\]\((<[^>]+>|[^)\s]+)(?:\s+"[^"]*")?\)')


def check():
    paths = candidates()
    published = set(paths)
    errors = []
    markdown = 0
    for name in paths:
        path = ROOT / name
        if path.is_symlink():
            errors.append(f'{name}: symlink is not a portable public input')
            continue
        if PRIVATE.search(name):
            errors.append(f'{name}: private artifact filename')
        if path.stat().st_size >= 100 * 1024 * 1024:
            errors.append(f'{name}: exceeds GitHub regular-file limit')
        data = path.read_bytes()
        if data.startswith((b'SQLite format 3\0', b'READX-BACKUP-1\n', b'READX-AUDIT-1\n')):
            errors.append(f'{name}: private artifact signature')
        if any(pattern.search(data) for pattern in SECRETS):
            errors.append(f'{name}: possible credential (value suppressed)')
        if path.suffix.lower() != '.md':
            continue
        markdown += 1
        try:
            content = data.decode('utf-8-sig')
        except UnicodeDecodeError:
            errors.append(f'{name}: Markdown must be UTF-8')
            continue
        # Ignore code samples; check inline file links, including UTF-8 filenames.
        prose = re.sub(r'```[^\n]*\n.*?```', '', content, flags=re.S)
        for match in LINK.finditer(prose):
            raw = match.group(1).strip('<>')
            url = urlsplit(raw)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(ROOT):
                errors.append(f'{name}: link outside repository: {raw}')
                continue
            relative = target.relative_to(ROOT).as_posix()
            if target.is_dir():
                exists = any(p.startswith(relative + '/') for p in published)
            else:
                exists = relative in published
            if not exists:
                errors.append(f'{name}: unpublished or missing link: {raw}')
    for error in errors:
        print(error)
    print(f'Repository check: {len(paths)} public files, {markdown} Markdown files, {len(errors)} issues.')
    return bool(errors)


if __name__ == '__main__':
    sys.exit(check())
