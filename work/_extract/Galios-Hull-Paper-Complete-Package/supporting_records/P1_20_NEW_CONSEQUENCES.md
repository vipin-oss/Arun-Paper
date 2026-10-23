# P1-20 — New Rigorous Consequences of the Joint Enumerator (Proposed)

**Starting point (frozen, unchanged):** under the standing hypotheses (G1)–(G6) of P1-05 / manuscript Sections 2–6 (square-free affine product `A = prod_s K_s`, common `n = P n_0`, compatible twists, labeled components and orbit positions, code-first pairing),

```
E(u,z) = sum_{labeled a} u^{dim C(a)} z^{dim Hull(a)}
       = prod_s prod_O tr( (T^{(P)}_{w_O}(u,z))^{L_O} ),
T^{(P)}_w(u,z)_{a,b} = u^{w(P-b)} z^{w min(P-b,a)}   (a = previous exponent, b = current exponent).
```

**Status of everything below: PROPOSED, pending review.** Nothing here edits the frozen blueprint (`02_THEOREM_BLUEPRINT.md`, SHA-256 `ec2fd8d5...cf438cff`, re-verified), the manuscript, or any proof package. No literature-novelty claim is made; Gate G1 remains DEFERRED (P1-19). Combinatorial identities in `Z[u,z]` hold for every integer `P >= 1`; their realization by codes uses the frozen hypotheses, where `P = p^rho`. Probabilistic statements use the uniform labeled model (all exponents independent uniform on `{0,...,P}`).

**Duplication rule used:** a result is only listed as new if it is not already C1–C6, Proposition 6.4, or N1–N3 as stated in `P1_15_OPTIONAL_COROLLARIES.md`; each section says exactly what it adds.

---

## R1. Complement–reversal symmetry of the joint distribution

**Theorem R1.** Fix one orbit of length `L` and weight `w`, and write `N_{L,w}(K,H)` for the coefficient of `u^K z^H` in `tr((T^{(P)}_w(u,z))^L)`. Then for all `K,H`,

```
N_{L,w}(K,H) = N_{L,w}(P w L - K, H).
```

Globally, with `D := P * sum_s sum_O w_O L_O = n * sum_s m_s` (the maximum, and ambient, `F_q`-dimension),

```
E(u,z) = u^D * E(u^{-1}, z),   i.e.   #{a : (dim C, dim Hull) = (K,H)} = #{a : (dim C, dim Hull) = (D-K, H)}.
```

*Proof.* It suffices to prove the per-orbit identity; the global one follows by multiplying over orbits (coefficients convolve and the shifts add to `D`). On one orbit define `alpha'_i = P - alpha_{-i}` (indices mod `L`). This is an involution of `{0,...,P}^L`: applying it twice returns `alpha_i`. Its code sum is `sum_i (P - alpha'_i) = sum_i alpha_{-i} = sum_i alpha_i = LP - sum_i (P - alpha_i)`, so the code contribution `K` maps to `PwL - K`. Its hull sum satisfies, edge by edge after the reindexing `j = -i+1`,

```
min(P - alpha'_i, alpha'_{i-1}) = min(alpha_{-i}, P - alpha_{-i+1}) = min(P - alpha_j, alpha_{j-1}),
```

so the hull contribution `H` is preserved exactly. Hence the involution pairs tuples of type `(K,H)` with tuples of type `(PwL-K, H)`, proving the coefficient identity. ∎

**Corollary R1.1 (conditional symmetry).** Whenever `Pr(dim C = K) > 0`, the conditional law of `dim Hull` given `dim C = K` equals its conditional law given `dim C = D - K`; in particular all conditional moments that exist agree at `K` and `D-K`.

*Proof.* By Theorem R1 the joint counts agree at `(K,H)` and `(D-K,H)` for every `H`; summing over `H` gives equal denominators `Pr(dim C = K) = Pr(dim C = D-K)`, so the normalized conditional distributions agree. ∎

