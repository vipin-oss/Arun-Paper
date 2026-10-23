# P1-19 — L1 Closure Report: What Can and Cannot Be Established About Overlap

**Paper at issue:** Indibar Debnath, Om Prakash & Habibul Islam, “Galois hulls of constacyclic codes over finite fields”, *Cryptography and Communications* 15(1), 111–127 (2023), DOI `10.1007/s12095-022-00591-6`; correction DOI `10.1007/s12095-022-00602-6`, 15, 129–130.
**Manuscript comparator:** the joint labeled enumerator for `(dim_{F_q} C, dim_{F_q} Hull_k(C))` over a square-free affine product (T1–T6, C1–C6), frozen blueprint SHA-256 `ec2fd8d58f8d2a986314f83997d750d689f7c88e98ec8f87753ab4c9cf438cff` (unchanged).
**Outcome in one line:** No lawful full text of L1 became available, no contact or reply is evidenced, and therefore **no L1-Q question can be upgraded from unresolved**. This report closes the *acquisition loop* rigorously at abstract level; it does not close Gate G1 and it establishes neither overlap nor non-overlap.

Status vocabulary used below: **confirmed** = inspected text proves it; **partial** = inspected text proves a narrower related fact; **not established** = the inspected evidence does not establish the stated overlap (which is not proof of absence); **unresolved** = the deciding evidence has not been inspected. Numbering follows the latest checklist in P1-10/P1-11 (Q4 = `B_i` bookkeeping, Q6 = affine scope); P1-09 used a different Q4/Q6 order for the same two questions.

---

## 1. Access routes: what was attempted in P1-19, and the outcome

Consistent with the instruction not to repeat exhausted searches, P1-19 performed **documentary and workspace checks for newly supplied evidence**, not another round of web hunting.

| Route | Exact P1-19 check | Outcome |
|---|---|---|
| Researcher-supplied copy in the repository/workspace | Repository was synchronized and clean at `f372f26`; filename search over `/home/user` for the DOI, article title, and author-name combinations; content search for the DOI string. | No supplied L1 copy. DOI hits occur only in the project’s own literature/audit/manuscript files. |
| Bundles already in the repo root | Inspected the entry lists of `Galios-Hull-Complete-Work-2026-10-20.zip` (169 entries) and `Galios-Hull-Submission-Phase10F.zip` (110 entries); opened the embedded `source-paper` PDFs only far enough to identify them. | No L1-looking filename. The embedded source paper is arXiv:2412.08512 (Debnath–Islam–Martínez-Moro–Prakash, affine algebra rings), i.e. repo L4 — not L1. |
| Prepared author/ILL drafts (P1-11) | Re-read `P1_11_L1_ACQUISITION_HANDOFF.md` and the worklog. | Both drafts are still marked **NOT SENT**; the acquisition-record table is empty; there is no documented sending, receipt, or reply. Arena sent nothing and claims no contact. |
| Institutional subscription / ILL | Not executable by Arena: no institutional credential exists in this workspace, and using the researcher’s would be the researcher’s own action. | Remains available only as a researcher action ( §5). Arena does not claim to have attempted it. |
| Legitimate repository copy | Not re-searched in P1-19: OpenAlex, Semantic Scholar, Unpaywall, arXiv and targeted web searches were already exhausted in P1-09/P1-10 with closed-access results. | No repository copy is known; no new copy surfaced in the workspace checks above. |
| Publisher / correction | Not repeated: Springer main article is closed (abstract/metadata only); the correction was lawfully read in full earlier. | The correction is a 2-page editorial notice, not the paper; its displayed `B_i` definitions do not settle scope. |

**Precise conclusion:** as of this report, the project still has **no lawful theorem-bearing copy of L1**, and there is **no evidence that any prepared request was sent or answered**. Any statement beyond that would be fabrication.

## 2. What is actually verified about L1 (abstract level only)

Verified from records inspected in P1-01…P1-10 and reaffirmed here without new inference:

1. Bibliographic identity: authors, journal, volume/pages/year, both DOIs, zbMATH/OpenAlex/Semantic Scholar/DBLP identifiers (see P1-10 §2).
2. The abstract announces: a formula for the dimension of Galois hulls of constacyclic codes, arranging the irreducible factors of `xⁿ − λ` over `F_q` “in a suitable way”; and, “considering some restrictions on q”, a count — corroborated at second hand by repo L4’s introduction (“they also counted the number of constacyclic codes of a given Galois hull dimension”).
3. The correction exists and is editorial as displayed; it shows `B_i`-style factor-set bookkeeping without settling the paper’s scope.
4. Access status in every checked index: closed, with no repository full text (OpenAlex `any_repository_has_fulltext = false`; Semantic Scholar `isOpenAccess = false`; Unpaywall `has_repository_copy = false`).

