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
