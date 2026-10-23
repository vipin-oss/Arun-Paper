# BUILD BLOCKER — no PDF in this package

`FINAL_IEEE_TIT_SUBMISSION.pdf` is **not** included because no TeX engine could
be installed in the audit sandbox (no `pdflatex`/`latexmk`/`tectonic`; no
reachable package index, release-asset host, or TeX Live bundle).

The PDF that this package's source produces is exactly what `./build.sh`
writes on any machine with TeX Live (which supplies `IEEEtran.cls`). The source
is self-contained: one `.tex` file, inline bibliography, standard packages only.

Do not substitute the pre-existing `P1_41_*.pdf` from the original upload: it was
built from the *uncorrected* source and is not a build of this file.
