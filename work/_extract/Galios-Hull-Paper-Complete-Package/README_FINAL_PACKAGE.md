# Galios-Hull — Final Paper Package (IEEE review version)

Updated through P1-54 (Introduction revised as six connected prose paragraphs; theorem-level comparisons with [DPI2023], [DP2025],
[DIMP2026] and [ES2026] from lawfully read full texts; author ORCID added;
all EAQECC material removed from the manuscript at the author's
direction; see `supporting_records/P1_42_GATE_G1_AND_ERROR_AUDIT.md`,
Sections C–F).

## Main files
- `manuscript/P1_15_MANUSCRIPT_DRAFT.tex` — version of record.
  SHA-256: `b9397448cd0591a53f56adf3b440b27de114c5ceca9ea6ced7e52b451dc5f303`
- `manuscript/P1_15_MANUSCRIPT_DRAFT.md` — synchronized Markdown companion.
  SHA-256: `71c3b7de4b1006ea66379a1913c725bfafc54c8783f78ece12ebf02092db57cb`
- `manuscript/P1_15_MANUSCRIPT_DRAFT.pdf` — compiled manuscript (16 pages).
  SHA-256: `49e44fefcf0f889d90ef02c6a03a7991c16fde1420b4747423ed4f6eb9a848b9`
- `manuscript/P1_15_MANUSCRIPT_DRAFT.log` — complete pdflatex log of the
  final pass.
- `manuscript/P1_41_MANUSCRIPT_IEEE_SINGLE_COLUMN.tex` — IEEEtran
  single-column review version (same content; IEEEtran numbering).
- `manuscript/P1_41_MANUSCRIPT_IEEE_SINGLE_COLUMN.pdf` — compiled IEEE
  review PDF (17 pages), with its `.log` alongside.
  SHA-256: `02dd8c4b5002a30810e4eb09b353dc2b51fb6f3705e52db0c3a6faf15ea80d14`
- `manuscript/references.bib` — standalone BibTeX form of the 23 cited
  references. The `.tex` uses an inline `thebibliography`, so BibTeX is not
  needed to compile the source as supplied.

The manuscript contains no external figure files and no tables:
all results are stated in prose and displayed equations. Author: Arun Kumar Yadav, School of Basic and Applied Sciences,
K.R. Mangalam University, Gurugram, arunyadav0307@gmail.com.
ORCID iD: 0009-0009-1169-3264.

## Compilation status
Both manuscript versions were compiled with pdflatex (two passes) in a
GitHub Actions (Debian/TeX Live) environment with no errors and no
undefined references or citations: the reading copy has 16 pages; the
IEEEtran single-column review version has 17 pages (within the journal's
50-page single-column submission limit). To recompile locally, run
pdflatex twice on either `.tex` file above (the IEEE version requires the
`IEEEtran` class).

## Contents
- `code/` — validator programs and saved outputs, including
  `validate_p1_42_edge_checks.py` and `validate_p1_45_dp2025_mean.py`.
- `supporting_records/` — frozen theorem blueprint, proof records,
  independent/proof audits, correction notes, the N1/N2 integration note,
  the P1-39 references note, the IEEE submission checklist, and the Gate G1
  audit record (P1-42, with P1-44–P1-47 update sections).
- `MANIFEST_SHA256.txt` — SHA-256 manifest for every packaged file except
  the manifest itself. Verify after extraction with
  `sha256sum -c MANIFEST_SHA256.txt` from the package root.

## Validation summary
- Example 9.4 correction checked at the \(h^\#\) exponent level:
  predecessor \(2187/2187\), successor \(27/2187\) in the GF(8) case
  (`code/validate_audit_fixes.py`).
- Corollary 8.5 (variance of the code dimension and zero covariance) uses
  the previously proved N1/N2 results and the exact P1-14 validation record.
- All 23 bibliography entries are cited; no citation key is unresolved.
- Independent P1-42 edge checks (`code/validate_p1_42_edge_checks.py`,
  48 cases) reproduce the transfer-trace distribution, the moment
  formulas, Cov = 0, the joint symmetry, and the LCD/SO/DC counts.
- P1-45 check (`code/validate_p1_45_dp2025_mean.py`, 1800 exact-rational
  cases plus DP2025 Example 3.6): the single-component hull mean of
  Theorem 8.2 coincides with [DP2025, Theorem 3.3].
- Finite computations are supporting evidence, not substitutes for proofs.

## Remaining blockers / status
- Visual proofreading of the compiled PDF by the author is still advised.
- Gate G1 is PARTIALLY RESOLVED: the per-code hull formula
  ([DPI2023, Theorem 3]) and the single-component hull mean
  ([DP2025, Theorem 3.3]) are identified and credited; novelty is not
  claimed to be fully established, and the paper has not been submitted.
- Journal-submission artefacts (cover letter, declarations, code/data
  DOI) remain author-side items.
