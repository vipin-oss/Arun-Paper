# Repo Review: do "Paper 1" aur "Paper 2" ka comparison

**Reviewed:** `Galios-Hull-Paper-Complete-Package-6ad0e87.zip` (P1) aur `Paper2_Simple_Article (2).zip` (P2)
**Date:** 25 Oct 2026 · Branch: `arena/772e0cc9-arun-paper`

---

## 1. Short answer (TL;DR)

1. **Dono overlap karte hain — core result ek hi hai.** Same family (repeated-root constacyclic codes over square-free affine algebra / finite product of fields), same `k`-Galois dual + hull exponent formula, same **transfer-matrix joint enumerator**, same LCD count `2^#orbits`, same symmetry, same mean/variance.
2. **Best paper = Paper 2.** Ye P1 ka superset hai: 27 pages vs 16, 34 proofs vs 23, 3 figures + 2 tables vs 0, incompatible twists, trapezoid support theorem, self-dual counts, complexity/algorithm, bade examples (F32, n=62, 3^31 codes).
3. **Yaani 2 different papers nahi ban sakte** (as-is). Same theorem ko do journals me bhejna = duplicate/self-plagiarism + "salami slicing" ka clear risk. **Ek hi paper submit karo = P2**, aur P1 ka sirf wo hissa merge karo jo P2 me nahi hai (Section 6 list).
4. Agar **do paper** chahiye, to split "same result ko tod kar" nahi, balki **naya direction** lena padega (Section 7 me 5 concrete ideas).
5. Text-level overlap bahut kam hai (8-word shingles sirf ~0.1–0.2% match) — matlab P2 ko **rewrite** kiya gaya hai. Plagiarism scanner pakdega nahi, **par mathematically result same hai** — reviewer/editor baad me pakad sakta hai, aur us waqt retraction-level issue ban sakta hai. Isliye text overlap kam hona "safe" nahi hai.

---

## 2. Dono packages me kya hai

| | **P1 — Galios-Hull-Paper-Complete-Package** | **P2 — Paper2_Simple_Article** |
|---|---|---|
| Title | *The joint code–hull distribution of repeated-root constacyclic codes over finite products of finite fields via transfer matrices* | *Joint Code-Dimension and k-Galois-Hull Enumerators for Repeated-Root Constacyclic Codes over Square-Free Affine Algebras* |
| Version date | 23 Oct 2026 (P1-42…P1-54 records) | 24 Oct 2026 ← **naya** |
| Authors | 1 (Arun Kumar Yadav + ORCID) | 4 (Yadav, Gupta, Soni, Pruthi) |
| Pages | 16 (reading copy) + 17 (IEEEtran single-column) | 27 |
| Class / format | `article` + `IEEEtran` review version | `article` (Elsevier-style; CRediT, funding, competing interest, data availability, AI declaration) |
| Theorem-like envs / proofs | 23 proofs, 0 figures, **0 tables** | **34 proofs, 3 figures, 2 tables** |
| Examples | 6 chhote examples (hand + Gram-matrix rank checks) | 5 families: F4, F8 (n=14), F4×F16 mixed, char 3 & 5, F32 (n=62, 3^31 codes) |
| References | 23 (inline `thebibliography`) | 37 in bib, 18 cited |
| Code / validation | **8 validator scripts + saved outputs + 16 supporting records + SHA-256 manifest** (self-audit trail) | Only `.tex` + `.pdf` + 3 figure PDFs + bib. `code/test_rr_enumerator.py`, `code/verify_rr.py`, `tables/verification_log.txt` **missing** |
| Extra | MD companion, proof/audit records (P1-04…P1-45), Gate G1 notes | figures, verification-coverage table, worked joint-distribution tables |

---

## 3. Result-by-result overlap (yahi asli sawaal hai)

