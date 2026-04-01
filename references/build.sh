#!/bin/bash
# Assembles the course from parts.
# Run from the course directory: bash build.sh
set -euo pipefail

# Validate required files exist
for f in _base.html _footer.html; do
  if [ ! -f "$f" ]; then
    echo "Error: $f not found. Run from the course directory." >&2
    exit 1
  fi
done

# Validate at least one module exists
if ! ls modules/*.html >/dev/null 2>&1; then
  echo "Error: No module HTML files found in modules/." >&2
  exit 1
fi

LC_ALL=C cat _base.html modules/*.html _footer.html > index.html
echo "Built index.html — open it in your browser."
