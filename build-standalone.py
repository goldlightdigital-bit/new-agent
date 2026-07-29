#!/usr/bin/env python3
"""Build self-contained, paste-ready single-file versions of each page.

Inlines css/styles.css, js/main.js, the favicon, and any assets/ raster images
(as base64 data URIs) into each source page, and rewrites cross-page links so
the standalone set stays internally consistent (e.g. index.html ->
gold-light-digital-standalone.html). Run after editing any source HTML/CSS/JS
or swapping an image:

    python3 build-standalone.py
"""
import base64
import mimetypes
import pathlib
import re
import urllib.parse

# source page -> standalone output name
PAGES = {
    "index.html": "gold-light-digital-standalone.html",
    "privacy.html": "privacy-standalone.html",
    "terms.html": "terms-standalone.html",
    "accessibility.html": "accessibility-standalone.html",
}

root = pathlib.Path(__file__).parent
css = (root / "css/styles.css").read_text()
js = (root / "js/main.js").read_text()
favicon = (root / "assets/favicon.svg").read_text()
favicon_data = "data:image/svg+xml," + urllib.parse.quote(favicon)

for src, out in PAGES.items():
    html = (root / src).read_text()
    html = html.replace(
        '<link rel="stylesheet" href="css/styles.css" />',
        "<style>\n" + css + "\n  </style>",
    )
    html = html.replace(
        '<script src="js/main.js" defer></script>',
        "<script>\n" + js + "\n  </script>",
    )
    html = html.replace(
        '<link rel="icon" type="image/svg+xml" href="assets/favicon.svg" />',
        f'<link rel="icon" type="image/svg+xml" href="{favicon_data}" />',
    )
    # inline any assets/ raster images referenced via src="..." as data URIs
    def _embed(m):
        raw = m.group(2)
        rel = urllib.parse.unquote(raw)  # decode %20 etc. to find the file
        path = root / rel
        if not path.exists():
            return m.group(0)
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        data = base64.b64encode(path.read_bytes()).decode()
        return f'{m.group(1)}="data:{mime};base64,{data}"'

    html = re.sub(r'(src)="(assets/[^"]+\.(?:png|jpe?g|webp|gif))"', _embed, html)

    # keep cross-page links pointing at the standalone siblings
    for page_src, page_out in PAGES.items():
        html = html.replace(f'"{page_src}', f'"{page_out}')

    (root / out).write_text(html)
    assert "css/styles.css" not in html and "js/main.js" not in html
    assert 'src="assets/' not in html, "unembedded image reference remains"
    print(f"{src:16s} -> {out:34s} ({len(html):,} bytes)")

print("done")
