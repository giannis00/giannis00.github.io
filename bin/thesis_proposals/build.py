"""Rebuild the medical thesis PDF using its original design assets.

Requires PyMuPDF. Run: python bin/thesis_proposals/build.py
The design reference retains the original header and logo. Carlito font files
come from google/fonts/ofl/carlito and retain their bundled OFL license.
"""

from pathlib import Path

import fitz


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUTPUT = ROOT / "assets/theses/ai-cutaneous-lymphoma-thesis-proposals-2026-27.pdf"
REFERENCE = HERE / "design-reference.pdf"

CSS = """
@font-face { font-family: Carlito; src: url(Carlito-Regular.ttf); }
@font-face { font-family: Carlito; src: url(Carlito-Bold.ttf); font-weight: bold; }
@font-face { font-family: Carlito; src: url(Carlito-BoldItalic.ttf); font-weight: bold; font-style: italic; }
body { font-family: Carlito; font-size: 11pt; line-height: 13.8pt; margin: 0; color: #000; }
p { margin: 0 0 8pt; text-align: justify; }
h1 { font-size: 16pt; line-height: 19.5pt; text-align: center; color: #1f3864; margin: 8pt 0 12pt; }
h2 { font-size: 12pt; line-height: 15pt; color: #1f3864; margin: 8pt 0 6pt; page-break-after: avoid; }
h3 { font-size: 11pt; line-height: 13.8pt; margin: 8pt 0 6pt; page-break-after: avoid; }
h4 { font-size: 11pt; line-height: 13.8pt; font-weight: bold; font-style: italic; margin: 5pt 0 5pt; page-break-after: avoid; }
.topic { margin-left: 18pt; }
.page { page-break-before: always; }
a { color: #0563c1; text-decoration: underline; }
table { border-collapse: collapse; width: 100%; font-size: 10pt; line-height: 12.5pt; margin-bottom: 7pt; }
td, th { border-bottom: 0.4pt solid #dddddd; padding: 3pt 4pt; text-align: left; vertical-align: top; }
th { color: #1f3864; font-weight: bold; }
.note { font-size: 10pt; line-height: 12.5pt; }
"""


def build(html_path=None, output_path=None, title=None, subject=None):
    html_path = Path(html_path) if html_path is not None else HERE / "medical-proposals.html"
    output_path = Path(output_path) if output_path is not None else OUTPUT
    reference = fitz.open(REFERENCE)
    width, height = reference[0].rect.width, reference[0].rect.height
    directory = HERE / "fonts"
    regular = fitz.Font(fontfile=str(directory / "Carlito-Regular.ttf"))
    story = fitz.Story(
        html=html_path.read_text(encoding="utf-8"),
        user_css=CSS,
        archive=fitz.Archive(str(directory)),
    )

    def rectangles(number, filled):
        return fitz.Rect(0, 0, width, height), fitz.Rect(72.1, 84.5, 525.85, 777), None

    result = story.write_with_links(rectangles)
    for number, page in enumerate(result, 1):
        # Story leaves a top-left coordinate transform in its content stream.
        # Isolate it before adding the original header and PDF-coordinate footer.
        page.wrap_contents()
        page.show_pdf_page(page.rect, reference, 0, overlay=False)
        page.insert_link({"kind": fitz.LINK_URI, "from": fitz.Rect(288.16, 45.15, 366.86, 54.15), "uri": "mailto:i.tsioulis@mc-class.gr"})
        pieces = [("Page ", 9), (str(number), 11), (" of ", 9), (str(len(result)), 11)]
        total = sum(regular.text_length(text, fontsize=size) for text, size in pieces)
        x = (width - total) / 2
        writer = fitz.TextWriter(page.rect)
        for text, size in pieces:
            writer.append((x, 803.4), text, font=regular, fontsize=size)
            x += regular.text_length(text, fontsize=size)
        writer.write_text(page, color=(0.498, 0.498, 0.498))

    # Carlito's shaped tt/ti/tti glyphs have no Unicode cmap entries. Supply
    # mappings so copying/searching the PDF returns letters, not glyph IDs.
    processed = set()
    for page in result:
        for font in page.get_fonts():
            if font[0] in processed or not font[3].startswith("Carlito "):
                continue
            processed.add(font[0])
            kind, value = result.xref_get_key(font[0], "ToUnicode")
            if kind != "xref":
                continue
            cmap_xref = int(value.split()[0])
            cmap = result.xref_stream(cmap_xref).decode("ascii")
            entries = ["<0082> <00740074>"]
            if "Italic" in font[3]:
                entries.append("<08a1> <00740069>")
            else:
                entries.extend(["<08a2> <00740069>", "<08b0> <007400740069>"])
            block = str(len(entries)) + " beginbfchar\n" + "\n".join(entries) + "\nendbfchar\n"
            result.update_stream(cmap_xref, cmap.replace("endcmap", block + "endcmap").encode("ascii"))
    result.set_metadata({
        "title": title or "Thesis Proposals in Artificial Intelligence for Cutaneous Lymphoma Research",
        "author": "Ioannis Tsioulis",
        "subject": subject or "Eight public-data AI dissertation topics for 2026-27",
        "keywords": "artificial intelligence, deep learning, cutaneous lymphoma, public data, thesis proposals",
        "creator": "Ioannis Tsioulis",
    })
    result.save(output_path, garbage=4, deflate=True)
    print(f"Built {output_path.name}: {len(result)} pages")


if __name__ == "__main__":
    build()
