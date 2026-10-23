# BUILD_REPORT.md — compilation, limits and iterations

## Toolchain

GitHub Actions, `ubuntu-24.04` runner, `texlive/texlive:latest` container
(the official TeX Live image), `latexmk -pdf -interaction=nonstopmode
-file-line-error -halt-on-error`.

Hard limits as required:

| limit | setting | where |
|---|---|---|
| per-compile wall clock | `timeout 120` around `latexmk` | workflow step "Compile (120 s cap)" |
| per-job wall clock | `timeout-minutes: 20` | workflow job definition |
| retries | none — a single compile invocation per run, `-halt-on-error` | workflow |
| loops | none; `latexmk` resolves references in a bounded dependency pass | workflow |

Actual compile time: ~10 s inside a ~95 s job (the job time is dominated by
checkout and container init, not by TeX).

## Build run history (all URLs under the branch)

| run | purpose | compile | outcome |
|---|---|---|---|
| 39951256018 | first build (apt-installed TeX Live) | OK | success; exposed the 3 pre-existing overfull boxes |
| 39951517788 | add publish step | OK | job cancelled after 8 min waiting on `apt-get update`; superseded |
| 39952446882 | TeX Live container | OK | compile + PDF upload OK; **git publish failed** (container file ownership) |
| 39952999687 | fix container git ownership | OK | **PDF published**; 3 overfull boxes (22.8/26.6/49.7 pt) reproduced |
| 39953361126 | correction 1: lemma to display, block paragraph, run-in head, breakable paths | OK | 2 of 3 overfull gone; the distribution block re-flowed at 43.8 pt |
| 39953617032 | correction 2: `\raggedright` on that block | OK | **0 overfull** |
| 39953936880 | correction 3: regression fix (duplicated `code/` prefix introduced in correction 1) | OK | **0 overfull, 0 errors, final** |

### Iteration budget: 3 of 3 used

The cap is three correction iterations. Exactly **three** runs changed the
manuscript source after the first successful compile:

1. run 39953361126 — the overfull-box repairs (lemma to display, block
   paragraph break, run-in head, breakable file paths);
2. run 39953617032 — `\raggedright` on the Example IX.4 distribution block,
   because repair 1 let that block re-flow at 43.8 pt;
3. run 39953936880 — repair of a regression that correction 1 itself
   introduced: two file paths rendered as `code/code/validate_...`.

Correction 3 is worth recording because the compiler could not catch it —
`latexmk` exited 0 with no warning. It was found only by rendering page 14 and
reading it. That is precisely why page-by-page inspection is part of this
audit and not a formality.

Two further runs (39951517788, 39952446882) changed only the workflow file, not
the manuscript, and are not counted as corrections.

## Final build state

```
latexmk exit code: 0
Overfull boxes:    0
Underfull boxes:   1   (the author-affiliation footnote, cosmetic and harmless)
Errors:            0
Undefined refs:    0
Undefined cites:   0
Pages:             17
Producer:          pdfTeX-1.40.29
```

Artifacts: `FINAL_IEEE_TIT_SUBMISSION.pdf`, `.log`, `BUILD_DIAGNOSTICS.md`,
`PDF_FONTS.txt`, `compile_stdout.txt`, all in `build/` (committed by CI) and
copied into `validation/`.
