# P1-05 — Formal Proof Package for T5–T6 and Corollaries C1–C4

**Command:** P1-05 — Formal Proof Package for T5–T6 and Corollaries C1–C4  
**Date:** 21 October 2026  
**Proof source:** `P1_04_PROOFS_T1_T4.md` (RR-1…RR-5, T1–T4, single component), whose conventions are rechecked at every point of use in §1.  
**Frozen statements:** transcribed verbatim-in-substance from `02_THEOREM_BLUEPRINT.md` before each proof; that file is **not** edited. PC-1…PC-6 remain **unapproved** (register GAP-17).

**Scope.** Labeled exponent assignments only; compatible twists only. This package proves T5, T6 (with the CRT/product assembly made explicit), C1, C2, C3, C4, and the `P = 1` specialization of these results. C5, C6, C7 are **not** proved here (see §8); in particular nothing in this file repairs or uses the frozen C5 hull mean, which is known to fail for `L_O = 1` (PC-1, unapproved).

---

## 0. Global standing hypotheses

Components are indexed `s = 1, …, N` with **fixed labels**. Throughout:

- **(G1)** `p` prime, `q = p^e`, `e ≥ 1`, and a **common** Galois index `k` with `0 ≤ k < e`.
- **(G2)** A **common** `ϱ ≥ 0`, `P = p^ϱ`, `n_0` with `gcd(n_0, p) = 1`, and common length `n = P·n_0`.
- **(G3)** `K_s = F_{q^{m_s}} = F_{p^{d_s}}`, `m_s ≥ 1`, `d_s = e·m_s`; `A ≅ ∏_{s=1}^N K_s` with the isomorphism fixed. A code over `A` is an `A`-submodule of `A^n`; counts are over labeled assignments, never equivalence classes.
- **(G4)** Per component: `σ_s(α) = α^{p^k}`, `ρ_s(α) = α^{p^{d_s−k}} = σ_s^{−1}` on `K_s` (note `d_s − k ≥ e − k ≥ 1`), `λ_s ∈ K_s*` **compatible**: `λ_s^{1 + p^{d_s−k}} = 1`; `μ_s` the unique `P`-th root of `λ_s`; `S_s = x^{n_0} − μ_s = ∏_{f∈F_s} f` (distinct monic irreducibles, (G2)); `M_s = S_s^P = x^n − λ_s`; `τ_s(f) = f#` with `#` as in P1-04 (S6).
- **(G5) Dual-order convention (verbatim, as in P1-04):** “The code-first pairing is `⟨x, y⟩_k = Σ_{i=0}^{n−1} x_i σ(y_i)`, and the code-first dual is `D(C) = { y ∈ K^n : ⟨c, y⟩_k = 0 for all c ∈ C }` — the code vector occupies the first slot and the candidate vector the second slot. The Euclidean dual is `C^⊥ = { z ∈ K^n : Σ_i c_i z_i = 0 for all c ∈ C }`, and `Hull_k(C) = C ∩ D(C)`.” The global pairing on `A^n` is the tuple of component pairings; `D_A` and `Hull_{A,k}` are defined componentwise (justified in §3).
- **(G6)** For a `τ_s`-orbit `O = (f_0, …, f_{L−1})` (with `τ_s(f_i) = f_{i+1}`, indices mod `L_O := L`), all factors have the same degree (P1-04, Lemma RR-2(vi)); the weight is `w_O = m_s · deg_{K_s}(f_O)`, and for a factor `f`, `w_f = m_s · deg_{K_s} f`.

`u, z` are indeterminates; all enumerator identities are in `Z[u, z]`.

---

## 1. Inputs from P1-04, with the convention recheck required by this command

The following are **previously proved** (P1-04) and are used as black boxes; the right-hand column records the independent convention check performed for this package.

