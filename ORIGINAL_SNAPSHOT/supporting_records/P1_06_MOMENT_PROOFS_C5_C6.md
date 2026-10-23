# P1-06 — Formal Moment Analysis for C5 and C6

**Command:** P1-06 — Formal Moment Analysis for C5 and C6  
**Date:** 21 October 2026  
**Inputs (all previously proved):** T1–T6, C1–C4 (`P1_04_PROOFS_T1_T4.md`, `P1_05_PROOFS_T5_T6_COROLLARIES.md`).  
**Frozen statements:** transcribed below before any derivation; `02_THEOREM_BLUEPRINT.md` is **not** edited. **PC-1 remains unapproved**: the corrected C5 hull mean is proved here as mathematics and presented as a proposal; adopting it into the blueprint requires the separate approval command.

---

## 0. Frozen statements (transcribed) and the random model

**Frozen C5.** “Uniform random labeled assignment par `E[dim C] = (n/2)·(Σ_s m_s)` (kul `F_q`-lambai ka aadha) aur `E[Hull] = [P(2P+1)/(6(P+1))] · Σ_O w_O L_O`. *Chaabi:* ek kenare par `min(P−α_i, α_{i−1})` do swatantra uniform `{0,…,P}` ka `min` hai; `E[min] = Σ_{t=1}^P ((P−t+1)/(P+1))² = P(2P+1)/(6(P+1))`. `P=1` par `1/4` — purana mean wapas.”

**Frozen C6.** “Variance: Orbit-swatantra yog; `L=1` (self-loop: `min(P−A,A)`), `L=2` (do kenare ek hi jodi ko saanjha karte hain), `L≥3` (sirf padosi kenare sah-sambandhit) — teeno cases ke band sutra (closed forms) Phase 4 me `P` ke parimaani (polynomial) roop me nikale jayenge.” **[RR-8]**

**Status of the frozen text, in advance.** The code-dimension mean in C5 is correct (proved in §2.1). The frozen hull mean is **incorrect**: its proof key (“two independent uniforms”) fails exactly on `L_O = 1` orbits, where the edge is a self-loop `min(P−A, A)`; consequently the “`P=1` gives `1/4`” remark is also wrong for those orbits (`ν_1 = 0`, §2.2). A corrected statement is proved in §2.4 and registered as proposal PC-1 (unapproved). C6 as frozen asserts no formula; §3 supplies the closed forms, discharging RR-8 at the level of mathematics (blueprint adoption again awaits the approval command).

**Random model.** A labeled assignment is chosen uniformly from the finite product set of T1/P1-05 Proposition 3.1. Equivalently: for each component `s`, orbit `O ∈ O_s`, and position `i`, the exponent `A^{(s,O)}_i` is uniform on `{0, …, P}`, and all these variables (over all `s, O, i`) are mutually independent — uniformity on a Cartesian product is the product of the uniform measures. For one orbit, drop the superscripts, write `L = L_O`, `w = w_O`, and define the cyclic edge variables
```
X_i = min(P − A_i, A_{i−1}),   i = 0, …, L−1   (indices mod L),     S_L = Σ_{i=0}^{L−1} X_i.
```
By T4 (P1-04/P1-05), the orbit contributes `w·(P − A_i)`-type terms to the code dimension and `w·S_L` to `dim_{F_q} Hull_k`; globally,
```
dim_{F_q} Hull_k = Σ_{s} Σ_{O∈O_s} w_O · S_{L_O}^{(s,O)}.            (1)
```
All expectations/variances below are exact rational numbers.

**Why `L = 1` and `L ≥ 2` must differ.** For `L ≥ 2`, the two arguments of each edge minimum, `P − A_i` and `A_{i−1}`, come from **two distinct** independent uniforms (also for `L = 2`: the two edges are the two ordered pairings of the same two distinct variables). For `L = 1` the single edge is a **self-loop**: its two arguments are `P − A` and `A`, two functions of the *same* variable. The statistics are genuinely different — e.g. at `P = 1`, `min(1−A, A) ≡ 0` on `{0,1}` (mean `0`), whereas `min` of two independent bits has mean `1/4`.

