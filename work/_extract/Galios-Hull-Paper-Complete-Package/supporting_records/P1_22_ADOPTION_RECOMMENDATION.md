# P1-22 — Adoption Recommendation for the Proposed Consequences (Integration-Readiness Check)

**Inputs:** `P1_20_NEW_CONSEQUENCES.md` (results R1–R4), `P1_21_PROOF_AUDIT.md` (independent re-derivation; all four correct with scope fences), the manuscript `P1_15_MANUSCRIPT_DRAFT.md/.tex`, the frozen blueprint (`02_THEOREM_BLUEPRINT.md`, SHA-256 `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff`, unchanged), `P1_15_OPTIONAL_COROLLARIES.md` (N1–N3), and the gap register. Repository at start: commit `dffd829`, local = remote, clean.

**This file is a recommendation only.** It is not an approval, and it edits neither the frozen blueprint nor the manuscript. Every candidate remains PROPOSED until a dated Commander decision (GAP-17 rule). No novelty claim is made; **Gate G1 remains DEFERRED** (L1 unread at theorem level, P1-19), so nothing here may be worded as "new" or "first" in the manuscript sense — the classifications below concern only mathematical correctness, non-duplication, and fit.

**Notation plan for any future integration (binding on the plan, to remove the P1-21 overload flag):**
- `Delta := n * sum_s m_s` — the maximum/ambient `F_q`-dimension (never bare `D`, which is reserved for the dual code `D(C)`).
- `N_SO(K)` — number of self-orthogonal labeled assignments with `dim C = K` (equivalently joint type `(K,K)`).
- `N_DC(K,H)` — number of dual-containing labeled assignments with `(dim C, dim Hull) = (K,H)`.
- `a_O := P * w_O * L_O` (the per-orbit LCD/Bernoulli weight; note `sum_O a_O = Delta`).
- `s_L^{(P,w)}(u,z) := tr((T^{(P)}_w(u,z))^L)` if R4 is ever displayed.

**Standing assumptions for all statements below:** the manuscript's hypotheses — `A = prod_s K_s` square-free affine with labeled components, common `n = P n_0`, `gcd(n_0,p)=1`, compatible twists `lambda_s^{1+p^{d_s-k}}=1`, code-first pairing, labeled exponent assignments; probabilistic statements use the uniform labeled model. Per orbit: `K(alpha) = w sum_i (P-alpha_i)`, `H(alpha) = w sum_i min(P-alpha_i, alpha_{i-1})`, indices mod `L`.

---

## 1. R1 — Joint complement–reversal symmetry → **RECOMMENDED for adoption**

**Exact statement (manuscript-ready form).** Let `Delta = n * sum_s m_s`. For all integers `K,H`,
`#{a : (dim C(a), dim Hull(a)) = (K,H)} = #{a : (dim C(a), dim Hull(a)) = (Delta-K, H)}`, equivalently `E(u,z) = u^{Delta} E(u^{-1}, z)`. Consequently, whenever `Pr(dim C = K) > 0`, the conditional law of `dim Hull` given `dim C = K` equals that given `dim C = Delta-K`.

**Verification of `Delta` against the manuscript's notation.** Per component `s`, `sum_{O in O_s} w_O L_O = m_s * sum_{f in F_s} deg_{K_s} f = m_s n_0`, because `F_s` is the set of distinct monic irreducible factors of the degree-`n_0` polynomial `x^{n_0} - mu_s` (manuscript Section 2). Hence `sum_O P w_O L_O = P n_0 sum_s m_s = n sum_s m_s = Delta`. This matches the manuscript exactly: `dim_{F_q}` sums carry the factor `m_s` per component (Theorem 5.2), each component code has `K_s`-dimension at most `n`, and `dim C + dim D(C) = Delta` — so `Delta` is both the maximum code dimension and the ambient dimension, as the symmetry requires. The map `Phi(alpha)_i = P - alpha_{-i}` is an involution of the full labeled assignment space (orbitwise product), sends `dim C` to `Delta - dim C` by the cyclic-sum computation, and preserves `dim Hull` termwise after the reindexing `j = -i+1` (P1-21 Section 1: proof complete under every stated hypothesis; `L=1`, `P=1`, `w>1` edge cases verified; the polynomial identity needs no field hypothesis beyond T5/T6 themselves).

