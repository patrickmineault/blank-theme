from setuptools import find_packages, setup

setup(
    name="blank_sphinx_theme",
    packages=find_packages(),
    entry_points={
        "sphinx.html_themes": [
            "blank_sphinx_theme = blank_sphinx_theme",
        ]
    },
)