---

## 1. One-edge moments (for `L ≥ 2` edges)

Let `U, B` be independent uniform on `{0, …, P}` and `X = min(U, B)` (an `L ≥ 2` edge has this law, with `U = P − A_i`).

**Lemma 1.1 (edge mean; frozen C5’s key quantity).** `E[X] = μ_P := P(2P+1)/(6(P+1))`.

*Proof.* For integer-valued `X ≥ 0`, `E[X] = Σ_{t≥1} Pr(X ≥ t)`. Now `Pr(min(U,B) ≥ t) = ((P−t+1)/(P+1))²` for `1 ≤ t ≤ P`, so `E[X] = (1/(P+1)²) Σ_{t=1}^P (P−t+1)² = (1/(P+1)²) Σ_{r=1}^P r² = (1/(P+1)²)·P(P+1)(2P+1)/6 = P(2P+1)/(6(P+1))`. ∎

**Lemma 1.2 (edge second moment and variance).**
```
E[X²] = P(P²+P+1)/(6(P+1)),    Var(X) = P(P+2)(2P²+4P+3) / (36(P+1)²).
```

*Proof.* For integer-valued `X ≥ 0`, `E[X²] = Σ_{t≥1} (2t−1) Pr(X ≥ t)` (since `x² = Σ_{t=1}^{x} (2t−1)`). With the same tail probabilities and the substitution `r = P−t+1`:
`E[X²] = (1/(P+1)²) Σ_{r=1}^P (2P+1−2r) r² = (1/(P+1)²) [ (2P+1)Σr² − 2Σr³ ]`.
Using `Σ_{r=1}^P r² = P(P+1)(2P+1)/6` and `Σ_{r=1}^P r³ = (P(P+1)/2)²`, the bracket equals `P(P+1)(2P+1)²/6 − P²(P+1)²/2`; dividing by `(P+1)²` and factoring the bracket as `P(P+1)·[ (2P+1)² − 3P(P+1) ]/6 = P(P+1)(P²+P+1)/6` (since `(2P+1)² − 3P(P+1) = P²+P+1`) gives `E[X²] = P(P²+P+1)/(6(P+1))`. Then
`Var(X) = E[X²] − μ_P² = [6P(P+1)(P²+P+1) − P²(2P+1)²] / (36(P+1)²)`, and the numerator expands (equivalently, factors) as `P(P+2)(2P²+4P+3)`: indeed `6P(P+1)(P²+P+1) − P²(2P+1)² = 2P⁴ + 8P³ + 11P² + 6P = P(P+2)(2P²+4P+3)`, as is checked by expanding the right side. ∎

**Lemma 1.3 (the one-variable profile).** For `0 ≤ c ≤ P` and `U` uniform on `{0,…,P}`, `F(c) := E[min(c, U)] = c(2P−c+1)/(2(P+1))`.

*Proof.* `E[min(c,U)] = Σ_{t=1}^{c} Pr(U ≥ t) = Σ_{t=1}^{c} (P−t+1)/(P+1) = (1/(P+1))·[ cP − c(c−1)/2 ] = c(2P−c+1)/(2(P+1))`. ∎

---

## 2. C5 — Means

### 2.1 Code-dimension mean (frozen C5, first part: correct)

For each factor `f`, `E[P − A_f] = P − P/2 = P/2` (mean of the uniform on `{0,…,P}` is `P/2`). By T4 and linearity,
`E[dim_{F_q} C] = Σ_s m_s Σ_{f∈F_s} deg(f)·(P/2) = Σ_s m_s·n_0·(P/2) = (n/2)·Σ_s m_s`,
using `Σ_{f∈F_s} deg f = deg S_s = n_0` and `n = P n_0`. ∎ (This is exactly the frozen claim; no correction needed.)

### 2.2 The `L = 1` orbit mean

**Proposition 2.2.** For `L = 1`, `E[X_0] = E[min(P−A, A)] = ν_P := ⌊P²/4⌋/(P+1)`.

