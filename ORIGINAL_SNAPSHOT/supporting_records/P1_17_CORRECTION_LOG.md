# P1-17 — Correction Log: Audit Corrections Applied to the Manuscript

**Specification:** `P1_16_INDEPENDENT_AUDIT.md`, items GAP-16-01 … GAP-16-08.
**Files corrected:** `P1_15_MANUSCRIPT_DRAFT.tex`, `P1_15_MANUSCRIPT_DRAFT.md` (kept in sync; the LaTeX remains the version of record).
**Not touched:** `02_THEOREM_BLUEPRINT.md` (frozen; SHA-256 re-verified `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff` before and after editing), all proof packages (P1-04/05/06), `P1_15_OPTIONAL_COROLLARIES.md` (N1–N3 remain unadopted candidates, still not used in the manuscript), and every core theorem/corollary statement and proof idea. No novelty or priority wording was added anywhere.

---

## 1. Bibliographic verification performed this phase (primary records actually inspected, 21 Oct 2026)

| Entry | Primary record inspected | What it established |
|---|---|---|
| CDL2015 | Crossref record for DOI 10.1016/j.ffa.2014.11.006 (publisher-deposited) + ScienceDirect article page | Authors Bocong Chen Hai Q. Dinh Hongwei Liu; title *Repeated-root constacyclic codes of length 2ℓ^m p^n*; FFA 33 (2015), 137–159. |
| Sharma2015 | Springer article page for DOI 10.1007/s12095-014-0106-5 | Anuradha Sharma, *Repeated-root constacyclic codes of length ℓ^t p^s and their dual codes*, Cryptogr. Commun. 7 (2015), 229–255. |
| WZLL2023 | AIMS (publisher) article page for DOI 10.3934/amc.2021044 | Tingting Wu, Shixin Zhu, Li Liu, Lanqiang Li, *Repeated-root constacyclic codes of length 6ℓ^m p^n*, AMC 17(5) (2023), 1154–1180. |
| ZWLL2025 | ScienceDirect article page for DOI 10.1016/j.ffa.2024.102542 + Crossref record | Qi Zhang, Weiqiong Wang, Shuyu Luo, Yue Li, *Repeated-root constacyclic codes of length k^sℓ^m p^n over finite fields*, FFA 101 (2025), Art. 102542. |
| Talbi2021 | arXiv record 2102.06995 | Authors: Sarra Talbi, Aicha Batoul, Alexandre Fotue Tabue, Edgar Martínez-Moro; title as cited. |
| ES2026 (Eldin name) | ScienceDirect article page for DOI 10.1016/j.ffa.2025.102712 + arXiv record 2305.15237 (incl. submission history) | Publisher author form "Ramy Taki Eldin"; arXiv submitter string "Ramy Taki Eldin F." ⇒ full form **Ramy F. Taki Eldin**. The form "Ramy Abu Eldin" appearing in one internal audit table is unsupported by either primary record. The manuscript already used "R. F. Taki Eldin", so **no change was needed**; the conflict is hereby resolved in favour of the primary records. |
| FZ2017 (Galois inner product origin) | Springer article page for DOI 10.1007/s10623-016-0282-8; corroborated by multiple citing papers' abstracts | Yun Fan, Liang Zhang, *Galois self-dual constacyclic codes*, Designs, Codes and Cryptography 84 (2017), 473–492 — the 2017 paper that introduced the ℓ-Galois inner product `Σ xᵢ yᵢ^{p^ℓ}`, which is exactly the pairing of manuscript §2 with `σ = p^k`. |
| BDS2006 | Science journal page + arXiv record quant-ph/0610092 | Todd Brun, Igor Devetak, Min-Hsiu Hsieh, *Correcting quantum errors with entanglement*, Science 314(5798) (2006), 436–439, DOI 10.1126/science.1131563 (DOI added to the entry). |
| ZKZ2026 (extra, see E12) | MDPI article page for DOI 10.3390/e28040407 | Enbin Zhang, Bo Kong, Xiying Zheng (initials supplied). |

