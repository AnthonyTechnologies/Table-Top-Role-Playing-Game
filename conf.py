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

# Ensure src is on sys.path for autodoc
ROOT = Path(__file__).parent.parent.resolve()
SRC = ROOT / "src"
if SRC.is_dir() and str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

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