**Nothing else is verified.** No theorem statement, hypothesis, proof, definition context, or body page of L1 has been read by this project. In particular, the abstract phrase “considering some restrictions on q” has never been expanded into assumptions on `q`, `n`, `λ`, or the Galois index, and must not be.

## 3. The manuscript side of the comparison (what would have to be matched)

For the extraction that a future full text must perform, the manuscript’s claims decompose as follows (frozen statements; § references to the current draft):

- **K1/finite-field hull formula:** Theorem 5.2 specialized to one field component: hull generator exponents `max(αᵢ, P − α_{i−1})` and edge sum with `min(P−αᵢ, α_{i−1})`, under compatibility and the code-first pairing.
- **K2/joint enumerator:** Theorem 6.3 — a **joint**, **labeled** count by `(dim C, dim Hull)` as a product over components and `τ`-orbits; not a marginal by hull dimension alone.
- **K3/transfer mechanism:** Theorem 6.1 — per-orbit trace `tr(T^{(P)}_{w_O}(u,z)^{L_O})`.
- **K4/counts:** Corollary 7.3 (LCD count `2^{#orbits}`) and Corollary 7.4 (self-orthogonal/dual-containing edge criteria and closed-walk counts).
- **K5–K6/moments:** Theorems 8.2/8.4 — means with the `L=1` constant `ν_P` separated, and variance `Σ w_O² V_{L_O}(P)` with `L=1/L=2/L≥3` regimes.
- **Affine assembly:** Proposition 6.2 — product over the labeled fields `K_s`; on its face outside a finite-field-only paper, but that scope statement is title/abstract-level until the text is read.

## 4. L1-Q1–Q6: evidence needed, evidence obtained, status, effect

### L1-Q1 — Length scope: does L1 allow `p | n`, or assume `gcd(n,p)=1`?
- **Evidence needed:** the setup/hypotheses of L1’s hull and counting theorems (any condition on `n`, `q`, `λ`, the Galois index; the meaning of “restrictions on q”).
- **Evidence obtained:** abstract only; no hypothesis text inspected.
- **Status:** **unresolved**.
- **Effect on the manuscript:** the repeated-root (`P>1`) finite-field specialization of Theorem 5.2 cannot yet be positioned against L1. This blocks any statement that the finite-field repeated-root hull formula is absent from L1. It does not affect the manuscript’s correctness.

### L1-Q2 — Is L1’s hull-dimension formula the same edge-sum as our T4 specialization?
- **Evidence needed:** L1’s exact hull-dimension theorem with hypotheses and pairing convention (code-first vs candidate-first changes the predecessor/successor form), compared term-by-term with `max(αᵢ, P − α_{i−1})` / `min(P−αᵢ, α_{i−1})`.
- **Evidence obtained:** abstract-level fact that *a* Galois hull-dimension formula is presented (a narrower topical fact only).
- **Status:** **unresolved** (topical overlap is partial at the level “a formula exists”; equivalence is not established).
- **Effect:** K1 must continue to be treated as potentially pre-occupied in finite fields; the manuscript already makes no priority statement for it, so no text change is required or permitted on present evidence.

### L1-Q3 — Is L1’s count marginal (hull dimension only) or joint in `(dim C, dim Hull)`; labeled codes or dimension values?
- **Evidence needed:** L1’s counting theorem statement and the definition of what is being counted.
- **Evidence obtained:** abstract announces a count of constacyclic codes by given Galois hull dimension (wording corroborated by L4’s introduction); nothing about a joint variable, labeled-vs-value counting, or a generating function.
- **Status:** **unresolved**. Specifically: a marginal hull-dimension count is *announced*; a joint `(dim C, dim Hull)` enumerator is **not established** — and its absence is equally not established.
- **Effect:** this is the highest-risk unknown for K2. The manuscript may truthfully say it *proves* a joint labeled enumerator (a statement about its own contents); it may not say or imply that L1 does not contain one.