| Input | Used for | Convention check |
|---|---|---|
| T1: `a ↦ ⟨g_a⟩` bijection, `dim_K ⟨g⟩ = n − deg g` | assignment parametrization in T6 | No dual convention involved. |
| RR-2 / T2: `#` multiplicative; `τ_s` permutes `F_s`, degree-preserving | dual exponents `β_i`; constancy of `w_O` on orbits | `#` uses coefficientwise `ρ_s` **and** reversal, normalized at the constant term: `f# = ρ̄(f^♮_ordinary)`; it is not the ordinary reciprocal. Multiplicativity is what licenses applying `#` factorwise to `h_a = ∏ f^{P−a_f}`. |
| RR-3: `C^⊥ = ⟨h^♮⟩` for `C = ⟨g⟩`, `h = (x^n−λ)/g` | inside T3/T4, hence inside T5–T6 only through T4 | `h^♮` is the **ordinary** reciprocal (no Frobenius), and RR-3 used no separability. The Frobenius enters only afterwards, via RR-4 — keeping `♮` (RR-3) and `#` (T3) distinct is essential; confusing them would replace `β_i` by ordinary-reciprocal exponents. |
| RR-4 / T3: `D(C(a)) = ⟨h_a#⟩`, exponent of `f_i` equal to `β_i = P − α_{i−1}` | T4, hence the hull edge weights in T5 | The derivation `D(C) = ρ_s(C^⊥)` solves `Σ c_i σ_s(y_i) = 0` for the **second-slot** candidate `y`, applying `σ_s^{-1} = ρ_s`. If the pairing were read candidate-first, the same computation would give `σ_s(C^⊥)`, the `σ_s`-reciprocal, and `β_i = P − α_{i+1}`; the frozen `h_a#` is correct precisely under (G5). Compatibility is used only to keep the dual in the same modulus `x^n − λ_s`. |
| RR-5 / T4: `Hull_k(C(a)) = ⟨lcm(g_a, h_a#)⟩`; `dim_{F_q} C(a) = Σ_s Σ_O w_O Σ_i (P − α_i)`; `dim_{F_q} Hull_k(C(a)) = Σ_s Σ_O w_O Σ_i min(P − α_i, α_{i−1})` | everything below | The orbit orientation `τ_s(f_i) = f_{i+1}` makes `α_{i−1}` the **predecessor**; the edge term `min(P − α_i, α_{i−1})` pairs current index `i` (first argument) with predecessor `i−1` (second argument). T5’s matrix convention (row = previous, column = current) is checked against exactly this in §2. |

No hypothesis beyond (G1)–(G6) is introduced anywhere below.

---

## 2. T5 — The transfer-matrix trace identity (RR-6)

**Frozen statement (transcribed).** *For one orbit (`L`, `w`) let `T = T^{(P)}_w(u,z)` be the `(P+1)×(P+1)` matrix with `T_{a,b} = u^{w(P−b)} z^{w·min(P−b, a)}` (order: previous state `a` → new state `b`). Then*
```
tr(T^L) = Σ_{α∈{0,…,P}^L} u^{w Σ_i (P−α_i)} z^{w Σ_i min(P−α_i, α_{i−1})}.
```

**Theorem T5.** Under (G1)–(G6), for every `τ_s`-orbit `O` with `L = L_O ≥ 1` and weight `w = w_O`, the displayed identity holds in `Z[u, z]`, where on the right `α = (α_0, …, α_{L−1})`, indices are mod `L`, and the two sums are the per-orbit contributions to `dim_{F_q} C(a)` and `dim_{F_q} Hull_k(C(a))` in T4.

**Proof.** Work in the commutative ring `R = Z[u, z]`; `T` has entries in `R`.

*Step 1: trace = closed walks.* By the definition of matrix multiplication, induction on `L` gives, for states `a_0, a_L ∈ {0, …, P}`,
```
(T^L)_{a_0, a_L} = Σ_{a_1, …, a_{L−1}} ∏_{j=1}^{L} T_{a_{j−1}, a_j},
```
(for `L = 1` the sum over intermediate states is empty and the formula reads `(T)_{a_0,a_1}`). Setting `a_L = a_0` and summing over `a_0` for the trace:
```
tr(T^L) = Σ_{a_0, …, a_{L−1} ∈ {0,…,P}} ∏_{j=1}^{L} T_{a_{j−1}, a_j},   a_L := a_0.     (1)
```
A summand is a **closed walk** `a_0 → a_1 → … → a_{L−1} → a_0` through the labeled positions `0, …, L−1` of the orbit. The correspondence with exponent assignments is a bijection: given the walk, set `α_i := a_i` (`i = 0, …, L−1`); given `α ∈ {0,…,P}^L`, the same formula defines a walk, and the closing edge is `a_{L−1} → a_0`, i.e. the edge into position `0` whose predecessor is position `L−1`. There is no quotient by rotation: positions are distinct labeled factors `f_0, …, f_{L−1}`, so walks with different starting positions are different assignments, exactly as T1’s parametrization requires. Hence the right side of (1) is a sum over `α ∈ {0,…,P}^L`, as claimed.

