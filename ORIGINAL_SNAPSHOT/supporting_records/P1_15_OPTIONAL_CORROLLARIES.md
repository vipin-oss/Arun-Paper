# P1-15 (companion) — Optional Candidate Corollaries N1–N3 (Pending Author Approval)

**Command:** P1-15 — Prepare the First Full Manuscript Draft (companion deliverable)  
**Date:** 21 October 2026

**Status: CANDIDATE RESULTS — PROVED, BUT NOT ADOPTED.** The three results below were proved completely in `P1_14_MATHEMATICAL_ADVANCEMENT.md` §4 and independently checked there (fresh symbolic derivation of the key constant `γ_P = P(P+2)/24`, plus exact rational enumeration in every test layer of `code/validate_p1_14.py`). They are **not** in the frozen blueprint `02_THEOREM_BLUEPRINT.md`, **not** used in `P1_15_MANUSCRIPT_DRAFT.tex` / `.md`, and must not be cited as results of the paper until the author/Commander adopts them (adoption, if desired, belongs in a dated blueprint correction note under the GAP-17 rule, exactly like the earlier PC-1…PC-5 items). This file is the holding place: full statements, full proofs, verification record, and precise insertion points.

**Standing model** (identical to the manuscript): hypotheses (G1)–(G6) of P1-05 / §2 of the draft; uniform distribution on labeled assignments; per orbit `O`, `A_i` iid uniform on `{0,…,P}`, `X_i = min(P−A_i, A_{i−1})` (indices mod `L = L_O`), orbit code contribution `w_O Σ_i (P−A_i)`, hull contribution `w_O Σ_i X_i`; `F(c) = E[min(c,U)] = c(2P−c+1)/(2(P+1))` (draft Lemma 8.1) and `μ_P = P(2P+1)/(6(P+1))` (draft Lemma 8.1) are used.

---

## N1 — Code dimension and hull dimension are uncorrelated

**Statement.** `Cov(dim_{F_q} C(a), dim_{F_q} Hull_{A,k}(C(a))) = 0` under the uniform labeled model — for every component/orbit configuration and every `P ≥ 1`. The two dimensions are **not independent** (see the remark): the only correct wording is “uncorrelated”.

**Lemma N1.1 (one shared variable, “self” pairing).** For independent `B, C` uniform on `{0,…,P}`, `Cov(B, min(B,C)) = P(P+2)/24 =: γ_P`.

*Proof.* Condition on `B = b`: `E[min(b,C)] = F(b)`, so `E[B·min(B,C)] = (1/(P+1)) Σ_b b·F(b) = (1/(2(P+1)^2)) Σ_b b²(2P+1−b)`. With `Σ_{b=0}^P b² = P(P+1)(2P+1)/6` and `Σ b³ = (P(P+1)/2)²`, the sum equals `(P/2)·(5P²+5P+2)/12`, hence `E[B·min(B,C)] = P(5P²+5P+2)/(24(P+1))`. Also `E[B]·E[min(B,C)] = (P/2)μ_P = P(4P²+2P)/(24(P+1))`. Subtracting: `γ_P = P(P²+3P+2)/(24(P+1)) = P(P+2)/24`. ∎

**Proof of N1.** Orbit blocks involve disjoint exponent variables, hence are independent (product model; draft Proposition 6.2 / P1-05 Prop. 3.1); cross-orbit covariance terms therefore vanish, and with `K_O = Σ_i (P−A_i)`, `S_O = Σ_j X_j` it suffices to show `Cov(K_O, S_O) = 0` for one orbit, since `Cov(dim C, dim Hull) = Σ_{s,O} w_O²·Cov(K_O, S_O)`. Expand: `Cov(K_O, S_O) = Σ_{i,j} Cov(P−A_i, X_j)`, where `X_j` depends only on `(A_j, A_{j−1})`.

- If `i ∉ {j, j−1}` (possible only for `L ≥ 3`): the two sides are functions of disjoint subfamilies of independent variables ⇒ covariance `0`.
- If `i = j`: `Cov(P−A_j, min(P−A_j, A_{j−1})) = γ_P` by Lemma N1.1 (with `B = P−A_j`, `C = A_{j−1}`).
- If `i = j−1` (requires `L ≥ 2`): `Cov(P−A_{j−1}, min(P−A_j, A_{j−1}))`. Put `C = A_{j−1}`, `B = P−A_j` (independent uniforms): this is `Cov(P−C, min(B,C)) = −Cov(C, min(B,C)) = −γ_P`, because `(B,C)` exchangeable gives `Cov(C, min(B,C)) = Cov(B, min(B,C))`.
- `L = 1`: the single term is `Cov(P−A, min(P−A, A))`. With `B = P−A` uniform, `min(B, P−B)` is invariant under `B ↦ P−B`, so `E[B·min(B,P−B)] = E[(P−B)·min(B,P−B)]`; averaging gives `E[B·min] = (P/2)·E[min] = E[B]·E[min]`, i.e. covariance `0`. (Both parity cases also confirmed symbolically in P1-14 Layer A.)

