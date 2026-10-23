# NOVELTY_MATRIX.md (round 2 — full-text where obtainable)

Access dates 2026-10-23. This round upgraded several rows from abstract-only to
**full text** and downgraded none.

## Access status, honestly stated

| work | access achieved this round | evidence |
|---|---|---|
| DIMP2026 (Debnath–Islam–Martínez-Moro–Prakash, Discrete Math. 349(2) 114750) | **FULL TEXT** — arXiv HTML of arXiv:2412.08512 (the same paper, "Submitted to Discrete Mathematics") | read §1–§2 and the structural abstract; confirms method |
| DP2025 (Debnath–Prakash, AMC 19(6) 1569–1604) | **abstract + introduction only** — the AIMS full-text link redirects to a login/paywall page | full text **NOT** read; no claim otherwise |
| DPI2023 (Debnath–Prakash–Islam, Cryptogr. Commun. 15 111–127) | abstract-only (Springer landing) | full text **NOT** read |
| DIYP2026 (AMC 22 1–18) | abstract-only (AIMS landing) | full text **NOT** read |
| DPI2023corr | metadata-only | — |
| Anderson et al. 2024 (IEEE TIT 70(5) 3190–3201) | **FULL TEXT** (author PDF) — bibliographic record verified independently | confirms the reference is real and correctly cited |
| Li–Shi–Ling 2025 (IEEE TIT 71(1) 273–286) | metadata verified via two independent citing sources | reference real; volume/pages/DOI match |

Two IEEE TIT references were independently confirmed after Crossref was found
unreachable from this sandbox; the DP2025 and DPI2023 DOIs were confirmed in
round 1 against the publisher landing pages.

## What DIMP2026 actually does (full-text finding)

DIMP2026 studies `k`-Galois hulls of `lambda`-constacyclic codes over the affine
algebra `A = F_q[X_1..X_l]/<t_1(X_1),...,t_l(X_l)>` with the `t_i` square-free.
It decomposes `A` into a direct sum of simple ideals, finds **generators** of
the code, its Galois dual and its Galois hull componentwise, derives a
**dimension formula** per code, gives an LCD condition, and applies the result
to EAQECCs. It also counts the *cardinality of the set of achievable hull
dimensions* `delta_k(n,q,lambda)`.

It does **not** present a bivariate joint enumerator of `(dim C, dim Hull)`, nor
mean/variance formulas, nor a transfer-matrix formulation. So the manuscript's
positioning — "complementing the F_q-component form in [DIMP2026]" — is
accurate, and the novelty claim survives full-text contact with its nearest
neighbour.

## Claim-by-claim

| Claim | Status | Basis |
|---|---|---|
| per-code Galois hull dimension, single field | **known** — DPI2023 | abstract; paper self-attributes |
| average hull dimension, single field | **known** — DP2025 | abstract explicitly states this; second-order statistics absent from the abstract |
| componentwise generator + dimension over a product/affine algebra | **known** — DIMP2026 | full text |
| achievable-hull-dimension count `delta_k` | **known** — DIMP2026 | full text |
| **joint** `(dim C, dim Hull)` enumerator by transfer matrices, any orbit length | **appears new** | no prior statement located in any of the above |
| LCD count `2^{#orbits}`, independent of `P` | **appears new** (as a corollary) | none of the above states it |
| exact mean of hull dimension over this family | **not new in substance** (DP2025 has an average formula); the orbit-decomposed form with the separate `nu_P` constant is a re-derivation, and the paper says so in Remark 7.4 |
| exact **variance** and covariance structure | **appears new** | DP2025 abstract mentions averages only; full text unread, so this is a "not located" finding |
| `Cov(dim C, dim Hull) = 0` | **appears new** | as above |

## Classification the manuscript should carry into review

* **Original**: the transfer-matrix joint enumerator, its corollaries on counts
  and symmetry, the variance/covariance results, the orientation analysis.
* **Direct corollaries of known results**: the per-code hull generator and
  dimension (DPI2023 / DIMP2026 specializations) — correctly presented as such.
* **Known**: the average hull dimension (DP2025).
* **Unverified novelty**: every "appears new" row above is
  *absence-of-evidence*, not proof. In particular DP2025's full text was not
  read; if it contains a variance formula, Remark 7.4's claim that the
  second-order results "have no counterpart in [DP2025]" would need a one-line
  correction. This is the single highest-value thing a referee with access can
  check, and it is flagged in `REMAINING_RISKS.md`.

The manuscript makes no priority claim and uses no "first", which is the right
posture given the above.