*Step 2: the weight of one walk.* By the frozen entry definition, with row `a_{j−1}` = previous exponent and column `a_j` = current exponent,
`T_{a_{j−1}, a_j} = u^{w(P − a_j)} z^{w·min(P − a_j, a_{j−1})}`.  
Therefore
```
∏_{j=1}^{L} T_{a_{j−1}, a_j} = u^{w Σ_{j=1}^{L} (P − a_j)} · z^{w Σ_{j=1}^{L} min(P − a_j, a_{j−1})}.
```
Since `a_L = a_0`, the multiset `{a_1, …, a_L}` equals `{α_0, …, α_{L−1}}`, so `Σ_{j=1}^{L} (P − a_j) = Σ_{i=0}^{L−1} (P − α_i)`. Reindexing the hull sum by `i := j` (with `α_L := α_0` and predecessor `α_{j−1} = α_{i−1}` mod `L`) gives `Σ_i min(P − α_i, α_{i−1})`. Substituting into (1) yields the stated identity.

*Step 3: consistency with T4.* By T4 (§1), the orbit `O` contributes `w Σ_i (P − α_i)` to `dim_{F_q} C(a)` and `w Σ_i min(P − α_i, α_{i−1})` to `dim_{F_q} Hull_k(C(a))`. These are exactly the two exponents above, with the same orientation: current state `α_i` appears in `P − α_i`, predecessor `α_{i−1}` in the second argument of `min`. (Using the transposed matrix would reverse every walk; the trace is unchanged, but the bijection with assignments would then pair `min(P − α_i, α_{i+1})` — a different labeling of the same sum. The frozen row/column convention is the one matching T3–T4, and it is the one used here.)

*Case `L = 1`.* There is one position and one (closing) edge, the self-loop: `tr(T) = Σ_{a=0}^P T_{a,a} = Σ_a u^{w(P−a)} z^{w·min(P−a, a)}`, matching the formula with `α_{−1} = α_0`. ∎

**Remark.** The proof uses only the definition of matrix multiplication in a commutative ring and T4’s local contributions. In particular it is valid for every `P ≥ 1`, every `L ≥ 1`, and every `w ≥ 1`, with no field computation. This discharges RR-6.

---

## 3. The CRT/product assembly (the multi-component step of T6)

**Proposition 3.1 (assembly).** Under (G1)–(G6):

(i) The coefficient-tuple isomorphism `A[x] ≅ ∏_s K_s[x]` induces `A[x]/(x^n − λ) ≅ ∏_s K_s[x]/(x^n − λ_s)`, where `λ = (λ_s)_s`.

(ii) Ideals of a finite product of rings are exactly products of ideals of the factors. Hence `λ`-constacyclic `A`-codes (ideals of the ring in (i), i.e. `A`-submodules of `A^n` closed under the componentwise `λ`-constacyclic shift) correspond bijectively to tuples `(C_s)_s` of `λ_s`-constacyclic codes `C_s ⊆ K_s[x]/(x^n − λ_s)`, and exponent assignments correspond to tuples of component assignments; the total number is `∏_s (P+1)^{|F_s|} = (P+1)^{Σ_s |F_s|}` (with T1).

(iii) `D_A(C) = ∏_s D_s(C_s)` and `Hull_{A,k}(C) = ∏_s Hull_k(C_s)`.

(iv) `dim_{F_q} C = Σ_s m_s·dim_{K_s} C_s` and `dim_{F_q} Hull_{A,k}(C) = Σ_s m_s·dim_{K_s} Hull_k(C_s)`.

**Proof.** (i) A polynomial over `A = ∏_s K_s` is a tuple of polynomials over the `K_s` (coefficients are tuples), giving the ring isomorphism `A[x] ≅ ∏_s K_s[x]`; the element `x^n − λ` maps to the tuple `(x^n − λ_s)_s`, and quotienting a product ring by a product ideal gives the product of quotients. **No coprimality between components is needed**: this is the direct-product decomposition of the square-free algebra `A` itself, not a Chinese-remainder gluing of coprime moduli inside one component. Inside a component, the only coprimality used is (G2)’s `gcd(n_0, p) = 1`, which is what makes `S_s` separable with distinct factors (P1-04). All components share the same length `n` (G2); without a common `n`, `A^n` and a global twist `λ` would not be defined.