**Proof location:** P1-20 Section R1; independently re-derived in P1-21 Section 1 (verdict: correct, complete).
**Validation evidence:** `code/validate_p1_20.py` (grid `P in {1..4}`, `L in {1..4}`, `w in {1,2}`, coefficientwise); P1-21 fresh parameters `(P,L,w) = (5,3,3), (5,5,1), (6,4,2), (7,3,3), (4,5,2)` (the `P=6` case tests the polynomial identity only). All passed; evidence only, proof is the involution.
**Relationship to existing results:** C2 is the `H`-summed (marginal) shadow; no frozen corollary states the joint symmetry or the conditional-law consequence. No duplication.
**Recommended placement:** Section 6, as a corollary immediately after Theorem 6.3 (integration phase handles the automatic renumbering of Proposition 6.4). One paragraph statement + involution proof; the conditional-law sentence as a second short corollary or remark.
**Decision: RECOMMENDED** — strongest of the candidates: complete elementary proof, genuinely joint content, useful (halves independent joint coefficients; explains the symmetric conditional pattern).

## 2. R2 — Restricted SO/DC enumerators → **RECOMMENDED for adoption**

**Exact statement (with cleaned notation).** Per orbit define `S_w(t)_{a,b} = t^{w(P-b)}` if `a+b >= P` else `0`, and `G_w(u,z)_{a,b} = u^{w(P-b)} z^{w a}` if `a+b <= P` else `0` (row `a` = previous exponent, column `b` = current, the T5/Theorem 6.1 convention; the closing edge in the trace is the orbit-boundary edge). Then
`sum_{a self-orthogonal} t^{dim C(a)} = prod_s prod_O tr(S_{w_O}(t)^{L_O})` (joint form at `t = u z`, since `dim Hull = dim C` there), and
`sum_{a dual-containing} u^{dim C(a)} z^{dim Hull(a)} = prod_s prod_O tr(G_{w_O}(u,z)^{L_O})`.
Moreover `N_SO(K) = N_DC(Delta-K, K)` for all `K`.

**Verification against C4 and the transfer convention.** C4 (Corollary 7.4) gives the edge criteria `a+b >= P` (SO) / `<= P` (DC) and, via `dim D(C) = sum_O w_O sum_i alpha_i`, the hull dimension on DC tuples; the matrices attach exactly the per-edge code weight `w(P-b)` and, for DC, the dual/hull weight `w a` from the previous vertex, whose cyclic sum is `w sum_i alpha_i`. Boundary cases confirmed in P1-21: `L=1` reduces to the diagonal conditions `2a >= P` / `2a <= P`; `u=z=1` collapses both sides to the C4 counts `prod tr(B_P^{L_O})`, `prod tr((B'_P)^{L_O})`. The P1-20 `(P=2,L=2)` example was reproduced by hand in P1-21 (SO `{(0,0):1,(1,1):2,(2,2):3}`; DC `{(4,0):1,(3,1):2,(2,2):3}`, with `N_DC(4-K,K) = N_SO(K)`). The bare letter `D` for counting functions is **removed** from this plan (`N_SO`, `N_DC` above; `Delta` for the constant), resolving the P1-21 notation flag.

