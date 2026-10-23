# P1-40 — Final PDF Proofreading Record and IEEE Submission Checklist

**Date:** 22 October 2026. **Manuscript source commit:** `3e4f87f` (package
commit `eb90a79`). **Compiled files:** `compiled/P1_15_MANUSCRIPT_DRAFT.pdf`
(17 pages, pdfTeX-1.40.28, SHA-256 `db8319853b7332af63a807f28aeafd37f43116976fdfd5fd4bb39f3968787549`)
and the matching `.log` (0 errors, 0 undefined references/citations).

## 1. Visual proofreading (all 17 pages inspected page-by-page)

- p.1: title, author (Arun Kumar Yadav; School of Basic and Applied
  Sciences, K.R. Mangalam University, Gurugram; arunyadav0307@gmail.com),
  abstract (~161 words), keywords and MSC render correctly.
- pp.1–3: Introduction, new P1-39 citations [1], [2], [6], [11], [16]–[18]
  and Table 1 (positioning) render cleanly inside the margins.
- pp.3–10: Sections 2–8, theorem/lemma environments, displays and proofs
  are clean; the Corollary 6.4 display and Lemma 8.3 items stay on-page.
- p.11: Theorem 8.4 and Corollary 8.5 (variance formula; Cov = 0;
  "uncorrelated (they need not be independent)") render correctly.
- pp.12–14: Examples 9.1–9.6, the split two-row tuple display of
  Example 9.1, the breakable joint-distribution list of Example 9.4, and
  Table 2 (ten EAQECC rows) all render inside the margins.
- pp.15–17: Limitations/quantum remark, conclusion (no novelty claim),
  and all 25 references render correctly; the seven P1-39 entries appear
  as [1], [2], [6], [11], [16], [17], [18] with the verified metadata.
- Overfull boxes after the layout fix are at most about 60pt and stay
  within the printed page area; the two off-page overflows (271pt,
  1599pt) were fixed in commit `3e4f87f`. No genuine visible layout
  problem remains; no source change was needed in P1-40, so the ZIP and
  manifest are unchanged.

## 2. Target journal and current requirements (checked 22 Oct 2026)

**Recommended target: IEEE Transactions on Information Theory** — the
paper's enumerative algebraic coding-theory content matches the
Transactions' coding-theory scope, and several directly related hull
papers (relative hulls; hull mass formulas) appeared there in 2024–2025.

Requirements from the IEEE Information Theory Society "Information for
Authors" (itsoc.org/it-trans/author-info) and the May-2025 page-limit
notice:

- [ ] Submit via the IEEE Author Portal for the journal
      (`ieee.atyponrex.com/journal/t-it`); PDF only for review.
- [ ] **Single-column version required for review**; from 1 May 2025 the
      submission must comply with the **50-page IEEE Transactions
      single-column limit** (current paper: 17 pages in article class —
      convert with the IEEE Template Selector single-column Transactions
      template and re-check the count).
- [ ] Final two-column version limited to **25 pages** (conversion of the
      present paper is expected to be well below this; verify after
      conversion).
- [ ] Abstract: at most 250 words, one paragraph, self-contained, no
      displayed equations/tables/references (current ~161 words — OK;
      re-check after template conversion).
- [ ] Index terms: 5–10 keywords after the abstract (current draft lists
      6 topics plus an MSC line — replace with IEEE Index Terms, ideally
      from the IEEE Thesaurus, and drop/relocate the MSC line as the
      template requires).
- [x] **ORCID is mandatory for all authors** at submission — author-supplied
      ORCID iD 0009-0009-1169-3264 added to the manuscript (23 Oct 2026;
      checksum-valid and the public record name matches the author).
- [ ] References in IEEE numbered style, cited in order of appearance
      (already satisfied; DOIs included).
- [ ] Hybrid journal: Open Access is optional (OA fee US$1,750 if chosen
      and accepted); traditional submission remains available. Any
      page/color charges are confirmed at acceptance — do not prepay or
      assume them.
- [ ] The Society encourages posting the submitted paper on arXiv at the
      time of submission (author decision; disclose any prior posting in
      the portal).
- [ ] On acceptance, be ready to supply: figure/table originals (tables
      are native LaTeX — fine), a biographical sketch and photo (IEEE
      biography format), and the signed IEEE copyright form.

## 3. Submission-package checklist (author to complete; nothing invented)

- [ ] IEEEtran conversion of the manuscript (single-column for review),
      recompiled and re-proofread; keep the present 17-page PDF as the
      reading copy until conversion is verified.
- [ ] Cover letter: title; single author and affiliation as in the
      manuscript; corresponding-author e-mail; statement that the work
      is original and not under consideration elsewhere (author must
      confirm this is true before signing); note that validation code
      accompanies the submission (see below).
- [ ] Author metadata in the portal: full name, affiliation, e-mail,
      ORCID iD; confirm single-author status and corresponding-author
      designation.
- [ ] Declarations to confirm truthfully at submission: funding (state
      only if applicable), conflicts of interest, author contributions
      (single author), and any prior dissemination.
- [ ] Code/data availability statement (suggested wording, with the link
      to be filled by the author): "The validation scripts and saved
      outputs accompanying this paper (`validate_p1_14.py`,
      `validate_p1_20.py`, `validate_code_table.py`,
      `validate_audit_fixes.py`) are available at [repository URL /
      DOI to be supplied by the author]." Do not state a DOI that does
      not exist; if a persistent archive is wanted, mint one (e.g.
      Zenodo) before submission.
- [ ] Gate G1 remains **DEFERRED**: the manuscript makes no novelty or
      priority claim, and the introduction already fences the comparison
      with the 2023 paper to abstract level. Keep that wording; do not
      strengthen claims in the cover letter.
- [ ] Final author visual proofread of the IEEE-formatted PDF before
      pressing "submit" (this checklist does not submit anything).
