# P1-21 — Independent Proof Audit of the Proposed Consequences R1–R4

**Object audited:** `P1_20_NEW_CONSEQUENCES.md` and `code/validate_p1_20.py`, against the frozen blueprint (`02_THEOREM_BLUEPRINT.md`, SHA-256 `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff`, unchanged), the manuscript (Theorems 5.2, 6.1, 6.3; Corollaries 7.3, 7.4; Proposition 6.4), and the proof packages P1-04/P1-05/P1-06. Repository at audit start: commit `0da7e45`, local = remote, clean.

**Audit method.** Each proof was re-derived from the definitions, not checked against its own text. Exact computation (fresh audit-side enumeration, Section 6) was used only as corroboration. **No adoption decision is made; R1–R4 and N1–N3 all remain PROPOSED. The frozen blueprint and manuscript are not edited. No novelty claim is made; Gate G1 remains DEFERRED.**

**Standing notation.** One orbit: length `L >= 1`, weight `w >= 1`, exponents `alpha_0,...,alpha_{L-1} in {0,...,P}`, indices mod `L`. Per-orbit contributions (T4/manuscript Theorem 5.2): code `K(alpha) = w * sum_i (P - alpha_i)`, hull `H(alpha) = w * sum_i min(P - alpha_i, alpha_{i-1})`. Global dimensions are sums over orbits/components; `D := sum_O P w_O L_O` is the maximum code dimension (shown below to equal `n * sum_s m_s`). Uniform labeled model for probabilistic statements. Combinatorial identities are in `Z[u,z]` for integer `P >= 1`; code realization needs the frozen hypotheses.

**Verdicts in one line each** (details and proofs below): **R1 correct** (complete involution proof; genuinely new joint content). **R2 correct** (matrices, orientation, boundary conditions verified; genuine distribution refinement of C4; one notation overload flagged). **R3 correct for every `P >= 1`, odd or even** (but it is the normalized form of N3 — not an independent second result). **R4 correct** (generic Cayley–Hamilton recurrence; only the `P=1` case is an explicit closed form — scope must be stated that way). **No statement among R1–R4 is refuted; no correction to any statement is required.** Two wording fences are recorded in Section 7.

---

## 1. R1 — the symmetry `N(K,H) = N(D-K,H)`

### 1.1 The map, stated on the full labeled assignment space

A global labeled assignment is the disjoint union of its orbit restrictions `alpha^{(O)} in {0,...,P}^{L_O}` (manuscript Theorem 6.3 / T1). Define `Phi` orbit by orbit: for `alpha in {0,...,P}^L`,

```
Phi(alpha)_i := P - alpha_{-i}        (indices modulo L).
```

**`Phi` is an involution.** `Phi(Phi(alpha))_i = P - Phi(alpha)_{-i} = P - (P - alpha_{-(-i)}) = alpha_i`. Hence `Phi` is a bijection of each orbit cube, and the orbitwise product map is a bijection (indeed an involution) of the full labeled assignment space (Cartesian product over all `(s,O)`). No hypothesis beyond the orbit decomposition is used; in particular compatibility/field structure is irrelevant to this combinatorial step — it enters only through T4/T5 identifying the cube sums with code/hull dimensions.

### 1.2 Code dimension transforms as claimed

`K(Phi(alpha)) = w * sum_i (P - Phi(alpha)_i) = w * sum_i alpha_{-i} = w * sum_i alpha_i` (reindexing a cyclic sum). Since `K(alpha) = w * sum_i (P - alpha_i) = wPL - w * sum_i alpha_i`, we get `K(Phi(alpha)) = PwL - K(alpha)` per orbit. Summing over orbits: `dim C(Phi(a)) = D - dim C(a)` with `D = sum_O P w_O L_O`. (Consistency of `D`: per component `sum_O w_O L_O = m_s * sum_{f in F_s} deg f = m_s n_0`, the distinct irreducible factors of `x^{n_0} - mu_s` having degrees summing to `n_0`; hence `D = P n_0 sum_s m_s = n sum_s m_s`, the ambient `F_q`-dimension — as it must be, since `dim C + dim D(C) = n sum_s m_s`.)