**Proof location:** P1-20 Section R2; re-derived in P1-21 Section 2 (correct; orientation/boundary verified).
**Validation evidence:** P1-20 validator (restricted traces = brute force on the grid, including `H=K` on SO and `H = w sum alpha` on DC tuples); P1-21 fresh cases `(5,3,3), (6,4,2), (7,3,3)`. All passed.
**Relationship:** a distribution-level refinement of C4 (same closed-walk mechanism; C4 is exactly the `u=z=1` specialization, to be stated as such). Not a restatement, provided the text presents the *distributions* as the content and the count collapse as a check.
**Recommended placement:** Section 7, as a new corollary immediately after Corollary 7.4, including the `N_SO(K) = N_DC(Delta-K,K)` symmetry and the `P=2,L=2` counts as a worked line.
**Decision: RECOMMENDED** — genuine new distributions, complete proof, natural fit next to C4.

## 3. R3 + N3 — one unified LCD candidate → **RECOMMENDED for adoption (as a single result only)**

**Unified exact statement.** (i) (N3 form) `sum_{a : Hull(a)=0} u^{dim C(a)} = prod_O (1 + u^{a_O})`, `a_O = P w_O L_O`. (ii) (R3 form) Under the uniform labeled model conditioned on `Hull(a) = 0`, `dim C =d sum_O a_O xi_O` with `xi_O` independent `Bernoulli(1/2)`; hence `E[dim C | LCD] = Delta/2` and `Var(dim C | LCD) = (P^2/4) sum_O (w_O L_O)^2`.

**Verification.** The LCD criterion (C3/Corollary 7.3: hull zero iff every orbit is constant `0` or `P`) was re-audited in P1-21 for all `L` and all `P >= 1`; conditioning a uniform product distribution on this product event gives per-orbit independence and the two equally likely options with code contributions `a_O` and `0`. The Bernoulli parameters `a_O = P w_O L_O` are correct for arbitrary `P` (odd allowed — parity never enters; contrast the parity-split `L=1` hull variance in C6, a different quantity), arbitrary `L_O`, and arbitrary weights `w_O >= 1`; boundary cases `P=1`, `L=1`, and the degenerate zero-orbit case are consistent (P1-21 Sections 3.1–3.2). `sum_O a_O = Delta` by the same factor-degree computation as in Section 1 above, so the mean `Delta/2` is in manuscript notation.

**Proof location:** P1-20 Section R3 (= P1-15 companion N3); re-derived P1-21 Section 3.
**Validation evidence:** P1-20 validator (E5-type configuration: LCD count `16`, mean `21 = Delta/2`, variance `185`); P1-21 odd case `P=5`, `(L,w)=(1,2),(2,1)`: count `4`, mean `10`, variance `50`, matching formulas.
**Relationship:** C3 is the `u=1` count. R3 and N3 are **the same result** in unnormalized vs. normalized form — presenting them as two contributions would be duplication and is **rejected** (Section 5). The unified corollary's added value over C3 is the full conditional law.
**Recommended placement:** Section 7, as a single corollary immediately after Corollary 7.3, stated in the order (i) generating function, (ii) conditional law with mean/variance.
**Decision: RECOMMENDED as one unified corollary** (low-depth but exact and quotable; the conditional-law form is the useful one).

## 4. R4 — Orbit-length recurrence → **DEFERRED (supporting proposition; not for the main text now)**

**Exact statement.** For fixed `P,w` and `s_L = s_L^{(P,w)}(u,z)` (with the formal `s_0 := P+1`), there exist `c_1,...,c_{P+1} in Z[u,z]`, independent of `L`, with `s_{L+P+1} = sum_j c_j s_{L+P+1-j}` for all `L >= 0` (characteristic polynomial of the `(P+1) x (P+1)` matrix `T^{(P)}_w`, Cayley–Hamilton). At `P=1` only: `s_{L+2} = (1+u) s_{L+1} - u(1-z) s_L`, `s_0=2`, `s_1=1+u`, with `s_L = lambda_+^L + lambda_-^L`, `lambda_{+/-} = ((1+u) +/- sqrt((1-u)^2+4uz))/2` (general `w` by `(u,z) -> (u^w,z^w)`).

