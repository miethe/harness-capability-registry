from __future__ import annotations

from pathlib import Path

from hcr.io import write_text


def build_standalone_app(root: Path) -> Path:
    """Build a portable one-file version of the static Harness Matrix app."""
    app = root / "app"
    index = (app / "index.html").read_text(encoding="utf-8")
    css = (app / "styles.css").read_text(encoding="utf-8")
    data_js = (app / "data" / "registry.bundle.js").read_text(encoding="utf-8")
    app_js = (app / "app.js").read_text(encoding="utf-8")

    # Avoid an upstream release note containing a literal closing script tag from
    # terminating the embedded JSON script block.
    data_js = data_js.replace("</", "<\\/")
    app_js = app_js.replace("</", "<\\/")

    standalone = index.replace(
        '<link rel="stylesheet" href="styles.css">',
        f"<style>\n{css}\n</style>",
    )
    standalone = standalone.replace(
        '<script src="data/registry.bundle.js"></script>',
        f"<script>\n{data_js}\n</script>",
    )
    standalone = standalone.replace(
        '<script src="app.js"></script>',
        f"<script>\n{app_js}\n</script>",
    )

    output = root / "generated" / "Harness_Matrix_Standalone.html"
    write_text(output, standalone)
    return output
