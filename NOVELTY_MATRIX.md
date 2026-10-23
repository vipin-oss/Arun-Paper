# NOVELTY_MATRIX.md — literature and novelty forensics

Access level is stated for every row. **No paywalled full text was read.**
"Metadata-only" means title/venue/DOI/abstract as returned by a public index on
2026-10-23; "full text" was never available from this sandbox.

## Closest prior work

| Key | Work | Verified how | What it already does |
|---|---|---|---|
| DPI2023 | Debnath, Prakash, Islam, *Galois hulls of constacyclic codes over finite fields*, Cryptogr. Commun. 15 (2023) 111–127, doi:10.1007/s12095-022-00591-6 | metadata + abstract (Springer landing page) | per-code Galois hull dimension over a finite field, including repeated-root lengths; counts codes by hull dimension **alone** under restrictions on q |
| DPI2023corr | Correction, ibid. 15 (2023) 129–130, doi:10.1007/s12095-022-00602-6 | metadata (Springer) | textual corrections only |
| DP2025 | Debnath, Prakash, *Average dimensions of Galois hulls of constacyclic codes*, Adv. Math. Commun. 19(6) (2025) 1569–1604, doi:10.3934/amc.2025010 | metadata + abstract (AIMS) | formula for **average** Galois hull dimension over finite fields, plus the ring R_{m,q}; no second-order statistics in the abstract |
| DIYP2026 | Debnath, Islam, Yadav, Prakash, *Study of small Galois hull dimensions of constacyclic codes*, Adv. Math. Commun. 22 (2026) 1–18, doi:10.3934/amc.2025054 | metadata + abstract (AIMS) | existence/characterization of constacyclic codes with Galois hull dimension 1 and 2 |
| DIMP2026 | Debnath, Islam, Martínez-Moro, Prakash, *Galois hulls of constacyclic codes over affine algebra rings*, Discrete Math. 349(2) (2026) 114750, doi:10.1016/j.disc.2025.114750 | metadata (ScienceDirect landing, arXiv:2412.08512) | hull generator and dimension componentwise over a decomposed alphabet |
| ES2026 | Taki Eldin, Solé, *Generator polynomial matrices of the Galois hulls of multi-twisted codes*, FFA 109 (2026) 102712 | metadata | generator-matrix machinery for Galois hulls of multi-twisted codes |
| Sendrier1997 | *On the dimension of the hull*, SIAM J. Discrete Math. 10(2) (1997) 282–293 | metadata | random linear codes have bounded hull dimension in probability |

## Claim-by-claim novelty assessment

| Claim in the manuscript | Status | Basis |
|---|---|---|
| per-code Galois hull formula, single field | **NOT new** — attributed to DPI2023 by the paper itself | metadata supports attribution; the manuscript states it explicitly in the intro and in Remark 4.5 |
| average hull dimension, single field | **NOT new** — attributed to DP2025 | DP2025 abstract states exactly this; the manuscript's Remark 7.4 claims numerical agreement with DP2025 Thm 3.3, which is **full-text unverified** here |
| componentwise hull over a product of fields | **partially anticipated** by DIMP2026 (affine algebra rings); the manuscript positions itself as complementing it | metadata only |
| **joint** (code dim, hull dim) enumerator via transfer matrices, unrestricted orbit length | **appears new** in this specific form | no located prior work states a bivariate joint enumerator; absence of a found statement is not a proof of novelty |
| LCD count `2^{#orbits}` independent of P | **appears new** as a corollary of the joint enumerator | no located prior statement |
| exact mean **and variance** of hull dimension over the repeated-root family | **variance appears new**; mean not new | DP2025 abstract mentions averages only |
| uncorrelatedness of the two dimensions (`Cov = 0`) | **appears new** | no located prior statement |

## Residual novelty risk

Moderate, and correctly managed. The manuscript never claims priority, never
uses "first", and attributes every neighbouring result it relies on. The one
comparison that could not be checked here is the numerical agreement with
[DP2025, Thm 3.3] in Remark 7.4 and the orbit-length restriction attributed to
[DPI2023, Thm 4] in Remark 4.5 — both are full-text claims. A referee with
access should confirm those two sentences; if either is off, it is a one-line
wording repair, not a structural problem.

Searches performed were limited to these titles/DOIs; a systematic
citation-graph sweep of the hull-distribution literature (Li–Shi, Li–Shi–Ling,
Bouyuklieva et al., all cited) was **not** performed and is listed as a residual
risk.
