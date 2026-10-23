# VALIDATION_REPORT.md

## 1. Environment and its consequences

No TeX engine exists in this sandbox (`pdflatex`, `latexmk`, `bibtex`,
`tectonic` all absent; `apt` has no reachable index; GitHub release assets and
tectonic's bundle relay are unreachable). Therefore:

* **no PDF was produced**, and
* **no page-level or box-level verification was possible**.

Everything else below was executed. The verifier is dependency-free Python 3
(stdlib only) so it reproduces anywhere.

## 2. Independent implementation (not the package's code)

`work/independent/verify_independent.py` was written from the definitions in
the manuscript, not from its formulas and not from any `code/validate_*.py`:

* `K = F_{p^d}` as `F_p[t]/(m)` with explicit irreducible `m`; field axioms
  (distributivity, associativity, linearity of Frobenius) self-tested;
* `sigma(x) = x^{p^k}`, `rho = sigma^{-1} = x^{p^{d-k}}`, `rho o sigma = id`
  asserted elementwise;
* `D(C)` computed by **solving the linear system** `sum_j c_j sigma(y_j) = 0`
  over `F_p` (d scalar equations per code basis vector), i.e. from the pairing
  definition;
* `Hull(C) = C ∩ D(C)` by span-intersection linear algebra — no formula used;
* `f#` implemented literally as `rho(c_0)^{-1} sum_i rho(c_i) x^{r-i}`;
* the paper's statements are then *compared against* this ground truth.

Non-degeneracy check `dim C + dim D = n*d` was asserted for every assignment in
every family: it never failed.

## 3. Coverage

10 families, exhaustive over all labeled assignments (no sampling, no seed):

| family | n | factors (deg) | orbits | assignments |
|---|---|---|---|---|
| F_3, P=1, n0=4 | 4 | 1,1,2 | 1,1,1 | 8 |
| F_3, P=3, n0=2 | 6 | 1,1 | 1,1 | 16 |
| F_3, P=3, n0=4 | 12 | 1,1,2 | 1,1,1 | 64 |
| F_5, P=5, n0=2, λ=−1 | 10 | 1,1 | 2 | 36 |
| F_5, P=5, n0=4, λ=−1 | 20 | 2,2 | 2 | 36 |
| F_4, k=1, P=2, n0=3 | 6 | 1,1,1 | 1,1,1 | 27 |
| F_4, k=0, P=2, n0=3 | 6 | 1,1,1 | 2,1 | 27 |
| F_4, k=1, P=4, n0=3 | 12 | 1,1,1 | 1,1,1 | 125 |
| F_9, k=1, P=3, n0=2 | 6 | 1,1 | 1,1 | 16 |
| F_9, k=1, P=1, n0=4 | 4 | 1,1,1,1 | 1,1,1,1 | 16 |

Note `P` is always a power of `p` (required: `(x^{n0}-mu)^P = x^n - lambda`
fails otherwise in odd characteristic) and `m_s` is the field degree over `F_q`.

## 4. Results

```
cases=10 non-ok=0 failed_checks=0
RESULT: PASS
```

Checks that passed in **every** family:

* `dim C` from T1 vs the actual `F_p`-rank of `⟨g_a⟩`;
* `dim Hull` from T4 vs the actual `dim(C ∩ D(C))`;
* hull generator `lcm(g_a, h_a^#)` vs the actual intersection subspace;
* `⟨h_a^#⟩` vs `D(C)` (Prop. transport / T3);
* T6 joint enumerator (product of transfer-matrix traces) vs brute-force
  joint distribution — exact multiset equality;
* C1 total count `(P+1)^{#factors}`;
* C3 LCD count `2^{#orbits}`;
* C4 self-orthogonal vs dual-containing counts equal, and the edge predicates
  `a_{i-1}+a_i >= P` / `<= P`;
* C5 mean of hull dimension and mean of code dimension;
* C6 variance (all three regimes `L=1`, `L=2`, `L>=3` exercised);
* `Var(dim C) = P(P+2)/12 · sum w_f^2`;
* `Cov(dim C, dim Hull) = 0`.

Earlier failures during development were traced to **bugs in my own harness**
(a K-valued equation collapsed into one `F_p` row; a code basis missing the
`K`-scalar multiples), not to the manuscript. They are recorded here because
the correction direction matters: the paper's dual-generator claim survived
once the harness was fixed.

## 5. `tau_s` is not an involution (defect confirmation)

`F_8 = F_2[t]/(t^3+t+1)`, `k=0`, `n0=7`: the seven linear factors of `x^7-1`
form `tau`-orbits of lengths **6 and 1**, and `tau^3 != id`. This is the
evidence behind the five wording repairs in `CHANGELOG_MINIMAL.md`.

## 6. Example 9.3 reproduced exactly

F_4, k=1, λ=1, P=2, n0=5, n=10, m_s=2). My brute-force `F_2`-dimensions,
divided by `m_s`, reproduce the manuscript's 15-cell distribution
cell for cell:

```
(0,0):1 (1,1):1 (2,0):1 (2,2):2 (3,3):2 (4,2):2 (4,4):3 (5,5):3
(6,2):2 (6,4):3 (7,3):2 (8,0):1 (8,2):2 (9,1):1 (10,0):1
```

mean = 23/9, variance = 194/81, LCD = 4, SO = DC = 12 — all as stated.
Examples 9.1 and 9.2 were recomputed by hand (`Var(S_2)=44/81`, `V_3(1)=3/16`,
`E=3/4`). Examples 9.4–9.6 were **not** reproduced (see `REMAINING_RISKS.md`).

## 7. Static LaTeX validation (substitute for a compile)

Run on `FINAL_IEEE_TIT_SUBMISSION.tex` with comments stripped:

| check | result |
|---|---|
| `\begin`/`\end` balance | balanced, nothing left open |
| brace balance | 0 |
| `\label` count / duplicates | 38 / none |
| `\ref`/`\eqref` targets | all defined |
| `\cite` keys vs `\bibitem` | 23 cited, 23 defined, exact match, no uncited entries |
| inline `$` parity | even |

This is **not** a compile. Undefined control sequences, font and package
availability, overfull boxes and final page count remain unverified.

## 8. Copy-paste build

```
latexmk -pdf -interaction=nonstopmode -halt-on-error FINAL_IEEE_TIT_SUBMISSION.tex
```

(two `pdflatex` passes, then `bibtex`, then two more, if thebibliography is
replaced by BibTeX; as shipped the bibliography is inline, so two passes
suffice).