For `L ≥ 2` each `j` contributes exactly one `γ_P` (from `i=j`) and one `−γ_P` (from `i=j−1`) — for `L=2` these two indices exhaust `{0,1}`, for `L≥3` all other `i` contribute `0` — so `Cov(K_O, S_O) = L·(γ_P − γ_P) = 0`; for `L=1` it is `0` directly. Summing with weights `w_O²` over all orbits and components gives `0`. ∎

**Remark (uncorrelated ≠ independent).** At `P=1, L=2, w=1`: `Pr(dim C = 2) = 1/4`, `Pr(dim Hull = 1) = 1/2`, but `Pr(dim C = 2, dim Hull = 1) = 0 ≠ 1/8` (exact enumeration, P1-14 Layer B). Any use of N1 must say “uncorrelated”, never “independent”.

**Verification record.** `Cov = 0` exactly (rational arithmetic) in all 58 Layer-B orbit configurations, all six Layer-C field distributions, and the Layer-D two-component distribution of `code/validate_p1_14.py`; `γ_P` re-derived symbolically (Layer A).

**Insertion point if adopted:** manuscript §8, immediately after Theorem 8.4 (C6), as a theorem “The code and hull dimensions are uncorrelated”, with the dependence remark. It pairs naturally with N2.

---

## N2 — Variance of the code dimension

**Statement.** `Var(dim_{F_q} C(a)) = [P(P+2)/12] · Σ_s Σ_{f∈F_s} w_f²`, where `w_f = m_s·deg_{K_s} f`.

*Proof.* By T4 (draft Theorem 5.2), `dim_{F_q} C = Σ_{s,f} w_f (P − A_f)` with the `A_f` independent uniform on `{0,…,P}` (product model). `Var(P − A_f) = Var(U)` for `U` uniform on `{0,…,P}`: `E[U] = P/2`, `E[U²] = P(2P+1)/6`, so `Var(U) = P(2P+1)/6 − P²/4 = P(P+2)/12`. Independence ⇒ variances add with coefficients `w_f²`. ∎ Consistent with C5’s mean `E[dim C] = (n/2)·Σ_s m_s`.

**Verification record.** Per orbit `w²L·P(P+2)/12` on the whole Layer-B grid; all field cases (e.g. GF(8): `Var(C) = 14/3 = 7·(2·4/12)`); Layer-D global `190/3`.

**Insertion point if adopted:** manuscript §8, next to N1 (together N1+N2 complete the second-order summary of the two margins: means from C5, `Var(Hull)` from C6, `Var(C)` from N2, `Cov = 0` from N1).

---

## N3 — LCD refinement: joint (LCD, code-dimension) count

**Statement.** `Σ_{a : Hull(a) = 0} u^{dim_{F_q} C(a)} = ∏_{s} ∏_{O∈O_s} (1 + u^{P·w_O·L_O})`. At `u=1` this is C3 (`2^{#orbits}`).

*Proof.* By the C3 argument (draft Corollary 7.3), `Hull(a) = 0` iff on every orbit `α ≡ 0` or `α ≡ P`. The orbit’s code-dimension contribution (T4) is `w_O Σ_i (P−α_i)`, equal to `P·w_O·L_O` for `α ≡ 0` and to `0` for `α ≡ P`. Hence the per-orbit generating polynomial over LCD-admissible tuples is `1 + u^{P w_O L_O}`, and independence over orbits/components (T1, product assembly) gives the product. ∎

**Verification record.** Everywhere C3 was verified (`[z^0] = 2` per orbit on the Layer-B grid; field LCD counts; Layer-D convolution).

**Insertion point if adopted:** manuscript §7, immediately after Corollary 7.3 (C3), as its refinement corollary.

---

## Adoption checklist (for the author/Commander — Arena takes no decision)

1. Decide adopt / reject for each of N1, N2, N3 (they are independent of one another; N1 and N2 are natural as a pair).
2. If adopted: add a dated correction note to the blueprint under the GAP-17 rule and renumber into the manuscript (suggested: §7 N3 after C3; §8 N1+N2 after C6); if rejected: this file remains their record and the manuscript stands as drafted.
3. Either way: no statement in the current manuscript draft depends on N1–N3, so the draft needs no change beyond insertion if adoption is approved.
