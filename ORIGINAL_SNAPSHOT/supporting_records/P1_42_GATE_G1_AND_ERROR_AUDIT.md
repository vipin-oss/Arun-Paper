# P1-42 — Gate G1 Comparison Status and Focused Error-Audit Record

**Date:** 22 October 2026. **Manuscript:** reading copy at `3e4f87f`;
IEEE single-column review version at `6ad0e87` (both compiled; see §4).

## A. Gate G1 — status at P1-42: DEFERRED (superseded by §C, P1-44 update of 23 Oct 2026: PARTIALLY RESOLVED)

**Access attempt (22 Oct 2026).** The publisher page for Debnath–Prakash–
Islam, *Galois hulls of constacyclic codes over finite fields*, Cryptogr.
Commun. 15(1), 111–127 (2023), doi:10.1007/s12095-022-00591-6, was
re-examined. Only the **abstract and reference list** are lawfully
readable without a subscription ("This is a preview of subscription
content"); the correction (doi:10.1007/s12095-022-00602-6) is known only
to exist (pp. 129–130). A bounded search for a lawful author/institutional
copy found none (ResearchGate listings were not used as a lawful source;
no paywall circumvention was attempted).

**What can and cannot be compared.** From the publisher abstract alone,
L1 (i) gives "a formula for the dimension of Galois hulls of constacyclic
codes" by arranging the irreducible factors of \(x^n-\lambda\) over
\(\mathbb{F}_q\), and (ii) under "some restrictions on \(q\)" calculates
"the number of constacyclic codes of length \(n\) over \(\mathbb{F}_q\)
for a given Galois hull dimension". Theorem numbers, hypotheses (in
particular whether \(p\mid n\) / repeated roots are allowed), counting
objects, and formulas of L1 are **not** available, so no theorem-level
comparison is possible. The comparison below is therefore limited to
abstract-level scope; it establishes neither overlap nor non-overlap.

| Aspect | L1 (2023), abstract-level only | This manuscript (exact locations) |
|---|---|---|
| Setting | constacyclic codes over \(\mathbb{F}_q\) (root multiplicity not stated in abstract) | repeated-root length \(n=Pn_0\), \(P\) a power of \(\mathrm{char}\), finite products of fields, compatible twists (Thm. V.2/5.2) |
| Hull dimension | formula for a given code's Galois hull dimension | hull generator \(\mathrm{lcm}(g_a,h_a^\#)\) and dimension formula (Thm. V.2/5.2) |
| Counting | number of codes with a given Galois hull dimension, under unstated restrictions on \(q\) | joint enumerator \(\prod \mathrm{tr}((T^{(P)}_{w_O})^{L_O})\) for the pair \((\dim C, \dim\mathrm{Hull}_k(C))\) (Thm. VI.3/6.3); LCD/SO/DC specializations (Cors. VII.3–VII.6); moments incl. Var/Cov (Thm. VIII.4, Cor. VIII.5) |
| Proof technique | not available (full text unread) | transfer-matrix traces over reciprocal-involution orbits; predecessor convention fixed by the code-first pairing (Sec. II) |

**Conclusion (at P1-42).** G1 remained **DEFERRED**: resolution required
a lawfully read full text of L1 and its correction. That full text was
subsequently obtained lawfully (see §C); §A is retained as the historical
record of the abstract-level stage.

## B. Focused error audit — no confirmed errors found; nothing corrected

The checks below were performed; they corroborate, but (per the task
rule) do not by themselves prove, the manuscript's results.

