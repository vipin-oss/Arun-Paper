# CHANGELOG_MINIMAL.md — every edit, with location and reason

Base: `ORIGINAL_SNAPSHOT/manuscript/P1_41_MANUSCRIPT_IEEE_SINGLE_COLUMN.tex`
(1474 lines). Output: `FINAL_IEEE_TIT_SUBMISSION.tex` (1475 lines).
Diff size: 6 hunks, 8 changed lines. No equation, theorem number, symbol,
section, result, citation, or author detail was touched.

| # | Location (base line) | Before | After | Class | Reason |
|---|---|---|---|---|---|
| 1 | 53–54, abstract | "governed by the reciprocal **involution** on those factors" | "governed by the reciprocal **map** on those factors" | P0 (factual terminology) | `tau_s` is a permutation, not an involution: F_8, k=0, n0=7 has a `tau`-orbit of length 6 (verified). Definition 3.2 already says "is a permutation" |
| 2 | 147, intro | "orbit of the reciprocal **involution** on these factors" | "orbit of the reciprocal **map** on these factors" | P0 | same |
| 3 | 158, intro | "orbits of the reciprocal **involution**" | "orbits of the reciprocal **map**" | P0 | same |
| 4 | 278, Definition heading | `[compatibility and the **involution** \(\tau_s\)]` | `[compatibility and the **reciprocal map** \(\tau_s\)]` | P0 | same; heading contradicted the body of the same definition |
| 5 | 1315, conclusion | "orbits of the reciprocal **involution**" | "orbits of the reciprocal **map**" | P0 | same |
| 6 | 849–852, moments | "…so **the typical code** of the family has a hull growing linearly with n, in contrast to random linear codes…" | "…so **the mean hull dimension** grows linearly with n, whereas the hull dimension of a random linear code stays bounded in probability [Sendrier]" | P0 (claim strength) | a mean statement does not license a typical-code statement without a concentration argument; the comparison is now mean-versus-typical, which is exactly what is proved |

## Deliberately not changed

* **`D(C) = rho(C^perp)` and the `sigma`/`rho` slot order** — the text is already
  correct (lines 235–237 define `rho = sigma^{-1} = x^{p^{d_s-k}}`; line 425 uses
  `D(C) = rho(C^perp)`). The earlier audit's "sigma^{e-k}" hypothesis does not
  hold against this file. No edit.
* **"involution" at lines 629, 636, 780** — these refer to
  `alpha -> P - alpha`, which is a genuine involution. Replacing the word there
  would introduce an error. Kept.
* **`P = 1` statements** — the claim that every hull vanishes at `P = 1` is
  correct and was verified; nothing to repair.
* **Examples, tables, numbers** — untouched; Example 9.3 reproduces exactly.
* **Novelty wording** — already conservative and well attributed. No edit.
* **P2 typography (overfull lines ~22.8pt/26.6pt/49.7pt)** — not implementable
  blind: without a TeX engine the boxes cannot be located or the repair
  verified. Deferred rather than guessed, per the no-unverified-change rule.
* **README page/reference counts** — the README's claims about the shipped PDFs
  are unverifiable here and are irrelevant to the manuscript itself; left as is
  and flagged in `VALIDATION_REPORT.md` §7.

## Diff reproduction

```
diff -u ORIGINAL_SNAPSHOT/manuscript/P1_41_MANUSCRIPT_IEEE_SINGLE_COLUMN.tex \
        FINAL_IEEE_TIT_SUBMISSION.tex
```