| Mathematical content | P1 | P2 | Status |
|---|---|---|---|
| Square-free component decomposition + parametrization of codes | Thm 3.1 | `prop:decomposition`, `lem:factorisation`, `prop:global-selection` | **Same** |
| Frobenius-twisted reciprocal involution on kernel factors | Thm 3.2 | `lem:reciprocal`, `lem:root-action` | **Same** |
| `k`-Galois dual: generator + exponent formula `βᵢ = P − α_{i−1}` | Lem 4.1, Props 4.2, Thm 4.3 | `thm:dual-generator`, `prop:dual-translation`, `prop:dual-exponents` | **Same** |
| Hull generator `lcm(g, h#)` + min-edge dimension formula | Lem 5.1, Thm 5.2 | `lem:hull-generator`, `prop:min-edge` | **Same** |
| Local transfer trace `tr((T_w)^L)` | Thm 6.1 | `lem:trace` | **Same** (P↔M notation) |
| **Main joint enumerator `∏ tr(T^{a_O}_w)`** | **Thm 6.3** | **`thm:main`** | **Same theorem** (P2 adds dimension-only factor for incompatible components) |
| Complement–reversal symmetry `N(K,H)=N(Δ−K,H)` | Cor 6.4 | `cor:symmetry` (+ `lem:telescoping`) | **Same** |
| Simple-root `P=1` binary-matrix specialization | Prop 6.5 (explicit 2×2) | sirf implicitly | P1 zyada explicit |
| Total count `(M+1)^{N_F}` | Cor 7.1 | `E(1,1)` check | Same |
| Code-dimension marginal | Cor 7.2 | `cor:marginals` | Same |
| **LCD count `2^{#orbits}`** | Cor 7.3 (+ conditional refinement) | `prop:lcd-count` | **Same** |
| SO / DC counts + restricted enumerators | Cor 7.4–7.5 | `prop:dimension-criteria`, `prop:extremal-counts` | Same core |
| Exact mean, variance, Var(dim C), Cov = 0 | Thm 8.2, 8.4, Cor 8.5 | `lem:edge-moments`, `prop:moments` | **Same** |
| Conditional law of hull given dimension | partial | `prop:conditional` | P2 zyada clear |
| **Attainable pairs = exact trapezoid (support theorem)** | ✗ | **`thm:support`** + `cor:hull-values`, `cor:global-support` | **P2 new** ⭐ |
| **Incompatible twists included (`S^comp`/`S^inc` split)** | sirf compatible (remark) | **`prop:compatibility`, `prop:incompatible`** | **P2 new** ⭐ |
| **Self-dual codes via midpoint `M/2` (char 2)** | ✗ | **`cor:self-dual`** | **P2 new** ⭐ |
| **Polynomial-time DP + complexity bound** | ✗ | **`prop:complexity`** | **P2 new** ⭐ |
| Short-orbit / threshold phenomena (`a_O=1,2`) | ✗ | `prop:short-orbits`, `prop:threshold` | **P2 new** ⭐ |
| Long prose intro (6 connected paragraphs, careful literature positioning) | ✔ (behtar) | 4-paragraph intro | P1 behtar |
| Audit trail + runnable validators + proof records | ✔ | ✗ | **P1 behtar** |
| Figures / tables / large worked data | ✗ | ✔ | P2 behtar |

**Conclusion:** P2 = P1 + 6 naye results + better presentation. Same-paper relationship hai, "do alag papers" nahi.

---

## 4. Kaunsa best hai — aur kyu

### Paper 2 jeetta hai (yehi submit karo)

- **Coverage:** main theorem hi nahi, uske aage ka poora package — support (trapezoid), extremes (LCD/SO/DC/self-dual), moments, conditional laws, algorithm + complexity. P2 ek "complete" paper hai; P1 "first draft + proofs" lagta hai.
- **Mathematical strength:** 34 proofs (P1: 23). Naye results actually non-trivial hain — especially `thm:support` (dimension-only bound `η ≤ min{κ, Δ−κ}` **sufficient nahi** hai; exact trapezoid milta hai) aur incompatible-component handling (`U`-only factor `Σ_{r=0}^{M} U^{w r}`).
- **Evidence:** exact joint distribution F8/n=14 aur F32/n=62 (3^31 codes) ke figures + exhaustive verification table (char 2, 3, 5) — ye reviewer ko "believable" banata hai. P1 me koi figure/table nahi.
- **Journal-readiness:** 4 authors ke saath, CRediT, funding, competing-interest, data-availability, AI-use declaration — ye Elsevier/LAA/Finite Fields Appl type submission ka standard hai. P1 single-author + IEEEtran hai.
- **Fresher literature:** 37 refs vs 23, correction `debnathCorrection2023` bhi bib me hai.

