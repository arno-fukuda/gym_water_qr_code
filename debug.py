import segno

PAYLOAD = "10016010072530031202511272324"
HTML_OUT = "qr_debug_all.html"
VERSION = 2
SCALE = 6

EC_LEVELS = ["L", "M", "Q", "H"]
MASKS = list(range(8))


def qr_to_svg_inline(qr, scale):
    """Return inline SVG for a Segno QR code (compatible with your version)."""
    return qr.svg_inline(scale=scale)   # <-- THIS WORKS ON ALL VERSIONS


def main():
    html = []
    html.append("<!DOCTYPE html><html><head><meta charset='utf-8'/>")
    html.append("<title>All 32 QR Variants</title>")
    html.append("""
    <style>
        body { font-family: sans-serif; padding: 20px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 20px; }
        .cell { border: 1px solid #ccc; padding: 10px; border-radius: 8px; text-align: center; }
        .label { margin-top: 8px; color: #444; font-size: 14px; }
    </style>
    """)
    html.append("</head><body>")
    html.append(f"<h1>All 32 QR Code Variants (Version 2)</h1>")
    html.append(f"<div>Payload: <code>{PAYLOAD}</code></div>")
    html.append("<div class='grid'>")

    for ec in EC_LEVELS:
        for mask in MASKS:
            qr = segno.make(
                PAYLOAD,
                version=VERSION,
                error=ec,
                mask=mask,
                boost_error=False
            )

            svg = qr_to_svg_inline(qr, SCALE)

            html.append("<div class='cell'>")
            html.append(svg)
            html.append(f"<div class='label'>EC {ec}, Mask {mask}</div>")
            html.append("</div>")

    html.append("</div></body></html>")

    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"\nGenerated {HTML_OUT} with all 32 variants.\n")


if __name__ == "__main__":
    main()
