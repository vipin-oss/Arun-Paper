#!/usr/bin/env python3
"""Minimal Markdown -> PDF converter for project deliverables.

Usage: python3 code/md_to_pdf.py INPUT.md OUTPUT.pdf

Uses only fpdf2 + system DejaVu fonts (full Unicode/math coverage).
Rendering only: the .md source is never modified. Math asterisks are
protected as U+2217 so fpdf's markdown italics do not mangle them.
"""
import re
import sys

from fpdf import FPDF

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
STAR = "\u2217"  # asterisk operator, for math stars


class PDF(FPDF):
    def footer(self):
        self.set_y(-12)
        self.set_font("dejavu", "", 7)
        self.set_text_color(120, 120, 120)
        self.cell(0, 8, f"Page {self.page_no()}/{{nb}}", align="C")


def clean_inline(text: str) -> str:
    # code spans: literal content, protect stars inside
    def _code(m):
        return m.group(1).replace("*", STAR)

    text = re.sub(r"`([^`]*)`", _code, text)
    # hide bold markers while single stars are being protected
    text = text.replace("**", "\uE000")
    # math stars attached to symbols: K*, h^*, (phi)^*, x* ...
    text = re.sub(r"(?<=[\w^\)\]\}])\*", STAR, text)
    text = re.sub(r"\*(?=\s*\u2208)", STAR, text)  # stray '*)' cases
    # any remaining isolated star not forming an *italic* pair -> operator;
    # valid italic pairs are copied through untouched for fpdf markdown
    out, i = [], 0
    while i < len(text):
        if text[i] == "*":
            j = text.find("*", i + 1)
            seg = text[i + 1 : j] if j != -1 else ""
            if (j != -1 and seg and len(seg) < 120 and "\n" not in seg
                    and not any(c in seg for c in "^_`")):
                out.append("__" + seg + "__")  # fpdf2 italics marker
                i = j + 1
            else:
                out.append(STAR)
                i += 1
        else:
            out.append(text[i])
            i += 1
    return "".join(out).replace("\uE000", "**")


def is_table_row(line: str) -> bool:
    s = line.strip()
    return s.startswith("|") and s.endswith("|") and s.count("|") >= 2


def table_cells(line: str):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def main() -> None:
    src, dst = sys.argv[1], sys.argv[2]
    lines = open(src, encoding="utf-8").read().splitlines()

    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.set_margins(18, 16, 18)
    pdf.set_auto_page_break(True, margin=16)
    pdf.add_font("dejavu", "", f"{FONT_DIR}/DejaVuSans.ttf")
    pdf.add_font("dejavu", "B", f"{FONT_DIR}/DejaVuSans-Bold.ttf")
    pdf.add_font("dejavu", "I", f"{FONT_DIR}/DejaVuSans.ttf")  # faux italic
    pdf.add_font("dejavu", "BI", f"{FONT_DIR}/DejaVuSans-Bold.ttf")
    pdf.add_font("mono", "", f"{FONT_DIR}/DejaVuSansMono.ttf")
    pdf.add_font("mono", "B", f"{FONT_DIR}/DejaVuSansMono-Bold.ttf")
    pdf.add_page()

    def body(text, size=9.5, height=4.9, font="dejavu", style="", indent=0):
        pdf.set_x(pdf.l_margin + indent)
        pdf.set_font(font, style, size)
        pdf.set_text_color(20, 20, 20)
        pdf.multi_cell(0, height, text, markdown=(font == "dejavu"),
                       new_x="LMARGIN", new_y="NEXT")

    i = 0
    para = []

    def flush_para():
        if para:
            body(clean_inline(" ".join(s.strip() for s in para)))
            pdf.ln(1.6)
            para.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # code fence
        if stripped.startswith("```"):
            flush_para()
            block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            i += 1
            pdf.set_fill_color(242, 242, 242)
            pdf.set_x(pdf.l_margin)
            pdf.set_font("mono", "", 7.6)
            pdf.multi_cell(0, 4.2, "\n".join(block), fill=True,
                           new_x="LMARGIN", new_y="NEXT")
            pdf.ln(2)
            continue

        # heading
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush_para()
            level = len(m.group(1))
            title = clean_inline(m.group(2).replace("**", "")).replace("__", "")
            sizes = {1: 15, 2: 12.5, 3: 11, 4: 10}
            pdf.ln(2.5 if level > 1 else 0)
            pdf.set_font("dejavu", "B", sizes.get(level, 9.5))
            pdf.set_text_color(10, 10, 10)
            pdf.set_x(pdf.l_margin)
            pdf.multi_cell(0, 6 if level <= 2 else 5.4, title,
                           new_x="LMARGIN", new_y="NEXT")
            pdf.ln(1.2)
            i += 1
            continue

        # horizontal rule
        if re.match(r"^-{3,}$", stripped):
            flush_para()
            pdf.ln(1)
            pdf.set_draw_color(170, 170, 170)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(2.5)
            i += 1
            continue

        # table
        if is_table_row(line):
            flush_para()
            rows = []
            while i < len(lines) and is_table_row(lines[i]):
                if not re.match(r"^\|[\s:\-\|]+\|$", lines[i].strip()):
                    rows.append(table_cells(lines[i]))
                i += 1
            for r, cells in enumerate(rows):
                txt = "  |  ".join(clean_inline(c) for c in cells)
                body(txt, size=7.8, height=4.3,
                     style="B" if r == 0 else "")
            pdf.ln(2)
            continue

        # list item (unordered or numbered), possibly multi-line start
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", line)
        if m and not stripped.startswith("**Ag") :
            flush_para()
            marker = "•" if m.group(2) in ("-", "*") else m.group(2)
            indent = 6 + min(len(m.group(1)), 8)
            body(clean_inline(f"{marker}  {m.group(3)}"), indent=indent)
            pdf.ln(1.2)
            i += 1
            continue

        # blank line
        if not stripped:
            flush_para()
            i += 1
            continue

        para.append(line)
        i += 1

    flush_para()
    pdf.output(dst)
    print(f"WROTE {dst}")


if __name__ == "__main__":
    main()
