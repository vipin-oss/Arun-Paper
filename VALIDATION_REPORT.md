# VALIDATION_REPORT.md (round 2 — post-build)

Status: **all computational gates PASS**. PDF built by CI from this exact
source, inspected page by page.

## 1. Environment (round 1 limitation, now resolved)

Round 1 had no TeX engine and no PDF. That is fixed: compilation now runs on
GitHub Actions in the official `texlive/texlive` container, and the built PDF is
committed back to the branch (`build/`, plus `FINAL_IEEE_TIT_SUBMISSION.pdf` at
the root). See `BUILD_REPORT.md`.

## 2. Three independent verification layers

| layer | script | scope | result |
|---|---|---|---|
| definition-level finite-field | `work/independent/verify_independent.py` | 10 families, **every** assignment, dual computed from the pairing definition and hull as a subspace intersection | 0 failed checks |
| symbolic (all P) | `work/independent/verify_symbolic.py` | 15 closed forms as polynomial identities in P (parity-split) | 0 failures |
| examples | `work/independent/verify_examples.py` | Examples 9.4, 9.5, 9.6 | all reproduced |

None of the three calls the package's `code/validate_*.py`, and none uses the
paper's formulas to compute ground truth — they are the *prediction*, not the
oracle.

### 2.1 Symbolic layer (new in round 2)

The finite-field layer can only test individual `P`. Because the closed forms
are parity-dependent for `P` even/odd, each was proved as a symbolic identity
with `sympy`, splitting `P = 2m` / `P = 2m+1`:

`E[min(U,V)]`, `E[min(U,V)^2]`, `F(c)`, `Var(X)`, `nu_P` (both parities),
`V_1(P)` (both parities), `E[X_i X_{i+1}]`, `kappa_P`, `E[X_0 X_1]`,
`Cov(X_0,X_1)`, `V_2(P)`, `Var(X)+2kappa_P`, `V_L(P)`, `Var(P-A_f)`,
`gamma_P`. **15/15 PASS** — these hold for every `P`, not just tested ones.

### 2.2 Examples 9.4–9.6 (new in round 2)

| example | what was checked | result |
|---|---|---|
| 9.4 (F_8, k=1, P=2, n0=7, 2187 assignments) | all **44 cells** of the printed joint distribution; mean 11/3; variance 10/9; LCD 4; SO = DC = 258 | **exact match** |
| 9.4 orientation claim | for all 2187 assignments, exponents of `h#` by trial division: predecessor `P - alpha_{i-1}` matches **2187/2187**; successor `P - alpha_{i+1}` matches **27/2187** | **exact match to the paper's stated 27** |
| 9.5 (F_2 x F_4, 729 assignments) | orbit data `(1,1),(2,3)` and `(1,2),(2,6)`; convolution assembly; mean 11; variance 230/9; LCD 16 | **exact match** |
| 9.6 (F_9, lambda = iota, P=3, n0=4, 16 assignments) | all 7 cells; mean 7/2; variance 15/4; LCD 2; SO = DC = 10 | **exact match** |

The 9.4 orientation check is the strongest single result in this report: it
confirms a specific, falsifiable integer claim (27) that would be wrong under
the opposite convention. It is reproducible (`SEED = 20261023` for the
definition-level sample; the orientation check is exhaustive, not sampled).

## 3. What finite verification does and does not establish

Passing finite tests is **not** a proof of the universal theorems. The
distinction this audit maintains:

* Theorems T1–T6 and the corollaries are established by **inspection of the
  written proofs** (see `AUDIT_REVIEWER.md`), which are complete arguments, not
  appeals to computation.
* The computations confirm that the proofs are not mis-stated — that the
  formulas as printed agree with the objects they describe — and they would
  have caught a wrong constant, a wrong index, or a wrong orientation.
* The symbolic layer upgrades the moment formulas from "true for the tested
  `P`" to "true as polynomial identities in `P`".
* Nothing in the paper's logic depends on the computations; §9 says so
  explicitly ("the proofs of Sections III–VIII are independent of them"), and
  that sentence is now literally true.

## 4. Build and visual inspection (round 2)

```
latexmk exit 0 | overfull 0 | underfull 1 (cosmetic) | errors 0 | pages 17
```

Rendered every one of the 17 pages at 100–110 dpi and read them. Checked:
title/abstract/index-term block, section continuity I–XI, equation layout,
symbol rendering (`sigma`, `rho`, `tau`, `alpha`, `min`, `dim`, `Hull`),
display-math alignment, the two large enumeration tables, page breaks, and all
23 references. No clipped math, no overlapping text, no orphaned headings.

A mechanical margin audit (any text block outside a 40 pt safe area on any
page) returned zero hits.

**One real defect was found this way and fixed**: my own `\allowbreak` repair
rendered two paths as `code/code/validate_...`. The compiler reported success.

## 5. `tau_s` is not an involution (unchanged conclusion)

`F_8`, `k=0`, `n0=7`: the seven linear factors of `x^7-1` form `tau`-orbits of
lengths 6 and 1, and `tau^3 != id`. This is the evidence behind the five
wording repairs in `CHANGELOG_MINIMAL.md`.

## 6. Residual computational gaps

* Example 9.4's definition-level cross-check used a fixed-seed sample of 64
  assignments (the aggregate numbers are exhaustive). A full 2187-assignment
  linear-algebra sweep was not run — it would take roughly 20 minutes, above
  the per-task cap.
* Examples 9.1–9.3: 9.3 reproduced cell-for-cell in round 1; 9.1 and 9.2 by hand.
* The package's own claimed totals (2769 field-level assignments, 52 (P,L)
  pairs) remain **unverified** and are not relied on here.
