#!/usr/bin/env bash
# Build all three versions of the paper.
# TeX Live / MiKTeX; IEEEtran (from texlive-publishers) is needed only for the
# two two-column/peer-review targets, not for the single-column one.
set -e
build () {
  name="$1"
  pdflatex -interaction=nonstopmode "$name" >/dev/null || true
  bibtex "$name"        >/dev/null || true
  pdflatex -interaction=nonstopmode "$name" >/dev/null || true
  pdflatex -interaction=nonstopmode "$name" >/dev/null || true
  echo "built $name.pdf"
}
build main_singlecolumn  # SINGLE COLUMN, single spaced  (no IEEEtran needed)
build main               # two-column IEEEtran journal layout
build main_peerreview    # single column, double spaced (IEEE review format)