### Paper 1 kahan behtar hai (isse merge karo, alag paper nahi)

- Intro aur **literature positioning** ka prose zyada soch-samajh kar likha hai (DPI2023 / DP2025 / DIMP2026 / ES2026 ke saath theorem-level comparison).
- **`Prop 6.5` (`P=1` ka explicit 2×2 matrix)** — P2 me ye explicit nahi.
- **Reproducibility package:** 8 validator scripts + saved outputs + independent audit records + SHA-256 manifest. P2 ka "Data availability" statement isi tarah ka code maangta hai, par zip me code hai hi nahi.
- **Conditions/hypotheses par careful remarks** (e.g. "Theorem 6.1 ek polynomial identity hai, `P` power of p hona field construction ke liye zaroori hai").

---

## 5. "Same paper banenge ya 2 different?" — seedha jawab

- **As-is submit karna = duplicate publication.** Same main theorem, same counting corollaries, same moment formulas. Ek hi result ko do journals me bhejna COPE guidelines ke against hai; agar baad me pakda gaya to retraction + authors ki credibility ka nuksaan.
- **Text overlap kam hai** (0.1–0.2% 8-gram) — iska matlab sirf ye hai ki P2 ko paraphrase kiya gaya, **mathematical overlap kam nahi hua**. Journals similarity-check me pakad nahi payenge, lekin referees (same community: Debnath, Prakash, Martínez-Moro etc. hi is topic par kaam kar rahe hain) 100% pakad lenge.
- **Do alag papers tabhi banenge jab content alag ho**, wording alag ho — ye nahi.

**Recommendation: P2 ko single paper banao, P1 ko uska superseded draft maano** (repo me `archive/paper1_v0/` me rakh do reference ke liye). Ek paper with 27–30 pages, jo 2 papers se zyada strong hai.

---

## 6. Agar ek paper (P2) finalize karna hai — merge checklist

P1 se P2 me ye cheezein le aao:

1. **`Prop 6.5` (`P=1` explicit binary transfer matrix)** — 4 lines ka corollary, achha "sanity check" hai.
2. **Intro ke 6 paragraphs** (ya unka literature-comparison hissa) — P2 ka intro chhota hai; P1 ka version reviewer-friendly hai. **Par novelty claim ek hi hona chahiye** (neeche point 5).
3. **Hypotheses remarks** ("polynomial identity vs field construction") — P2 ke `thm:main` ke baad.
4. **Validation code + verification log** package me daalo: P1 ke `code/validate_*.py` + P2 ke `test_rr_enumerator.py`, `verify_rr.py`, `tables/verification_log.txt`, `tools/build_simple_article.py`. Abhi P2 ki zip me ye nahi hain, jabki Section "Independent verification" aur "Data availability" inhi ko cite karte hain — **ye submission-blocker hai**.
5. **Novelty claim consistency:** P1 ke records kehte hain "no novelty claim is made anywhere" + Gate G1 "PARTIALLY RESOLVED"; P2 ka intro concrete novelty claim karta hai (joint distribution vs DPI2023/DP2025/DIMP2026/ES2026). Ek hi line le lo — aur `DPI2023` cite karte waqt **`debnathCorrection2023` bhi cite karo** (abhi bib me hai par text me cite nahi hua).
6. **Abstract wording fix:** P2 abstract kehta hai "exact enumerator of all 3^31 repeated-root codes of length 62 over F32", lekin Table 2 me us row ka mode "seeded sample, 12 words" hai. Sahi wording: *"the exact enumerator of the full family of 3^31 codes (obtained by the transfer-matrix DP), with direct linear-algebra verification on sampled codes"* — warna referee isse overclaim samjhega.
7. Cleanup: figure filenames `fig5_*`, `fig6_*` (numbering leftover) → `fig2_*`, `fig3_*`; 19 uncited bib entries hatao ya cite karo; pacakge/title ka typo "**Galios**" → "Galois".

