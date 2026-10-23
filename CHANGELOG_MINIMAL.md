# CHANGELOG_MINIMAL.md — complete, cumulative

Base: `ORIGINAL_SNAPSHOT/manuscript/P1_41_MANUSCRIPT_IEEE_SINGLE_COLUMN.tex`
(1474 lines, unmodified, read-only).
Final: `FINAL_IEEE_TIT_SUBMISSION.tex`.

**No theorem, proof step, equation, symbol, definition, numerical value,
section, citation, author detail or title was altered.** Every edit is a repair
of terminology, claim strength, IEEE compliance, or line breaking.

## Round 1 — scientific/terminology (6 edits in 6 hunks)

| # | Location | Before | After | Reason |
|---|---|---|---|---|
| 1 | abstract | "reciprocal **involution** on those factors" | "reciprocal **map** on those factors" | `tau_s` is a permutation; F_8, k=0, n0=7 has a `tau`-orbit of length 6 |
| 2 | §I | "reciprocal **involution** on these factors" | "reciprocal **map**" | same |
| 3 | §I | "orbits of the reciprocal **involution**" | "orbits of the reciprocal **map**" | same |
| 4 | Definition 3.2 head | "[compatibility and the **involution** `tau_s`]" | "[compatibility and the **reciprocal map** `tau_s`]" | heading contradicted the definition body, which says "is a permutation" |
| 5 | §XI | "orbits of the reciprocal **involution**" | "orbits of the reciprocal **map**" | same |
| 6 | §VIII | "so **the typical code** of the family has a hull growing linearly with n" | "so **the mean hull dimension** grows linearly with n, whereas the hull dimension of a random linear code stays bounded in probability" | a mean does not license a typical-code claim without concentration |

## Round 2 — IEEE TIT compliance (2 edits)

| # | Location | Before | After | Reason |
|---|---|---|---|---|
| 7 | index terms | 12 words: "Constacyclic codes, repeated-root codes, Galois hull, joint enumerator, transfer matrix, finite fields." | 10 words: "Constacyclic codes, Galois hull, joint enumerator, transfer matrices, finite fields." | TIT requires five to ten words |
| 8 | abstract | "the number of LCD codes" | "the number of linear complementary dual codes" | abstract must not use abbreviations |

## Round 2 — typography, found in the compiled PDF (6 edits)

| # | Location | Before | After | Reason |
|---|---|---|---|---|
| 9 | Lemma 8.1 | two inline expectations in running text | same two formulas as one display | removes a 22.8 pt overfull box; identical content |
| 10 | Example 9.4 | `{\footnotesize ...}` run into the paragraph | `\par{\footnotesize\raggedright ... \par}` | the 14-cell list could not be broken and overflowed by 49.7 pt, then 43.8 pt |
| 11 | §IX | `\paragraph{Computational verification.}` | `\paragraph{Computational verification}` | IEEEtran appends the colon; the run-in head overflowed by 26.6 pt |
| 12–14 | §IX, 4 occurrences | `\texttt{code/validate_audit_fixes.py}`, `\texttt{code/validate_p1_14.py}` | `\texttt{code/}\allowbreak\texttt{validate_...}` | the long `\texttt` token had no break opportunity |
| 15 | regression repair | `\texttt{code/}\allowbreak\texttt{code/validate_...}` | `\texttt{code/}\allowbreak\texttt{validate_...}` | edit 12–14 duplicated the `code/` prefix; caught by reading the rendered page 14, not by the compiler |

Edits 9–15 change **no words of the text** except removing one stray period in
a run-in heading; they change only where lines break.

## Deliberately not changed

* `D(C) = rho(C^perp)`, the `sigma`/`rho` slot order (already correct),
  `rho = sigma^{-1} = x^{p^{d_s-k}}`.
* "involution" at three places referring to `alpha -> P - alpha` — that one
  *is* an involution; changing it would be an error.
* The `P = 1` statements (verified correct).
* All theorems, proofs, examples, numbers, citations, title, author block.
* Novelty wording (already conservative and correctly attributed).

## Reproduction

```
diff -u ORIGINAL_SNAPSHOT/manuscript/P1_41_MANUSCRIPT_IEEE_SINGLE_COLUMN.tex \
        FINAL_IEEE_TIT_SUBMISSION.tex
```

