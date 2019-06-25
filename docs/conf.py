# -*- coding: utf-8 -*-
"""Configuration file for the Sphinx documentation builder.

This file does only contain a selection of the most common options. For a
full list see the documentation:

* http://www.sphinx-doc.org/en/stable/config

"""

from __future__ import division, print_function, unicode_literals

# from datetime import datetime

from recommonmark.parser import CommonMarkParser

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
__author__     = 'Imran Iqbal'                                     # noqa: E221
__copyright__  = 'Copyright (C) 2019, MYII'                        # noqa: E221
__license__    = 'Apache-2.0'                                      # noqa: E221
__version__    = 'latest'                                          # noqa: E221
__maintainer__ = 'Imran Iqbal'                                     # noqa: E221


# -- Project information -----------------------------------------------------

project = 'golang-formula'
copyright = __copyright__.replace('Copyright (C) ', '')  # noqa: A001
author = __author__
version = __version__
release = __version__


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain golangs here, relative to this directory.
golangs_path = ['golangs', '_golangs', '.golangs']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for the reStructuredText parser ---------------------------------

file_insertion_enabled = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar golangs, must be a dictionary that maps document names
# to golang names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these golangs by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'golang-formula'


# -- Options for Markdown output ---------------------------------------------

source_parsers = {
    '.md': CommonMarkParser,
}


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        'index',
        'golang-formula.tex',
        u'golang-formula Documentation',
        u'',
        'manual',
    ),
]


# -- Functions: `setup`, docstring preprocessing, etc. -----------------------

def setup(app):
    """Prepare the Sphinx application object.

    Used for providing a custom CSS file for override styles.

    Parameters
    ----------
    app : object
        The Sphinx application object.

    Returns
    -------
    app : object
        The Sphinx application object.

    """
    app.add_stylesheet('css/custom.css')
    return app