*Proof.* `E[min(P−A,A)] = (1/(P+1)) Σ_{a=0}^P min(P−a, a)`. The summands are symmetric under `a ↦ P−a`. If `P = 2m`: the values are `0, 1, …, m−1, m, m−1, …, 0`, summing to `2·Σ_{a=0}^{m−1} a + m = m(m−1) + m = m² = P²/4`. If `P = 2m+1`: the values are `0, 1, …, m, m, …, 0`, summing to `2·Σ_{a=0}^{m} a = m(m+1) = (P²−1)/4`. Both equal `⌊P²/4⌋`; divide by `P+1`. ∎

In particular `ν_1 = 0`, `ν_2 = 1/3`, `ν_3 = 1/2` — and `ν_P ≠ μ_P` for every `P ≥ 1` (e.g. `μ_P − ν_P > 0` since `μ_P ≥ μ_1 = 1/4 > 0 = ν_1` at `P=1`, and directly from the formulas in general), which is the quantitative form of the self-loop phenomenon of §0.

### 2.3 The `L ≥ 2` orbit mean

**Proposition 2.3.** For `L ≥ 2`, `E[S_L] = L·μ_P`.

*Proof.* Each `X_i` has the law of Lemma 1.1: for `L ≥ 3`, `A_i` and `A_{i−1}` are distinct coordinates; for `L = 2`, `X_0 = min(P−A_0, A_1)` and `X_1 = min(P−A_1, A_0)` are the two ordered pairings of the distinct pair `(A_0, A_1)`, each marginally `min` of two independent uniforms. Hence `E[X_i] = μ_P` for all `i`, and linearity of expectation (no independence needed) gives `E[S_L] = L μ_P`. ∎

### 2.4 Global mean and the PC-1 proposal

**Theorem 2.4 (mean hull dimension; proved mathematics).** Under (G1)–(G6) of P1-05 and the uniform labeled model,
```
E[dim_{F_q} Hull_k] = ν_P · Σ_{s} Σ_{O∈O_s, L_O = 1} w_O  +  μ_P · Σ_{s} Σ_{O∈O_s, L_O ≥ 2} w_O·L_O.
```

*Proof.* Take expectations in (1): `E[dim Hull] = Σ_{s,O} w_O·E[S_{L_O}]` by linearity, and apply Proposition 2.2 (`L_O = 1`) and Proposition 2.3 (`L_O ≥ 2`) orbit by orbit. (Cross-check via the proved enumerator: `E[dim Hull] = [z·∂_z E(u,z)/E(u,z)]_{u=z=1}` by T6, and the logarithmic derivative splits over the orbit product into the same per-orbit terms; the two computations agree because both are linearity of expectation over the orbit decomposition.) ∎

**Proposal PC-1 (unapproved — precise change requested).** Replace the frozen C5 hull-mean display `E[Hull] = [P(2P+1)/(6(P+1))]·Σ_O w_O L_O` and its proof key by Theorem 2.4’s split formula. What changes and why:

| Frozen C5 piece | Status | Replacement / reason |
|---|---|---|
| `E[dim C] = (n/2)·Σ_s m_s` | **Correct** (§2.1) | Unchanged. |
| `E[Hull] = μ_P·Σ_O w_O L_O` | **Incorrect** whenever an `L_O = 1` orbit exists | Split sum: `ν_P` on `L_O = 1` orbits, `μ_P·L_O` on `L_O ≥ 2` orbits (Theorem 2.4). The frozen proof key treats the self-loop edge as a min of two *independent* uniforms; it is `min(P−A, A)`. |
| “`P=1` par `1/4` — purana mean wapas” | **Incorrect** for `L_O = 1` | At `P = 1`: `E[Hull] = (1/4)·Σ_{L_O ≥ 2} w_O L_O` (since `ν_1 = 0`, `μ_1 = 1/4`); `L_O = 1` orbits contribute `0`. |

