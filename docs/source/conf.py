# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'


django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ocp13'
copyright = '2025, Sally PJ'
author = 'Sally PJ'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # pour docstrings style Google
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['**/migrations/*', '_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


def setup(app):
    app.add_css_file('custom.css')