**Comparison / non-duplication.** C2 already gives the code-dimension marginal as the product `prod_f (1 + u^{w_f} + ... + u^{P w_f})`, whose factors are reciprocal; that is only the `H`-summed shadow of R1. The joint identity at *fixed hull dimension*, and Corollary R1.1 for conditional hull laws, are not stated in the manuscript or in N1–N3.

---

## R2. Restricted joint enumerators for the self-orthogonal and dual-containing families

Recall C4 (manuscript Corollary 7.4): `C(a)` is self-orthogonal iff `alpha_{i-1} + alpha_i >= P` on every orbit edge, and dual-containing iff `alpha_{i-1} + alpha_i <= P` on every edge; C4 records only the total counts (the case `u = z = 1` below).

Define, per orbit of length `L` and weight `w`, the matrices over `Z[t]` resp. `Z[u,z]`

```
(S^{(P)}_w(t))_{a,b}  = t^{w(P-b)}            if a + b >= P, else 0,
(D^{(P)}_w(u,z))_{a,b} = u^{w(P-b)} z^{w a}    if a + b <= P, else 0.
```

**Theorem R2.**
(i) `sum_{a : C(a) self-orthogonal} t^{dim C(a)} = prod_s prod_O tr( (S^{(P)}_{w_O}(t))^{L_O} )`, and the restricted joint enumerator is obtained at `t = u z` (on this family `dim Hull = dim C`).
(ii) `sum_{a : C(a) dual-containing} u^{dim C(a)} z^{dim Hull(a)} = prod_s prod_O tr( (D^{(P)}_{w_O}(u,z))^{L_O} )`.

*Proof.* Both conditions are conjunctions over orbit edges (C4), and both dimensions are sums over orbits, so by the same finite distributive law as in T6 it suffices to prove the per-orbit identities; the trace expansion of T5 then converts closed walks into tuples.

(i) On a self-orthogonal tuple, `Hull = C`, hence `dim Hull = dim C`; the joint weight `u^{dim C} z^{dim Hull}` equals `(uz)^{dim C}`. Along an edge `a = alpha_{i-1} -> b = alpha_i`, the code contribution is `w(P-b)` and admissibility is `a + b >= P`; the product of the edge weights `t^{w(P-b)}` over a closed walk is `t` to the orbit code contribution. The trace therefore sums exactly over admissible tuples.

(ii) On a dual-containing tuple, `Hull = D(C)`, and by the dual-dimension formula (proof of Corollary 7.4) the per-orbit dual, hence hull, contribution is `w * sum_i alpha_i = w * sum_i alpha_{i-1}`. Along an edge `a -> b` we therefore attach weight `u^{w(P-b)}` (code part, from `b`) and `z^{w a}` (hull/dual part, from the previous exponent `a`), with admissibility `a + b <= P`. The product over a closed walk is `u^{code} z^{hull}` for that orbit, and the trace/product assembly finishes the proof. ∎

**Corollary R2.1 (refined SO/DC symmetry).** Let `S(K)` be the number of self-orthogonal assignments with `dim C = K` (so `(dim C, dim Hull) = (K,K)`), and `D(K,H)` the number of dual-containing assignments with `(dim C, dim Hull) = (K,H)`. Then `S(K) = D(D - K, K)` for all `K`.

*Proof.* Apply the per-orbit complement `alpha_i -> P - alpha_i` (no reversal). It maps the edge condition `>= P` to `<= P`, hence SO tuples to DC tuples bijectively. If `alpha` is self-orthogonal with code/hull dimension `K`, the image has code dimension `D - K`, and its hull dimension equals its dual dimension `sum w alpha_i`-complement, i.e. `D - (D - K) = K`. ∎

**Exact example (`P=2, L=2, w=1`, all 9 tuples).** Self-orthogonal joint counts: `{(0,0):1, (1,1):2, (2,2):3}`; dual-containing joint counts: `{(4,0):1, (3,1):2, (2,2):3}` — visibly related by Corollary R2.1 with `D = 4`, and both specialize at `u=z=1` to the C4 count `6 = tr(B_2^2)`.

