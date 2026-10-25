# Merged single paper (recommended submission version)

**Title:** *Joint Code-Dimension and k-Galois-Hull Enumerators for Repeated-Root
Constacyclic Codes over Square-Free Affine Algebras*

This folder is the **single, balanced paper** obtained by merging the two earlier
packages in this repository:

| source | role in the merge |
|---|---|
| `Paper2_Simple_Article (2).zip` | base text (newer, 34 proofs, figures, tables, incompatible twists, support trapezoid, self-dual counts, complexity) |
| `Galios-Hull-Paper-Complete-Package-6ad0e87.zip` | reading-copy details: `M=1` simple-root specialization with the explicit `2×2` transfer matrix, a remark fixing exactly which hypotheses the enumerator needs, an explicit scope-and-limitations paragraph, and the literature positioning around `DPI2023 / DP2025 / DIMP2026 / ES2026` |

The two old drafts must **not** be submitted separately: they share the same main
theorem, so two submissions would be duplicate publication. See
`../PAPER_COMPARISON_REPORT.md` for the full comparison.

## Contents

```
main.tex                  manuscript (article class, Elsevier-style front/back matter)
references.bib            bibliography (natbib + unsrtnat, 20 cited keys)
figures/
  fig1_workflow.pdf       pipeline figure
  fig2_joint_F8_n14.pdf   joint distribution, F_8, n = 14      (was fig5)
  fig3_joint_F32_n62.pdf  joint distribution, F_32, n = 62      (was fig6)
code/
  enumerator.py           transfer-matrix enumerator, restricted SO/DC/SD counts, moments
  checks.py               self-contained verification (Level 1 + Level 2)
  checks_output.txt       saved output of checks.py  (all checks pass)
  generate_tables.py      regenerates tables/ from the enumerator
tables/
  summary_families.csv    Table 1 data (11 families)
  joint_<slug>.csv        full joint multiplicities N_{kappa,eta} per family
```

## IEEE version (`paper/ieee/`)

For an IEEE journal submission there is a second, IEEEtran-format package — same
mathematical content, IEEE layout, IEEE-specific front/back matter, 192-word
abstract, 5 index terms, 31 references, and both a two-column journal file and
a single-column double-spaced peer-review file:

```
paper/ieee/
  main.tex                 two-column IEEEtran layout  (regular-paper format)
  main_peerreview.tex      same paper, single column + double spaced (for review)
  body.tex                 shared manuscript body (identical in both)
  references.bib           exactly the 31 cited entries
  figures/                 3 vector PDFs
  supplementary/           code + all generated data (zip this for submission)
  compliance_check.py      automated formal checks + budget measurement
  compliance_report.txt    saved output: all IEEE regular-paper checks pass
  COVER_LETTER.md          cover letter with placeholders
  build.sh                 builds both PDFs
  SUBMISSION_CHECKLIST.md  full checklist
```

It is submitted as a **regular paper** (no letter/correspondence form, no
5-page limit): 7 numbered sections, 2 appendices, Conclusion (singular) +
Acknowledgment + References in the IEEE order.

Measured budgets (`python3 compliance_check.py`, saved in
`compliance_report.txt`): abstract **192 words** (limit 200, no citations, no
displays), **5** alphabetized index terms, **31** references (all cited, none
uncited), **3** vector figures, **2** tables, **93** displays, estimated
**15–19 two-column pages** of a regular paper. The checker also verifies the
IEEE author/`\thanks` block, the absence of Elsevier-only matter, the section
order, all labels/refs/citations and the float conventions.

## Compile (arXiv / non-IEEE version)

```bash
pdflatex main && bibtex main && pdflatex main && pdflatex main
```

(no external packages beyond a standard TeX Live: `amsmath`, `amssymb`,
`amsthm`, `mathtools`, `mathrsfs`, `booktabs`, `tabularx`, `graphicx`, `tikz`,
`natbib`, `microtype`, `hyperref`)