---

# Round 3 — scientific corrections (3 hunks, 3 files touched: tex only)

Base for this round: commit `bd6d92a` (`FINAL_IEEE_TIT_SUBMISSION.tex`,
sha256 `7e340d7f…`). Result: sha256 `0677c614…`.
**No theorem, equation, numerical value, proof step, figure or citation
identifier was altered.** Only prose was corrected, in three places.

## Hunk 1 — line 235: the Galois-dual dictionary was wrong

```diff
@@ -232,11 +232,11 @@ The Euclidean dual is denoted \(C^\perp\).
 dual convention of Liu and Pan~\cite{LP2020}; in the finite-field case
-the dictionary is \(D(C) = \sigma^{e-k}(C^\perp)\). The slot order is part of the definition: the candidate \(y\) occupies
-the \(\sigma\)-twisted slot, and this is what makes
-\(D(C) = \rho(C^\perp)\) (coordinatewise \(\rho\);
-Proposition~\ref{prop:transport}) rather than the analogous statement
-with \(\sigma\). All dual formulas below use this convention. The global
+the dictionary is \(D(C) = \rho(C^\perp)\), where \(\rho\) acts
+coordinatewise, \(\alpha \mapsto \alpha^{p^{d_s-k}}\). The slot order is part of the definition: the candidate \(y\) occupies
+the \(\sigma\)-twisted slot, and this is what selects \(\rho\) rather
+than \(\sigma\) in that dictionary
+(Proposition~\ref{prop:transport}). All dual formulas below use this convention. The global
```

**Why.** `σ(α) = α^{p^k}` is a map; `σ^{e−k}` as a *composition power* satisfies
`σ^j(α) = α^{p^{kj}}`, so the printed dictionary asserts the map
`α ↦ α^{p^{k(e−k)}}`. The correct map is `ρ(α) = α^{p^{d_s−k}}`. These agree
only when `k(e−k) ≡ d_s−k (mod d_s)`. Independently verified as maps on the
fields, not on the notation:

| field | `k` | `σ^{e−k}` gives exponent | `ρ` gives | equal? |
|---|---|---|---|---|
| F_8 | 1 | `p^2` | `p^2` | yes |
| F_8 | 2 | `p^2` | `p^1` | **no** |
| F_16 | 1 | `p^3` | `p^3` | yes |
| F_16 | 2 | `p^4 ≡ 1` | `p^2` | **no** |
| F_16 | 3 | `p^3` | `p^1` | **no** |
| F_9 | 1 | `p^1` | `p^1` | yes |
| F_{2^4} (`e=2`, `m_s=2`, `k=1`) | 1 | reading `e−k=1` gives `p^1` | `p^3` | **no** |

So the old sentence was false for every `k` other than the special ones, with
either reading of `e` (`e` or `d_s`). It also contradicted line 237 two lines
later, which already said `D(C) = ρ(C^⊥)`. The replacement states the true
dictionary once and keeps the slot-order explanation; `d_s` is used rather than
`e` because `ρ` is defined per component where `K_s = F_{p^{d_s}}` and
`d_s = e m_s`.

## Hunk 2 — lines 850–861: "grows linearly" was not justified for every family

```diff
@@ -849,13 +849,19 @@
-\( \mu_P / P \to 1/3 \) as \( P \to \infty \) (and \( \mu_1 = 1/4 \)), the mean
-hull dimension is a positive proportion of the ambient dimension
-\( \Delta \) --- roughly \( \Delta/3 \) for large \( P \), \( \Delta/4 \) at
-\( P = 1 \), apart from the length-one-orbit correction --- so the mean
-hull dimension grows linearly with \( n \), whereas the hull dimension of
-a random linear code stays bounded in probability~\cite{Sendrier1997}.
+\( \mu_P / P \to 1/3 \) and \( \nu_P / P \to 1/4 \) as \( P \to \infty \),
+Theorem~\ref{thm:C5} yields
+\( \Delta/6 \le \E[\dim_{\Fq}\Hull_k(C)] \le \Delta/3 \) for every
+\( P \ge 2 \), where \( \Delta = \sum_s m_s n \) is the ambient
+\( \Fq \)-dimension; hence for every admissible family with \( P \ge 2 \)
+the mean hull dimension grows linearly in \( n \) with an explicit
+constant, whereas the hull dimension of a random linear code stays
+bounded in probability~\cite{Sendrier1997}. At \( P = 1 \) we have
+\( \nu_1 = 0 \), so the mean equals \( \tfrac14 \sum_{L_O \ge 2} w_O L_O \):
+it is a positive proportion of \( \Delta \) exactly when orbits of length
+at least two carry positive weight, and it vanishes identically when
+every orbit has length one, in which case every code of the family is
+LCD.
```

