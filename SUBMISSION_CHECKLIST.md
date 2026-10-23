# SUBMISSION_CHECKLIST.md — IEEE TIT production

The current official IEEE TIT author instructions could **not** be fetched from
this sandbox (no route to ieee.org). Per the review protocol, rules that could
not be read are marked **UNVERIFIED** and nothing was changed on the basis of
an unverified rule; the existing, already-compliant format is preserved.

| Item | Status | Evidence / note |
|---|---|---|
| Target journal | ✔ IEEE TIT | stated in `AUDIT_EDITOR.md` §1 |
| Document class | ✔ `IEEEtran` | `\documentclass[10pt,journal,draftclsnofoot,onecolumn]{IEEEtran}` |
| Column mode | ✔ single column (review) | never converted to two-column, as instructed |
| Abstract length | UNVERIFIED vs current limit | abstract is one paragraph, ~190 words |
| Index terms | ✔ `IEEEkeywords` | 6 terms |
| MSC line | ✔ present | 94B15, 94B05, 11T71 (non-IEEE convention, but harmless in review mode; TIT does not require it — remove if the editor objects) |
| Theorem environments | ✔ amsmath/amssymb/amsthm | numbering continuous per section |
| References | ✔ 23 entries, all cited | inline `thebibliography`; `references.bib` shipped for a BibTeX build |
| DOI in references | ✔ present where applicable | two book entries have none, correctly |
| "Manuscript received" footnote | UNVERIFIED / not present | IEEE requires it at final submission; add at acceptance |
| ORCID / funding footnote | partially present | ORCID and e-mail in `\thanks`; no funding statement |
| Figures and tables | none | paper is text/display-math only, so no figure-resolution rules apply |
| Page limit | UNVERIFIED | depends on the current TIT rule for regular papers |
| Author biography / photo | not present | required only at final production |
| PDF built from this exact source | ✘ **BLOCKED** | no TeX engine in the sandbox; see `REMAINING_RISKS.md` R1 |
| Source self-contained | ✔ | single `.tex`, no `\input`, no external assets, only standard packages |
| Deterministic rebuild | ✔ by construction | no timestamps, no random content, no generated tables |

## Pre-submission actions on a machine with TeX Live

1. `latexmk -pdf -interaction=nonstopmode -halt-on-error FINAL_IEEE_TIT_SUBMISSION.tex`
2. Check the log for `Overfull \hbox` warnings; three were reported in the
   author's earlier build (~22.8pt, ~26.6pt, ~49.7pt) and are **not yet
   repaired** — they are cosmetic and were left alone rather than guessed at.
3. Confirm the page count against the current TIT limit.
4. Add the "Manuscript received …" footnote.
5. Decide whether to keep the MSC line.