> Note: this sandbox has no LaTeX installation, so the merged file was checked by
> structural linting only (environment balance, all `\ref` targets defined, no
> duplicate labels, every `\cite` key present in `references.bib`, all three
> figure files present). **Please run one pdflatex pass and read the PDF.**

## Reproduce the numbers

```bash
python3 code/checks.py          # ~30 s; prints PASS/FAIL per claim
python3 code/generate_tables.py # rewrites tables/*.csv
```

`code/checks.py` verifies, among other things:

* the transfer trace against brute-force word enumeration (60 `(a,M,w)` cases);
* the closed forms for orbit lengths 1 and 2;
* the complement–reversal symmetry, the checksum `E(1,1)=(M+1)^N_F`, the LCD
  count `2^#orbits`, and the one-orbit trapezoid support;
* the mean/variance/Cov = 0 formulas;
* **all 11 rows of Table 1**, the joint table of Example 7.1, `E[η|κ=7]=533/131`
  (Example 7.2) and `max_κ E[η|κ] = 17.392` at `κ=31` (Example 8.1);
* **Level 2 (from the definitions):** for 7 small families over `F_4`, `F_8`,
  `F_3`, `F_9` it factors `x^{n'} − λ₀`, computes the reciprocal from its
  definition, reads off the orbit skeleton (recovering the skeletons quoted in
  Examples 7.1–7.3 independently), builds every generator matrix, computes the
  hull dimension as `dim C − rank(B σ^k(B)^T)`, and matches the full joint
  histogram with the trace product — 27, 27, 27, 2187, 64, 16 and 256 words.

## What changed relative to the base draft

1. **Added** §6.2 “The simple-root case `M=1`”: Proposition `prop:M1` (the
   transfer matrix becomes `[[U^w,1],[U^wZ^w,1]]`, the hull edge term is the
   indicator of a descent `1→0`, LCD count `2^#orbits`) with proof, plus
   Example `ex:M1` (`F_4`, `n=5`: `E=(1+U)(1+2U²Z²+U⁴)`, `E[η]=1`, `Var=1`,
   4 LCD codes) — all numbers machine-checked.
2. **Added** Remark `rem:hypotheses` under the main theorem: the trace product is
   a `Z[U,Z]` identity for every `M ≥ 1`; `M = p^t` is needed only for the field
   construction; incompatible components are counted, not excluded; counts are
   labeled; orbit orientation is irrelevant.
3. **Added** a scope-and-limitations paragraph and a second open direction
   (labeled → unlabeled counts) to the Conclusions.
4. **Removed** the unused threshold-layer proposition (never referenced later) —
   keeps the paper balanced rather than maximal.
5. **Fixed** the abstract overclaim: the `3^31` family is now described as the
   full joint *distribution* computed without enumerating the codes, not as a
   code-by-code verification.
6. **Fixed** the verification section and Table 2 so that they describe exactly
   what the supplied code does (no seeded-sample rows, no file names that do not
   exist); `Data availability` now names the actual files.
7. **Fixed** figure numbering (`fig5→fig2`, `fig6→fig3`), added the
   `debnathCorrection2023` citation in the introduction, and generated the CSV
   files that Table 1 already promised.

## Author-side items before submission

* Compile and proofread the PDF (see note above).
* Confirm the author list / affiliations / corresponding author / ORCID
  (base draft: Yadav, Gupta, Soni, Pruthi).
* Choose the journal. Fitting venues: *Linear Algebra Appl.*, *Finite Fields
  Appl.*, *Adv. Math. Commun.*, *Designs, Codes and Cryptography*,
  *J. Algebra Comb. Discrete Struct. Appl.*
* Cover letter + declarations; deposit `code/` + `tables/` (e.g. Zenodo) if the
  journal wants a DOI instead of supplementary files.
* The large families of Table 1 (`F_4×F_16`, `F_25`, `F_32`) are verified through
  the enumerator only, not code-by-code; this is stated in the paper, so no
  further action is needed unless you want to extend Level 2.
