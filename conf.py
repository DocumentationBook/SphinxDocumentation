"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
import os

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# import sphinxcontrib.spelling

# -- Project information -----------------------------------------------------

project = 'Detailed Sphinx'
copyright = '2023, Albert Bagdasarian'
author = 'Albert Bagdasarian'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.graphviz',
    'sphinxcontrib.plantuml',
    'sphinx.ext.doctest',
    # 'rinoh.frontend.sphinx',
    # 'sphinxcontrib.spelling',
]

# Extension config:
# plantuml_output_format = 'svg'

# spelling_word_list_file_name = 'custom_words.txt'
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '__test',]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css',
]

# To make Graphviz build correct hyperlinks:
graphviz_output_format = 'svg'

# Don't show source reST files, especially on public domains (combined with the next option):
html_show_sourcelink = False
# Don't create the __sources/ with source reST files.
html_copy_source = False

# if os.environ.get('READTHEDOCS') is not None:
#     plantuml = 'java -Djava.awt.headless=true -jar /usr/share/plantuml/plantuml.jar'

rst_prolog = """
.. warning:: This draft documentation is under development.
"""

# rinoh_documents = [dict(doc='index',        # top-level file (index.rst)
#                         target='manual')]   # output file (manual.pdf)