(ii) If `I` is an ideal of `∏_s R_s`, its projections `I_s` are ideals and `I ⊆ ∏_s I_s`; conversely, if `(x_s)_s ∈ ∏_s I_s`, then multiplying by the idempotent `e_t` (the element of `A` equal to `1` in component `t` and `0` elsewhere) shows each `(0,…,x_t,…,0) ∈ I`, and summing over `t` gives `(x_s)_s ∈ I`. Hence `I = ∏_s I_s`. The correspondence for codes and assignments follows componentwise from T1 (P1-04), and the count multiplies.

(iii) By (G5) the global pairing is componentwise: for `x = (x_s)`, `y = (y_s)`, the pairing value is the tuple `(⟨x_s, y_s⟩_{s,k})_s ∈ A`, which is `0` in `A` iff every component is `0`. Hence `y ∈ D_A(C)` iff `y_s ∈ D_s(C_s)` for all `s` (using (ii) to see `c` ranges over `C` iff each `c_s` ranges over `C_s`). Intersecting with `C = ∏_s C_s` componentwise gives the hull statement. Compatibility (G4) is what places each `D_s(C_s)` inside the same component quotient `K_s[x]/(x^n − λ_s)` (P1-04, T3); without it, (iii) still defines a product of transformed-twist codes, but the T6 formula in a single modulus is not asserted.

(iv) As `F_q`-vector spaces, `A^n ≅ ⊕_s K_s^n` (direct sum of the components), a product subspace has dimension equal to the sum of the component dimensions, and `dim_{F_q} V_s = [K_s : F_q]·dim_{K_s} V_s = m_s·dim_{K_s} V_s` for any `K_s`-subspace `V_s`. Apply this to `C` and to `Hull_{A,k}(C)` via (iii). ∎

---

## 4. T6 — The global joint enumerator (RR-7)

**Frozen statement (transcribed).** *Under the hypotheses above,*
```
E(u,z) := Σ_{labeled a} u^{dim_{F_q} C(a)} z^{dim_{F_q} Hull_k(C(a))}
        = ∏_{s=1}^N ∏_{O∈O_s} tr( T^{(P)}_{w_O}(u,z)^{L_O} ).
```

**Theorem T6.** Under (G1)–(G6), the displayed identity holds in `Z[u, z]`.

**Proof.** By Proposition 3.1(ii) and T1, the set of labeled global assignments is the Cartesian product
`Aset = ∏_{s=1}^N ∏_{f∈F_s} {0, …, P}` (the set of labeled global assignments),
and every `a ∈ Aset` is uniquely the disjoint union of its orbit restrictions `α^{(O)} ∈ {0,…,P}^{L_O}` over all pairs `(s, O)`. By T4 (with Proposition 3.1(iii)–(iv) converting component dimensions to `F_q`-dimensions),
```
dim_{F_q} C(a)      = Σ_{s} Σ_{O∈O_s} w_O Σ_{i=0}^{L_O−1} (P − α^{(O)}_i),
dim_{F_q} Hull_k(C(a)) = Σ_{s} Σ_{O∈O_s} w_O Σ_{i=0}^{L_O−1} min(P − α^{(O)}_i, α^{(O)}_{i−1}),
```
i.e. each global dimension is a **sum over `(s, O)` of a quantity depending only on the orbit’s own exponent tuple**. For each orbit define the local polynomial (in `Z[u, z]`)
`E_O(u, z) := Σ_{α∈{0,…,P}^{L_O}} u^{w_O Σ_i (P−α_i)} z^{w_O Σ_i min(P−α_i, α_{i−1})}`.  
By T5, `E_O(u, z) = tr( (T^{(P)}_{w_O}(u,z))^{L_O} )`.

It remains to factor the global sum. This is the finite distributive law: if an index set is a finite Cartesian product `∏_j J_j` and the exponent of each indeterminate is a sum `Σ_j Φ_j(α^{(j)})` over the factors, then
`Σ_{α ∈ ∏_j J_j} ∏_j u^{Φ_j(α^{(j)})} = ∏_j ( Σ_{α^{(j)} ∈ J_j} u^{Φ_j(α^{(j)})} )`  
(both sides expand to the same finite sum: the left side is the product of the right-side sums multiplied out; for two factors this is `Σ_{(x,y)} φ(x)ψ(y) = (Σ_x φ(x))(Σ_y ψ(y))`, and the general case follows by induction on the number of factors). Applying this with `j = (s, O)`, `J_j = {0,…,P}^{L_O}`, and the two exponent functions above (one for `u`, one for `z`, weights `w_O` included):
```
E(u, z) = ∏_{s=1}^N ∏_{O∈O_s} E_O(u, z) = ∏_{s=1}^N ∏_{O∈O_s} tr( (T^{(P)}_{w_O}(u,z))^{L_O} ).   ∎
```