**Comparison / non-duplication.** C4 gives the criteria and the two total counts, and notes the counts are equal. Theorem R2 keeps the full dimension distributions inside the two families (code-dimension distribution of self-orthogonal codes; joint `(dim C, dim Hull)` distribution of dual-containing codes), and Corollary R2.1 refines "the two counts are equal" to an equality distribution-by-distribution. None of this is in the manuscript or N1–N3. Validation: `code/validate_p1_20.py` compares both restricted traces against brute-force tuple enumeration on the grid `P in {1,2,3,4}`, `L in {1,2,3,4}`, `w in {1,2}` (all checks pass).

---

## R3. The exact conditional law of the code dimension given LCD

**Theorem R3.** Condition the uniform labeled model on the LCD event `Hull(a) = 0`. Then the per-orbit restrictions remain independent, each orbit is equally likely to be `alpha = 0` (code contribution `P w_O L_O`) or `alpha = P` (code contribution `0`), and therefore

```
dim C | LCD  =d  sum_O (P w_O L_O) * Bernoulli(1/2)     (independent summands),
E[u^{dim C} | LCD] = 2^{-#orbits} prod_O (1 + u^{P w_O L_O}),
E[dim C | LCD] = D/2,        Var(dim C | LCD) = (P^2/4) * sum_O (w_O L_O)^2.
```

*Proof.* By the C3 argument (manuscript Corollary 7.3), `Hull(a) = 0` iff every orbit is constant `0` or constant `P`; there are exactly two admissible tuples per orbit. Conditioning a uniform distribution on a product event preserves independence across orbits and makes the two options per orbit equally likely. The code contribution of the `alpha = 0` option is `w_O * sum_i P = P w_O L_O`, and of the `alpha = P` option is `0`. The displayed law, generating function, mean (`(1/2) sum_O P w_O L_O = D/2`), and variance (`(P w_O L_O)^2 * (1/4)` per independent Bernoulli summand) follow. ∎

**Exact example.** For the two-component configuration `P=2`, `(L_O,w_O) = (1,1),(2,3),(1,2),(2,6)` (729 assignments): LCD count `16`, conditional mean `21 = D/2` with `D = 42`, conditional variance `185 = (1+36+4+144)`. Verified by complete brute-force enumeration in `code/validate_p1_20.py`.

**Comparison / non-duplication, and the honest relation to N3.** C3 is only the count `2^{#orbits}` (`u=1`). N3 is the unnormalized generating product `prod (1 + u^{P w_O L_O})`; Theorem R3 is exactly its normalized probabilistic content — the full conditional law and its first two moments. So R3 should not be sold as independent of N3: rather, **R3 is the genuinely useful consequence of N3**, the form in which N3 says something beyond a count (e.g. LCD codes are, in this model, exactly as likely to sit at any "all-`0`/all-`P`" dimension pattern, with mean at half the ambient dimension). Status remains PROPOSED together with N3.

---

## R4. Orbit-length recurrences for the trace polynomials

**Theorem R4.** Fix `P` and `w`, put `s_L = tr((T^{(P)}_w(u,z))^L)` for `L >= 1` and `s_0 := P+1` (the formal value `tr(I)`), and let `chi(lambda) = lambda^{P+1} - c_1 lambda^P - ... - c_{P+1}` be the characteristic polynomial of `T^{(P)}_w(u,z)` over `Z[u,z]`. Then for all `L >= 0`,

```
s_{L+P+1} = c_1 s_{L+P} + c_2 s_{L+P-1} + ... + c_{P+1} s_L.
```

For `P = 1` (and `w = 1`; general `w` by the substitution `u -> u^w, z -> z^w`), `chi(lambda) = lambda^2 - (1+u) lambda + u(1-z)`, so

```
s_{L+2} = (1+u) s_{L+1} - u(1-z) s_L,   s_0 = 2,  s_1 = 1 + u,
s_L = lambda_+^L + lambda_-^L,  lambda_{+/-} = ( (1+u) +/- sqrt((1-u)^2 + 4 u z) ) / 2
```