---

## 7. Agar aap **do** papers chahte hi hain (legitimate tarika)

Same result ko todna galat hai. Do genuine options:

**Option A — Split by "theory" vs "computation" (medium risk, kam fayda)**
- Paper A: joint enumerator + support trapezoid + moments + extremal counts (pure theory).
- Paper B: exact algorithm + complexity + large-scale computations/verification + data.
- Problem: Paper B ka core tool Paper A hi hai; bina naye theorem ke ye "technical note" lagega. Sirf tab theek hai jab Paper B me naye results ho (asymptotics, average-case complexity, ya table-driven conjectures **proved** ho jayein).

**Option B — Doosra paper ek naye direction par (recommended, agar 2 papers chahiye)** — P2 khud "open directions" me kuch isi taraf ishara karta hai:
1. **Multivariate / multiple Galois indices:** ek hi family par `(dim C, η_{k1}, …, η_{kr})` ka joint enumerator (states explode — naya transfer-state design chahiye). Ye ek strong, genuinely naya paper hai.
2. **Unlabeled count:** labeled exponent assignments ki jagah **monomial-equivalence classes** ke hisaab se distribution (Burnside + automorphism group of the affine algebra). Bahut valuable, aur labeled vs unlabeled ka gap abhi khula hai.
3. **Chain rings / Z_{p^m}:** repeated-root constacyclic codes over `Z_{p^m}` ya Galois rings me Galois hull distribution (Grey map / torsion ke saath `min`-edge law badal jayega).
4. **Generalized Hamming weights ya relative/semi-δ hulls** ka same enumeration framework.
5. **Hull distribution → quantum/EAQECC performance:** P1 me EAQECC material author ke kehne par hata diya gaya tha; usko ek applied paper (hull distribution se EAQECC parameters ka expected value) bana sakte hain.

Har case me: pehla paper pehle **submit/accept** ho, doosre me pehle ko cite karo, aur text/result overlap 0 rakho.

---

## 8. Final verdict

| Sawaal | Jawab |
|---|---|
| Overlap? | **Haan — core mathematics same hai** (main theorem, LCD count, symmetry, moments). Text sirf paraphrase hua hai. |
| Best paper? | **Paper 2** — superset, 6 naye results, 34 proofs, figures/tables, journal-ready format. |
| Same paper banega? | **Haan, in effect wahi ek paper hai.** P2 = P1 + extensions + rewrite. |
| 2 different papers? | **As-is nahi.** Do paper chahiye to naya direction (Section 7 Option B) pakdo; same result ko split karna salami-slicing hoga. |
| Next step | P2 finalize karo (Section 6 checklist) → ek journal (LAA / Finite Fields Appl / Adv. Math. Commun. / DCC) → phir doosra paper naye direction par. |

---

## 9. Update — merged single paper (25 Oct 2026)

A single merged manuscript now exists in **`paper/`**:

* `paper/main.tex` — Paper 2 as base, with Paper 1's `M=1` specialization
  (+ new Proposition and Example, both machine-checked), a hypotheses remark
  under the main theorem, a scope-and-limitations paragraph, and the
  `debnathCorrection2023` citation added. The unused threshold-layer
  proposition was removed for balance; abstract and verification section were
  corrected to match what is actually proved/run.
* `paper/code/` — `enumerator.py` (transfer-matrix enumerator, SO/DC/SD counts,
  moments), `checks.py` (Level 1 + Level 2 verification, all checks pass,
  output saved), `generate_tables.py` (regenerates the tables from scratch).
* `paper/tables/` — `summary_families.csv` and one `joint_<family>.csv` per
  family.

Independently reproduced: all 11 rows of Table 1, the joint table of
Example 7.1, `E[η|κ=7]=533/131`, `max_κ E[η|κ]=17.392`, and — from the
definitions — the orbit skeletons and full joint histograms of 7 small
families over `F_4`, `F_8`, `F_3`, `F_9` (Gram-matrix ranks vs the trace
product, 2604 words in total). See `paper/README.md`.