**Hypotheses actually consumed (RR-7 checklist).** Common `P, n, k` and per-component compatibility (G1, G2, G4) — compatibility only via T3/T4; common length `n` for the product `A^n` (G2); fixed labeled decomposition with `A`-submodule codes (G3, Proposition 3.1(ii)); `gcd(n_0, p) = 1` only through the separable base `S_s` (G2/G4). This discharges RR-7.

---

## 5. Corollaries C1–C4

Each corollary is first transcribed from the frozen blueprint, then derived.

### C1 — Total count

**Frozen statement.** `E(1,1) = (P+1)^{Σ_s |F_s|}`.

**Derivation.** At `u = z = 1`, every entry of `T = T^{(P)}_{w_O}(1,1)` equals `1`, i.e. `T = J`, the `(P+1)×(P+1)` all-ones matrix. `J^2 = (P+1)J` (each entry of `J^2` is a sum of `P+1` ones), so `J^{L} = (P+1)^{L−1} J` for `L ≥ 1` by induction, and `tr(J^L) = (P+1)^{L−1}·(P+1) = (P+1)^L`. (Equivalently, by T5, `tr(T^L)` at `u=z=1` counts the `(P+1)^L` tuples `α`.) By T6,
`E(1,1) = ∏_s ∏_O (P+1)^{L_O} = (P+1)^{Σ_s Σ_O L_O} = (P+1)^{Σ_s |F_s|}`,
since the orbits of `s` partition `F_s`, so `Σ_O L_O = |F_s|`. This agrees with the direct count in Proposition 3.1(ii). ∎

### C2 — Code-dimension distribution

**Frozen statement.** `E(u,1) = ∏_s ∏_{f∈F_s} (1 + u^{w_f} + ⋯ + u^{P w_f})`, where `w_f = m_s·deg f`.

**Derivation.** Set `z = 1` in T6. In `T = T^{(P)}_w(u, 1)`, the entry `T_{a,b} = u^{w(P−b)}` does not depend on the row `a`. Write `c = (1, …, 1)^T` (column) and `r` for the row vector with `r_b = u^{w(P−b)}`; then `T = c·r` (outer product). Hence `T^L = (r·c)^{L−1}·T` (each internal contraction contributes the scalar `r·c`), and
`tr(T^L) = (r·c)^{L−1}·tr(T)`.  
Now `r·c = Σ_{b=0}^P u^{w(P−b)} = Σ_{j=0}^P u^{w j}` (substituting `j = P − b`), and `tr(T) = Σ_{a=0}^P u^{w(P−a)} = Σ_{j=0}^P u^{w j}` as well. Therefore
`tr( (T^{(P)}_w(u,1))^L ) = ( Σ_{j=0}^P u^{w j} )^L`.  
For an orbit `O`, every factor has the same degree (RR-2(vi)), hence the same weight `w = w_f` for all `f ∈ O`, and the orbit contributes `(Σ_{j=0}^P u^{w_f j})^{L_O} = ∏_{f∈O} (1 + u^{w_f} + ⋯ + u^{P w_f})`. Taking the product over all orbits and components (T6) gives exactly `∏_s ∏_{f∈F_s} (1 + u^{w_f} + ⋯ + u^{P w_f})`. ∎

(Consistency: at `u = 1` this returns C1.)

### C3 — LCD count

**Frozen statement.** `#{a : Hull = 0} = 2^{#orbits}`. (Here `Hull = 0` means `dim_{F_q} Hull_{A,k}(C(a)) = 0`, and `#orbits` is the total number of `τ_s`-orbits over all components.)

**Derivation.** `dim_{F_q} Hull_{A,k}(C(a)) = 0` iff every orbit contributes `0` in T4’s formula: the total is a sum of terms `w_O·min(P − α_i, α_{i−1})` with `w_O ≥ 1` and `min(·,·) ≥ 0`, so the sum vanishes iff `min(P − α_i, α_{i−1}) = 0` for every orbit and every `i` (equivalently, this is the coefficient of `z^0` in `E(1, z)`).

