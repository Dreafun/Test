import os
import sys
sys.path.insert(0, os.path.abspath("."))

project = "Test"
extensions = ["myst_parser", "sphinx_rtd_theme"]

html_theme = "furo"

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