Counterexamples to the frozen display (already brute-forced at vector level in P1-03 and reproduced by `validate_p1_06.py` at the orbit level): any model with an `L = 1` orbit, e.g. `P = 2, L = 1`: true per-orbit mean `ν_2 = 1/3` vs frozen `μ_2 = 5/9`. **This proposal changes nothing until approved; the frozen file stands.**

---

## 3. C6 — Variance of the hull dimension (RR-8)

Global structure first. In (1), the summands `w_O·S_{L_O}^{(s,O)}` for distinct `(s, O)` are functions of **disjoint** subfamilies of the independent exponent variables, hence are mutually independent under the product-uniform model (this is where CRT/product independence enters: the assignment set is a Cartesian product, T1/P1-05 Prop. 3.1, so the uniform measure factorizes over components and orbits). Therefore
```
Var(dim_{F_q} Hull_k) = Σ_{s} Σ_{O∈O_s} w_O² · Var(S_{L_O}),          (2)
```
and it suffices to compute `Var(S_L)` for one orbit. Note the variance adds with squared weights `w_O²`, the mean (Theorem 2.4) with weights `w_O`.

### 3.1 `L = 1`: the self-loop variance

**Proposition 3.1.** With `X = min(P−A, A)`, `A` uniform on `{0,…,P}`:
```
E[X²] = P(P²+2)/(12(P+1))  if P even;    E[X²] = P(P−1)/12  if P odd;
Var(X) = P(P+2)(P²+2P+4)/(48(P+1)²)  if P even;    Var(X) = (P−1)(P+3)/48  if P odd.
```

*Proof.* `E[X²] = (1/(P+1)) Σ_{a=0}^P min(P−a, a)²`. For `P = 2m` the squared values are `0²,…, (m−1)², m², (m−1)²,…, 0²`, so the sum is `2·Σ_{a=0}^{m−1} a² + m² = m(m−1)(2m−1)/3 + m² = m(2m²+1)/3`; substituting `m = P/2` gives `E[X²] = P(P²+2)/(12(P+1))`. For `P = 2m+1` the values `0,…,m` each occur twice, so the sum is `2·Σ_{a=0}^{m} a² = m(m+1)(2m+1)/3 = P(P²−1)/12` (using `m = (P−1)/2`, `m+1 = (P+1)/2`, `2m+1 = P`); dividing by `P+1` gives `E[X²] = P(P−1)/12`. Subtracting `ν_P²` (Proposition 2.2: `ν_P = P²/(4(P+1))` for even `P` in the form `m²/(2m+1)`, and `ν_P = (P−1)/4` for odd `P`): for even `P`, `Var = P(P²+2)/(12(P+1)) − P⁴/(16(P+1)²) = P(P+2)(P²+2P+4)/(48(P+1)²)` (common denominator `48(P+1)²`; the numerator identity `4P(P²+2)(P+1) − 3P⁴ = P(P+2)(P²+2P+4)` is by expansion); for odd `P`, `Var = P(P−1)/12 − ((P−1)/4)² = (P−1)(P+3)/48` (factoring `(P−1)` and using `P/12 − (P−1)/16 = (P+3)/48`). ∎

(Checks: `P = 1`: `Var = 0`, indeed `X ≡ 0`. `P = 2`: `2/9`. `P = 3`: `1/4`.)

### 3.2 `L ≥ 3`: adjacent covariance, independent non-neighbours

For `L ≥ 3`, `X_i` is a function of the pair `(A_i, A_{i−1})`.

**Lemma 3.2 (adjacent covariance).** For each `i`, with `X_i, X_{i+1}` consecutive edge variables (indices mod `L`, `L ≥ 3`),
```
Cov(X_i, X_{i+1}) =: κ_P = − P(P+2)(7P²+14P+9) / (360(P+1)²)   (< 0 for P ≥ 1).
```