### L1-Q4 — How do L1’s `B_i` sets relate to our `τ`-orbits and predecessor indexing?
- **Evidence needed:** the definitions surrounding the `B_i` sets in L1’s body, in the context the correction points to, mapped against `τ_s`-orbits of the irreducible factors.
- **Evidence obtained:** `B_i`-style displayed definitions in the correction only, without the paper’s definitions or theorems.
- **Status:** **unresolved**.
- **Effect:** whether C3/C4-type counts (LCD `2^{#orbits}`, edge criteria) could already be implicit in L1’s bookkeeping is unknown; no positioning of K4 against L1 is currently possible beyond the abstract.

### L1-Q5 — Does L1 contain mean/variance results?
- **Evidence needed:** a full-text check for expectation/variance statements (to be done on the text itself, not inferred).
- **Evidence obtained:** no moment result is visible at abstract level; repo L2 is the separately verified average-dimension paper.
- **Status:** **unresolved** (absence is not asserted).
- **Effect:** C5’s mean already cannot be a headline because of L2; C6’s variance positioning against L1 specifically remains open. No manuscript claim currently depends on L1 lacking moments.

### L1-Q6 — Finite fields only, or any product/affine assembly?
- **Evidence needed:** L1’s stated scope (title/abstract indicate finite fields; theorem-level scope requires the text).
- **Evidence obtained:** title and abstract are finite-field; no product/ring assembly is announced.
- **Status:** **not established** — an affine/product overlap is not established by any inspected evidence; equating that with a verified theorem-level exclusion would overstate title-level information.
- **Effect:** the affine-product assembly (Proposition 6.2, and with it the multi-component part of K2) remains the strongest separator **in the verified record**, phrased exactly that way — as a property of the inspected record, not as a fact about L1’s unread text.

**Summary of §4:** no question is *confirmed*; Q2 has a partial topical component at abstract level; Q6 is *not established* for affine overlap; Q1, Q3, Q4, Q5 (and the equivalence part of Q2) are **unresolved**. Neither “L1 duplicates the enumerator” nor “L1 does not overlap” is an available conclusion.

## 5. Overlap matrix, novelty wording, and Gate G1

- **Overlap matrix (`P1_09_OVERLAP_MATRIX.md`): no cell is changed.** Every L1 entry remains “?”: with zero new theorem-level evidence, editing a cell in either direction would be unsupported. The per-question disposition is recorded in §4 of this report instead, and the matrix should only be edited when a lawful text is extracted.
- **Novelty wording: unchanged.** The manuscript contains no novelty or priority claim (checked again in P1-17/P1-18), and its only L1 sentence stays strictly within the abstract (“determined the Galois hull dimension of constacyclic codes and the number of such codes with a given Galois hull dimension”). The safest internal wording remains the P1-09 §4.1 statement (“In the sources we have been able to inspect … we have not found …; we make no priority claim relative to that paper”). It must not be strengthened into “first”, “new”, or “no prior work”.
- **Gate G1: DEFER (unchanged).** The blocking item is unchanged and singular: a lawful theorem-bearing copy of L1. Correctness of the frozen core is unaffected; what remains gated is literature positioning and any novelty framing.

## 6. The one concrete next action (requires new evidence)

All workspace-side and index-side routes recorded in P1-09…P1-12 are exhausted, and re-running them would manufacture activity, not evidence. The single concrete step that can change the state is researcher-side and already prepared: **the researcher sends the P1-11 Draft 1B request through Dr. Habibul Islam (co-author/advisor) — or Draft 1 to the corresponding author, or files Draft 2 (ILL) — and places any lawfully received copy (or a dated note of the reply) into the workspace.** When that evidence exists, the follow-up work is mechanical and already specified: provenance record, theorem-level extraction with page/theorem references answering L1-Q1–Q6, overlap-matrix update, and only then a Gate-G1 re-vote. Until it exists, the correct action is to leave L1 marked unresolved and make no further acquisition rounds.

## 7. Files changed by this phase

- Created: `P1_19_L1_CLOSURE_REPORT.md` (this report; a PDF rendering accompanies it for reading).
- Updated: `04_BLUEPRINT_GAP_REGISTER.md`, `ARENA_WORKLOG.md` (P1-19 outcome lines).
- Deliberately unchanged: `P1_09_OVERLAP_MATRIX.md` (no supported cell change), the manuscript, the frozen blueprint (SHA-256 re-verified `ec2fd8d5…cf438cff`), proof packages, and the P1-11 drafts (still **NOT SENT**).
