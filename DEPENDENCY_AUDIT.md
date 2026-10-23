# DEPENDENCY_AUDIT.md — theorem-by-theorem proof audit

Manuscript: *The joint code–hull distribution of repeated-root constacyclic
codes over finite products of finite fields via transfer matrices*.
Item numbers below use the compiled numbering (Theorem III.1, etc.); the LaTeX
label is given for machine lookup.

**Scope.** 2 definitions, 13 theorems/lemmas/propositions, 10 corollaries,
6 examples = 31 items. Each is checked for: hypotheses actually used,
dependencies, boundary cases, external citations, and — separately — whether
its support is an algebraic proof or a finite computation.

---

## A. Standing hypotheses

| id | hypothesis | introduced |
|---|---|---|
| H1 | `p` prime, `q = p^e`, `0 <= k < e`, so `1 <= d_s - k <= d_s` | §II |
| H2 | `A ≅ ∏_s K_s`, `K_s = F_{q^{m_s}} = F_{p^{d_s}}`, `d_s = e m_s`, labels fixed | §II |
| H3 | `P` a power of `p`; `n = P n_0`, `gcd(n_0,p) = 1` (so `x^{n_0} - μ_s` is separable) | §II |
| H4 | `λ_s ∈ K_s^*`; `μ_s^P = λ_s`; `M_s = x^n - λ_s = (x^{n_0}-μ_s)^P` | §II |
| H5 | **compatibility**: `λ_s^{1+p^{d_s-k}} = 1` | Def. II.2 |
| H6 | the code-first pairing with `σ` on the *right* slot | Def. II.1 |
| H7 | uniform measure on **labeled** assignments | §VIII |

---

## B. Item-by-item audit

Legend for "support": **A** = algebraic proof (the written argument, checked by
inspection); **C** = finite computation (corroboration only, never a proof of a
universal statement); **S** = symbolic identity in `P` (a proof for that family
of statements, since it is an all-`P` polynomial identity).

### Definitions

| # | Item | Check | Verdict |
|---|---|---|---|
| D1 | **Def. II.1** code-first Galois pairing `⟨x,y⟩_k = Σ x_i σ(y_i)`, `D(C)`, `Hull_k` | Well-defined? `σ ∈ Aut(K_s)` is `F_p`-linear, so the pairing is `F_p`-bilinear and non-degenerate. Non-degeneracy is what makes `dim D(C) = n − dim C` valid, used later in Lemma IV.1. | sound; non-degeneracy verified as `dim C + dim D = n·d` on every assignment of all 10 test families (C) |
| D2 | **Def. II.2** compatibility + `τ_s(f) = f#` | `τ_s` must be a *permutation* of `F_s` for "orbits" to be defined. Stated as a consequence of Thm III.2(iii), not assumed. | sound; the word "involution" was wrong and has been repaired (a `τ`-orbit of length 6 exists, F_8, k=0, n0=7) |

### §III Parametrization

| # | Item | Hypotheses used | Depends on | Boundary cases | Support | Verdict |
|---|---|---|---|---|---|---|
| 1 | **Thm III.1** (T1) parametrization, `dim C = n − Σ a_f deg f` | H2, H3, H4 (square-freeness is *essential*: `x^{n_0}−μ_s` must split into distinct irreducibles) | Def. II.1 | `P = 1` (factors distinct); `n_0 = 1`; single factor | A + C | sound |
| 2 | **Thm III.2** (T2) reciprocal operation (i) multiplicativity (ii) `f#` is min. poly of `ξ^{−p^{d_s−k}}` (iii) `τ_s` permutes, compatibility ⇔ `μ_s^{1+p^{d_s−k}}=1` | H1, H4, H5 | — | `k = 0` ⇒ `σ = ρ = id` and H5 ⇔ `λ² = 1` (verified); `k = e−1` ⇒ `ρ` is one Frobenius step | A; (i) additionally C (2800 random pairs); (iii) C | sound |

### §IV The Galois dual

| # | Item | Hypotheses used | Depends on | Boundary cases | Support | Verdict |
|---|---|---|---|---|---|---|
| 3 | **Lemma IV.1** (RR3) Euclidean dual `C^⊥ = ⟨h^♮⟩` | H4, `h_0 ≠ 0` | — | `r = n` (`g = 1`), `r = 0` (`g = x^n−λ`) both treated explicitly | A | sound |
| 4 | **Prop. IV.2** transport `D(C) = ρ(C^⊥)` | H6 | Lemma IV.1, D2 | `λ` not compatible: modulus becomes `x^n − λ^{-p^{d_s-k}}`, stated | A + C | sound |
| 5 | **Thm IV.3** (T3) dual exponents `β_i = P − α_{i−1}` | H5 | Prop. IV.2, Thm III.2(i)(iii) | incompatible case explicitly excluded from the same-modulus reading | A + C | sound |