*Proof.* `X_i = min(P−A_i, A_{i−1})` and `X_{i+1} = min(P−A_{i+1}, A_i)` share exactly the one variable `A_i` (for `L ≥ 3`; in particular this includes every pair when `L = 3`). Condition on `A_i = b`: then `X_i = min(P−b, A_{i−1})` and `X_{i+1} = min(P−A_{i+1}, b)` are functions of the distinct variables `A_{i−1}, A_{i+1}`, hence conditionally independent, with conditional means `E[min(P−b, A_{i−1})] = F(P−b)` and `E[min(P−A_{i+1}, b)] = F(b)` (Lemma 1.3, using `P−A_{i+1}` uniform). Therefore `E[X_i X_{i+1}] = E[ F(P−A_i) F(A_i) ] = (1/(P+1)) Σ_{b=0}^P F(P−b) F(b)`. Substituting `F(c) = c(2P−c+1)/(2(P+1))`: the product in the sum is `b(P−b)(2P+1−b)(P+1+b) / (4(P+1)²)`, and `b(P−b)(2P+1−b)(P+1+b) = P(2P+1)(P+1)·b − (P²+3P+1)·b² − 2P·b³ + b⁴` (expansion). Summing with `Σ_{b=0}^P b = P(P+1)/2`, `Σ b² = P(P+1)(2P+1)/6`, `Σ b³ = (P(P+1)/2)²`, `Σ b⁴ = P(P+1)(2P+1)(3P²+3P−1)/30` and simplifying gives `E[X_i X_{i+1}] = P(P−1)(11P²+15P+6)/(120(P+1)²)`. (At `P = 1` this is `0`, correctly: `X_i = 1` forces `A_i = 0`, which forces `X_{i+1} = 0`.) Finally `κ_P = E[X_iX_{i+1}] − μ_P²`: with common denominator `360(P+1)²`, the numerator of `E[X_iX_{i+1}]` is `3P(P−1)(11P²+15P+6)` and the numerator of `μ_P²` is `10P²(2P+1)²`; their difference is `−7P⁴ − 28P³ − 37P² − 18P = −P(P+2)(7P²+14P+9)` (both expansions agree), so `κ_P = −P(P+2)(7P²+14P+9)/(360(P+1)²)` as displayed. The sign is negative for `P ≥ 1` since every factor in `P(P+2)(7P²+14P+9)` is positive — intuitively, a large shared `A_i` shrinks `P−A_i` inside `X_i` while enlarging the cap `A_i` inside `X_{i+1}`. ∎

**Lemma 3.3 (which pairs are independent).** For `L ≥ 4`, if `j ∉ {i−1, i, i+1}` (mod `L`), then `X_i` and `X_j` are independent, hence `Cov(X_i, X_j) = 0`. The `L` unordered adjacent pairs `{i, i+1}` are exactly the pairs with possibly nonzero covariance (for `L = 3` these are all `3` unordered pairs).

*Proof.* `X_i` is a function of `{A_i, A_{i−1}}` and `X_j` of `{A_j, A_{j−1}}`; the stated condition is exactly that these two 2-element index sets are disjoint. Functions of disjoint subfamilies of independent random variables are independent. Conversely each adjacent pair shares exactly one variable (Lemma 3.2’s setup). ∎

**Proposition 3.4 (`L ≥ 3` variance).** `Var(S_L) = L · P(P+2)(P²+2P+2) / (60(P+1)²)`.

*Proof.* `Var(S_L) = Σ_i Var(X_i) + 2·Σ_{i<j} Cov(X_i, X_j)`. Every `X_i` has variance `Var(X)` of Lemma 1.2 (marginally an `L ≥ 2` edge). By Lemmas 3.2–3.3, among the unordered pairs exactly the `L` adjacent pairs contribute, each with covariance `κ_P`. Hence `Var(S_L) = L·Var(X) + 2L·κ_P = L·[ P(P+2)(2P²+4P+3)/(36(P+1)²) − P(P+2)(7P²+14P+9)/(180(P+1)²) ]`. With denominator `180(P+1)²` the bracket’s numerator is `P(P+2)·[5(2P²+4P+3) − (7P²+14P+9)] = P(P+2)(3P²+6P+6) = 3P(P+2)(P²+2P+2)`, so the bracket equals `P(P+2)(P²+2P+2)/(60(P+1)²)`. ∎

