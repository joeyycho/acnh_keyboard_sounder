#!/usr/bin/env bash
# Local / CI helper: build KeyboardSounder with PyInstaller.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python -m pip install -r requirements-dev.txt
python -m PyInstaller --noconfirm --clean KeyboardSounder.spec

echo "Build output:"
ls -la dist/