### §V The hull

| # | Item | Hypotheses used | Depends on | Boundary cases | Support | Verdict |
|---|---|---|---|---|---|---|
| 6 | **Lemma V.1** intersection of ideals in a quotient | none beyond monic divisors | — | equality of *images* needs `(M) ⊆ (g),(l)`, which holds since `g,l | M` | A | sound |
| 7 | **Thm V.2** (T4) hull generator + both dimensions | H5 | Thm III.1, Thm IV.3, Lemma V.1 | `L = 1` orbit; orbits of unequal length; `P = 1` | A + C (exhaustive) | sound |

### §VI The enumerator

| # | Item | Hypotheses used | Depends on | Boundary cases | Support | Verdict |
|---|---|---|---|---|---|---|
| 8 | **Thm VI.1** (T5) transfer trace | none (a matrix identity, valid for every integer `P ≥ 1`) | — | `L = 1` self-loop treated explicitly | A + C | sound |
| 9 | **Prop. VI.2** product assembly | H2 | — | no coprimality needed between components (square-free algebra) | A + C (Example IX.5) | sound |
| 10 | **Thm VI.3** (T6) joint enumerator | H2, H5, labeled components | Thm III.1, Thm V.2, Thm VI.1, Prop. VI.2 | `N = 1`; one orbit | A + C (exhaustive) | sound |
| 11 | **Cor. VI.4** joint symmetry `K ↔ Δ−K` | — | Thm VI.3 | `L = 1`; `L = 2` | A + C | sound |
| 12 | **Prop. VI.5** `P = 1` specialization | H3 | Thm VI.1 | the matrix is given explicitly | A + C | sound |

### §VII Counting corollaries

| # | Item | Depends on | Boundary cases | Support | Verdict |
|---|---|---|---|---|---|
| 13 | **Cor. VII.1** total count `(P+1)^{Σ|F_s|}` | Thm VI.3 | `L = 1` (`J^1`) | A + C | sound |
| 14 | **Cor. VII.2** code-dimension distribution | Thm VI.3 | rank-one argument at `z = 1` | A + C | sound |
| 15 | **Cor. VII.3** LCD count `2^{#orbits}` | Thm V.2 | `L = 1` handled separately in the proof; `P ≥ 2` needed for the "`α ∉ {0,P}` ⇒ contradiction" step | A + C | sound |
| 16 | **Cor. VII.4** LCD refinement + conditional law | Cor. VII.3, H7 | `L = 1` contributes `P w_O L_O = P w_O` | A + C | sound |
| 17 | **Cor. VII.5** self-orthogonal / dual-containing | Thm V.2, Thm VI.1 | equality of the two counts via `α ↦ P−α` | A + C | sound |
| 18 | **Cor. VII.6** restricted enumerators | Cor. VII.5 | edge predicates `a+b ≥ P`, `≤ P` | A | sound (not separately computed; the underlying counts were) |

### §VIII Moments

| # | Item | Depends on | Boundary cases | Support | Verdict |
|---|---|---|---|---|---|
| 19 | **Lemma VIII.1** edge moments | — | `P = 1`; `c = 0`; `c = P` | A + S | sound |
| 20 | **Thm VIII.2** (C5) means | Thm V.2, Lemma VIII.1 | **`L = 1` must use `ν_P`, not `μ_P`**; `ν_1 = 0` | A + S | sound |
| 21 | **Lemma VIII.3** variance pieces (i) `L=1` (ii) `L≥3` covariance (iii) `L=2` | Lemma VIII.1 | `L = 2` is genuinely different from `L ≥ 3` at `L = 2`: `44/81` vs `8/27` at `P = 2` (both recomputed) | A + S | sound |
| 22 | **Thm VIII.4** (C6) variance | Lemma VIII.3, orbit independence (H7) | `V_1(1) = 0`, `V_2(1) = 1/4`, `V_L(1) = L/16` | A + S + C | sound |
| 23 | **Cor. VIII.5** second-order structure | Thm V.2, H7 | `Cov = 0` by `+γ_P`/`−γ_P` cancellation; `L = 1` by symmetry | A + S + C | sound |

### §IX Examples

