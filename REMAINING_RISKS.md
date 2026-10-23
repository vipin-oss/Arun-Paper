# REMAINING_RISKS.md

Ordered by consequence. Nothing here is hidden in the reports above.

## R1 — No PDF was built (BLOCKER for "submission-ready")

No TeX engine and no TeX Live tree is obtainable in this sandbox, and no
`pdfinfo`/`pdftoppm` either. Consequences: the required
`FINAL_IEEE_TIT_SUBMISSION.pdf` does not exist; no page-level visual inspection
was performed; undefined control sequences and package availability are
unverified; overfull boxes cannot be located or repaired.

Mitigation shipped: a dependency-free static LaTeX lint (env/brace/label/ref/cite
balance — all clean) and a one-line `latexmk` command. The source is
self-contained and needs only standard packages plus `IEEEtran.cls`, which any
IEEE author's TeX Live installation has.

**Do not** treat any pre-existing PDF in the original package as the PDF of this
source: those were built by the author's toolchain from the *uncorrected* file.

## R2 — Two full-text comparisons are unverified

Remark 4.5 (attribution of the orbit-length restriction to [DPI2023, Thm 4]) and
Remark 7.4 (numerical agreement of the mean with [DP2025, Thm 3.3]) could only
be checked at abstract/metadata level here. If either is inaccurate it is a
one-sentence repair, not a structural problem. No paywalled full text was read,
and none is claimed to have been read.

## R3 — Novelty is "no prior statement located", not "proved new"

The joint enumerator, the `2^{#orbits}` LCD count, the variance formulas and the
zero-covariance corollary were not found in the literature reachable from this
sandbox. That is an absence-of-evidence finding. A systematic citation-graph
sweep (forward citations of DPI2023/DP2025, the Li–Shi and Bouyuklieva mass-
formula line, and the multi-twisted/galois-hull literature) was not performed.

## R4 — Examples 9.4–9.6 not independently reproduced

E4 uses 2187 assignments over F_8 with n=14; E5/E6 involve two components and a
twist of order four. Full linear-algebra reproduction exceeded the time budget.
The identities those examples illustrate are verified on 10 smaller families,
and E1–E3 were reproduced (E3 cell-for-cell). A referee asking for the E4
table would get an honest "not re-derived here".

## R5 — Cosmetic typography not addressed

Three overfull lines (~22.8pt near the line-877 region, ~26.6pt near 1168,
~49.7pt near 1258 in the base file) were reported by the author's build. Without
a compiler they cannot be located reliably, and blind line-breaking is exactly
the kind of unverified change the protocol forbids. Deferred with the build.

## R6 — Scope statements that a referee may push on

* Enumeration is over **labeled** assignments, not equivalence classes. The
  paper says so twice; a referee may still ask for a monomial-equivalence
  version. That is future work, correctly listed as such.
* Reduced alphabets only (product of fields). Chain rings are explicitly out of
  scope; the neighbouring literature (DIMP2026, DPC2025, ES2026) does cover
  rings, so the positioning must stay precise.
* `P = 1` gives hull dimension zero throughout the family; this is correct but
  striking, and the paper explains it via the edge term rather than hiding it.

## R7 — Reproducibility of the *paper's* scripts

The package's `code/validate_*.py` were deliberately not used as evidence.
Their claimed outputs (≈48 edge cases, 1,800 mean comparisons, 2,187 orientation
checks) are **unverified** and are not cited as support anywhere in this audit.
The independent verifier is the evidence.
