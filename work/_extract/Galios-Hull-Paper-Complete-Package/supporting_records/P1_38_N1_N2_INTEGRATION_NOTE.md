# P1-38 — N1/N2 Integration Note

**Date:** 22 October 2026
**Baseline:** remote branch commit `549388036a720aa19158a6012c3e51f089d45fe2`.
**Action:** The previously developed candidate results N1 and N2 from
`P1_15_OPTIONAL_COROLLARIES.md` were integrated into the manuscript as one
concise result, Corollary 8.5 (`cor:secondorder`) in
`P1_15_MANUSCRIPT_DRAFT.tex` and the synchronized
`P1_15_MANUSCRIPT_DRAFT.md`, immediately after Theorem 8.4.

Integrated statement, under the uniform labeled model:

\[
\operatorname{Var}\big(\dim_{\mathbb F_q} C\big)
= \frac{P(P+2)}{12}\sum_s\sum_{f\in\mathcal F_s} w_f^2,
\qquad
\operatorname{Cov}\big(\dim_{\mathbb F_q} C,\,
\dim_{\mathbb F_q}\mathrm{Hull}_k(C)\big)=0.
\]

The wording is fenced as “uncorrelated”, not “independent”.

**Justification.** Full proofs already existed in the P1-15 optional
corollaries file: the variance formula follows from the independent uniform
exponents in Theorem 5.2, and the covariance vanishes orbit by orbit through
the \(+\gamma_P/-\gamma_P\) cancellation, with the \(L=1\) case handled by
symmetry. The existing P1-14 validation record checks both formulas in exact
arithmetic on its orbit grid and field cases; no new mathematical claim
beyond N1/N2 was added.

**Blueprint.** The frozen blueprint file `02_THEOREM_BLUEPRINT.md` was not
edited; its SHA-256 remains
`ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff`.
This note is the dated adoption record for the integration.

**Status fences.** Mathematical scope is frozen after this integration. No
novelty, priority, or non-overlap claim is made; Gate G1 remains DEFERRED.
