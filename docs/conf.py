# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import importlib.metadata

# Adding the directory to the PYTHONPATH
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from sgwbpy import __version__, __name__ as __package_name__

# Get package metadata.
_metadata = importlib.metadata.metadata(__package_name__)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = __package_name__
author = _metadata["Author-email"]
copyright = f"2025-%Y, {author}"
version = __version__
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",       # automatically generates documentation form docstrings
    "sphinx.ext.todo",
    "sphinx.ext.viewcode"      # adds links to source code in the documentation
    #"sphinx.ext.napoleon",      # for NumPy docstrings
]

autodoc_default_options = {     # configurating the autodoc extension...
    "members": True,
    "member-order": "bysource",
    "undoc-members": True,
    "private-members": True
}
autodoc_typehints = "none"      # show type hints only in the docstring not in the firm
#autodoc_typehints_format = "short"
todo_include_todos = True

# Options for syntax highlighting.
pygments_style = "default"
pygments_dark_style = "default"

# Options for internationalization.
language = "en"

# Options for markup.
rst_prolog = f"""
.. |Python| replace:: `Python <https://www.python.org/>`__
.. |Sphinx| replace:: `Sphinx <https://www.sphinx-doc.org/en/master/>`__
.. |numpy| replace:: `NumPy <https://numpy.org/>`__
.. |GitHub| replace:: `GitHub <https://github.com/>`__
"""

# Options for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]     # Excludes these directories while searching for source code

# Options for templating.
templates_path = ["_templates"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinxawesome_theme"
html_theme_options = {
    "awesome_external_links": True,
}
#html_logo = "_static/logo_small.png"       Add your own image
#html_favicon = "_static/favicon.ico"       Add your own icon
html_permalinks_icon = "<span>#</span>"
#html_static_path = ["_static"]             Save icon and image in the _static directory and uncomment this line