| # | Item | Support | Verdict |
|---|---|---|---|
| 24 | Ex. IX.1 (`P=2, L=2`) | hand-checked, all 9 tuples | correct |
| 25 | Ex. IX.2 (`P=1, L=3`) | hand-checked, all 8 words | correct |
| 26 | Ex. IX.3 (F_4, `n_0=5`) | **independently reproduced cell-for-cell** (15/15), mean 23/9, var 194/81, LCD 4, SO=DC=12 | correct |
| 27 | Ex. IX.4 (F_8, `n_0=7`, 2187) | **reproduced**: all 44 cells, mean 11/3, var 10/9, LCD 4, SO=DC=258, and the orientation claim 2187/2187 vs 27/2187 | correct |
| 28 | Ex. IX.5 (F_2 × F_4, 729) | **reproduced**: orbit data, assembly, mean 11, var 230/9, LCD 16 | correct |
| 29 | Ex. IX.6 (F_9, `λ=ι`, 16) | **reproduced**: all 7 cells, mean 7/2, var 15/4, LCD 2, SO=DC=10 | correct |

---

## C. Which hypotheses are actually used (and only there)

| hypothesis | used by | *not* used by |
|---|---|---|
| H5 compatibility | Thm III.2(iii), Thm IV.3, Thm V.2, Thm VI.3 and everything above them | Thm III.1, Lemma IV.1, Prop. IV.2, Thm VI.1, all of §VIII (they are about the exponent/matrix model) |
| H3 separability | Thm III.1 (factorization into distinct irreducibles) | §VIII moments (pure combinatorics of the exponent model) |
| H7 uniform labeling | §VIII only | all counting results in §VII (which are labeled counts by construction) |

This matches the paper's own claims: §IV–§V restrict to compatible twists, and
§X says the hull formula is not asserted otherwise.

## D. Boundary cases

| case | behaviour | checked |
|---|---|---|
| `P = 1` | hull contribution of an `L = 1` orbit is `min(1−α, α) = 0`; if **all** orbits have length 1 the hull vanishes for every code, so the family is entirely LCD | verified on three families (max hull 0, LCD count = total count) |
| `P = 1`, mean | `ν_1 = 0`, so the mean is `¼·Σ_{L≥2} w_O L_O` — **not** `Δ/4` | verified exactly |
| `L = 1` | uses `ν_P`, not `μ_P`; this is the paper's stated pedagogical point | verified |
| `L = 2` | two edges share both variables; `V_2 ≠ V_{L≥3}|_{L=2}` | verified (`44/81` vs `8/27` at `P = 2`) |
| `k = 0` | `σ = ρ = id`; compatibility ⇔ `λ² = 1` | verified on F_4, F_9, F_8 |
| `k = e−1` | `ρ` is a single Frobenius step; `d_s − k = 1 > 0` | verified |
| `N = 1`, one orbit | Cor. VI.4 and VII.3 degenerate correctly | verified |
| `λ = −1` (negacyclic) | used in test families with `p` odd | verified |

## E. Dependence on cited results

| citation | role in the paper | status |
|---|---|---|
| [FZ2017] | introduces the `k`-Galois inner product | attribution only, no theorem used |
| [LP2020] | code-first slot convention | convention only |
| [DPI2023, Thm 3] | Remark V.3: single-component specialization of Thm V.2 | **abstract-level only**; the paper presents its own proof, so nothing rests on it |
| [DPI2023, Thm 4] | Remark V.3: their orbit-length restriction (1,2,4) | abstract-level only; descriptive, not load-bearing |
| [DP2025, Thm 3.3] | Remark VIII.3: single-component agreement | **fixed-text point**: the published Table 1 entry (q=4, n=7, λ=ω, k=1, Δ_1=1) reports E = 3/2; the paper's formula gives `ν_1·1 + μ_1·6 = 3/2`, and the independent computation gives 3.0 in F_2-dimensions = 3/2 in F_4-dimensions. Agrees. |
| [Sendrier1997] | contrast with random linear codes | descriptive |

## F. Algebraic proof vs finite computation — explicit separation

**What the computations establish.** For each tested family, the *printed
formulas* agree with the *objects they describe*, where those objects were
computed from the definitions (dual by solving the pairing equations, hull by
subspace intersection). This rules out wrong constants, wrong indices, wrong
orientation, and mis-stated boundary behaviour. The symbolic layer proves the
15 moment identities for **all** `P`.

**What the computations do not establish.** They do not prove T1–T6 for
arbitrary `N`, `n_0`, orbit structure, or field. Those rest on the written
arguments in §III–§VIII, which are complete and which this audit checked line
by line (table B). No step in the paper appeals to computation; §IX says so
explicitly, and that sentence is accurate.

**No gap was found.** No theorem, equation, numerical value or proof step was
modified in this round; the three changes are a corrected dictionary, a
restricted asymptotic claim, and a softened literature comparison.

## G. Verdict

All 25 numbered mathematical items: **sound**. The only defects found in the
whole audit were in the surrounding prose (the dictionary at line 235, the
growth claim, and the DP2025 absence claim), all three now repaired.