1. **Existing validators (re-run, all exit 0):**
   `validate_p1_14.py` (orbit-level enumeration vs transfer traces on the
   52-pair \((P,L)\) grid, moment closed forms), `validate_p1_20.py`,
   `validate_code_table.py` (all 10 EAQECC rows: hull dimension both from
   Thm. 5.2 and the code-first Gram matrix; distances independently),
   `validate_audit_fixes.py` (Example 9.4 orientation: \(h^\#\) exponents
   match predecessor 2187/2187 vs successor 27/2187 over \(\mathbb{F}_8\);
   Example 9.6 twist; P = 4, 8, 9 cases).
2. **New independent edge checks** (`code/validate_p1_42_edge_checks.py`,
   output saved alongside): for 48 \((P,L,w)\) cases, fresh enumeration
   of all assignments reproduces (i) the transfer-matrix trace
   distribution (via independent bivariate-polynomial matrix powers),
   (ii) \(\mathbb{E}[\dim C]\), \(\mathbb{E}[\mathrm{Hull}]\)
   (\(\mu_P\), \(\nu_P\) regimes), (iii) \(V_1/V_2/V_{\ge3}\) variances,
   (iv) \(\mathrm{Var}(\dim C)=\frac{P(P+2)}{12}\sum w_f^2\) and
   \(\mathrm{Cov}(\dim C,\dim\mathrm{Hull}_k(C))=0\) of Corollary VIII.5,
   (v) the \(K\leftrightarrow\Delta-K\) symmetry, (vi) LCD count \(2\)
   per orbit, (vii) SO count = DC count. All passed.
3. **Conventions/notation:** predecessor index \(\alpha_{i-1}\) is used
   consistently with the code-first pairing (Definition II.1); hull
   generator exponent \(\max(\alpha_i, P-\alpha_{i-1})\); dimension
   counts are over labeled assignments (scope stated in Sec. X); the
   \(L=1\) vs \(L\ge2\) mean constants \(\nu_P,\mu_P\) are not
   interchanged; Corollary VIII.5 says "uncorrelated", not "independent".
4. **References/citations:** 25 bibliography entries, all cited, no
   unresolved keys in either compiled version (0 undefined references in
   both logs); the seven P1-39 entries were verified against publisher
   records; citation-to-claim wording in the introduction matches what
   those papers establish (mass formulas, one-dimensional hulls,
   double-cyclic hull counts, relative hulls, Galois-hull constructions).
5. **IEEE formatting:** both logs are error-free; the IEEE version is 18
   pages in the required single-column review format (limit 50).

**Mathematical errors: none confirmed in the checks above; none
corrected; none knowingly left unresolved.** This is not a claim that
the manuscript is error-free: the audit is a focused corroboration of
the stated formulas on the grids and cases listed, and Gate G1 (Part A)
is still open.

## C. Version consistency

Reading copy `.tex` `362710c00998…`, IEEE `.tex` (same content under
IEEEtran; conversion commit `6ad0e87`), both PDFs/logs in `compiled/`,
this record, the validators (including the new P1-42 script/output), and
the refreshed package/manifest all correspond to the same manuscript
content; only packaging files changed in P1-42, so the manuscripts were
not recompiled.

## C. P1-44 update (23 Oct 2026) — full-text comparison; G1: PARTIALLY RESOLVED

**Access.** The full text of L1 was obtained lawfully: the Commander
supplied the publisher PDF of Debnath–Prakash–Islam, *Cryptogr. Commun.*
15(1), 111–127 (2023), doi:10.1007/s12095-022-00591-6 (17 pp.; PDF
metadata title/author/DOI verified against the publisher record). The
publisher PDF is **not** committed to this repository (licence). The
published correction, doi:10.1007/s12095-022-00602-6 (pp. 129–130), was
read in full lawfully via the publisher page (P1-43): it makes only minor
textual/reference corrections and does not alter any theorem of L1.

**Theorem-by-theorem comparison** (journal pagination of L1):

| L1 result | Statement (hypotheses) | Relation to this manuscript |
|---|---|---|
| Theorem 3 (pp. 119–120) | \(q=p^e\); \(n=n'p^\nu\), \(\gcd(p,n')=1\), \(\nu\ge0\) (**repeated-root lengths included**); \(\operatorname{ord}(\lambda)=r\mid(1+p^{e-k})\); \(\gcd(n',r)=1\). \(\dim\mathrm{Hull}_k(C)=\sum_t\sum_{j\in D_t}\operatorname{ord}_j(q)\,b_{tj}\) with \(b_{tij}=a_tp^\nu-\sum_i\max(u_i,p^\nu-u_{i-1})\) over reciprocal cycles of length \(a_t\) | **Equivalent, single field.** With \(P=p^\nu\), per cycle \(a_tP-\sum_i\max(u_i,P-u_{i-1})=\sum_i\min(P-u_i,u_{i-1})\) by \(P-\max(u,P-v)=\min(P-u,v)\); \(\operatorname{ord}_j(q)\) is our orbit weight \(w_O\); their \(\beta_t(j)\) counts cycles as our orbits do. Hence Thm. 5.2/V.2 (T4), restricted to one field component, **is** L1 Thm. 3; the per-code hull-dimension formula is **not new** and is now credited as such in the manuscript (Introduction, Table 1, remark after Thm. 5.2/V.2). Differences: ours is over a finite product of fields with \(\mathbb{F}_q\)-scaling \(m_s\), and assumes compatibility \(\lambda_s^{1+p^{d_s-k}}=1\) only (no \(\gcd(n_0,r)=1\) hypothesis) |
| Corollary 1 (pp. 120–121) | \(\gcd(q,n)=1\) specialization; hull dimensions of the same form and \(\le n/2\) | Simple-root specialization; subsumed by Thm. 5.2/V.2 at \(P=1\) |
| Theorem 4 (pp. 123–126) | Number of \(\lambda\)-constacyclic codes with hull dimension \(L\), under \(e\mid4(e-k)\), \(e\nmid2(e-k)\), so reciprocal-orbit lengths \(a_t\in\{1,2,4\}\); explicit case-split sums (separate \(q\) even/odd), single field, hull dimension only | **Different object.** No joint \((\dim C,\dim\mathrm{Hull})\) distribution, no transfer-matrix/generating-function form, no arbitrary orbit lengths, no moments. Our Thms. 6.2–6.3 (T5/T6), Cors. 7.3–7.6 and moment results Thm. 8.2/8.4, Cor. 8.5 have no counterpart in L1 as far as its full text shows |

**What is genuinely absent from L1** (verified against the full text):
the joint code–hull enumerator as a product of transfer-matrix traces;
arbitrary reciprocal-orbit lengths in the counting; the product-of-fields
assembly; exact mean/variance formulas for the hull dimension under the
uniform labeled model, including the variance regimes \(L=1,2,\ge3\) and
\(\operatorname{Cov}(\dim C,\dim\mathrm{Hull}_k(C))=0\) (Cor. 8.5/VIII.5).
(Averages of hull dimensions over finite fields are treated in the
*separate* paper DP2025; no identity with our Thm. 8.2/VIII.2 under
matched hypotheses is claimed.)

**Incidental observation.** L1, Example 6 (p. 122), prints hull dimension
\(2\) for \(C=\langle(x+1)^2(x^4+2x^3+x^2+2x+1)\rangle\) over
\(\mathbb{F}_{27}\); applying L1 Thm. 3 (equivalently our Thm. 5.2) gives
\(\operatorname{ord}_2(27)\cdot1+\operatorname{ord}_{10}(27)\cdot1
=1+4=5\). This appears to be an arithmetic slip in their example
(summing the \(b\)'s without the \(\operatorname{ord}_j(q)\) weights);
our manuscript does not use that example, and no change to our text
arises from it.

**Status.** G1 is **PARTIALLY RESOLVED**: the L1 overlap is now
identified at theorem level and credited; the manuscript no longer
carries any abstract-only fence for [DPI2023]. **Remaining novelty
uncertainty (explicit):** (i) no exhaustive theorem-level comparison has
been made against DP2025 (averages), ES2026 and DIMP2026 beyond the
positioning in Table 1; (ii) whether the joint-enumerator/moment package
and the product-of-fields assembly constitute a sufficient advance is an
editorial/referee judgment, not established here; (iii) L1 Thm. 3 carries
the extra hypothesis \(\gcd(n',r)=1\), so the formulas are proved
equivalent only where both sets of hypotheses apply. Novelty is **not**
claimed to be fully established, and the paper has not been submitted.

## D. P1-45 update (23 Oct 2026) — DP2025 mean comparison

**Access.** The full text of Debnath–Prakash, *Average dimensions of
Galois hulls of constacyclic codes*, Adv. Math. Commun.,
doi:10.3934/amc.2025010 [DP2025], was supplied lawfully by the Commander
(36 pp. publisher PDF; not committed to this repository, licence).

**Comparison (field case).** DP2025 Theorem 3.3 (their §3.1, \(n=n'p^\nu\),
\(\operatorname{ord}(\lambda)\mid 1+p^{e-k}\)) gives the average Galois
hull dimension over \(\mathbb{F}_q\) as
\(E_k = n - A\Delta_1 - B\sum_{t\ge2} a_t\Delta_t\) with
\(A=\frac{3P+1}{4}-\frac{\delta_P}{4(P+1)}\), \(B=\frac{P(4P+5)}{6(P+1)}\),
\(P=p^\nu\), \(\Delta_t\) the total degree of distinct factors in
reciprocal cycles of length \(a_t\) (\(\sum_t a_t\Delta_t=n'\)). Using
\(n=P n'\), \(P-B=\mu_P\) and \(P-A=\nu_P\), this is exactly
\(\nu_P\Delta_1+\mu_P\sum_{t\ge2}a_t\Delta_t\) — the single-component
case of the manuscript's Theorem 8.2/VIII.2 hull mean. Hence **the hull
mean is not new for a single field**; it is now credited in the
manuscript (remark after Theorem 8.2/VIII.2; Table 1 row [DP2025]).
Verified in exact rational arithmetic for \(P=1,\dots,9\) on 1800 random
\(\Delta\)-vectors, and on DP2025 Example 3.6 (\(23/4\), reproduced):
`code/validate_p1_45_dp2025_mean.py`,
`code/validation_p1_45_dp2025_mean_output.txt`. DP2025 contains **no**
variance or covariance formula, so Theorem 8.4/VIII.4 and Corollary
8.5/VIII.5 remain without counterpart there. Its §4 treats the auxiliary
ring \(R_{m,q}=\mathbb{F}_q[u]/(u^m-u)\) (Theorem 4.23 average), which is
outside the matched-hypotheses comparison made here.

**Wording caveat recorded.** As printed in the supplied text, §3.1 of
DP2025 describes the ensemble \(\mathcal{C}(n,q,\lambda)\) with adjacent
exponents in cycles of length \(\ge2\) taken unequal; however the
constant their Lemma 3.2 assigns to those edges,
\(\frac{P(4P+5)}{6(P+1)}\), equals the *unconditional* expectation of
\(\max(u,P-v)\) for independent uniform \(u,v\) (e.g. \(P=1\): \(3/4\),
whereas conditioning on \(u\ne v\) gives \(1/2\)). Their Theorem 3.3
formula therefore coincides with the uniform labeled-ensemble mean, as
verified above. The discrepancy is recorded without attributing intent;
no change to our manuscript arises from it.

**Gate status.** G1 remains **PARTIALLY RESOLVED**. Remaining novelty
uncertainty: theorem-level comparison against ES2026 and DIMP2026 is
still outstanding; whether the joint enumerator, second-order results
and product-of-fields assembly constitute a sufficient advance remains
an editorial/referee judgment. Novelty is not claimed to be fully
established; the paper has not been submitted.

## E. P1-46 update (23 Oct 2026) — DIMP2026 comparison (arXiv v1)

**Access and caveat.** The full text compared here is arXiv:2412.08512v1
(11 Dec 2024), *Galois hulls of constacyclic codes over affine algebra
rings* by Debnath–Islam–Martínez-Moro–Prakash, supplied lawfully by the
Commander (27 pp.; not committed to this repository). The manuscript
cites the published version, *Discrete Math.* 349(2) (2026), Art. 114750;
**publisher theorem numbering has not been verified against the arXiv
text**, so theorem numbers below are arXiv v1 numbers only.

**Setting.** Their alphabet \(A=\mathbb{F}_q[X_1,\dots,X_\ell]/\langle
t_1,\dots,t_\ell\rangle\) with square-free \(t_i\) is semisimple; via
primitive idempotents they project onto component codes
\(C_{S(\nu)}\subseteq\mathbb{F}_q^n\) over the **same** field
\(\mathbb{F}_q\) (\(\lambda_{S(\nu)}\in\mathbb{F}_q^*\)), indexed by
Frobenius-conjugacy classes \(S(\nu)\in\hat S\). This is the special case
\(K_s=\mathbb{F}_q\) (\(m_s=1\)) of the manuscript's product-of-fields
setting; our components are arbitrary finite fields \(K_s\) with
\(\dim_{\mathbb{F}_q}=m_s\dim_{K_s}\).

**Theorem-level comparison (arXiv v1 numbering).**

| DIMP2026 result | Relation to this manuscript |
|---|---|
| Theorem 7: hull generator \(\bigoplus_{S(\nu)}\mathrm{lcm}(g_{S(\nu)},h^\#_{S(\nu)})\) over \(A\) | Same componentwise lcm structure as our Theorem 5.2/V.2 for \(K_s=\mathbb{F}_q\); ours is in exponent form over arbitrary \(K_s\) and feeds the joint enumerator |
| Theorem 8: \(q\)-dimension of hull, \(n=n'p^{e'}\) (**repeated-root included**), \(\gcd(\mathrm{ord}\,\lambda,n')=1\), \(\mathrm{ord}(\lambda)\mid(1+p^{e-k})\); formula \(\sum_{S(\nu)}\sum_t\sum_j \mathrm{ord}_j(q)\,b^{S(\nu)}_{tj}\) | Exactly the sum over \(\mathbb{F}_q\)-components of DPI2023 Theorem 3 (their ref. [9]); agrees with our Theorem 5.2/V.2 restricted to \(K_s=\mathbb{F}_q\). Per-code hull dimension over an \(\mathbb{F}_q\)-component product is therefore **not new**; credited via the updated Introduction/Table 1 |
| Corollary 3.4 (\(\gcd(n,q)=1\)), Corollary 3.5 (cardinality of the set of *attainable* hull dimensions in two special cases), Theorem 9 (sufficient LCD criterion, \(\gcd(n,q)=1\)) | Attainable-value range/LCD *criteria*, not counts of codes. Our Corollaries 7.3–7.6 count labeled codes (LCD \(=2^{\#\mathrm{orbits}}\) etc.) — different objects |
| Theorem 10 + Gray map: EAQECCs from hull dimensions | Application layer; our conditional EAQECC remark is analogous in kind, not compared parameter-by-parameter |

**Absent from DIMP2026 (verified):** any counting or enumeration of
codes by hull dimension — their conclusion (p. 26) states this
enumeration over \(A\) is **still open**; the joint
\((\dim C,\dim\mathrm{Hull})\) distribution; transfer-matrix formulas;
moments (mean/variance/covariance); component fields beyond
\(\mathbb{F}_q\) with \([\,K_s:\mathbb{F}_q\,]\) scaling; per-component
compatibility in place of the global
\(\gcd(\mathrm{ord}\,\lambda,n')=1\) hypothesis.

**Status.** G1 remains **PARTIALLY RESOLVED**. ES2026 (Eldin–Solé) is now
the only closest-work item without a theorem-level comparison; the
publisher-vs-arXiv numbering caveat for DIMP2026 also remains. Whether
the remaining package (joint enumerator, second-order results,
extension-field assembly) is a sufficient advance remains an
editorial/referee judgment. Novelty is not claimed to be fully
established; the paper has not been submitted.

## F. P1-47 update (23 Oct 2026) — ES2026 comparison (arXiv v1)

**Access and caveat.** Eldin–Solé, *Generator polynomial matrices of the
Galois hulls of multi-twisted codes*, arXiv:2305.15237v1 (24 May 2023),
was read in full lawfully via the arXiv HTML full text (the Commander did
not hold a PDF; arXiv is the authors' open-access version of record for
this comparison). The manuscript cites the published version, *Finite
Fields Appl.* 109 (2026), Art. 102712; **publisher theorem numbering has
not been verified against the arXiv text**, so numbers below are arXiv v1
numbers only.

**Setting.** Multi-twisted (MT) codes over a **single** finite field
\(\mathbb{F}_{p^e}\): index \(\ell\), block lengths \(m_j\), shift
constants \(\lambda_j\), viewed as free modules over the PID
\(\mathbb{F}_q[x]\); constacyclic codes are the index-one case. No
hypothesis \(\gcd(m_j,p)=1\) is imposed (the PID method also covers
repeated-root moduli). The hull is MT under the compatibility condition
\(\Lambda^{-p^{-\kappa}}=\Lambda\), i.e.
\(\lambda_j^{-p^{e-\kappa}}=\lambda_j\) for all \(j\) — the same condition
as our per-component \(\lambda_s^{1+p^{d_s-k}}=1\) at index one.

**Theorem-level comparison (arXiv v1 numbering).**

| ES2026 result | Relation to this manuscript |
|---|---|
| Theorem 10: GPM \(\mathbf{H}_\kappa\) for the Galois dual of an MT code; Corollary 11: hull is MT under compatibility | Per-code dual/hull machinery for a *given* code. At index one this yields a generator (one generator polynomial) for dual/hull of a given constacyclic code, consistent in content with our Theorems 4.3/5.2 but in GPM/Hermite-normal-form form, not exponent form |
| Theorem 21: \(\dim\mathcal{Q}_{\mathbf{G}}=\dim\mathcal{C}-\dim h_\kappa(\mathcal{C})\), with \(\dim\mathcal{Q}_{\mathbf{G}}\) computable from the determinantal divisors of \(\mathfrak{B}_{\mathbf{G}}\); Corollary 22 (self-orthogonal iff \(\mathfrak{B}_{\mathbf{G}}=\mathbf{0}\)); Corollary 26 (LCD criterion); Theorems 25/28: GPM for \(h_\kappa(\mathcal{C})\) | A hull-*dimension formula for a given code* via an associated quasi-cyclic code and determinantal divisors. No closed exponent formula along reciprocal orbits, and no product over components/fields |
| (whole paper) | **Absent (verified):** counting or enumeration of codes by hull dimension; any distribution over a family of assignments; joint \((\dim C,\dim\mathrm{Hull})\) laws; moments (mean/variance/covariance); products of finite fields with \([K_s:\mathbb{F}_q]\) dimension scaling. Their examples are individual optimal/MDS codes, not enumerations |

**Status.** With §§C–F, all four closest works in Table 1 have now been
compared at theorem level from lawfully read full texts (DPI2023, DP2025:
publisher full texts supplied by the Commander; DIMP2026, ES2026: arXiv
v1, publisher numbering unverified). The per-code hull formula
(DPI2023 Thm. 3; DIMP2026 Thm. 8 over \(\mathbb{F}_q\)-components;
ES2026 GPM machinery at index one) and the single-field hull mean
(DP2025 Thm. 3.3) are prior art and are credited as such. No counterpart
has been found in these texts for: the joint code–hull enumerator as a
product of transfer-matrix traces over arbitrary reciprocal-orbit
lengths; the labeled LCD/self-orthogonal/dual-containing counts over a
product of finite fields; or the second-order results (Theorem 8.4,
Corollary 8.5). G1 nevertheless remains **PARTIALLY RESOLVED**: the
comparison covers the identified closest literature, not all literature;
publisher numberings for DIMP2026/ES2026 are unverified; and whether the
remaining package constitutes a sufficient advance is an
editorial/referee judgment. Novelty is not claimed to be fully
established, and the paper has not been submitted.
