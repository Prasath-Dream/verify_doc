# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = """RB-RA8D1
Quick Start Guide"""
copyright = '2025, PHYTEC'
author = 'PHYTEC'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_title = 'EK-RA8D1'

# Generated RST files: rstfile1, rstfile2

html_css_files = ['custom_overrides.css']

html_js_files = ['spx_toggle.js', 'spx_anim.js', 'spx_img_click.js']
