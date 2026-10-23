#!/bin/sh
# Reproduce FINAL_IEEE_TIT_SUBMISSION.pdf from the exact shipped source.
# Requires a TeX Live installation providing IEEEtran.cls (standard for IEEE authors).
set -e
latexmk -pdf -interaction=nonstopmode -halt-on-error FINAL_IEEE_TIT_SUBMISSION.tex
echo "PDF written: FINAL_IEEE_TIT_SUBMISSION.pdf"
