# P1-41 — IEEEtran Single-Column Review Conversion: Record

**Date:** 22 October 2026. **Source of conversion:** the 17-page
article-class manuscript at commit `3e4f87f` (unchanged; it remains the
reading copy). **Converted file:**
`P1_41_MANUSCRIPT_IEEE_SINGLE_COLUMN.tex` (conversion commit `6ad0e87`).

## Template options (verified, not guessed)

- IEEE Transactions on Information Theory author information
  (itsoc.org/it-trans/author-info) requires a **single-column version
  for reviewing** and, from 1 May 2025, compliance with the 50-page
  IEEE Transactions single-column submission limit.
- The IEEEtran class documentation (IEEEtran HOWTO) gives the
  single-column, double-spaced review form as
  `\documentclass[10pt,journal,draftclsnofoot,onecolumn]{IEEEtran}`.
  That is exactly what was used. Only formatting changed: class/geometry
  removed, author block put in the IEEE `\thanks` form, Keywords became
  `IEEEkeywords` (the Mathematics Subject Classification line retained
  below it). No mathematical statement, proof, example, table, or any of
  the 25 references was altered; cross-references automatically follow
  IEEEtran's Roman section numbering (e.g. Corollary VIII.5) and the two
  tables become Table I/II.

## Compilation and visual verification

- Compiled with pdflatex (two passes, GitHub Actions/TeX Live, CI commit
  `8fec7dd`): `compiled/P1_41_MANUSCRIPT_IEEE_SINGLE_COLUMN.pdf`,
  **18 pages** — within the 50-page single-column limit.
- The log has **0 errors, 0 undefined references/citations, 0 LaTeX
  warnings**; 3 overfull boxes of at most about 50pt, all inside the
  one-inch review margins.
- All 18 pages were rendered and inspected visually: title/author
  footnote, abstract and Index Terms, Table I (positioning), Sections
  II–XI, Corollary VIII.5 ("uncorrelated (they need not be independent)"),
  Examples IX.1–IX.6, Table II (ten EAQECC rows), and all 25 references
  render correctly with consistent IEEEtran numbering.

## Author-side items remaining (nothing invented, nothing submitted)

- Register/link the author's ORCID iD (mandatory at IEEE submission).
- Declarations and code/data statements from the P1-40 checklist,
  confirmed truthfully by the author (no DOI or link has been invented).
- Final two-column version (≤ 25 pages) will be needed only after
  acceptance; the open-access option, biography/photo and copyright form
  are acceptance-stage items. Gate G1 remains DEFERRED.
