"""Build the Word syllabus from Markdown.

Usage (from the syllabus/ folder):  python build_syllabus_docx.py [input.md] [output.docx]

Runs pandoc with Connor's v1 syllabus as the style template, then post-processes the .docx:
  - replaces the v1 template's placeholder page header text
  - makes title and heading text black (the template's theme makes them blue)
"""
import os
import re
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "syllabus_v2.md")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "NRES701A_Syllabus_v2_DRAFT.docx")
TEMPLATE = os.path.join(HERE, "..", "Causality Seminar Syllabus v1.docx")

HEADER_REPLACEMENTS = [
    (b"Department of [Department]", b"Natural Resources &amp; Environmental Science"),
    (b"Spring Semester", b"NRES 701A, Spring 2027"),
    (b"<w:t>2027</w:t>", b"<w:t>DRAFT v2</w:t>"),
]

BLACK_STYLES = {"Title", "Subtitle"} | {f"Heading{i}" for i in range(1, 10)}
BLACK_STYLES |= {s + "Char" for s in BLACK_STYLES}


def blacken_styles(xml: str) -> str:
    def fix_style(m):
        block = m.group(0)
        if m.group(1) not in BLACK_STYLES:
            return block
        block = re.sub(r"<w:color [^>]*/>", '<w:color w:val="000000" />', block)
        # Title underline border
        block = re.sub(r'(<w:bottom [^>]*?)w:color="[0-9A-Fa-f]{6}"( w:themeColor="[^"]*")?',
                       r'\1w:color="000000"', block)
        return block

    return re.sub(r'<w:style [^>]*w:styleId="([^"]+)".*?</w:style>', fix_style, xml, flags=re.S)


def main():
    subprocess.run(["pandoc", SRC, "-f", "markdown", "-t", "docx",
                    f"--reference-docx={TEMPLATE}", "-o", OUT], check=True)
    tmp = OUT + ".tmp"
    with zipfile.ZipFile(OUT) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zi.infolist():
            data = zi.read(item.filename)
            if re.fullmatch(r"word/header\d*\.xml", item.filename):
                for old, new in HEADER_REPLACEMENTS:
                    data = data.replace(old, new)
            elif item.filename == "word/styles.xml":
                data = blacken_styles(data.decode("utf8")).encode("utf8")
            zo.writestr(item, data)
    os.replace(tmp, OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