Fix one orbit and suppose `min(P − α_i, α_{i−1}) = 0` for all `i`. **Claim: `α` is either identically `0` or identically `P`.** Suppose some `α_m ∉ {0, P}` (possible only if `P ≥ 2`). Since `min(P − α_{m+1}, α_m) = 0` and `α_m > 0`, we must have `P − α_{m+1} = 0`, i.e. `α_{m+1} = P`. Then `min(P − α_{m+2}, α_{m+1}) = min(P − α_{m+2}, P) = P − α_{m+2} = 0` forces `α_{m+2} = P`; continuing around the finite cycle, every `α_i = P`, contradicting `α_m ∉ {0, P}` (for `L = 1` the starting supposition already gives `min(P − α_0, α_0) = 0` only for `α_0 ∈ {0, P}` when `P ≥ 2`, and for `P = 1` there are no interior values at all). Hence every `α_i ∈ {0, P}`. If both values occur, choose `i` with `α_i = 0` whose predecessor has `α_{i−1} = P` (such a boundary index exists on a cycle containing both values); then `min(P − α_i, α_{i−1}) = min(P, P) = P ≥ 1`, contradiction. So `α ≡ 0` or `α ≡ P`: exactly **2** admissible tuples per orbit, for every `P ≥ 1` — the count is independent of `P`. Choices on distinct orbits/components are independent (T1, Proposition 3.1(ii)), so the total count is `2^{#orbits}`. ∎

(This proof replaces the frozen one-line sketch, whose forward-propagation wording is imprecise for interior exponents; the **statement** needed no correction.)

### C4 — Self-orthogonal and dual-containing characterizations

**Frozen statement.** `C ⊆ D(C)` ⟺ on every orbit edge `α_{i−1} + α_i ≥ P`; the count is `∏_O tr(B_P^{L_O})` with `(B_P)_{a,b} = 1` if `a + b ≥ P`, else `0`. Conversely `D(C) ⊆ C` ⟺ `α_{i−1} + α_i ≤ P` on every edge. (The frozen text states no count for the dual-containing side; see PC-4 below.)

**Derivation.** Work globally; all dimension identities are over `F_q` via T4/Proposition 3.1.

*Self-orthogonal side.* By definition `Hull_{A,k}(C) = C ∩ D_A(C) ⊆ C`, so `C ⊆ D_A(C)` iff `C ∩ D_A(C) = C` iff `dim Hull = dim C` (a subspace equals a containing subspace iff dimensions agree). By T4,
```
dim C − dim Hull = Σ_{s,O} w_O Σ_i [ (P − α_i) − min(P − α_i, α_{i−1}) ].
```
For each edge, `(P − α_i) − min(P − α_i, α_{i−1}) = max(0, P − α_i − α_{i−1})`: if `α_i + α_{i−1} ≤ P`, then `min(P − α_i, α_{i−1}) = α_{i−1}` and the difference is `P − α_i − α_{i−1} ≥ 0`; if `α_i + α_{i−1} ≥ P`, then `min(P − α_i, α_{i−1}) = P − α_i` and the difference is `0`. Each summand is `≥ 0` and `w_O ≥ 1`, so the total is `0` iff every edge satisfies `α_{i−1} + α_i ≥ P`. This proves the characterization.

For the count: the condition factorizes over orbits. On one orbit, admissible tuples are the closed walks on states `{0,…,P}` whose every step `a → b` satisfies `a + b ≥ P`; by the trace expansion of §2 Step 1 applied to the `0/1`-matrix `B_P` (same computation with weights `0/1`), their number is `tr(B_P^{L_O})`. Independence over orbits (T1) gives the global count `∏_O tr(B_P^{L_O})` (product over all components’ orbits).

