# AUDIT_EDITOR.md — desk review (handling-editor view)

Manuscript: *The joint code–hull distribution of repeated-root constacyclic
codes over finite products of finite fields via transfer matrices*.
Target: IEEE Transactions on Information Theory, single-column review format.

## 1. Scope and fit

Repeated-root constacyclic codes, Galois (Frobenius-twisted) duality, hull
dimension, and exact enumeration of the joint (code dimension, hull dimension)
distribution. This is squarely within TIT's coding-theory remit; the paper is a
counting/enumeration contribution with an exact algebraic engine, not a
constructions-with-parameters paper. Length is appropriate for a full paper.

## 2. What the paper actually claims (and what it explicitly disclaims)

The introduction is unusually disciplined: the per-code hull-dimension formula
(single field) is attributed to Debnath–Prakash–Islam 2023 [DPI2023], the
average hull dimension to Debnath–Prakash 2025 [DP2025], small-hull
classification to [DIYP2026], and the componentwise ring setting to
[DIMP2026]. The novelty claim is confined to **joint** enumeration by two
dimensions, for unrestricted orbit length, over a product of fields, with exact
first and second moments. That is a defensible claim and it is stated at the
right strength.

One overclaim was found and repaired: the moments section inferred "the typical
code of the family has a hull growing linearly with n" from a mean alone. Mean
behaviour does not license a typical-code statement without concentration. The
sentence now states the mean, and contrasts it with the random-linear-code
behaviour (Sendrier) as a mean-versus-typical comparison. See
`CHANGELOG_MINIMAL.md` item 6.

## 3. Presentation and production

* Abstract: accurate, self-contained, no unsupported priority claim.
* Notation: heavy but consistent; the code-first pairing convention is stated
  once and its consequences (predecessor index `alpha_{i-1}`) are flagged in
  both the theorem chain and the limitations section.
* Limitations section: present, specific, and honest (labeled assignments only,
  compatible twists only, no distances, reduced alphabets only).
* Bibliography: 23 entries, every one cited, no uncited entries, all citation
  keys resolve.
* Terminology defect found: `tau_s` was called an "involution" in five places
  while Definition 3.2 itself correctly calls it a permutation. It is genuinely
  not an involution — an orbit of length 6 occurs (F_8, k=0, n0=7, verified in
  `VALIDATION_REPORT.md` §5). Repaired; the three remaining uses of
  "involution" all refer to `alpha -> P - alpha`, which is an involution.

## 4. Compliance status

The source is IEEEtran `journal` class, one column, `draftclsnofoot`, which is
the correct review-mode configuration for TIT. The current official IEEE TIT
author instructions could **not** be retrieved from this sandbox (no route to
ieee.org), so page limits for the final version, the required
"Manuscript received" footnote, ORCID/funding footnote form, and the current
reference-style rules are recorded as **UNVERIFIED** in
`SUBMISSION_CHECKLIST.md` rather than asserted. Nothing was changed on the basis
of an unverified rule.

## 5. Verdict

**Major revision — completed in house.** The scientific content survives
audit; two wording defects (mean/typical inference; `tau_s` called an
involution) were material to accuracy and are fixed. Production acceptance is
blocked by one non-scientific item only: no PDF could be built in this
environment. See `REMAINING_RISKS.md`.
