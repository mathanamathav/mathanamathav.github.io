#!/usr/bin/env bash
# Rebuild the LaTeX resume, copy the PDF into the site, and regenerate the HTML version.
# Usage: scripts/update-cv.sh [path-to-Latex_Resume]   (default: ../Latex_Resume)
set -euo pipefail

cd "$(dirname "$0")/.."
SRC="${1:-../Latex_Resume}"

(cd "$SRC" && latexmk -pdf -interaction=nonstopmode -halt-on-error resume.tex >/dev/null)
mkdir -p static/cv assets/cv
cp "$SRC/resume.pdf" static/cv/resume.pdf
python3 scripts/tex2html.py "$SRC/resume.tex" assets/cv/resume.html

echo "CV updated: static/cv/resume.pdf, assets/cv/resume.html"
