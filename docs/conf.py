#!/usr/bin/env python
"""Sphinx configuration for proxyarrays.

This configuration enables extensive API documentation using autodoc and autosummary, better type and Google/NumPy style
docstring parsing via Napoleon, and several convenience extensions like viewcode, intersphinx, and todo.
"""

# Imports #
# Standard Libraries #
import sys
from datetime import datetime, timezone
from pathlib import Path

# Ensure root is on sys.path for autodoc
ROOT = Path(__file__).parent.resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Project Information #
project = 'Table Top Role Playing Game'
author = "Anthony Fong"
copyright = f"{datetime.now(tz=timezone.utc).year}, {author}"

# General configuration #
extensions = []

exclude_patterns = ["python-styleguide", "_build"]


# HTML output
html_theme = 'furo'
html_theme_options = {}

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_js_files = [
    'custom.js',
]

