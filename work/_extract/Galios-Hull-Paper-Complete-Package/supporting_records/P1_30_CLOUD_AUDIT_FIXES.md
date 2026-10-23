# P1-30 — Cloud audit fix log (22 October 2026)

Response to the independent referee-style cloud audit (11 pages, recommendation: major revision; mathematics verified correct — 0 mismatches across 96 orbit-level configurations and 7,847 explicitly constructed codes). Each finding is mapped to the action taken. Manuscript edits are in `P1_15_MANUSCRIPT_DRAFT.tex` and the synchronized `P1_15_MANUSCRIPT_DRAFT.md`. No theorem statement or proof was changed. Gate G1 remains DEFERRED; no novelty or priority claim was added anywhere.

## Major findings

- **M1 (contribution not demonstrated).** Added a "Contributions and positioning" paragraph in the Introduction with an explicit contribution list (dual/hull exponent form; joint law as transfer-matrix traces with the $K\leftrightarrow\Delta-K$ symmetry; LCD/self-orthogonal/dual-containing closed forms; exact mean/variance with $L=1,2,\ge3$ regimes), a complexity statement ($O(\log L)$ matrix multiplications per orbit trace vs $(P+1)^L$ assignments for direct enumeration), and a positioning table against [DP2025], [DPI2023]+correction, [DIMP2026], [ES2026]. The table states that the DPI2023 comparison is based on the published abstracts only and no theorem-level comparison is asserted (Gate G1). The question whether Theorem 8.2 reproduces the averages of [DP2025] is deliberately not claimed; the moments section now states that comparisons require matching hypotheses. The suggested CLT/spectral closed form was **not** added (would be new, unproved mathematics).
- **M2 (false orientation claim, Example 9.4).** Deleted. Replaced by the correct statement: the hull dimension is orientation-invariant per assignment ($\min(P-a,b)-\min(P-b,a)=b-a$ telescopes around the orbit), so a Gram-rank dimension check cannot certify orientation; orientation is visible in the hull generator, whose exponent vector equals the predecessor prediction $P-\alpha_{i-1}$ on all 2187 assignments (successor: only 27) — verified in `code/validate_audit_fixes.py` §3b. The remark after Theorem 6.3 and the §10 convention text were corrected to the same per-assignment invariance statement. The full joint distribution of Example 9.4 was also added (minor m9).
- **M3 ("affine algebras" cosmetic).** Title changed to "...over finite products of finite fields via transfer matrices". §2 now defines "affine algebra" and "square-free" ('etale/reduced) and states plainly that only the product decomposition, the component twists and the weights $w_O$ enter; keywords updated accordingly.
- **M4 (constacyclic generality not exercised).** §2 now gives the number of compatible twists, $\gcd(1+p^{d_s-k},\,p^{d_s}-1)$. New **Example 9.6**: $\mathbb{F}_9$, $k=1$, $\lambda=\iota$ of order 4, $P=3$, $n_0=4$ — two irreducible quadratics, one $\tau$-orbit of length 2, 16 assignments, joint distribution $\{(0,0):1,(2,2):2,(4,4):3,(6,6):4,(8,4):3,(10,2):2,(12,0):1\}$, $\mathbb{E}[H]=7/2$, $\mathrm{Var}=15/4$, LCD $=2$, SO $=$ DC $=10$, all Gram-verified (`validate_audit_fixes.py` §1).
- **M5 (verification not reproducible).** Computational-verification paragraph rewritten with the exact decomposition: orbit grid of 52 pairs $(P,L)$, $P\in\{1,2,3,4,5,7,8,9\}$, $1\le L\le 8$, $(P+1)^L\le10^5$; field-level Gram cases $27+27+256+256+16+2187 = 2769$ assignments listed case by case; Example 9.5's 729 checked by convolution; new cases with $P=4,8,9$ added and verified ($\mathbb{F}_2$ $P=4$: 25, $P=8$: 81; $\mathbb{F}_3$ $P=9$: 100). All scripts and saved outputs are in `code/` (`validate_p1_14.py`, `validate_p1_20.py`, `validate_code_table.py`, `validate_audit_fixes.py`). Remaining author action: deposit the code in a repository with a DOI at submission time.
- **M6 (quantum remark hypotheses).** The remark now states its hypotheses (finite-field case $N=m_1=1$, $q=p^e$, $0\le k<e$), notes the product case needs distance control, points to the ten Table-2 codes as explicit instances with independently computed distances, and states that no asymptotic family is claimed because the distance is the limiting quantity for repeated-root families. (The code table itself was added earlier and already computes $d$ independently.)
- **M7 (uniform model motivation).** New "The model." paragraph at the start of §8: the uniform measure is uniform over the codes of the family itself (bijection of Theorem 3.1); the typical hull grows linearly with $n$ (roughly $\Delta/3$ for large $P$, $\Delta/4$ at $P=1$), in contrast to random linear codes [Sendrier1997]; the variance quantifies fluctuations, and the moments describe the typical entanglement cost $c=n-K-H$.

## Minor findings

- **m1** Draft date removed (`.tex` `\date{}`, `.md` author line). (The "Galios" spelling is the project/repository name, not a manuscript artefact — not changed.)
- **m2** Internal tags T1–T6, C1–C6 removed from all theorem/corollary headings.
- **m3** Notation collisions addressed where safe: $\varrho$ eliminated (P is "a power of $p$"); the algebraic root $\alpha$ in Theorem 3.2(ii) renamed $\xi$; the field symbol $K$ removed from Proposition 4.2. Remaining overloads are locally scoped and standard.
- **m4** Theorem 8.4's variance formulas split into an `aligned` display (the $L\ge3$ hypothesis is on its own line and cannot be cut off); Lemma 8.3(ii) rephrased so $\kappa_P<0$ precedes the fraction. (To be confirmed visually at compilation — no LaTeX compiler in the sandbox.)
- **m5** "Affine algebra", "square-free", "labeled" defined in §2 before use; abstract rewritten plainly (~140 words, no undefined symbols).
- **m6** Code-first convention dictionary to Liu–Pan added after Definition 2.1 ($D(C)=\sigma^{e-k}(C^\perp)$); reference [LP2020] added (verified: *Des. Codes Cryptogr.* 88 (2020), 241–255, doi:10.1007/s10623-019-00681-2).
- **m7** Lemma 4.1 marked as the classical constacyclic dual with citations [HP2003, MS1977].
- **m8** The LCD count $2^{\#\text{orbits}}$ is stated for labeled assignments in the full repeated-root family; special-length enumerations are cited in the Introduction and not used (no unverified cross-check claimed).
- **m9** Full joint distribution of Example 9.4 added.
- **m10** §10 limitations rewritten as prose (*Scope.*) plus an *Open problems* paragraph (incompatible twists; counting up to equivalence; multi-twisted extension; distance distributions).

Also added: [Sendrier1997] N. Sendrier, *SIAM J. Discrete Math.* 10(2) (1997), 282–293, doi:10.1137/S0895480195294027 (verified). The positioning table makes the EAQECC code table **Table 2** (was Table 1); all references updated.

## Verification after the fixes

- `code/validate_audit_fixes.py` exits 0 (16 + 25 + 81 + 100 brute-forced assignments for Examples 9.6 and $P=4,8,9$; orientation invariance on all tuples for $(P,L)=(2,6),(3,4),(2,1),(4,3)$; hull-generator predecessor exponents 2187/2187, successor 27/2187). Output: `code/validation_audit_fixes_output.txt`.
- `code/validate_p1_20.py` and `code/validate_code_table.py` re-run after the edits, outputs byte-identical to the saved ones. `code/validate_p1_14.py` exits 0 with Layers B–D byte-identical; its symbolic Layer A is skipped in this sandbox (no sympy installed), so the saved output from the sympy run is retained.
- Structural scan of the `.tex`: no undefined `\ref`, balanced braces, `\begin`/`\end` counts equal, no leftover internal tags, false claim, draft marker or $\varrho$.

## Not done (author / later actions)

1. Compile the `.tex` twice with pdflatex (no compiler in the sandbox) and visually confirm m4 and the two tables' layout; upload the resulting `.log`/`.pdf` for the P1-29 layout review.
2. Deposit `code/` with a DOI (e.g. Zenodo) and cite it in a data/code availability statement; add cover letter, declarations, ORCID and target-journal choice at submission time (audit §"Submission package check").
3. The complete-package ZIP (`Galios-Hull-Paper-Complete-Package-ea18e8c.zip`) is now stale; refresh it after the compiled-PDF review.
