# SUBMISSION_CHECKLIST.md — verified against the official TIT rules

Source of the rules: **IEEE Information Theory Society, "Information for
Authors", https://www.itsoc.org/it-trans/author-info, accessed 2026-10-23.**
(Round 1 could not reach IEEE; this round retrieved the actual TIT author page.)

## Requirements and compliance

| # | Requirement (as printed on itsoc.org) | Our value | Status |
|---|---|---|---|
| 1 | abstract "of not more than 250 words" | **165 words** (measured on the compiled text) | **PASS** |
| 2 | abstract self-contained, one paragraph, "without abbreviations, footnotes, references, displayed mathematical equations or tabular material" | one paragraph, no citations, no displayed math. Round 1 had the abbreviation "LCD"; **expanded to "linear complementary dual"** and the abbreviation removed entirely | **PASS** (after fix) |
| 3 | "a list of index terms … after the abstract, a total of five to ten words in length" | **10 words**: Constacyclic codes, Galois hull, joint enumerator, transfer matrices, finite fields | **PASS** (after fix; was 12) |
| 4 | "a **single-column version** of a submission is **required** for reviewing" | `IEEEtran` `10pt,journal,onecolumn,draftclsnofoot` — 17 pages, one column | **PASS** |
| 5 | "fewer than **50 pages** in IEEE Transactions single-column format"; mandatory from 2025-05-01 | **17 pages** | **PASS** |
| 6 | final two-column version "limited to **25 pages**" | not applicable at review; 17 one-column pages will compress well under 25 | n/a |
| 7 | author footnote on first page; prior-presentation statement if applicable | author footnote present with affiliation, e-mail, ORCID. No conference version exists, so no presentation statement is required | **PASS** |
| 8 | "prepared to supply … originals of figures, biographical sketches, and a signed copyright form" upon acceptance | paper has no figures; biography/copyright are post-acceptance items | **PASS** (n/a now) |
| 9 | submission via Author Portal `ieee.atyponrex.com/journal/t-it` | not submitted — that is the author's action | **OUT OF SCOPE** |
| 10 | ORCID readiness | ORCID 0009-0009-1169-3264 printed in the footnote. The ORCID public API is unreachable from this sandbox, so the identifier's **match to the author was not independently verified here** | **UNVERIFIED** |

## Production state

| item | status |
|---|---|
| Source self-contained | **PASS** — one `.tex`, inline `thebibliography`, standard packages + `IEEEtran.cls` only |
| PDF built from this exact source | **PASS** — CI run 39953936880, `latexmk exit 0`, `SOURCE_SHA256.txt` pins the source hash |
| Compilation errors | **PASS** — 0 |
| Undefined references / citations | **PASS** — 0 |
| Overfull boxes | **PASS** — 0 (round 1 had 3: 22.8 / 26.6 / 49.7 pt) |
| Underfull boxes | 1, in the author-affiliation footnote; cosmetic |
| Visual inspection, all pages | **PASS** — 17/17 rendered and read |
| References | **PASS** — 23 entries, all cited, all cited keys defined; the two IEEE TIT self-citations and the four Debnath et al. entries independently confirmed |
| MSC line | present (94B15, 94B05, 11T71). Not an IEEE requirement; harmless in review mode, removable at the author's discretion |

## Remaining author actions before pressing submit

1. Confirm the ORCID iD is the author's own (unverifiable from here).
2. Decide on keeping the MSC line.
3. Add the "Manuscript received …" footnote at acceptance.
4. Supply biography and signed copyright form at acceptance.
5. If the author wants the arXiv preprint route (encouraged by TIT), the
   compiled PDF is ready to upload as-is.