### 3.3 `L = 2`: the two edges share **both** variables

For `L = 2`, `X_0 = min(P−A_0, A_1)` and `X_1 = min(P−A_1, A_0)`: the pair is not an “adjacent with one shared variable” pair — both variables appear in both edges, and Lemma 3.2 does not apply.

**Lemma 3.5 (`L = 2` cross moment).** `E[X_0 X_1] = P²(P−1)/(12(P+1))`, and `Cov(X_0, X_1) = −P²(P+2)²/(36(P+1)²)`.

*Proof.* Write `A, B` for `A_0, A_1`; `X_0 X_1 = min(P−A, B)·min(P−B, A)`. For nonnegative integers, `E[X_0X_1] = Σ_{s,t ≥ 1} Pr(X_0 ≥ s, X_1 ≥ t)`. Now `X_0 ≥ s` iff `A ≤ P−s` and `B ≥ s`; `X_1 ≥ t` iff `B ≤ P−t` and `A ≥ t`. Both hold iff `t ≤ A ≤ P−s` and `s ≤ B ≤ P−t`, which is nonempty iff `s + t ≤ P`, in which case each of `A, B` has exactly `P−s−t+1` admissible values. Hence `Pr = ((P−s−t+1)/(P+1))²` if `s+t ≤ P`, else `0`. Grouping by `r = P−s−t+1 ∈ {1, …, P−1}` (the number of positive pairs `(s,t)` with `s+t = P−r+1` is `P−r`):
`E[X_0X_1] = (1/(P+1)²) Σ_{r=1}^{P−1} (P−r) r² = (1/(P+1)²)·P²(P−1)(P+1)/12 = P²(P−1)/(12(P+1))`,
where `Σ_{r=1}^{P−1} (P−r)r² = P·(P−1)P(2P−1)/6 − ((P−1)P/2)² = P²(P−1)(P+1)/12` (using the power sums up to `P−1`). Then `Cov = E[X_0X_1] − μ_P²`; with denominator `36(P+1)²`, `E[X_0X_1] = 3P²(P²−1)/(36(P+1)²)`, and `3(P²−1) − (2P+1)² = 3P²−3 − (4P²+4P+1) = −P²−4P−4 = −(P+2)²`, giving `Cov(X_0,X_1) = −P²(P+2)²/(36(P+1)²)`. ∎

**Proposition 3.6 (`L = 2` variance).** `Var(S_2) = P(P+2)(P²+2P+3) / (18(P+1)²)`.

*Proof.* `Var(S_2) = 2·Var(X) + 2·Cov(X_0,X_1)` (Lemma 1.2, Lemma 3.5) `= (2/(36(P+1)²))·[ P(P+2)(2P²+4P+3) − P²(P+2)² ]`. The bracket factors: `P(P+2)·[ (2P²+4P+3) − P(P+2) ] = P(P+2)(P²+2P+3)`. Hence `Var(S_2) = P(P+2)(P²+2P+3)/(18(P+1)²)`. ∎

Sanity: at `P = 1`, `S_2 ∈ {0, 1}` with `Pr(S_2 = 1) = 1/2`, so `Var = 1/4`; the formula gives `1·3·6/(18·4) = 1/4`. Note the `L = 2` formula is **not** the `L = 2` substitution of Proposition 3.4 (which would give `2·P(P+2)(P²+2P+2)/(60(P+1)²)`; at `P = 2`: `8/27 ≈ 0.296` vs the correct `44/81 ≈ 0.543`) — the shared-pair dependence is genuinely different, as frozen C6 anticipated.

### 3.4 Global variance theorem (C6 mathematics)