(the last identity in the quadratic extension, by equality of initial values and recurrence).

*Proof.* `T = T^{(P)}_w(u,z)` is a `(P+1) x (P+1)` matrix over the commutative ring `Z[u,z]`; the Cayley–Hamilton theorem over commutative rings gives `T^{P+1} = c_1 T^P + ... + c_{P+1} I`. Multiplying by `T^L` and taking traces yields the recurrence. For `P=1`, `T = [[u,1],[u z,1]]` (manuscript Proposition 6.4), and `det(lambda I - T) = (lambda - u)(lambda - 1) - u z = lambda^2 - (1+u) lambda + u(1-z)`; the closed form is the standard solution of the two-term recurrence. The scaling `T^{(P)}_w(u,z) = T^{(P)}_1(u^w, z^w)` (entrywise, already noted in P1-14) transfers everything to general `w`. ∎

**Comparison / non-duplication.** T5 evaluates the trace for one orbit length; nothing in the manuscript relates different lengths. R4 says the sequence of orbit enumerators at fixed `P` is linear-recurrent of order at most `P+1` in `L`, with the explicit two-term recurrence and closed form at `P=1`. This is a computational/structural consequence (long orbits at fixed `P` need only the first `P+1` traces plus the recurrence), not a new counting theorem; it is included because it is exact, proved, and was specifically investigated. Validation: the `P=1` recurrence is checked polynomial-for-polynomial for `L = 0..6` in `code/validate_p1_20.py`.

---

## 5. Conditional hull statistics at fixed code dimension: exact formula, and what is false

**Exact (but not closed) formula.** For any `K` with `[u^K] E(u,1) > 0`, finite-sum differentiation gives

```
E[ dim Hull | dim C = K ] = [u^K] ( (z d/dz) E(u,z) )_{z=1}  /  [u^K] E(u,1),
```

and similarly for factorial moments. This is exact, and by R1.1 the left side is symmetric under `K <-> D-K`. **But no simpler closed form follows from the existing framework**, and in particular zero covariance does not make the conditional mean constant:

