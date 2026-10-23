# P1-16 — Independent Mathematical and Bibliographic Audit of the Manuscript

**Audit object:** `P1_15_MANUSCRIPT_DRAFT.tex` (LaTeX, 980 lines) and `P1_15_MANUSCRIPT_DRAFT.md`, against the frozen blueprint (`02_THEOREM_BLUEPRINT.md`, SHA-256 `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff`, re-verified this phase), proof packages P1-04 (T1–T4), P1-05 (assembly, T5–T6, P=1 recovery), P1-06 (C1–C6), the P1-14 audit, and `P1_15_OPTIONAL_COROLLARIES.md` (N1–N3).
**Audit posture:** written from scratch as a hostile re-reading. Earlier "verified" labels were not trusted; every load-bearing derivation was re-derived or re-checked independently in this phase (hand derivation, exact enumeration at *new* parameter values, and recomputation of the manuscript's printed numbers from its own printed distributions).
**Anchor convention:** references are to the `.tex` sections/theorems and to `.md` section numbers where they differ.

---

## 1. Overall verdict

The manuscript's mathematics is **correct as stated**. No mathematical error, sign error, orientation error, or overstatement of the frozen claims was found in T1–T6, the product assembly, the `P=1` specialization, C1–C6 (including the corrected C5 with its `L=1`/`L≥2` split and the `w_O²`-weighted C6 with separate `L=1`, `L=2`, `L≥3` regimes), or in the candidate corollaries N1–N3. The delicate covariance cancellations behind C6 and behind N1/N2 were **independently re-derived by hand this phase** (§3 below) and confirmed symbolically/numerically at new parameter values.

What remains is a short list of minor matters: two one-sentence justification gaps, a numbering mismatch between the two draft files, and several bibliography completion/verification items for the proof stage. None requires a change to any theorem statement, and the frozen blueprint needs **no** correction.

## 2. theorem-by-theorem audit

| Item | Verdict | How it was re-checked this phase |
|---|---|---|
| T1 parametrization (.tex §3, Thm 3.1) | Correct | Re-read against P1-04 RR-1; bijection/dimension argument re-traced; no hidden separability use (`M = ∏f^P` from char-`p` Freshman's dream is correct since `gcd(n₀,p)=1` makes `x^{n₀}−μ_s` separable: derivative `n₀x^{n₀−1}` shares no root with it, all roots nonzero). |
| T2 reciprocal (Thm 3.2) | Correct | Hand re-check: (i) multiplicativity incl. normalizing constants `(fg)₀=f₀g₀`; (ii) root transport `β = α^{−p^{d_s−k}}` and the minimal-polynomial strengthening (proved in P1-04 RR-2(iv)); (iii) `μ`-compatibility ⟺ `λ`-compatibility via `(μ^{1+D})^P = λ^{1+D}` plus `y^P=1 ⟹ y=1` in char `p`; `β^{n₀} = ρ(μ_s)^{-1} = μ_s` under compatibility, so `τ_s(f) | x^{n₀}−μ_s`; inverse via the `σ`-analogue. |
| Euclidean dual Lemma (Lem 4.1) | Correct, one micro-gap | The `[x^{n−1}](a·revₙ d)` orthogonality computation re-derived from scratch (manuscript's displayed `revₙ(h^♮ v) = h₀⁻¹ h(x) V(x)`, `deg(uV) ≤ n−2` — correct). See GAP-16-01 for the unstated boundary cases. |
| Transport `D(C)=ρ(C^⊥)` (Prop 4.2) | Correct | Slot order re-checked: `y ∈ D(C) ⟺ Σ cᵢσ(yᵢ)=0 ∀c ⟺ σ(y) ∈ C^⊥ ⟺ y ∈ ρ(C^⊥)`; `ρ̄(h^♮) = h^{#}` coefficientwise; compatibility gives modulus `xⁿ−λ` back. The convention is genuinely load-bearing and is stated as such. |
| T3 dual exponents `β_i = P − α_{i−1}` (Thm 4.3) | Correct | Re-derived: `h_a = ∏ f^{P−a_f}` → T2(i) → `∏ g^{P − a_{τ⁻¹g}}`; `τ⁻¹(f_i) = f_{i−1}`. Orientation certified against field data by E4 (see §5). |
| hull Lemma (Lem 5.1) and T4 (Thm 5.2) | Correct | lcm/gcd exponent bookkeeping and `P − max(u,v) = min(P−u,P−v)` re-checked; dimension displays (over `K`, then `×m_s` to `F_q`, `w_O = m_s deg f`) traced factor by factor. |
| T5 transfer trace (Thm 6.1) | Correct | Closed-walk bijection re-checked including `L=1` self-loop and `L=2` backtrack; `(P+1)^L` labelled tuples confirmed vs. `(P+1)^{L−1}(P+1)` trace count. Rotation subtlety: tuples and their rotations are distinct *labelled* assignments and are counted separately on both sides — consistent (witness in §6). |
| Product assembly (Prop 6.2) | Correct | Ideals of a finite ring product; componentwise pairing/dimensions `Σ_s m_s dim_{K_s}`; no coprimality is (incorrectly) invoked. |
| T6 enumerator (Thm 6.3) | Correct | Distributive-law factorization over the Cartesian product of orbit assignments; coefficient interpretation = labelled counts only. |
| `P=1` recovery (Prop 6.5 in .tex; mislabelled 6.4 in .md — GAP-16-03) | Correct | `min(1−b,a) = 1[(a,b)=(1,0)]`; matrix `[[u^w,1],[u^w z^w,1]]` re-read entry by entry. |
| C1 (Cor 7.1) | Correct | `J²=(P+1)J`, `tr(J^L)=(P+1)^L` re-verified. |
| C2 (Cor 7.2) | Correct | Rank-one at `z=1`: `T = c r`, `r·c = Σ_{j=0}^P u^{wj}`, `tr(T^L) = (r·c)^{L−1} tr(T)`; orbit weight uniformity used correctly. |
| C3 LCD (Cor 7.3) | Correct | Boundary argument re-traced in all cases (`P=1` and `L=1` explicitly sound); exactly 2 tuples per orbit, independent across orbits. |
| C4 self-orth./dual-cont. (Cor 7.4) | Correct | `dim C − dim Hull = Σ w Σ max(0, P−α_i−α_{i−1})` and dual analogue via `dim D(C) = Σ w Σ α_{i−1}` re-derived; counts equal by `α ↦ P−α` involution; independently reproduced numerically (144=144 in E5, 12=12 in E3). |
| C5 means (Thm 8.2) | Correct | Full independent re-derivation in §3(a), incl. the `L=2` subtlety (each `X_i` still a min of two *distinct* independent uniforms) and `ν₁ = 0` hygiene (§3(d)). |
| C6 variance (Thm 8.4 + Lem 8.3) | Correct | Full independent re-derivation in §3(b): covariance cancellation `Var(X) + 2κ_P = P(P+2)(P²+2P+2)/(60(P+1)²)`, `L=2` non-interpolation, `w_O²` weights all re-derived by hand and re-confirmed at new `(P,L)` (§3, §7). |
| Examples E1–E5 (§9) | Correct | E1 nine-tuple table re-derived and E2 distribution re-derived *by hand in this audit* (§3(c)); E3's printed statistics recomputed from the printed distribution alone (Probe B, §7); E5 recomputed by independent convolution (Probe C). |
| N1, N2, N3 (optional file) | Correct as stated | N1/N2 variance/covariance identities re-derived by hand (§3(e)); N1's dependence witness at `P=1, L=2, w=1` re-verified by hand; N3 binomial per orbit with `C=H ⟺ α≡P`; all cross-checked numerically (P1-14) plus fresh probes (§7). **Still unadopted candidates** — correctly kept out of the main text; adoption remains an author decision. |

Manuscript ↔ blueprint ↔ proof-package cross-check: every theorem/corollary in the draft matches its frozen statement (including the PC-1 `L=1`/`L≥2` split in C5, the corrected `ν_P`, the `w_O²` weights and `γ_self`-based `κ_P` in C6, and the PC-4 dual-containing equality). No silent strengthening or weakening found, except the T2(ii) minimal-polynomial strengthening, which is proved in P1-04 RR-2(iv) and so is supported. The PC-5 labels (labeled assignments; compatible twists; square-free `A`; EAQECC caution) are all respected in the text; the Introduction stays strictly within abstract-verified descriptions of prior work and makes **no** theorem-level comparison with L1 (Gate G1 correctly untouched).

## 3. Independent C5/C6 audit (hand re-derivations)

All sums were reworked without reference to P1-06. `U,V` i.i.d. uniform on `{0,…,P}`.

**(a) Edge expectations.** `Pr(min(U,V) ≥ t) = ((P+1−t)/(P+1))²` gives `E[min] = Σ_{r=1}^P r²/(P+1)² = μ_P = P(2P+1)/(6(P+1))` ✓, and `E[min²] = P(P²+P+1)/(6(P+1))` ✓ (draft Lem 8.1), hence
`Var(X) = [6P(P²+P+1) − P²(2P+1)²]/(36(P+1)²) = P(P+2)(2P²+4P+3)/(36(P+1)²)` ✓ (manuscript's factored form re-expanded by hand).
`F(c) = E[min(c,U)] = Σ_{t=1}^c (P+1−t)/(P+1) = c(2P−c+1)/(2(P+1))` ✓.

**(b) Covariances.** Adjacent edges (`L ≥ 3`): with `F` as above,
`E[X_i X_{i+1}] = (1/(P+1)) Σ_b F(P−b)F(b)`. Substituting `m = P+1`, `F(b)F(P−b) = [ (m−1)² − (b−m+1)² ][ m(2m−1) − ((m−1)² − (b−m+1)²) ]`-form and summing in the variable `j = b − (m−1) ∈ {−(m−1),…,1}` (or equivalently the power sums `Σbʲ, j≤4`, replicated by hand) yields
`E[X_iX_{i+1}] = P(P−1)(11P²+15P+6)/(120(P+1)²)`, so
`κ_P = E[·] − μ_P² = −P(P+2)(7P²+14P+9)/(360(P+1)²)` ✓ (the quartic numerator `150P⁴+…` was re-factored by hand; matches Lem 8.3(ii)).
Then `Var(X) + 2κ_P = [10num_Var − 2num_κ-stuff]`: over `360(P+1)²`,
`10·P(P+2)(2P²+4P+3) − 2·P(P+2)(7P²+14P+9) = 6P(P+2)(P²+2P+2)`, giving exactly `P(P+2)(P²+2P+2)/(60(P+1)²)` per position — the printed `V_L` for `L≥3` ✓. This is the covariance cancellation; it is genuine and the resulting per-orbit factor `L` (not `L²`) is correct because only the `L` adjacent pairs covary.
`L=2`: `E[X₀X₁] = Σ_{s+t≤P} ((P−s−t+1)/(P+1))² = Σ_{r=1}^{P−1}(P−r)r²/(P+1)² = P²(P−1)/(12(P+1))` ✓; `Cov = −P²(P+2)²/(36(P+1)²)` ✓ (numerator collapse `3P²(P−1)(P+1) − P²(2P+1)² = −P²(P+2)²` re-done by hand);
`V₂ = 2Var(X)+2Cov = P(P+2)(P²+2P+3)/(18(P+1)²)` ✓.
`L=1`: `V₁` re-derived from `Σ_a min(P−a,a)²` for both parities (`P=2m`: `m(2m²+1)/3`; `P=2m+1`: `m(m+1)(2m+1)/3`) minus `ν_P²` ✓, both branches.

**(c) E1/E2 by hand.** E1 (`P=2,L=2,w=1`): all nine `(Σ(2−α_i), Σ min(2−α_i,α_{i−1}))` values recomputed — printed table exact; `ΣH = 10 → E = 10/9 = 2μ₂` ✓; `ΣH² = 14 → Var = 14/9 − 100/81 = 44/81 = V₂(2)` ✓; exactly two `H=0` tuples ✓.
E2 (`P=1,L=3`): enumerating the 8 binary cycles, `1→0`-transitions give `{(0,0):1,(1,1):3,(2,1):3,(3,0):1}` ✓; `Var(H) = 3/4 − 9/16 = 3/16 = V₃(1)` ✓.

**(d) Formula hygiene.** `ν₁=0, μ₁=1/4` (no double-count of `L=1` orbits at `P=1`) ✓; `ν_P ≤ μ_P` for all `P≥1` with equality only at `P=1` (`3⌊P²/4⌋ ≤ P(2P+1)/2`, since `3P²/4 ≤ P² + P/2`) ✓ — this is exactly the C5-PC-1 correction, and it is correctly reflected in the theorem, the proof, the Introduction's warning paragraph, and E3's `23/9`. The printed marginal ``[z^0]T_O = 2`` per orbit (C3 coefficient view) and the `E(u,1)` factorization (C2) are consistent with T5/T6.

**(e) N1/N2.** Per orbit, `Cov(Σᵢ (P−Aᵢ), Σᵢ Xᵢ) = L·γ + L·γ' ` with `γ = E[(P−A₀)min(P−A₀,A₋₁)] − (P/2)μ_P = P(P+2)/24` and `γ' = E[(P−A₁)min(P−A₀,A₋₁)] − (P/2)μ_P = −P(P+2)/24`, recomputed from the defining sums — the cancellation `γ + γ' = 0` is exact in every length `L≥1`, including `L=2` where the two slots (`shared current variable` vs `independent current variable`) are still distinct, and `L=1` (`γ_self = E[(P−A)min(P−A,A)] − (P/2)ν_P = P(P+2)/24` handled separately) ✓. Hence `Cov(dim C, dim Hull) = 0` globally (N1) ✓, while dependence is real: at `P=1,L=2,w=1`, `Pr(K=2)=1/4, Pr(H=1)=1/2, Pr(K=2 ∧ H=1)=0 ≠ 1/8` (re-verified by hand) ✓. `Var(dim C) = [P(P+2)/12]·Σ_s Σ_f w_f²` (N2) ✓, consistent with the global identity `Σ_sΣ_f w_f² = Σ_{s,O} w_O² L_O`. N3's per-orbit `1 + u^{PwL}` binomial ✓.

## 4. Hypotheses audit

- **Prime powers:** `P = p^ρ` is needed only where the field construction enters (T1–T4); the draft says this explicitly (remark after Thm 6.3) and T5 is stated/proved for every integer `P ≥ 1`. No overreach. A rotation subtlety — labelled vs. cyclically identified assignments — is stated everywhere ("labeled exponent assignments"), and C1's total `(P+1)^{Σ|F_s|}` pins the convention; no place silently passes to equivalence classes.
- **`P=1`:** binary specialization sound; the trap `ν₁` ≠ `μ₁` is handled correctly (`ν₁=0`).
- **`L=1, L=2`:** both treated separately wherever needed (C5, C6); the `L≥3` variance formula is *not* extrapolated to `L=2` (draft's own `44/81` vs `8/27` witness at `P=2` is correct).
- **Repeated roots / squarefree `A`:** `A` is a product of fields (reduced); the draft never claims chain-ring generality, and the Limitations section fences this. `gcd(n₀,p)=1` is what makes `x^{n₀}−μ_s` separable — stated and used correctly.
- **Compatibility:** gates exactly the steps that need it (T3's same-modulus form onward); the two-modulus fallback is stated honestly in the remark after Thm 4.3 and in Limitations. The `𝔽₉` counterexample (`λ` of order 8, `k=1`: `λ⁴ = −1`) was re-verified by hand this phase (in `𝔽₉*` of order 8, `λ⁴` has order 2, hence equals `−1` ✓, and `λ^{−3} = λ⁵ ≠ λ` since `λ` has order 8 ✓).
- **Pairing convention:** code-first with `ρ = σ⁻¹` is defined in §2, propagated through Prop 4.2/T3/T4, and the convention-dependence is disclosed in Limitations. The enumerator's insensitivity to orbit reversal is *correctly* flagged as making the statement-convention essential; the field-level certificate E4 genuinely pins the orientation because it compares hull dimensions assignment-by-assignment on a length-6 orbit, where predecessor/successor readings differ (verified extensively in P1-14 Layer C; see §7).
- **Uniform model:** means/variances are explicitly about uniform labelled assignments; independence holds across orbits only — stated.

## 5. orientation and convention check (explicit)

The chain `code-first pairing → D(C)=ρ(C^⊥) → h^{#} → β_i = P − α_{i−1} → edge term min(P−α_i, α_{i−1}) → transfer matrix T_{a,b}` was followed link by link in §2–§6 of the draft and found internally consistent; the E4 assignment-level agreement (GF(8), orbit length 6, `n=14`) is a valid certificate: with the successor reading, hull dimensions would differ on generic assignments on that orbit, so the brute-force match would fail. Nothing in the draft's later sections (corollaries, moments, examples) contradicts the frozen convention; the reversed-convention code of the earlier prototype (GAP-02 history) did not leak into the manuscript.

## 6. Counterexample attempts

Active attempts were made against each potential failure mode; **none succeeded**:

1. **Overall joint law:** `validate_p1_14.py` Layers B–D (52 `(P,L)` pairs, 58 weighted orbit configurations, 2,769 field-level assignments over GF(4)/GF(8)/GF(9)/GF(3), assignment-level Gram-rank comparisons) re-ran unmodified this phase — exit 0, output byte-identical to the saved record (all four layers, including the sympy symbolic re-derivation Layer A; environment note in §8).
2. **Moments at new values:** independent exact enumeration at `(P,L) ∈ {(11,2),(11,3),(4,5),(6,3),(10,2),(12,1)}` — values *outside* every earlier grid — reproduced `E[S_L]`, `Var(S_L) = V_L(P)`, `Var(orbit code-dim) = L·P(P+2)/12`, and `Cov = 0` exactly at all six points (Probe A).
3. **Printed numbers:** E3's `E[H]=23/9`, `Var(H)=194/81`, LCD 4, self-orth = dual-cont = 12, and `Cov=0` recomputed from the printed 15-entry distribution alone (Probe B); E5's `729/16/144/144/11/230/9` recomputed by an independent convolution from the printed orbit data (Probe C). All exact.
4. **Boundary probes:** `L=1` vs `L≥2` means (`ν_P` vs `μ_P`), `P=1` orbit behaviour (`ν₁=0`), hypotheses at `P=1` (binary matrix), the `𝔽₉` incompatible-twist witness, and the labelled-vs-cyclic count at `P=1,L=3` (8 labelled vs 4 rotation classes; the enumerator counts 8 ✓ — Probe D) were each checked deliberately.

Where a statement *would* fail, the audit notes the manuscript already fences it: `V_L (L≥3)` at `L=2`, the `μ_P`-for-all-`L` mean (defeated by `ν_P`), hull claims without compatibility, and EAQECC parameters from the enumerator alone. The only genuine "would-fail" items found are presentational/bibliographic, below.

## 7. Reproducible checks run this phase

1. `git log/status/ls-remote` + blueprint `sha256sum` — remote at `523c342` = manuscript commit; blueprint hash unchanged. (Local checkout metadata had restarted at the base commit with files untracked; restored locally via `git reset --hard origin/arena/...` after verifying every working-tree blob hash-matched its remote blob — project tree byte-identical post-restore; remote untouched.)
2. `python3 code/validate_p1_14.py` — exit 0, `ALL P1-14 INDEPENDENT AUDIT CHECKS PASSED`, **byte-identical** to `code/validation_p1_14_output.txt` (all layers). Note: the sandbox starts without sympy (Layer A then self-skips with a notice); sympy 1.14.0 was installed transiently to obtain the full four-layer run, exactly as in P1-14.
3. Ad-hoc probes A–D (run from `/tmp`, not repository artifacts; fully specified by their descriptions in §6): fresh-value moment/N1/N2 checks, E3 printed-distribution recomputation, E5 independent convolution, labelled-count witness. All passed.
4. Manuscript structure re-verified on the final `.tex`: balanced braces/environments, 33 labels, no missing refs/cites, **all 15 bibliography entries cited**, no novelty/priority wording. LaTeX compilation remains impossible in this sandbox (no toolchain) — the draft is compile-ready but the `.tex` has never been compiled; that is a remaining unverifiable item (§9), not a defect found.

## 8. Issues found

**No mathematical errors.** Issues, each classified:

- **GAP-16-01 — missing justification (minor).** Lem 4.1's proof: the degree bound `deg(uV) ≤ n−2` is stated without the boundary cases `r = 0` (then `v = 0`) and `s = 0` (`u = 0`), which the proof's quantifiers imply but never say. *Correction:* add one sentence: "If `r=0` or `s=0` the corresponding factor is `0` and orthogonality is trivial."
- **GAP-16-02 — missing justification (minor).** §2 defines "a code over `A`" as an `A`-submodule of `Aⁿ` without saying *constacyclic*; Thm 3.1's last sentence then speaks of "global codes (as `A`-submodules)" corresponding to assignment tuples. Strictly, the correspondence is with `λ`-constacyclic codes (ideals of `A[x]/(xⁿ−λ)`). The Introduction uses the correct phrase, so this is a definitional tightening only. *Correction:* add to §2 "A `λ`-constacyclic code over `A` is an ideal of `A[x]/(xⁿ−λ)`, equivalently a shift-invariant `A`-submodule of `Aⁿ`" (cf. P1-05 Prop 3.1(ii)).
- **GAP-16-03 — presentation.** The `.md` companion labels the simple-root recovery "Proposition 6.4"; in the `.tex` it is **Proposition 6.5**, because Remark after Thm 6.3 shares the theorem counter (Remark 6.4). The `.md`'s Example 9.2 reference inherits the mismatch. *Correction:* make remarks unnumbered in the `.tex` (`\newtheorem*{remark}`-style or separate non-counting environment), which restores 6.4 and matches the companion; or renumber the companion. Verify the `.md`'s other numbers are otherwise exact — they are (Thm 6.1/6.3, Prop 6.2, Cor 7.1–7.4, Thms 8.2/8.4, Examples 9.1–9.5 all agree with the `.tex` under the shared counter).
- **GAP-16-04 — bibliographic problem + missing justification (minor).** The §10 entanglement-assisted remark rests its `[[n, K−H, d; n−K−H]]` parameter form solely on `Brun–Devetak–Hsieh` (Euclidean setting). For a `k`-Galois hull the formula needs the standard Galois-hull rank identity; the draft neither states it nor cites a Galois-EAQECC source (the repository-verified `DIMP2026`/`ZKZ2026` contain such constructions). Also, the BDS2006 metadata itself is standard but is not verified by any repository record. *Correction:* verify BDS2006 metadata from the publisher, add the one-line rank justification or cite a Galois-hull EAQECC reference alongside; keep the distance fencing exactly as is.
- **GAP-16-05 — bibliographic problem.** The `k`-Galois inner product is used from §2 onward with no citation of its origin in the literature. The repository audit records this foundation only as an unresolved research item (its full bibliographic record was never established in-repo). *Correction:* complete this reference from the primary source at the submission stage and cite it at first use; do **not** fill in details from memory.
- **GAP-16-06 — bibliographic problems (minor, proof-stage).** (a) Missing article titles and/or author initials: CDL2015 (no title), Sharma2015 (no title), WZLL2023 (initials only, no title), ZWLL2025 (no title), Talbi2021 (authors without initials). (b) Author-name form conflict in the repository records for the first author of ES2026 ("Ramy F. Taki Eldin" from the arXiv-derived record vs. "Ramy Abu Eldin" in a later audit table) — the draft follows the former; confirm against the publisher/arXiv title page. (c) The Introduction cites Talbi2021 for "chain and serial rings" while the entry is the chain-ring paper; either add the serial-ring reference or narrow the phrase. None of these affects any mathematical statement.
- **GAP-16-07 — presentation (micro).** Thm 5.2's statement names the component code `C_s(a)` but displays global (summed-over-`s`) dimensions; the predecessor shorthand `α_i` suppresses `(s,O)`. The same shorthand is used consistently afterwards, so a single clause ("indices `α_i` refer to the `(s,O)` orbit under discussion") suffices.
- **GAP-16-08 — bibliographic note (no action required in text).** The §1 characterizations of DIMP2026 ("simple-root (idempotent) framework with a repeated-root case under additional hypotheses") and ES2026 are verified against the **arXiv** full texts (repo P1-01/P1-09); the publishers' versions were never theorem-checked, and the draft prudently makes no theorem-number claims about either. The DPI2023 sentence likewise stays within its abstract-verified scope. Recorded here so the proof stage does not "strengthen" any of these sentences.

## 9. Prioritized correction list (proposed; none applied — manuscript unchanged)

**Priority 1 (before any submission):** GAP-16-04 (correct support for the EAQECC remark), GAP-16-05 (Galois-pairing origin citation, from primary source), GAP-16-02 (constacyclic-over-`A` definition), GAP-16-01 (Lemma boundary sentence).
**Priority 2 (polish):** GAP-16-03 (remark numbering / companion alignment), GAP-16-06 (bibliographic completeness + Eldin name form), GAP-16-07 (T4 shorthand clause).
**Priority 3 (production):** insert author names/affiliations; compile the LaTeX (unavailable in this sandbox) and proofread the compiled output, including displayed-number cross-references.
**Explicitly not corrections:** the frozen blueprint (no change needed or proposed); N1–N3 (correct, but adoption is an author decision — left in the optional file); Gate G1/L1 (remains DEFERRED; L1's full text was not available to this audit either, and nothing in the manuscript depends on it).

## 10. Remaining unverifiable items

1. L1 (DPI2023) theorem-level content — full text unavailable; L1-Q1–Q6 open; novelty question untouched by this audit (none claimed anywhere).
2. Publisher-version theorem numbering/content for DIMP2026/ES2026 (arXiv versions verified instead) — GAP-16-08.
3. BDS2006 metadata and the Fan–Zhang origin record (GAP-16-04/05) — not verifiable from repository evidence; flagged, not guessed.
4. LaTeX compilation — no toolchain in the sandbox; structure was verified programmatically instead.
5. The author placeholder and any journal-specific formatting — production items, out of scope here.

## 11. Files changed by this phase

- `P1_16_INDEPENDENT_AUDIT.md` (this file) — created.
- `04_BLUEPRINT_GAP_REGISTER.md`, `ARENA_WORKLOG.md` — P1-16 outcome appended (incl. GAP-16-01…08).
- **Unchanged, deliberately:** `P1_15_MANUSCRIPT_DRAFT.tex/.md`, `P1_15_OPTIONAL_COROLLARIES.md`, `02_THEOREM_BLUEPRINT.md` (hash re-verified `ec2fd8d5…cf438cff`), all proof packages and validators. Probe scripts were run from `/tmp` and are fully described in §6–§7 rather than added to the repository.