### 1.3 Hull dimension is preserved

`H(Phi(alpha)) = w * sum_i min(P - Phi(alpha)_i, Phi(alpha)_{i-1}) = w * sum_i min(alpha_{-i}, P - alpha_{-i+1})`. Substituting `j = -i + 1` (a bijection of `Z/LZ`), the `i`-th term is exactly the original hull term at position `j`, namely `min(P - alpha_j, alpha_{j-1})`. So the hull sums are equal **term by term after reindexing** — no averaging or identity of totals is needed. Therefore `H(Phi(alpha)) = H(alpha)` per orbit, and globally `dim Hull(Phi(a)) = dim Hull(a)`.

Combining 1.2–1.3: `Phi` pairs assignments of joint type `(K,H)` with assignments of type `(D-K,H)`, bijectively. Hence `N(K,H) = N(D-K,H)` for all integers `K,H` (with `N = 0` off the support), equivalently `E(u,z) = u^D E(u^{-1},z)` as polynomials (the right side is a polynomial because `E` has `u`-degree at most `D` and the identity is coefficientwise). Corollary R1.1 follows: summing over `H` gives `Pr(dim C = K) = Pr(dim C = D-K)`, so whenever the conditioning value has positive probability the normalized conditional laws of `dim Hull` at `K` and `D-K` coincide, and so do all conditional moments. ∎

### 1.4 Edge cases and hypothesis check

