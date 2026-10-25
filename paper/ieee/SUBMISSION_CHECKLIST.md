# IEEE submission package — format compliance and checklist

Target journal: **IEEE Transactions on Information Theory** (regular paper).
Files are in this folder; the manuscript body is shared, so both versions are
always identical in content.

| file | purpose |
|---|---|
| `main.tex` | **two-column** IEEEtran journal version (camera-ready style) |
| `main_peerreview.tex` | **single-column, double-spaced** peer-review version (submission) |
| `body.tex` | the manuscript body, `\input` by both wrappers |
| `references.bib` | 31 entries — exactly the cited ones, IEEEtran style |
| `figures/` | three vector PDF figures, referenced by both versions |
| `supplementary/` | the Python code and all generated data (zip this) |
| `build.sh` | builds both PDFs |

```bash
cd paper/ieee && ./build.sh      # needs texlive-publishers (IEEEtran)
```

---

## 1. Managed quantities (measured on the files as they stand)

| item | requirement | this paper |
|---|---|---|
| Abstract length | ≤ **200 words** (IEEE Trans. IT) | **192 words** |
| Index terms | 3–6, alphabetized | **5**: constacyclic codes, Galois hulls, LCD codes, repeated-root codes, transfer matrices |
| References | no fixed cap; typically 25–45 for a Trans. IT regular paper | **31**, all cited, no uncited entries in the bib |
| Figures | vector, called out in text | **3** (all PDF, numbered in order, captions below) |
| Tables | captions above | **2** (both `table*`, spanning both columns, `\scriptsize`) |
| Displayed equations | numbered sequentially (IEEE style) | **93** |
| Numbered results | — | **3** theorems, **12** lemmas, **15** propositions, **6** corollaries, **2** definitions, **8** examples, **8** remarks; **34** proven claims |
| Sections | — | **7** sections, 22 subsections |
| Body length | — | 12.3k words, 3 figures, 2 tables |
| Estimated printed length | — | **≈14–16 two-column pages**; ≈38–45 pages in the double-spaced peer-review format |

These are estimates: the sandbox has no TeX installation, so **the page count
must be read off the compiled PDF**. If the Associate Editor asks for a shorter
paper, use §5 below — no theorem has to be dropped.

## 2. Formatting rules already applied

* `\documentclass[journal]{IEEEtran}` — IEEE two-column journal layout, Times,
  10 pt, US Letter, automatic running heads, IEEE equation/section numbering.
* Peer-review variant: `\documentclass[journal,peerreview]{IEEEtran}` with
  `\IEEEpeerreviewmaketitle` (single column, double spaced, wide margins).
  *If your local `IEEEtran.cls` is older and does not know
  `\IEEEpeerreviewmaketitle`, replace it with `\maketitle` — everything else
  stays the same.*
* Title/author block: `\author{...}` with seven `\thanks` footnotes
  (dates, funding, one affiliation per author, corresponding author, ORCID,
  supplementary-material note) — the IEEE pattern.
* `abstract` environment + `IEEEkeywords` environment (IEEE "Index Terms").
* Figures: PDF, captions **below**, `figure*` for the full-width pipeline
  figure, `\linewidth` widths so both versions scale correctly.
* Tables: captions **above**, `booktabs` rules, `table*`, `\scriptsize`,
  2.5 pt column separation; the two very long decimal expansions were replaced
  by `3^{31}` and `5^{31}` (their decimal expansions are written out in the
  `F_{32}` example) so the table cannot overflow.
* Widest displays (7 of the 93) are set in `\small` so that they fit a
  3.5 in column.
* Bibliography: `\bibliographystyle{IEEEtran}` + `\bibliography{references}`,
  numbered by citation order, DOI field kept where available.
* Elsevier-only matter (CRediT, competing interests, data-availability,
  generative-AI declaration, MSC codes) was removed; a single IEEE
  **Acknowledgment** replaces it and points to the supplementary code.

