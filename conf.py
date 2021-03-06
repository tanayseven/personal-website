# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Tanay Rambles'
copyright = '2021, Tanay PrabhuDesai'
author = 'Tanay PrabhuDesai'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "ablog",
    "sphinx.ext.intersphinx",
    "sphinx_panels",
]

# Turns on feeds for our website
blog_baseurl = "https://tanayseven.com"
blog_title = "Tanay Rambles"
# blog_path: should match the directory you keep posts in, if you change this
# make sure to also change the name of the folder
blog_path = "blog"
# blog_feed_fulltext: Choose to display full text in blog feeds, default is False.
blog_feed_fulltext = True
# Glob pattern that grabs all posts so you don't need to specify which posts are blog posts in each post
# This pattern facilitates a folder structure such as posts/2020/my-awesome-post.rst
blog_post_pattern = "blog/*/*"
# post_redirect_refresh: Number of seconds (default is 5) that a redirect page waits before refreshing the page
# to redirect to the post.
post_redirect_refresh = 1
# post_auto_image: Index of the image that will be displayed in the excerpt of the post. Default is 0, meaning no
# image. Setting this to 1 will include the first image
post_auto_image = 1
# post_auto_excerpt: Number of paragraphs (default is 1) that will be displayed as an excerpt from the post. Setting
# this 0 will result in displaying no post excerpt in archive pages.
post_auto_excerpt = 1

blog_authors = {
    'tanay': (author, blog_baseurl),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "github_url": "https://github.com/tanayseven/",
    "twitter_url": "https://twitter.com/tanayseven/",
    "search_bar_text": "Search...",
    "search_bar_position": "navbar",
    "show_toc_level": 0,
}

html_sidebars = {
    "index": ["about.html"],
    "about": ["about.html"],
    "talks": ["about.html"],
    "blog": ["tagcloud.html", "archives.html"],
    "blog/**": ["postcard.html", "recentposts.html", "archives.html"],
}


def setup(app):
    app.add_css_file("custom.css")
