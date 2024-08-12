# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import pkg_resources

sys.path.append(os.path.abspath("../.."))
sys.path.append(os.path.abspath(".."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

try:
    release = pkg_resources.get_distribution("brainfuck_art").version
except pkg_resources.DistributionNotFound:
    print(
        "To build the documentation, the distribution information of "
        "brainfuck_art has to be available.  Either install the package "
        'into your development environment or run "setup.py develop" '
        "to setup the metadata. A virtualenv is recommended. "
    )
    sys.exit(1)

project = "brainfuck_art"
copyright = "2024, "
author = "Pablo Marcos-Manchón"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosummary",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Add mappings
intersphinx_mapping = {
    "python": ("http://docs.python.org/3", None),
}

autodoc_default_options = {"members": True, "inherited-members": True}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
#html_favicon = "https://dratio.io/favicon/favicon.ico"
#html_logo = "https://dratio.io/branding/logo.png"
html_theme_options = {
    "github_url": "https://github.com/pablomm/brainfuck-art",
    "navbar_start": ["navbar-logo"],
    "icon_links": [
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/brainfuck-art",
            "icon": "https://www.python.org/static/apple-touch-icon-144x144-precomposed.png",
            "type": "url",
        },
    ],
}
html_context = {
    "github_user": "pablomm",
    "github_repo": "brainfuck-art",
    "github_version": "main",
    "doc_path": "docs",
}