## 3. Fill these in before uploading (search for `XXXX`)

1. `\thanks` #1 — manuscript received / revised / accepted / publication dates.
2. `\thanks` #2–#5 — e-mail addresses of V. Gupta, P. Soni, M. Pruthi
   (currently `\texttt{XXXX}`), and confirm the corresponding author.
3. Funding sentence — currently "This work received no external funding."
4. If you have a grant, add it to `\thanks` #1 (IEEE requires the grant number).
5. Final-version only (not at submission): IEEE author biographies and photos,
   plus the manuscript ID / DOI footnotes from the editorial office.

## 4. Submission package (what to upload)

```
main_peerreview.pdf      <- manuscript (peer-review format)
figures/*.pdf            <- 3 figures (usually also embedded; upload anyway)
references.bib           <- optional, for the editorial system
supplementary.zip        <- contents of supplementary/ :
                            enumerator.py, checks.py, generate_tables.py,
                            checks_output.txt, summary_families.csv,
                            joint_*.csv           (11 files)
```

`checks_output.txt` is the complete verification log: it reproduces every row of
Table I, both worked joint tables, the conditional means quoted in the examples,
and the finite-field Gram-matrix checks of Table II.

## 5. If a shorter paper is requested (no result is lost)

Move, in this order, to the supplementary material and replace each by one
sentence in the main text:

1. The examples on `F_4 × F_16`, `F_25` and `F_32` (labels `ex:mixed`,
   `ex:char35`, `ex:F32`) and **Table I** → supplementary;
   keep Table II (the exhaustively verified families) in the paper.  Saves
   ≈2 pages.
2. **Subsection "Short orbits"** (proposition `prop:short-orbits` and its
   example `ex:a2M2`) → supplementary;
   the closed forms are quoted once in the moments section.  Saves ≈1 page.
3. **Section VII-A** (computing the orbit data, `sec:orbit-data`) → compress
   to a paragraph;
   the algorithm and its complexity (`sec:dp`, `prop:complexity`) stay.
   Saves ≈0.7 page.
4. Only if still too long: print the 8 remarks in `\small` or fold three of the
   shortest ones into footnotes.  Saves ≈0.5 page.

## 6. If you decide to send it to a different IEEE venue

| venue | what changes |
|---|---|
| **IEEE Trans. Inform. Theory** (default here) | as delivered |
| **IEEE Trans. Communications / Trans. IT "Correspondence"** | abstract ≤ 150 words, ≤ 5 printed pages → the paper does not fit; would need the theory part only (Theorem 1, support theorem, moments) |
| **IEEE Communications Letters** | 5 printed pages, abstract ≤ 100 words → not suitable for this paper |
| **IEEE Access** | abstract 150–250 words, no `IEEEkeywords` limit but keep 5; **re-add** the section headings `AUTHOR CONTRIBUTIONS`, `FUNDING`, `CONFLICTS OF INTEREST`, `DATA AVAILABILITY` (the Elsevier-style declarations removed from this version), article-processing charge applies |

For IEEE Access, the declarations can be taken verbatim from
`../main.tex` (CRediT statement, funding, competing interest, data
availability, AI-use declaration).

## 7. Final self-check before pressing submit

- [ ] `./build.sh` runs without errors; no "??" citations, no undefined references.
- [ ] Abstract is 192 words (already under the 200-word limit).
- [ ] Index terms alphabetized (they are).
- [ ] Every figure/table is called out in the text (`Fig. 1–3`, `Table I–II`).
- [ ] Page count of `main.pdf` noted in the cover letter.
- [ ] `XXXX` placeholders all replaced.
- [ ] Supplementary zip opens and `python3 checks.py` prints `ALL CHECKS PASSED`.
- [ ] ORCID linked in the IEEE author portal (A. K. Yadav: 0009-0009-1169-3264).