Nothing was filled in from memory: every field added above traces to a record in this table.

## 2. Edits applied (both manuscript versions unless stated)

- **E1 — Numbering (GAP-16-03; .tex only).** `\newtheorem{remark}[theorem]{Remark}` → `\newtheorem*{remark}{Remark}`: remarks are now unnumbered, so the simple-root recovery is **Proposition 6.4** in the LaTeX, matching the Markdown companion exactly (which already had 6.4). A counter simulation over the corrected `.tex` (§4 below) confirms every other number is unchanged and identical to the companion (Thm 6.1/6.3, Prop 6.2, Cor 7.1–7.4, Thm 8.2/8.4, Examples 9.1–9.5 …).
- **E2 — Euclidean-dual lemma boundary cases (GAP-16-01; §4 Lemma).** Inserted, after the dimension sentence: the cases `r = 0` (`g = 1`, `C = Kⁿ`, `C^⊥ = {0}`, `h^♮` of degree `n` has no nonzero multiple of degree `< n`) and `s = 0` (`h = 1`, `C = {0}`, `C^⊥ = Kⁿ`, `h^♮ = 1`) are verified from the definitions, then "Assume `r, s ≥ 1` below, so that `V` is defined (and `v = 0` gives `d = 0`)". This restores exactly the boundary handling present in the source proof P1-04 RR-3; no statement changed.
- **E3 — Constacyclic codes over `A` defined (GAP-16-02; §2).** Added: a `λ`-constacyclic code over `A` is an `A`-submodule of `Aⁿ` closed under the componentwise `λ`-constacyclic shift `(c₀,…,c_{n−1}) ↦ (λc_{n−1}, c₀, …, c_{n−2})`; under `Aⁿ ≅ A[x]/(xⁿ−λ)` the shift is multiplication by `x`, so these codes are exactly the ideals of `A[x]/(xⁿ−λ)` — an equivalence needing no separability or compatibility — and "code over `A`" henceforth means such a code (cf. assembly Proposition 6.2 / P1-05 Prop. 3.1(ii)). Theorem 3.1's closing sentence now says "`λ`-constacyclic codes over `A` correspond to tuples of component assignments (Proposition …)" instead of "global codes (as `A`-submodules)".
- **E4 — Galois pairing attributed (GAP-16-05; §1 and §2).** New reference [FZ2017] added and cited at the first Introduction mention and at the §2 definition ("the `k`-Galois inner product introduced by Fan and Zhang"), with the code-first slot order unchanged.
- **E5 — EAQECC remark justified and kept conditional (GAP-16-04; §10).** The remark now states its hypotheses (`N=1`, `m₁=1`, `[n,K]` code over `F_q`, `H = dim Hull_k(C)`), defines `c = rank(Π ρ(Π)ᵀ)` for a parity-check matrix `Π`, and proves `c = (n−K) − H`: the kernel of the pairing map `D(C) → (C^⊥)*`, `y ↦ (z ↦ Σ zᵢyᵢ)`, is exactly `C ∩ D(C)`. The parameter form `[[n, K−H, d_EA; n−K−H]]` is then attributed to the entanglement-assisted construction **in its Galois form** [DIMP2026] within the framework of [BDS2006], with `d` renamed `d_EA` = "the distance furnished by that construction and must be determined independently". The fencing is unchanged: the enumerator yields `(K,H)` only, no quantum parameter from it alone, affine case needs distance control.
- **E6–E10 — Bibliography completions (GAP-16-06a).** Titles and initials supplied from §1's records: CDL2015 (title), Sharma2015 (title), WZLL2023 (T. Wu, S. Zhu, L. Liu, L. Li + title), ZWLL2025 (Q. Zhang, W. Wang, S. Luo, Y. Li + title), Talbi2021 (S. Talbi, A. Batoul, A. Fotue Tabue, E. Martínez-Moro). BDS2006 gained its verified DOI.
- **E11 — Citation-scope narrowing (GAP-16-06c; §1).** "Galois hulls over chain and serial rings appear in [Talbi2021]" → "Galois hulls of cyclic serial codes over a finite chain ring are studied in [Talbi2021]" (the cited paper is the chain-ring one; no serial-ring reference was added, so the claim was narrowed instead).
- **E12 — Extra consistency (noticed during this phase).** ZKZ2026 authors given as surnames only; initials `E. Zhang, B. Kong, X. Zheng` supplied from the MDPI record (§1). Flagged here so the change is not silent.
- **E13 — Micro-clarification (GAP-16-07; Theorem 5.2).** Added "here and below, `αᵢ` refers to the orbit `(s,O)` under discussion" after the dimension displays.
- Also: a two-line header comment in the `.tex` records this correction round and points to this log. The author placeholder "[Author names and affiliations to be inserted]" is deliberately untouched (author-side item).

