#!/usr/bin/env bash
# Portable serial N/S/T comparison. See --help for bounded smoke controls.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$ROOT/rerun.py" "$@"
