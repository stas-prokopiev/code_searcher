"""sphinx main configuration file"""
# -*- coding: utf-8 -*-
import os
import sys
import inspect
import shutil

__location__ = os.path.join(os.getcwd(), os.path.dirname(
    inspect.getfile(inspect.currentframe())))


#####
# My function to copy all .rst files in the docs folder
try:
    print("*" * 79)
    print("Copying all .rst files from:")
    copy_rst_from_here = os.path.abspath('../..')
    past_rst_here = os.path.abspath('.')
    print(copy_rst_from_here)
    print(past_rst_here)
    list_files_to_copy = [
        os.path.join(copy_rst_from_here, f)
        for f in os.listdir(copy_rst_from_here)
        if os.path.isfile(os.path.join(copy_rst_from_here, f)) and f.endswith(".rst")
    ]
    print("*" * 79)
    print("Files will be copied: ")
    for int_file_num, str_file_path in enumerate(list_files_to_copy):
        str_filename = os.path.basename(str_file_path)
        print("--> ", int_file_num, ")", str_filename)
        str_new_path = os.path.join(past_rst_here, str_filename)
        shutil.copyfile(str_file_path, str_new_path)
    print("*" * 79)
except BaseException:
    print("WARNING: Unable to move the .rst files.")
#####

# -- Run sphinx-apidoc -------------- ----------------------------------------
try:  # for Sphinx >= 1.7
    from sphinx.ext import apidoc
except ImportError:
    from sphinx import apidoc

output_dir = os.path.join(__location__, "api")
module_dir = os.path.join(__location__, "../../src/code_searcher")
try:
    shutil.rmtree(output_dir)
except FileNotFoundError:
    pass

try:
    import sphinx
    from pkg_resources import parse_version
    cmd_line_template = "sphinx-apidoc -f -o {outputdir} {moduledir}"
    cmd_line = cmd_line_template.format(
        outputdir=output_dir, moduledir=module_dir)
    args = cmd_line.split(" ")
    if parse_version(sphinx.__version__) >= parse_version('1.7'):
        args = args[1:]
    apidoc.main(args)
except BaseException as e:
    print("Running `sphinx-apidoc` failed!\n{}".format(e))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.3'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.napoleon',
    'sphinx.ext.autosummary', 'sphinx.ext.viewcode',
]


#####
# Napoleon settings

napoleon_google_docstring = True
napoleon_numpy_docstring = True

#####
autodoc_member_order = 'bysource'
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'code_searcher'
copyright = u'2020, Stanislav Prokopyev'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''  # Is set by calling `setup.py docs`
# The full version, including alpha/beta/rc tags.
release = ''  # Is set by calling `setup.py docs`


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ---------------------------------------------------

html_theme = 'classic'




# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True
html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'code_searcher-doc'
add_module_names = True