**Assessment.** Correct (P1-21 Section 4; `P=1` independently verified, including `s_2 = 1+u^2+2uz` by direct squaring and by enumeration). But per task item 4: the general recurrence is the *generic* Cayley–Hamilton fact for any matrix; P1-20/P1-21 demonstrate no concrete enumerator consequence in the manuscript beyond faster long-orbit computation, and for `P >= 2` there is no closed form (coefficients are computable, e.g. via Newton identities, which is not a closed form; minimality of the order is not claimed). The explicit closed form is therefore **restricted to `P=1`**, the already-transparent simple-root case.
**Recommended placement:** none in the main text at this time. Keep as a supporting proposition in the P1-20/P1-21 record; if the integration phase wants it, at most a two-line remark after Theorem 6.1 ("at fixed `P` the traces are linear-recurrent in `L` of order at most `P+1`; at `P=1`, ...") with the `P>=2` closed-form wording prohibited.
**Decision: DEFERRED** — correct but generic; revisit only if a concrete application (e.g. a long-orbit family where the recurrence is actually used) is added.

## 5. Rejected items and counterexample record (do not integrate in any form)

1. **Presenting R3 and N3 as two results** — rejected: duplication (Section 3).
2. **"Conditional hull mean at fixed code dimension is constant"** — false: `P=1,L=3,w=1`, joint distribution `{(0,0):1,(1,1):3,(2,1):3,(3,0):1}` gives conditional means `0,1,1,0` despite `Cov=0` (N1). The pattern is exactly the R1 symmetry — a further reason R1 is the right way to say something here.
3. **Independence of `dim C` and `dim Hull`** — false: same distribution, `Pr(K=2)Pr(H=1) = 9/32 != 3/8 = Pr(K=2,H=1)`. N1 wording must remain "uncorrelated".
4. **Palindromy in `z`** — false: hull marginal `{0:2, 1:6}` in the same example.
5. **A general (`P >= 2`) closed form for `tr(T^L)`, or minimality of the R4 order** — not established; prohibited wording (Section 4).
6. **Bare `D` for the maximum dimension or DC counting function** — rejected notation (dual-code clash); `Delta`, `N_DC` mandated in Section 1's notation plan.
7. Naive coefficient monotonicity in `L` and Perron–Frobenius growth **as results** — ill-posed resp. standard background (P1-20 Section 7, P1-21 Section 7); not integrated.

## 6. Summary of recommendations

| Candidate | Decision | One-line reason |
|---|---|---|
| R1 (joint symmetry + conditional law) | **Recommended** | Complete involution proof; genuinely joint content beyond C2; clean placement after Theorem 6.3 |
| R2 (SO/DC restricted enumerators + symmetry) | **Recommended** | Complete proof; full distributions refining C4's counts; fits after Corollary 7.4; notation cleaned (`N_SO/N_DC`, `Delta`) |
| R3/N3 unified (LCD conditional law) | **Recommended (single corollary)** | Exact Bernoulli law/mean/variance from C3; useful form of N3; duplication avoided by unifying |
| R4 (orbit-length recurrence) | **Deferred** | Correct but generic Cayley–Hamilton; explicit closed form `P=1` only; no demonstrated concrete consequence yet |
| Items in Section 5 | **Rejected** | False (with counterexamples), duplicative, or prohibited wording/notation |

Also recorded for completeness: N1/N2 (covariance package) were **not** re-decided in this phase — they remain candidates in `P1_15_OPTIONAL_COROLLARIES.md` with the P1-20 Section 6 assessment (clean but modest; "uncorrelated, not independent" fencing mandatory). Validators relevant to this recommendation were re-run for this phase: `validate_p1_20.py` (exit 0, output byte-identical to its saved record) and `validate_p1_14.py` (exit 0, byte-identical), confirming the frozen core and the candidate evidence base are unchanged. If the Commander adopts any item, integration must proceed by a dated blueprint correction note under GAP-17 with the notation plan above; until then the blueprint, the manuscript, and all statuses are exactly as they were.
