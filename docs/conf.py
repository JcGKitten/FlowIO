# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    print(os.getcwd())
    print(os.listdir('..'))
    sys.path.insert(0, os.path.abspath('../src'))
else:
    sys.path.insert(0, os.path.abspath('../src'))

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'FlowIO'
copyright = '2025, Scott White'
author = 'Scott White'


# -- General configuration ---------------------------------------------------

master_doc = 'index'
autodoc_member_order = 'bysource'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'autoclasstoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'nbsphinx'
]

autodoc_default_options = {
    'members': True,
    'private-members': False,
    'inherited-members': True,
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

autoclasstoc_sections = [
        'public-methods'
]

autoclass_content = 'both'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # 'logo': 'logo.png',
    # 'github_user': 'whitews',
    # 'github_repo': 'flowio',
    # 'github_banner': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]