*Dual-containing side.* Again `Hull = C ∩ D_A(C) ⊆ D_A(C)`, so `D_A(C) ⊆ C` iff `dim Hull = dim D_A(C)`. By T3, on one orbit the dual generator has exponents `β_i = P − α_{i−1}`, so T4 applied to the dual assignment gives `dim D(C(a)) = Σ_{s,O} w_O Σ_i (P − β_i) = Σ_{s,O} w_O Σ_i α_{i−1} = Σ_{s,O} w_O Σ_i α_i` (reindexing `i ↦ i+1` in the last sum; the orbit sum is cyclic). Hence
```
dim D(C) − dim Hull = Σ_{s,O} w_O Σ_i [ α_{i−1} − min(P − α_i, α_{i−1}) ],
```
and for each edge, `α_{i−1} − min(P − α_i, α_{i−1}) = max(0, α_i + α_{i−1} − P)`: if `α_i + α_{i−1} ≤ P`, then `min(P − α_i, α_{i−1}) = α_{i−1}` and the difference is `0`; if `α_i + α_{i−1} ≥ P`, then `min(P − α_i, α_{i−1}) = P − α_i` and the difference is `α_i + α_{i−1} − P ≥ 0`. So `dim D(C) − dim Hull = 0` iff every edge satisfies `α_{i−1} + α_i ≤ P`, proving the converse characterization. ∎

**Proposed completion PC-4 (unapproved; not part of frozen C4).** The same closed-walk argument gives `#{a : D(C) ⊆ C} = ∏_O tr((B′_P)^{L_O})` with `(B′_P)_{a,b} = 1` iff `a + b ≤ P`. Moreover the two counts in C4 are equal: the involution `α_i ↦ P − α_i` on each orbit maps `{α_{i−1} + α_i ≥ P}` bijectively to `{α_{i−1} + α_i ≤ P}` (as `(P − α_{i−1}) + (P − α_i) ≤ P ⟺ α_{i−1} + α_i ≥ P`), preserving closed walks. Adding the displayed count to the frozen corollary remains subject to the PC approval command; the **characterization** above is frozen and is proved as stated.

---

## 6. Simple-root recovery: the `P = 1` specialization (Gate G3 bookkeeping for T5/T6/C1–C4)

Set `ϱ = 0`, so `P = 1`. Then:

- **Model.** `μ_s = λ_s` (the unique 1st root), `M_s = S_s = x^{n_0} − λ_s`, which is separable with distinct factors (`gcd(n_0, p) = 1`); assignments are binary, `a_f ∈ {0, 1}`, and `g_a` is a squarefree divisor — the classical simple-root constacyclic parametrization. `σ_s, ρ_s, τ_s` are unchanged (they depend on `d_s, k`, not on `P`), and compatibility is the same condition.
- **Local terms (T4 at `P = 1`).** `P − α_i = 1 − α_i`, and `min(1 − α_i, α_{i−1})` equals `1` if `(α_{i−1}, α_i) = (1, 0)` and `0` otherwise: the hull contribution of an edge is the indicator of the transition `1 → 0`. Hence `dim Hull` counts, with weights `w_O`, the number of `1 → 0` transitions around each orbit — the predecessor (simple-root) hull formula in this notation.
- **Transfer matrix (T5 at `P = 1`).** With states `{0, 1}` (row = previous `a`, column = current `b`), `T^{(1)}_w(u,z)_{a,b} = u^{w(1−b)} z^{w·min(1−b, a)}` gives
```
T^{(1)}_w(u,z) = ⎡ u^w        1   ⎤      (a=0 row)
                 ⎣ u^w z^w    1   ⎦      (a=1 row)
```
since `min(1,0) = 0`, `min(0,0) = 0`, `min(1,1) = 1`, `min(0,1) = 0`. The T6 product `∏_s ∏_O tr( (T^{(1)}_{w_O})^{L_O} )` is therefore exactly the predecessor binary-state joint enumerator, with the same orbit/orientation conventions (`τ(f_i) = f_{i+1}`, predecessor `α_{i−1}`, closing edge from position `L−1` to position `0`). This proves algebraically — not just by analogy — that the `P = 1` specialization of T5/T6 **is** the stated simple-root formula.
- **Corollaries at `P = 1`.** C1: `E(1,1) = 2^{Σ_s |F_s|}` (all squarefree divisors). C2: `E(u,1) = ∏_s ∏_f (1 + u^{w_f})`. C3: `2^{#orbits}` (unchanged — C3 is `P`-independent). C4: self-orthogonal iff no edge is `(0,0)` (i.e. `α_{i−1} + α_i ≥ 1` on every edge), dual-containing iff no edge is `(1,1)` (i.e. `α_{i−1} + α_i ≤ 1` on every edge), counted by `tr(B_1^{L_O})` resp. `∏ tr((B′_1)^{L_O})` (the latter via PC-4).

