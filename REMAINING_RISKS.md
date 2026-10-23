# REMAINING_RISKS.md (round 2)

Ordered by consequence. R1 from round 1 is closed; the rest are narrowed.

## R1 — CLOSED. PDF now exists and was inspected

Round 1 had no TeX engine. Round 2 builds in CI (TeX Live container) and the
built PDF is committed. 17 pages, 0 errors, 0 overfull boxes, every page
rendered and read. See `BUILD_REPORT.md`.

## R2 — DP2025 full text not read (highest-value remaining check)

The AIMS full-text link resolves to a paywall. The manuscript's Remark 7.4
asserts that its mean agrees with [DP2025, Thm 3.3] and that "no variance or
covariance formula is given there". The first half is supported by the abstract
(which does present average-dimension formulas); the **second half is not
verifiable without the full text**. If DP2025 does contain second-order
results, one clause of Remark 7.4 needs revising. Everything else stands.

Similarly, Remark 4.5 attributes an orbit-length restriction (1, 2 and 4) to
[DPI2023, Thm 4] on abstract-level information only.

## R3 — Novelty remains "not located", not "proved new"

DIMP2026 was read in full (arXiv HTML) and does not contain the joint
enumerator, the moments, or the transfer-matrix formulation; that is a solid
data point. DP2025 and DPI2023 were not read in full. No systematic forward-
citation sweep was performed. The manuscript makes no priority claim, which
keeps this risk proportionate.

## R4 — ORCID not independently verified

`0009-0009-1169-3264` is printed in the author footnote. `pub.orcid.org` is
unreachable from this sandbox, so the iD's match to the author is unverified.
This is a 30-second check for the author and must not be assumed.

## R5 — Definition-level coverage of Example 9.4 is sampled

The aggregate claims for Example 9.4 are exhaustive (all 2187 assignments via
the exact enumerator), and the orientation claim is exhaustive (2187/2187). The
*definition-level* dual/hull recomputation for 9.4 used a fixed-seed sample of
64 assignments, because a full sweep would exceed the per-task time cap. No
mismatch was found.

## R6 — Package-claimed computations remain unverified

The numbers the paper attributes to its own scripts — 2769 field-level
assignments, 52 (P,L) pairs, and the various small cases in
`code/validate_audit_fixes.py` — were **not** re-run and are not relied on.
The independent verifier substitutes for them where they matter. The paper's
§IX sentence that the proofs do not depend on these computations is correct.

## R7 — Scope statements a referee may still push on

Labeled assignments only (not monomial-equivalence classes); reduced alphabets
only (no chain rings); no distances. All three are explicitly stated in §X, so
they are scope limits rather than defects.

## R8 — Cosmetic

One underfull box in the author footnote. No action needed.