**Counterexample (disproof of the constant-conditional-mean strengthening).** At `P=1, L=3, w=1` the joint distribution is `{(0,0):1, (1,1):3, (2,1):3, (3,0):1}` (manuscript Example 9.2). Hence `E[H | K] = 0, 1, 1, 0` for `K = 0, 1, 2, 3` — not constant — while `Cov(dim C, dim Hull) = 0` by N1 (and directly from this distribution). So: uncorrelated (N1) is the strongest general second-order statement; conditional means genuinely vary with `K`, in the symmetric pattern forced by R1.1. Any future wording must keep this distinction. (Independence is likewise false — the same distribution gives `Pr(K=2) Pr(H=1) = (3/8)(6/8) = 9/32 != 3/8 = Pr(K=2,H=1)`; cf. the P1-14 witness. Recorded here only to fence N1's wording.)

## 6. What N1–N3 actually buy (assessment, with the one-line proofs)

- **N1 + N2 (second-order package; modest but clean).** Together with C5/C6, N1 (`Cov = 0`) and N2 (`Var(dim C) = [P(P+2)/12] sum_f w_f^2`) complete the covariance matrix of `(dim C, dim Hull)` to a diagonal one, and immediately give `Var(dim C +/- dim Hull) = Var(dim C) + Var(dim Hull)` and "the least-squares linear predictor of `dim Hull` from `dim C` is the constant `E[dim Hull]`" (slope `Cov/Var = 0` whenever `Var(dim C) > 0`). These are one-line consequences of the definitions once N1/N2 are granted — useful as a quotable summary, not as new depth. Section 5's counterexample fences their meaning.
- **N3.** Its useful content is R3 (full conditional law under LCD, with mean `D/2` and variance `(P^2/4) sum (w_O L_O)^2`); as a bare product identity it is a refinement of C3, with R3 it becomes a distributional statement.
- **Net assessment.** N1–N3 are worth adopting only with these scopes stated: N1/N2 as the complete second-order summary (with "uncorrelated, not independent" attached), N3 in its R3 conditional-law form. None of them changes the main theorem.

## 7. Investigated and discarded (no theorem manufactured)

1. **"Conditional hull mean at fixed code dimension is constant"** — FALSE; counterexample in Section 5. Discarded.
2. **Palindromic symmetry in the hull variable** (an analogue of R1 for `z`) — FALSE: at `P=1, L=3, w=1` the hull marginal is `{0:2, 1:6}`, not symmetric. The complement–reversal involution of R1 works precisely because hull is preserved while code dimension flips; no involution flipping hull at fixed code dimension exists in general. Discarded.
3. **Independence of `dim C` and `dim Hull`** — FALSE (Section 5; P1-14 witness). Only uncorrelatedness (N1) holds. Discarded as a strengthening.
4. **Monotonicity of fixed coefficients `[u^K z^H] tr(T^L)` in `L`** — not claimed: as `L` grows the support itself shifts (both dimensions scale with `L`), so naive monotonicity is ill-posed; no well-posed monotone statement with a proof was found. Not promoted.
5. **Large-`L` asymptotics** — for fixed `u, z > 0` the matrix `T(u,z)` is entrywise positive, so Perron–Frobenius would give `(1/L) log tr(T^L) -> log rho(T(u,z))`. This is a direct application of a standard theorem with no enumerator-specific content, so it is recorded here as available background, **not** counted among the new results and not proposed for the manuscript.

## 8. Validation record (evidence, not proof)

`code/validate_p1_20.py` (stdlib only, exact integer/`Fraction` arithmetic; output saved as `code/validation_p1_20_output.txt`, final line `ALL P1-20 VALIDATION CHECKS PASSED`, 173 checks) verifies on finite grids: R1 per-orbit and global symmetry; R2 both restricted traces against brute-force enumeration, including `H = K` on SO tuples and `H = w sum alpha` on DC tuples (`P in {1,2,3,4}`, `L in {1,2,3,4}`, `w in {1,2}`); the R2 worked example; R3's LCD count/mean/variance by complete enumeration of the 729-assignment configuration; R4's `P=1` recurrence polynomial-for-polynomial (`L = 0..6`, with `s_1 = 1 + u`, `s_2 = 1 + u^2 + 2 u z`); and Section 5's conditional means `0,1,1,0` with `Cov = 0`. Earlier validators (`validate_p1_14.py` etc.) are untouched; finite checks support but do not replace the proofs above.

## 9. Status summary

| Result | Content | Status |
|---|---|---|
| R1 + R1.1 | Joint coefficient symmetry `N(K,H) = N(D-K,H)`; conditional hull law symmetric in `K` | Proved here; PROPOSED |
| R2 + R2.1 | Full restricted enumerators for SO / DC families; distribution-level SO/DC symmetry | Proved here; PROPOSED |
| R3 | Exact conditional law of `dim C` given LCD (mean `D/2`, variance `(P^2/4) sum (w_O L_O)^2`) | Proved here (= probabilistic content of N3); PROPOSED |
| R4 | Order-`(P+1)` recurrence in orbit length; explicit `P=1` recurrence and closed form | Proved here; PROPOSED |
| Section 5 | Exact coefficient formula for conditional hull moments; disproof of constant conditional mean | Proved here (formula + counterexample); fences N1 |
| Section 6 | N1/N2 covariance package (`Var` of sum/difference; constant linear predictor) | One-line consequences of N1/N2; PROPOSED with them |
| Section 7 items | Constant conditional mean; `z`-palindromy; independence; naive monotonicity; PF asymptotics as a "result" | Rejected / not promoted, with reasons |

No statement in the frozen blueprint or manuscript is altered, and no novelty or priority claim is made (Gate G1 DEFERRED, P1-19). Adoption of any item above into the blueprint/manuscript would require a dated author/Commander decision under the GAP-17 rule.
