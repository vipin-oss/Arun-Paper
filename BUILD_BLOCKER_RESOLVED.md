# BUILD BLOCKER — RESOLVED in round 2

Round 1 shipped this file because no TeX engine could be installed in the audit
sandbox. That limitation is now bypassed: compilation runs in GitHub Actions on
the official `texlive/texlive` container.

`FINAL_IEEE_TIT_SUBMISSION.pdf` in this package **is** the output of the CI
build of this exact source:

* source SHA-256 `7e340d7f03dd055f7828e3e57605b0f2461bd28b1e27986f66426ac05177bfe6`
  (see `build-logs/SOURCE_SHA256.txt`, computed by the build itself);
* the same hash is the SHA-256 of `FINAL_IEEE_TIT_SUBMISSION.tex` here;
* `latexmk` exit 0, 0 errors, 0 undefined references, 0 overfull boxes;
* 17 pages, pdfTeX-1.40.29.

To rebuild from scratch: `./build.sh` (requires TeX Live with `IEEEtran.cls`).