- `L = 1`: `Phi(alpha_0) = P - alpha_0` (reversal is trivial); hull term `min(P-a,a)` is invariant under `a -> P-a`; code `K -> Pw - K`. Holds.
- `P = 1`: exponents binary; `Phi` is complement composed with reversal; hull counts `1->0` transitions, preserved by the termwise computation above. Holds.
- `w > 1`: `w` is a common factor of both contributions; the argument is unchanged (audited at `w = 2, 3`).
- The reversal is what makes 1.3 termwise. (Audit remark, **not** a claim: dropping the reversal — complement alone — produced no counterexample on the audited grid `P <= 4, L <= 4`, so this audit does **not** assert that reversal is necessary; R1's proof neither needs nor makes that assertion. No use is made of this remark.)
- Hypotheses: the identity for the *enumerator polynomial* is exactly as strong as T5/T6; no new field hypothesis is introduced. For `P` not a prime power it remains a true polynomial identity about the cube sums, with no code interpretation — same status as T5's remark in the manuscript.

### 1.5 Verdict and genuine content

**R1 is CORRECT, with a complete proof.** Genuine content: C2 gives only the code-dimension marginal (the `H`-summed shadow); the joint symmetry at fixed hull dimension and the conditional-law symmetry (R1.1) are not in C1–C7 or N1–N3. The proof is elementary (one involution), but the statement is a real structural fact about `E(u,z)`, e.g. it halves the independent joint coefficients and forces the symmetric conditional-mean pattern seen in Section 5 of P1-20.

---

## 2. R2 — restricted self-orthogonal / dual-containing enumerators

### 2.1 From the C4 criteria to the matrices

Audited inputs (manuscript Corollary 7.4, proved in P1-05 Section 5): on every orbit edge (previous `a = alpha_{i-1}`, current `b = alpha_i`, indices mod `L`):

```
C(a) self-orthogonal  iff  a + b >= P on every edge;   then Hull = C, so dim Hull = dim C.
C(a) dual-containing  iff  a + b <= P on every edge;   then Hull = D(C).
```

Also from T3/Corollary 7.4's proof: per orbit, `dim D(C) = w * sum_i alpha_{i-1} = w * sum_i alpha_i` (cyclic reindexing), while `dim C = w * sum_i (P - alpha_i)`.

**Self-orthogonal matrix.** `S_w(t)_{a,b} = t^{w(P-b)}` if `a+b >= P`, else `0`. In `tr(S_w(t)^L)`, the trace expansion (as in T5) sums over closed walks `a_0 -> a_1 -> ... -> a_{L-1} -> a_0`; the step `a_{j-1} -> a_j` contributes the factor for edge `j`, including the **closing edge** `a_{L-1} -> a_0`, which is precisely the orbit-boundary condition (edge `0` with predecessor `alpha_{L-1}`). Every closed walk is one exponent tuple, admissibility is enforced edge by edge, and the product of step weights is `t^{w * sum_j (P - a_j)} = t^{K(alpha)}`. Hence `tr(S_w(t)^L) = sum_{alpha SO on this orbit} t^{K(alpha)}`. Setting `t = u z` gives the joint weight `u^{K} z^{K} = u^{dim C} z^{dim Hull}` on this family. **Orientation check:** the exponent uses the *current* vertex `b`, matching T5's convention (row = previous, column = current); because both contributions are cyclic sums, a transposed reading would give the same trace polynomial here, but the stated orientation is the one consistent with T5. **Boundary `L=1`:** the trace is the diagonal sum over `2a >= P` of `t^{w(P-a)}` — the self-loop condition `alpha_0 + alpha_0 >= P`, correct.

**Dual-containing matrix.** `D_w(u,z)_{a,b} = u^{w(P-b)} z^{w a}` if `a+b <= P`, else `0`. A closed walk contributes `u^{w sum_j (P-a_j)} * z^{w sum_j a_{j-1}} = u^{K(alpha)} z^{w sum_i alpha_i}`; on admissible (dual-containing) tuples, `w sum_i alpha_i` is the per-orbit hull dimension because `Hull = D(C)` and `dim D(C)` has the displayed form. So `tr(D_w(u,z)^L) = sum_{alpha DC on this orbit} u^{K(alpha)} z^{H(alpha)}`, with the closing edge enforcing the boundary condition at position `0` exactly as above; `L=1` gives the diagonal sum over `2a <= P`, correct.

**Global assembly.** Both admissibility conditions are conjunctions over orbits and both dimensions are sums over orbits, so the finite distributive law (as in T6) gives the global products `prod_s prod_O tr(...^{L_O})`. Specializing `u = z = 1` makes every admissible step weight `1`, recovering precisely the C4 counts `prod tr(B_P^{L_O})` and `prod tr((B'_P)^{L_O})`. ∎

### 2.2 The symmetry `S(K) = Dcal(D-K, K)` (notation renamed here, see 2.4)

Let `N_SO(K)` = number of self-orthogonal assignments with `(dim C, dim Hull) = (K,K)`, and `N_DC(K,H)` = number of dual-containing assignments with `(dim C, dim Hull) = (K,H)`. **Claim: `N_SO(K) = N_DC(D-K, K)`.** Proof: the per-orbit complement `beta_i = P - alpha_i` (no reversal) maps edge sums `a+b >= P` to `(P-a)+(P-b) <= P`, hence is a bijection from self-orthogonal to dual-containing assignments (applied orbitwise; inverse is itself). If `alpha` is self-orthogonal, then `dim C(beta) = sum_O w_O sum_i alpha_i = D - dim C(alpha) = D - K`, and `dim Hull(beta) = dim D(C(beta)) = sum_O w_O sum_i beta_i = sum_O w_O sum_i (P - alpha_i) = K` (equivalently `D - dim C(beta)`). Hence the bijection pairs the two counted sets. ∎ Summing over `K` recovers C4's "the two counts are equal" — the claim is its distribution-level refinement.

### 2.3 The `P=2, L=2, w=1` example reproduced directly

All nine tuples, with `(K,H) = (sum(2-alpha_i), sum min(2-alpha_i, alpha_{i-1}))` and edge sums taken cyclically:

| alpha | (K,H) | edge sums | SO (`>=2`)? | DC (`<=2`)? |
|---|---|---|---|---|
| (0,0) | (4,0) | 0,0 | no | yes |
| (0,1) | (3,1) | 1,1 | no | yes |
| (0,2) | (2,2) | 2,2 | yes | yes |
| (1,0) | (3,1) | 1,1 | no | yes |
| (1,1) | (2,2) | 2,2 | yes | yes |
| (1,2) | (1,1) | 3,3 | yes | no |
| (2,0) | (2,2) | 2,2 | yes | yes |
| (2,1) | (1,1) | 3,3 | yes | no |
| (2,2) | (0,0) | 4,4 | yes | no |

SO joint counts: `{(0,0):1, (1,1):2, (2,2):3}` (note `H=K` throughout, as forced). DC joint counts: `{(4,0):1, (3,1):2, (2,2):3}` — and indeed `N_DC(4-K, K)` for `K=0,1,2` gives `1,2,3 = N_SO(K)`, with orbit maximum `D = 4`, illustrating 2.2. **Coefficient interpretation:** in the SO enumerator, the coefficient of `t^K` (equivalently of `u^K z^K`) counts self-orthogonal assignments of code dimension `K`; in the DC enumerator, the coefficient of `u^K z^H` counts dual-containing assignments with code dimension `K` and hull (= dual) dimension `H`; at `u=z=1` both collapse to the C4 total `6 = tr(B_2^2)` for this orbit.

### 2.4 Verdict, genuine content, one notation flag

**R2 is CORRECT** — matrices derived from the criteria with correct orientation, exponents, closing-edge boundary conditions (including `L=1`), and the symmetry claim proved. Genuine content: C4 states criteria + two total counts + their equality; R2 adds the full dimension distributions inside both families and the distribution-level symmetry. It is a *refinement by the same closed-walk mechanism*, not a new method — that is the honest scope. **Notation flag (not an error):** P1-20 uses the letter `D` both for the global maximum dimension and (as `D(K,H)`) for the DC counting function, in a context where `D(C)` is also the dual code. If R2 is ever adopted, rename the counting function (e.g. `N_DC`) as done in 2.2 above. No text is changed now.

---

## 3. R3 — the LCD-conditioned code-dimension law

### 3.1 Proof from the exact LCD criterion

The LCD criterion (C3, manuscript Corollary 7.3, proof audited): `Hull(a) = 0` iff **every** orbit restriction is constant: `alpha = (0,...,0)` or `alpha = (P,...,P)`. (Boundary audit of that criterion: for `L=1` it reads `min(P-a,a)=0 iff a in {0,P}`, true for all `P`; for `L >= 2` the propagation argument excludes any interior value and any mixture of `0`/`P` values, for all `P >= 1`. No parity condition appears anywhere.)

Therefore the LCD event in the full assignment space is the Cartesian product over orbits of the 2-element sets `{0-orbit, P-orbit}`. The uniform distribution on a Cartesian product, conditioned on a Cartesian-product event, is the product of the uniform distributions on the factors. Hence, conditionally on LCD:

- the orbit restrictions are **independent**;
- each orbit takes its two admissible tuples with probability `1/2` each;
- the code contribution of the orbit is `P w_O L_O` (for `alpha = 0`: `w * sum_i P`) or `0` (for `alpha = P`), each with probability `1/2`.

That is, with independent `xi_O ~ Bernoulli(1/2)`, `dim C | LCD =d sum_O (P w_O L_O) * xi_O`. The probability generating identity `E[u^{dim C}|LCD] = 2^{-#orbits} prod_O (1 + u^{P w_O L_O})` is immediate, and:

```
E[dim C | LCD]  = (1/2) sum_O P w_O L_O = D/2,
Var(dim C | LCD) = sum_O (P w_O L_O)^2 * (1/4) = (P^2/4) * sum_O (w_O L_O)^2,
```

using independence (variances add) and `Var(xi_O) = 1/4`. ∎

### 3.2 `P` odd? Boundary cases

**`P` may be odd — no restriction.** The proof uses only `P >= 1` integer; parity never enters (contrast the `L=1` hull *variance* in C6, which is parity-split — a different quantity). In the code model `P = p^rho` may be an odd prime power (e.g. `P=3,9`) or a power of 2; the combinatorial statement is identical. Boundary cases: `P=1` (both binary tuples are LCD since `min(1-a,a)=0`; contributions `wL` or `0`); `L=1` (two point masses at `Pw` and `0`); arbitrary `w_O >= 1` (pure scaling of the Bernoulli weights); zero orbits (empty sum: `dim C = 0`, `D = 0`, mean/variance `0` — formulas agree, degenerate but consistent). All were included in the exact checks (Section 6), including odd `P=5` with mixed weights: configuration `(L,w) = (1,2),(2,1)` gives LCD count `4`, conditional mean `10`, variance `50`, matching `(P/2)(2+2) = 10` and `(25/4)(4+4) = 50`.

### 3.3 Verdict and duplication assessment

**R3 is CORRECT.** Duplication assessment (the important part): R3 is *exactly* N3 normalized by the C3 count, plus its first two moments. The Bernoulli representation and the mean/variance are one-paragraph consequences of C3 + uniformity. So: relative to **C3**, R3 adds real distributional content (a full conditional law, not just the count `2^{#orbits}`); relative to **N3**, it adds only the normalization and moments. **R3 and N3 must not be adopted as two separate results** — the adoptable item is "N3 in conditional-law form (R3)". Classification: correct, useful, low-depth corollary of the frozen C3.

---

## 4. R4 — the orbit-length recurrence

### 4.1 Derivation with dimensions and signs made explicit

Fix `P, w`. `T = T^{(P)}_w(u,z)` is an `m x m` matrix with **`m = P+1`**, over the commutative ring `R = Z[u,z]`. Its characteristic polynomial `chi_T(lambda) = det(lambda I - T)` is monic of degree `m` with coefficients in `R`. Write it as `chi_T(lambda) = lambda^m - c_1 lambda^{m-1} - ... - c_m` (so `c_j = -[lambda^{m-j}] chi_T`). Cayley–Hamilton over a commutative ring gives `chi_T(T) = 0`, i.e. `T^m = c_1 T^{m-1} + ... + c_m I`. Multiplying by `T^L` (`L >= 0`) and taking the trace, with `s_L := tr(T^L)` for `L >= 1` and the **formal** `s_0 := tr(I) = m = P+1`:

```
s_{L+P+1} = c_1 s_{L+P} + ... + c_{P+1} s_L        for all L >= 0.   ∎
```

The coefficients `c_j` depend on `(P, w, u, z)` (through `T_1(u^w, z^w)` for general `w`) but **not** on `L`. "Order at most `P+1`" is the correct wording: the trace sequence may satisfy a lower-order recurrence for special `(u,z)`; minimality is not claimed and not needed. Note `L=0` is not an orbit length; `s_0` is only the auxiliary initial value that makes the recurrence valid from `L=0`.

### 4.2 Independent verification at `P=1`

For `w=1`, `T = [[u, 1], [u z, 1]]` (Proposition 6.4). Direct computation: `det(lambda I - T) = (lambda - u)(lambda - 1) - u z = lambda^2 - (1+u) lambda + u(1 - z)`. In the sign convention of 4.1, `c_1 = 1+u`, `c_2 = -u(1-z)`, so the predicted recurrence is `s_{L+2} = (1+u) s_{L+1} - u(1-z) s_L`. Initial values: `s_0 = 2` (trace of `I_2`), `s_1 = tr(T) = 1 + u`. Independent check at the next step: `T^2 = [[u^2 + u z, (1+u)], [u z (1+u), 1 + u z]]`-diagonal entries give `tr(T^2) = 1 + u^2 + 2 u z`, while the recurrence predicts `(1+u)(1+u) - 2u(1-z) = 1 + u^2 + 2 u z`. Agreement. (The full two-variable polynomial recurrence was also checked for `L = 0..6` by the P1-20 validator and again in Section 6.) The closed form `s_L = lambda_+^L + lambda_-^L` with `lambda_{+/-} = ((1+u) +/- sqrt((1-u)^2 + 4 u z))/2` holds in the quadratic extension `R[sqrt((1-u)^2+4uz)]`: both sides satisfy the same recurrence with the same initial values `2` and `lambda_+ + lambda_- = 1+u`; this argument is valid also when `lambda_+ = lambda_-` (discriminant `0`), where it reduces to `s_L = 2 lambda^L`. General `w`: substitute `(u,z) -> (u^w, z^w)`. ∎

### 4.3 Generic existence vs. new closed form — the honest separation

Cayley–Hamilton guarantees a linear recurrence with polynomial coefficients for the trace sequence of **any** finite matrix; that part of R4 is generic linear algebra, and for `P >= 2` the coefficients `c_j` are *not* given in closed form in P1-20 (they are computable, e.g. from `s_1,...,s_{P+1}` via Newton identities / Faddeev–LeVerrier, but computing them is not a closed form). The concrete new content of R4 is therefore exactly: (i) the observation that the orbit enumerators at fixed `P` form a linear-recurrent sequence in `L` of order `<= P+1` (nothing in C1–C7/N1–N3 relates different orbit lengths), useful for long-orbit computation; and (ii) the explicit two-term recurrence and closed form at `P=1`. **R4 must not be presented as a general closed form for `tr(T^L)`.** With that scope, **R4 is CORRECT**.

---

## 5. Comparison with C1–C7 and N1–N3; what is genuinely new

| Proposed | vs. existing statements | Genuinely new content (audited) |
|---|---|---|
| R1 | C2 gives the code marginal product; nothing joint at fixed `H` | Joint coefficient symmetry `N(K,H)=N(D-K,H)`; conditional hull law equal at `K` and `D-K` (R1.1). **New.** |
| R2 | C4 = criteria + counts at `u=z=1` + equality of totals | Full dimension distributions inside SO/DC families; distribution-level symmetry `N_SO(K)=N_DC(D-K,K)`. **New as distributions; same closed-walk mechanism as C4.** |
| R3 | C3 = count only; N3 = unnormalized product | As a conditional *law with mean/variance*: new vs. C3; **vs. N3 it is a restatement in normalized form** — adopt at most one of R3/N3. |
| R4 | T5 evaluates one `L`; no cross-`L` statement exists | Recurrence across orbit lengths (generic CH) + explicit `P=1` closed form. **New but low-depth; no general closed form.** |
| (P1-20 Section 5) | N1 (`Cov=0`) | The exact coefficient formula for `E[H|K]` is definitional; the *counterexample* (conditional means `0,1,1,0` at `P=1,L=3`) is the valuable part: it refutes the constant-conditional-mean strengthening and fences N1. Consistent with this audit (R1.1 explains the symmetry `0,1,1,0` of that pattern). |
| (P1-20 Section 6) | C5, C6, N2 | `Var(dim C +/- dim Hull) = Var C + Var H` and constant linear predictor are one-line consequences of N1+N2+C6. Correct; summary value only. |
| C7 (EAQECC) | — | R1–R4 have **no** bearing on C7; distances remain external. Nothing in P1-20 was claimed there, correctly. |

No item among R1–R4 is a *silent* restatement of a frozen corollary: R2 at `u=z=1` and R3 at `u=1` collapse to C4/C3 by design (recorded as specializations, not as content), and R3-vs-N3 duplication is between two *proposed* items, flagged in 3.3.

## 6. New exact checks (corroboration only; fresh parameters, audit-side code)

Fresh enumeration code written for this audit (not imported from `validate_p1_20.py`), exact integer/`Fraction` arithmetic; `P=6` instances test the polynomial identity only (not a prime power — same status as the manuscript's T5 remark):

- **R1 + R2 + R3 (orbit level)** at `(P,L,w) = (5,3,3), (5,5,1), (6,4,2), (7,3,3), (4,5,2)`: R1 symmetry holds coefficientwise in every case; at `(5,3,3), (6,4,2), (7,3,3)` both R2 restricted traces equal brute-force restricted enumeration exactly; per-orbit LCD admissible code contributions are exactly `{0, P w L}` in every case. All checks passed.
- **R3 at odd `P=5`**, configuration `(L,w)=(1,2),(2,1)` by complete enumeration: LCD count `4`, conditional mean `10`, variance `50` — equal to the formulas (3.2).
- **R4 evaluated recurrence**: at `(u,z) = (2,3)`, the trace sequences for `P=2` (`s_0..s_9 = 3, 11, 185, 2099, ...`) and `P=3` (`4, 27, 1673, 52731, ...`) satisfy the order-`(P+1)` recurrence built from the evaluated characteristic polynomials; the `P=1` polynomial recurrence was rechecked for `L=0..6` (`s_1 = 1+u`, `s_2 = 1+u^2+2uz`). All checks passed.
- The committed P1-20 validator was also re-run unmodified: `ALL P1-20 VALIDATION CHECKS PASSED` (173 checks). Finite checks corroborate; the proofs in Sections 1–4 are the evidence.

**No counterexample to any of R1–R4 was found**, in the proofs or on the grids. Accordingly there is no correction proposal for any statement; the only recommended changes are the wording fences in Section 7, and they concern future adoption text, not the P1-20 report's correctness.

## 7. Verdicts and wording fences (for any future adoption decision — none made here)

| Result | Verdict | Required scope wording if ever adopted |
|---|---|---|
| R1 (+R1.1) | **Correct; proof complete; genuinely new joint content.** Strongest of the four as a statement. | State `D = n sum_s m_s`; keep "joint/fixed-hull" emphasis vs. C2. |
| R2 (+symmetry) | **Correct; matrices/orientation/boundaries verified; genuine distribution refinement of C4.** | Rename the DC counting function (`N_DC`) to avoid the `D` overload; present as refinement of C4, `u=z=1` specialization noted. |
| R3 | **Correct for all `P>=1` (odd included); low-depth corollary of C3.** | Adopt only as "N3, conditional-law form" — never as a second result alongside N3. |
| R4 | **Correct; generic (Cayley–Hamilton) + explicit only at `P=1`.** | Say "order at most `P+1`"; never "closed form" for `P>=2`; `s_0` flagged as formal. |

Rejected / not promoted (unchanged from P1-20, re-confirmed here): constant conditional hull mean at fixed code dimension (**false**, counterexample in P1-20 Section 5, consistent with R1.1's symmetry); independence of the two dimensions (**false**); palindromy in the hull variable (**false**, `{0:2, 1:6}` at `P=1,L=3`); naive monotonicity in `L` (ill-posed); Perron–Frobenius growth (standard background, not a result).

**Overall audit conclusion:** R1–R4 are mathematically correct as stated in P1-20, under exactly the hypotheses recorded above. Their depths differ: R1 is a clean new structural symmetry; R2 is a genuine distributional refinement of C4 by a known mechanism; R3 is N3 in its useful normalized form; R4 is a generic recurrence with an explicit simple-root case. All remain **PROPOSED**; the frozen blueprint and manuscript are untouched by this audit, and no novelty or publication-readiness claim is made (Gate G1 DEFERRED).