**Scope note.** This recovery concerns T5, T6, C1–C4 only. It deliberately makes no claim about the frozen C5 remark “`P = 1` gives `1/4`”: that remark is false for `L_O = 1` orbits (`ν_1 = 0`), is already recorded (GAP-01/PC-1), and is not used anywhere above.

---

## 7. Dependency map

**Previously proved (P1-04; used as inputs, conventions rechecked in §1):**
```
Fact 0.1/0.2 (K[x] PID/UFD) ─► RR-1 ─► T1 ──────────────┐
RR-2 (#, τ) ─► T2 ─► T3 (with RR-3, RR-4) ─► T4 ────────┤
RR-3 (Euclidean dual) ─► T3          RR-5 (lcm) ─► T4 ──┘
```

**New in this package:**
```
T4 (orbit-local dimension sums) ─► T5 [trace = closed walks; RR-6 discharged] ─┐
Prop. 3.1 (CRT/product assembly; ideals, dual, dimensions) ───────────────────┤
Finite distributive law ──────────────────────────────────────────────────────┴► T6 [RR-7 discharged]
T6 + T5 (J-power / rank-one trace) ─► C1, C2
T4 (hull sum = 0 termwise) ─► C3
T4 + T3 (dim D via β_i; nonnegative edge differences) ─► C4
§2–§5 at ϱ = 0 ─► P = 1 recovery (2×2 matrix; 1→0 transition indicator)
```

**Distinguishing old from new:** T5’s only new content is the closed-walk expansion (RR-6); T6’s only new content is Proposition 3.1 plus the distributive law (RR-7). Both are proved above in full; neither relies on any computation.

---

## 8. Remaining obligations (not proved here; no claim made)

1. **C5** — frozen hull mean is incorrect for `L_O = 1`; the corrected split (`μ_P` for `L_O ≥ 2`, `ν_P` for `L_O = 1`) is candidate **PC-1**, unapproved. The `F_q` code-dimension mean in frozen C5 is correct but is not re-proved here (P1-03 §4.2 records the derivation).
2. **C6 / RR-8** — variance closed forms (`L = 1`, `L = 2`, `L ≥ 3` covariances) remain open; exact finite-sum obligations are listed in P1-03 §4.3.
3. **C7 / RR-9** — conditional EAQECC statement only; the enumerator alone yields no distance or quantum parameter.
4. **PC-1…PC-6** — all unapproved. PC-4’s dual-containing count is proved above as a labeled proposal; PC-2/PC-3 concern blueprint wording (the dual-order sentence; `f(0) ≠ 0`) adopted inside P1-04/P1-05 hypotheses only.
5. **Gate G1** — literature/novelty remains open and untouched by these proofs; no novelty or priority claim is made.

---

## 9. Computational cross-check (supporting evidence, not proof)

Executed for this package (21 Oct 2026); existing artifacts unmodified:

```
python3 code/validate_p1_03.py   # rerun: exit 0, output byte-identical to code/validation_p1_03_output.txt
                                 # (single-component T5/T6 + C1-C4 vs Gram-rank brute force;
                                 #  6 vector cases, 2,806 assignments; 31 (P,L) orbit pairs)
python3 code/validate_p1_05.py   # NEW script; output code/validation_p1_05_output.txt
                                 # final line: ALL P1-05 MULTI-COMPONENT ASSEMBLY CHECKS PASSED
```

The new P1-05 check is the first **multi-component** test: `A = GF(2) × GF(4)` (`q = 2`, `k = 0`, `λ = (1,1)`, `P = 2`, `n_0 = 7`, `n = 14`; component weights `m_1 = 1`, `m_2 = 2`), 729 labeled global assignments. It verifies that the joint `F_q`-dimension distribution obtained by adding independently brute-forced (Gram-rank) component dimensions equals (i) the convolution of the component distributions, (ii) the T6 product of per-orbit transfer traces with weights `w_O = m_s·deg f_O` (orbits `(L,w) = (1,1), (2,3)` and `(1,2), (2,6)`), and (iii) the C1 total `3^6 = 729`, the C2 marginal, C3’s count `2^4 = 16`, and C4’s self-orthogonal/dual-containing counts `144 = 144`. What it cannot prove: the CRT/`A`-submodule correspondence (Proposition 3.1 is a proof, not a computation), the T5/T6 formulas in general, or anything for `k > 0`, `λ ≠ 1`, `P ≠ 2`, or `N > 2`. Finite agreement is supporting evidence only.
