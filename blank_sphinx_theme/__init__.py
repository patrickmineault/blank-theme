from pathlib import Path


def setup(app):
    here = Path(__file__).parent.resolve()
    app.add_html_theme("blank_sphinx_theme", str(here / "theme" / "blank_sphinx_theme"))