**Theorem 3.7 (variance of the hull dimension).** Under the hypotheses of Theorem 2.4,
```
Var(dim_{F_q} Hull_k) = Σ_{s} Σ_{O∈O_s} w_O² · V_{L_O}(P),
V_1(P) = P(P+2)(P²+2P+4)/(48(P+1)²)  (P even),   (P−1)(P+3)/48  (P odd);
V_2(P) = P(P+2)(P²+2P+3)/(18(P+1)²);
V_L(P) = L·P(P+2)(P²+2P+2)/(60(P+1)²)   (L ≥ 3).
```

*Proof.* Equation (2) (independence across components/orbits under the product-uniform model, via T1 and P1-05 Proposition 3.1) reduces the claim to `Var(S_L)` for one orbit, which is Proposition 3.1 (`L = 1`), Proposition 3.6 (`L = 2`), and Proposition 3.4 (`L ≥ 3`). The squared weight `w_O²` appears because `Var(w_O·S) = w_O² Var(S)`. No cross-orbit covariance terms appear: distinct orbits involve disjoint exponent variables. ∎

**What remains unsimplified / open.** Nothing in the variance of `dim Hull` is left as a finite sum: every case is a closed rational function of `P` (piecewise by parity only for `L = 1`). Not treated here (and not claimed): variance of `dim C`, mixed covariance `Cov(dim C, dim Hull)`, higher moments, and the variance under any non-uniform or equivalence-class model. Blueprint adoption of Theorem 3.7 as C6’s closed forms is part of the same future approval decision as PC-1…PC-6 (PC-6 asked that C6 be marked “to be proved (RR-8)” until then; RR-8 is now discharged mathematically).

---

## 4. Dependency map

Previously proved: T1 (assignment product model), T4 (hull dimension = orbit sums (1)), T6 (enumerator; used only for the cross-check remark in Theorem 2.4), P1-05 Prop. 3.1 (component/orbit independence of the product model). New in this package: Lemmas 1.1–1.3 (edge moments), Propositions 2.2–2.3 and Theorem 2.4 (means; PC-1 mathematics), Propositions 3.1/3.4/3.6, Lemmas 3.2/3.3/3.5, Theorem 3.7 (variances; RR-8 mathematics). Still open elsewhere: C7 (RR-9), PC-1…PC-6 approvals, Gate G1 (novelty; untouched).

---

## 5. Computational verification (supporting evidence, not proof)

Executed for this package (21 Oct 2026); earlier scripts/outputs unmodified:

```
python3 code/validate_p1_06.py    # NEW; output code/validation_p1_06_output.txt
                                  # final line: ALL P1-06 MOMENT CHECKS PASSED
python3 code/validate_p1_03.py    # rerun: exit 0, byte-identical to saved output
python3 code/validate_p1_05.py    # rerun: ALL P1-05 MULTI-COMPONENT ASSEMBLY CHECKS PASSED
```

`validate_p1_06.py` works in exact rational arithmetic and compares three layers for `P ∈ {1, 2, 3, 4, 5, 8, 9}` (all prime powers `p^ϱ`, including `P = 1 = p^0`): (1) the closed forms of §§1–3; (2) exact finite sums for every building block (`Σ_a min(P−a,a)^{1,2}`, edge tail sums, the `Σ_b F(P−b)F(b)` adjacent sum, the `(s,t)` double sum for `L = 2`); (3) direct enumeration of `A`-tuples for `L ∈ {1, 2, 3, 4, 6}` (capped at 300k tuples; the two largest `(P, L) = (8,6), (9,6)` cases are covered by layers (1)–(2) only). It also verifies the **global** assembly: mean adds with weights `w_O`, variance with `w_O²` — against direct global enumeration for `P = 2`, orbits `(L,w) = (1,2), (2,1), (3,1)` (729 tuples) and against exact convolution of per-orbit distributions for `P = 3`, orbits `(1,2), (2,1), (3,3), (6,1)`.

What this verifies: the displayed rational formulas agree with brute force and with the independent finite sums at the tested `(P, L)`, including all three variance regimes and the parity split at `L = 1`. What it cannot prove: the formulas for untested `(P, L)` (the proofs in §§1–3 do that), the product-model independence (proved from T1/CRT, §0), or anything outside the labeled uniform compatible-twist model.
