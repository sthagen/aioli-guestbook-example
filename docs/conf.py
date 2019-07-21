import sys
import os

here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(".."))

import aioli_guestbook

project = "Aioli Guestbook"
copyright = "2019 Robert Wikman"
author = u"Robert Wikman <rbw@vault13.org>"

version = aioli_guestbook.export.version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinxcontrib.httpdomain"
]

source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

html_static_path = ["_static"]

html_context = {
    "maintainer": "Robert Wikman <rbw@vault13.org>",
    "project_pretty_name": "Aioli Guestbook",
}

html_favicon = "_static/favicon.png"
html_theme = "alabaster"
html_sidebars = {
    "**": [
        "about.html", "navigation.html",
    ]
}

html_theme_options = {
    "sidebar_width": "170px",
    "sidebar_collapse": True,
    "fixed_sidebar": True,
    "logo_name": None,
    "font_family": "arial",
    "github_repo": "aioli-framework/aioli-guestbook-example",
    "github_banner": True,
}

# Output file base name for HTML help builder.
htmlhelp_basename = "aioli_guestbook_doc"


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "aioli_guestbook.tex", "Aioli Guestbook Documentation",
     "Robert Wikman \\textless{}rbw@vault13.org\\textgreater{}", "manual"),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "aioli_guestbook", "Aioli Guestbook Documentation",
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, "aioli_guestbook", "Aioli Guestbook Documentation", author,
     "aioli_guestbook", "Aioli Guestbook Example", "Miscellaneous"),
]
