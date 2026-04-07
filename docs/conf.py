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

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#7c4dff",
        "color-brand-content": "#ff4d88",
    },
    "dark_css_variables": {
        "color-brand-primary": "#bb86fc",
        "color-brand-content": "#ff79c6",
    },
}

myst_enable_extensions = ["colon_fence",
"deflist",
"dollarmath",
"amsmath",
"html_admonition",
"html_image",
"tasklist",]
