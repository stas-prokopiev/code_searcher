=============
CODE_SEARCHER
=============

.. image:: https://img.shields.io/github/last-commit/stas-prokopiev/code_searcher
   :target: https://img.shields.io/github/last-commit/stas-prokopiev/code_searcher
   :alt: GitHub last commit

.. image:: https://img.shields.io/github/license/stas-prokopiev/code_searcher
    :target: https://github.com/stas-prokopiev/code_searcher/blob/master/LICENSE.txt
    :alt: GitHub license<space><space>

.. image:: https://readthedocs.org/projects/local-simple-database/badge/?version=latest
    :target: https://local-simple-database.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/stas-prokopiev/code_searcher.svg?branch=master
    :target: https://travis-ci.org/stas-prokopiev/code_searcher

.. image:: https://img.shields.io/pypi/v/code_searcher
   :target: https://img.shields.io/pypi/v/code_searcher
   :alt: PyPI

.. image:: https://img.shields.io/pypi/pyversions/code_searcher
   :target: https://img.shields.io/pypi/pyversions/code_searcher
   :alt: PyPI - Python Version

.. contents:: **Table of Contents**

Short Overview.
=========================

code_searcher is a simple Python package(**py>=2.7 or py>=3.4**) with the main purpose to
make searching through your project codebase fast and simple.

Currently, fully supported file types are **.py** and **.ipynb**
nonetheless, search functional can be applied to any file extensions which can be read as plain text in utf-8 encoding.

In additional it allows you to get some useful info about your project codebase.
For more info check section: **Typical examples of Usage**

More info.
=========================

The main reason of building this package was to create universal
tool to help support changes in methods signatures in both .py and .ipynb files.

It's becoming quite useful when your project outgrows 1k lines of code and manual replacement becomes too annoying
(Too easy to overlook replacement somewhere).

For more info check section: **Typical examples of Usage**

Installation
============

* Install via pip:

.. code-block:: bash

    pip install code_searcher

Typical examples of Usage
=========================

| In any case, the first thing you need to do is to import the necessary module and initialize class obj.
| To do so you need to give pathes to folders in which all your files located (searcher will look deeper to full extent).

If you have a code of all your projects structured
that there is the main folder for all .py files and
there is the main folder for all .ipynb files then use them.

.. code-block:: python

    from code_searcher import code_searcher_class
    LIST_STR_FOLDERS_WHERE_TO_LOOK = ["path_to_dir_1", "path_to_dir_1", ...]
    code_searcher_obj = code_searcher_class(
            LIST_STR_FOLDERS_WHERE_TO_LOOK,
            list_str_file_extensions=[".py", "ipynb"],
    )

Please note that first initialization can be a long process if the folders where you search for files are deep and wide.

But after finding all files they won't be downloaded again unless they were changed. So excellent performance is expected.

1) To find all occurrences of some code.
--------------------------------------------------------------------------------------------------

*E.G. You've changed a function signature and want to do necessary changes in the library.*

*To find all the places where this function was used use the code below*

.. code-block:: python

    code_searcher_obj.search("line_to_look_for")

*Output:*

.. code-block:: console

    ===============================================================================
    For folder: c:\users\stanislav\desktop\my_python_projects\code_search_engine\project\code_searcher\src\code_searcher

    --> For extension: .py
    ----> Found in:  code_searcher_class.py
    ------> 0) line: 93  Code_line: line_to_look_for(
    ------> 1) line: 444  Code_line: def line_to_look_for(

    --> For extension: ipynb
    ----> NOTHING FOUND.
    ===============================================================================
    Overall occurrences found:  2


2) To find all occurrences of some regular expression pattern
--------------------------------------------------------------------------------------------------

.. code-block:: python

    code_searcher_obj.search_with_re("^from __future__ import[\s]+")

*Output:*

.. code-block:: console

    ===============================================================================
    For folder: c:\users\stanislav\desktop\my_python_projects\code_search_engine\project\code_searcher\src\code_searcher

        --> For extension: .py
        ----> Found in:  additional_functions.py
        ------> 0) line: 12  Code_line: from __future__ import print_function
        ----> Found in:  code_searcher_class.py
        ------> 1) line: 11  Code_line: from __future__ import print_function
        ----> Found in:  decorators.py
        ------> 2) line: 12  Code_line: from __future__ import print_function
        ----> Found in:  working_with_files.py
        ------> 3) line: 12  Code_line: from __future__ import print_function

        --> For extension: ipynb
        ----> NOTHING FOUND.
    ===============================================================================
    Overall occurrences found:  4

3) To see some statistics about your library.
------------------------------------------------------

.. code-block:: python

    print(code_searcher_obj)

*Output:*

.. code-block:: console

    Folders to search in:
    --> c:\users\stanislav\desktop\my_python_projects\code_searcher\src\code_searcher
    --> c:\users\stanislav\desktop\my_python_projects\code_searcher\jupyter_notebooks

    Extensions to check:
    --> .py
    --> .ipynb

    ===============================================================================
    Files Statistic of current code library:
    ===============================================================================
    --> For folder: c:\users\stanislav\desktop\my_python_projects\code_searcher\src\code_searcher
    --> Files_found = 4  Code_lines = 664
    ----> .py:  Files_found = 4;  Code_lines = 664;
    ----> .ipynb:  Files_found = 0;  Code_lines = 0;
    ===============================================================================
    --> For folder: c:\users\stanislav\desktop\my_python_projects\code_searcher\jupyter_notebooks
    --> Files_found = 1  Code_lines = 22
    ----> .py:  Files_found = 0;  Code_lines = 0;
    ----> .ipynb:  Files_found = 1;  Code_lines = 22;
    ===============================================================================

4) To add new files to examine.
--------------------------------------------------------------------------------------------------

*If you've created a new file inside folder given to code_searcher then you should update files for code_searcher*

.. code-block:: python

    code_searcher_obj.update_files()

5) To get dictionary with content of all satisfy files.
--------------------------------------------------------------------------------------------------

*For now on this dictionary structure is*

*{"dir_path_1": {"file_extension_1": {"absolute_file_path_1": str_file_content, ..}, ..}, ..}*

.. code-block:: python

    code_searcher_obj.dict_str_file_by_path_by_ext_by_dir

Links
=====

    * `Pypi <https://pypi.org/project/code-searcher/>`_
    * `readthedocs <https://code-searcher.readthedocs.io/en/latest/>`_
    * `GitHub <https://github.com/stas-prokopiev/code_searcher>`_

Local links
=============

    * `CHANGELOG <CHANGELOG.rst>`_.
    * `CONTRIBUTING <CONTRIBUTING.rst>`_.

Contacts
========

    * Email: stas.prokopiev@gmail.com
    * `vk.com <https://vk.com/stas.prokopyev>`_
    * `Facebook <https://www.facebook.com/profile.php?id=100009380530321>`_

License
=======

This project is licensed under the MIT License.
