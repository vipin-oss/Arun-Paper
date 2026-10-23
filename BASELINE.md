# BASELINE — Phase A (intake, before any edit)

Date: 2026-10-23 (UTC).  Repository: `vipin-oss/Arun-Paper`, branch
`arena/7ef3434e-arun-paper`, base commit `08e929c`.

## Uploaded artefact

| property | value |
|---|---|
| file | `Galios-Hull-Paper-Complete-Package-6ad0e87.zip` |
| size | 990,471 bytes |
| entries | 47 (no directories counted as files) |
| top-level dir | `Galios-Hull-Paper-Complete-Package/` (single root) |
| path safety | no absolute paths, no `..` components, no symlinks |
| unpacked | 47 files, ~1.5 MB |

Safety check performed with `zipfile` before extraction: every member path was
normalised and rejected if it escaped the target, and Unix mode bits were
inspected for `S_IFLNK`. Nothing hostile found.

## Provenance of the two manuscript files

`manuscript/P1_15_MANUSCRIPT_DRAFT.tex` and
`manuscript/P1_41_MANUSCRIPT_IEEE_SINGLE_COLUMN.tex` differ in 18 lines, all of
them preamble (`\documentclass`, `geometry`, author block, `keywords` ->
`IEEEkeywords`, MSC line). **The body is byte-identical.** `P1_41` is therefore
the canonical IEEE review source and the base of `FINAL_IEEE_TIT_SUBMISSION.tex`.

The two shipped PDFs (16 pp / 17 pp) were produced before this audit by the
author's toolchain. They are **not** outputs of any build performed here and are
not offered as the PDF of the final source.

## Read-only snapshot

`ORIGINAL_SNAPSHOT/` is a byte copy of the extracted package with write
permission removed. Per-file digests: `work/original_sha256.txt` (47 lines).
The package's own `MANIFEST_SHA256.txt` verifies against the extracted files
(`sha256sum -c` all OK), so the manifest is not merely a claim.

## Environment (relevant limitations)

* No TeX engine and no TeX Live tree: `pdflatex`, `latexmk`, `bibtex`,
  `tectonic` all absent; `apt-get` cannot reach a package index; GitHub release
  assets and tectonic's bundle relay are not reachable from this sandbox.
* No `pdfinfo` / `pdftoppm`; page-level visual inspection was impossible here.
* Python 3.11 + stdlib only was used for all verification. The verifier is
  dependency-free by design so that it reproduces anywhere.