## 3. Verification performed

1. **Structural (on the corrected `.tex`):** braces balanced (depth scan), all environment types begin/end-matched (15, including math internals); 33 labels, all `\ref` targets defined; 16 `\bibitem`s, **all cited, no undefined citations**; a counter simulation reproduces the intended numbering with Proposition 6.4 for the `P=1` recovery and confirms no other number moved. The `.md` has 16 reference entries, [FZ2017] cited in its text, and no "serial rings" phrasing remains.
2. **Validators:** `python3 code/validate_p1_14.py` — exit 0, final line `ALL P1-14 INDEPENDENT AUDIT CHECKS PASSED`, output **byte-identical** to the saved `code/validation_p1_14_output.txt` (all four layers including the symbolic Layer A; sympy was already present in the environment — nothing was installed this phase). The manuscript's mathematics was not altered, so this confirms the corrected files still describe the validated statements; E2 restores the boundary handling already present in P1-04 RR-3, and E5's rank identity is proved inline in the remark itself (rechecked as item 4 below).
3. **Boundary-case re-verification (E2)** was done from the definitions, not by analogy: for `r=0`, `⟨h^♮⟩` (multiples of degree `< n`, equivalently the ideal in the quotient, where `h^♮ = xⁿ − λ⁻¹ ≡ 0`) is `{0} = C^⊥`; for `s=0`, `h^♮ = 1` generates `Kⁿ = C^⊥`; in both cases the dimension count `dim = r` also remains valid, so the rest of the proof is untouched.
4. **Rank identity (E5)** checked by the kernel argument above; the matrix of the pairing map in the bases (rows of `Π`, rows of `ρ(Π)`) is precisely `Π ρ(Π)ᵀ`, and `dim D(C) = n − K`.
5. **Frozen blueprint:** SHA-256 `ec2fd8d5…cf438cff` identical before/after; final `git diff` inspected to confirm only the intended files changed (manuscript `.tex`/`.md`, this log, gap register, worklog).

## 4. What could not be done / unresolved items

1. **LaTeX compilation:** no `pdflatex`/`xelatex`/`latexmk`/`tectonic` exists in this environment (checked this phase) and nothing was installed. The `.tex` is structurally verified as above but has **not** been compiled; compilation and a visual proofread remain author-side (this also covers display-equation numbering in the compiled output).
2. **Gate G1 / L1 (DPI2023 full text):** untouched and still DEFERRED; nothing in these corrections depends on it, and no sentence about L1 was strengthened.
3. **GAP-16-08:** the §1 characterizations of DIMP2026/ES2026 rest on the arXiv full texts (repo-verified); publisher versions were not theorem-checked — intentionally left as is.
4. **Author placeholder** remains for the authors to fill; journal-specific bibliography style (e.g. abbreviated journal names, issue numbers for FZ2017 `84(3)`) is a production-stage choice.
5. No mathematical issue remains open from the P1-16 audit; GAP-16-01…07 are addressed by E1–E13 and GAP-16-08 is a recorded no-action note.
