import os
import sys

# Add project root so autodoc can import the package/module
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

project = "demo-release-repo"
extensions = [
    "sphinx.ext.autodoc",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []

# HTML output
html_theme = "sphinx_rtd_theme"

# Autodoc options
autodoc_member_order = "bysource"
autodoc_typehints = "description"
