"""Fetch listed first-party 47 Skin images without overwriting valid files.
Run optionally through GitHub Actions or GitHub Codespaces if a network is available.
"""
from __future__ import annotations
import json
import os
import tempfile
import urllib.request
from pathlib import Path
from PIL import Image, UnidentifiedImageError

BASE = Path(__file__).resolve().parent
DEST = BASE / 'public' / 'assets'
DEST.mkdir(parents=True, exist_ok=True)
manifest = json.loads((BASE / 'asset-manifest.json').read_text(encoding='utf-8'))

def valid(path: Path) -> bool:
    try:
        if not path.is_file() or path.stat().st_size < 300:
            return False
        with Image.open(path) as img:
            img.verify()
        with Image.open(path) as img:
            return img.width > 20 and img.height > 20
    except (OSError, UnidentifiedImageError):
        return False

ok = failed = skipped = 0
for item in manifest:
    target = DEST / item['filename']
    url = item.get('source_url')
    if valid(target):
        print(f"KEEP {target.name} (verified)")
        skipped += 1
        continue
    if not url:
        print(f"PENDING {target.name}: original source URL not verified")
        failed += 1
        continue
    temp_path = None
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; 47SkinPortfolioAssetAudit/1.0)'})
        with urllib.request.urlopen(req, timeout=25) as response:
            status = response.status
            mime = response.headers.get('Content-Type', '').split(';')[0].lower()
            if status != 200 or not mime.startswith('image/'):
                raise ValueError(f'HTTP {status} / Content-Type {mime}')
            with tempfile.NamedTemporaryFile(dir=DEST, prefix='.asset-', delete=False) as tmp:
                temp_path = Path(tmp.name)
                total = 0
                while True:
                    chunk = response.read(1024 * 256)
                    if not chunk:
                        break
                    total += len(chunk)
                    if total > 25_000_000:
                        raise ValueError('Image exceeds 25 MB safety cap')
                    tmp.write(chunk)
        if not valid(temp_path):
            raise ValueError('Downloaded data is not a valid image')
        with Image.open(temp_path) as img:
            detected = img.format.lower()
        expected = target.suffix.lower()
        if detected == 'jpeg': detected = 'jpg'
        if (expected == '.jpg' and detected != 'jpg') or (expected == '.png' and detected != 'png'):
            raise ValueError(f'Format mismatch: expected {expected}, got {detected}')
        os.replace(temp_path, target)
        temp_path = None
        print(f'OK {target.name} ({target.stat().st_size} bytes)')
        ok += 1
    except Exception as exc:
        print(f'FAILED {target.name}: {type(exc).__name__}: {exc}')
        failed += 1
    finally:
        if temp_path and temp_path.exists(): temp_path.unlink()
print(f'RESULT downloaded={ok} already_valid={skipped} failed_or_pending={failed}')