**Why — two independent defects in one sentence.**

1. The old text claimed "roughly `Δ/4` at `P = 1`". But `ν_1 = 0`, so at
   `P = 1` the mean is `¼·Σ_{L_O≥2} w_O L_O`, which is `0` whenever every orbit
   has length one. Verified on three families where all orbits have length 1:
   `F_3, n_0=4`, `F_4, n_0=3`, `F_9, n_0=4` — in each, max hull dimension over
   all assignments is `0`, and the LCD count equals the total count. So `Δ/4`
   is not merely "apart from a correction"; it is wrong, not even asymptotically
   in `n` (that family has `Δ = n` fixed and mean 0).
2. "grows linearly with `n`" silently varies `P` while `Δ = Σ m_s n`. The
   replacement states the dependence explicitly and gives a two-sided bound
   proved from Theorem VIII.2, valid for every `P ≥ 2`.

**Proof of the bound** (elementary, and checked numerically for all `P` in
`[2,400)`): for `P = 2m`, `ν_P = m²/(2m+1) ≥ m/2 ≥ P/4 ≥ P/6`; for `P = 2m+1`,
`ν_P = m(m+1)/(2m+2) = m/2 ≥ P/6` as soon as `3m ≥ 2m+1`, i.e. `m ≥ 1`. For the
upper bound, `μ_P = P(2P+1)/(6(P+1)) ≤ P/3` because `2P+1 ≤ 2(P+1)`. Multiplying
by `w_O L_O` and summing gives `Δ/6 ≤ E ≤ Δ/3`.

| family | `P` | exact mean (F_q) | `Δ/6` | `Δ/3` | inside |
|---|---|---|---|---|---|
| F_3, n_0=2 | 3 | 1 | 1 | 2 | yes |
| F_3, n_0=4 | 3 | 2 | 2 | 4 | yes |
| F_5, n_0=2 | 5 | 55/18 | 5/3 | 10/3 | yes |
| F_5, n_0=4 | 5 | 55/9 | 10/3 | 20/3 | yes |
| F_4, k=1, n_0=3 | 2 | 1 | 1 | 2 | yes |
| F_4, k=0, n_0=3 | 2 | 13/9 | 1 | 2 | yes |
| F_4, k=1, n_0=3 | 4 | 12/5 | 2 | 4 | yes |
| F_9, k=1, n_0=2 | 3 | 1 | 1 | 2 | yes |

## Hunk 3 — lines 927–929: unverifiable absence claim about DP2025

```diff
@@ -924,9 +930,10 @@
-display above. No variance or covariance formula is given there; the
-second-order results below (Theorem~\ref{thm:C6} and
-Corollary~\ref{cor:secondorder}) have no counterpart in~\cite{DP2025}.
+display above. That work treats average hull dimensions, that is, the first
+moment; the second-order results below (Theorem~\ref{thm:C6} and
+Corollary~\ref{cor:secondorder}) are established here independently of
+\cite{DP2025}.
```

**Why.** DP2025's full text is behind a paywall and could not be read in either
round of this audit; asserting that a specific formula is absent from a paper
one has not read is not a defensible claim. The abstract does state that the
paper gives average (first-moment) formulas, which is what the replacement now
relies on. Nothing is lost scientifically: the theorem and corollary are proved
in this manuscript regardless.

## Unchanged in this round

Every theorem, lemma, proposition, corollary, proof, example, table entry,
numerical value, citation and section heading. The three edits are confined to
two paragraphs of prose and one remark. `DEPENDENCY_AUDIT.md` is new evidence,
not a change to the paper.
