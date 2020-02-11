=============
CODE_SEARCHER
=============

.. image:: https://travis-ci.org/stas-prokopiev/code_searcher.svg?branch=master
    :target: https://travis-ci.org/stas-prokopiev/code_searcher

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
tool to help support changes in functions signatures in both .py and .ipynb files.

It's becoming quite useful when your project outgrows 1k lines of code and manual replacement becomes too annoying
(Too easy to overlook replacement somewhere).

But in a time this package becomes something a little bit large than that.

For example, this package allows you:

    1) To get names of all outer packages used inside your project to build a short requirements.txt.
    2) To get names of all functions that were defined but never used (to keep your code as short as possible)
    3) To print all places where length of code line exceeds some N (If you want make your code complaint with pep8 code length condition)
    4) To get content of all files with asked extensions directly.
    5) To print some statistics about your codebase (Like number of non empty code lines per extension per folder).

For more info check section: **Typical examples of Usage**

Installation
============

* Install via setup.py:

.. code-block:: bash

    git clone git@github.com:stas-prokopiev/code_searcher.git
    cd code_searcher
    python setup.py install

* Install via pip:

.. code-block:: bash

    pip install code_searcher

Typical examples of Usage
=========================

In any case, the first thing you need to do is to import the necessary module and initialize class obj.

To do so you need to replace "path_to_folder_1" from the code below on most parent folder of all files you want to analyze.

If you have a code of all your projects structured
that there is the main folder for all .py files and
there is the main folder for all .ipynb files then use them.

.. code-block:: python

    from code_searcher import code_searcher_class
    LIST_STR_FOLDERS_WHERE_TO_LOOK = ["path_to_folder_1", "path_to_folder_2", ...]
    code_searcher_obj = code_searcher_class(
            LIST_STR_FOLDERS_WHERE_TO_LOOK,
            list_str_file_extensions=[".py", "ipynb"],
    )

Please note that first initialization can be a long process if the folders where you search for files are deep and wide.

But after finding all files they won't be redownloaded again unless they were changed. So excellent performance is expected.

1) To find all occurrences of some code.
--------------------------------------------------------------------------------------------------

*E.G. You've changed a function signature and want to do necessary changes in the library.*

*To find all the places where this function was used use the code below*

.. code-block:: python

    code_searcher_obj.search_code_in_the_library(
        str_code_to_search="print_places_where_line_length_exceed_N",
        bool_is_to_search_case_sensitive=True,
    )

*Output:*

.. code-block:: console

    For folder: c:\users\stanislav\desktop\my_python_projects\code_search_engine\project\code_searcher\src\code_searcher

    --> For extension: .py
    ----> Found in:  code_searcher_class.py
    ------> 0) line: 93  Code_line: print_places_where_line_length_exceed_N(
    ------> 1) line: 444  Code_line: def print_places_where_line_length_exceed_N(

    --> For extension: ipynb
    ----> NOTHING FOUND.


2) To find all occurrences of some regular expression pattern
--------------------------------------------------------------------------------------------------

.. code-block:: python

    code_searcher_obj.search_code_in_the_library_with_re(
        str_code_to_search="^from __future__ import[\s]+"
    )

*Output:*

.. code-block:: console

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

3) To see some statistics about your library.
------------------------------------------------------

.. code-block:: python

    print(code_searcher_obj)

*Output:*

.. code-block:: console

    Folders to search in:
    --> c:\users\stanislav\desktop\my_python_projects\code_search_engine\project\code_searcher\src\code_searcher
    --> c:\users\stanislav\desktop\websim\all_websim_scripts\working_with_expression_alphas\dashboard
    Extensions to check:
    --> .py
    --> ipynb

    Files Statistic of current code library:
    --> For folder: c:\users\stanislav\desktop\my_python_projects\code_search_engine\project\code_searcher\src\code_searcher
    --> Files_found = 5  Code_lines = 1203
    ----> .py:  Files_found = 5;  Code_lines = 1203;
    ----> ipynb:  Files_found = 0;  Code_lines = 0;
    ===============================================================================
    --> For folder: c:\users\stanislav\desktop\websim\all_websim_scripts\working_with_expression_alphas\dashboard
    --> Files_found = 4  Code_lines = 175
    ----> .py:  Files_found = 0;  Code_lines = 0;
    ----> ipynb:  Files_found = 4;  Code_lines = 175;
    ===============================================================================

4) To add new files to examine.
--------------------------------------------------------------------------------------------------

*If you've created a new file inside folder given to code_searcher then you should update files for code_searcher*

.. code-block:: python

    code_searcher_obj.update_files()

5) To check which functions were defined but never used.
--------------------------------------------------------------------------------------------------

*It can be used in order to have your library as short as possible.*

.. code-block:: python

    code_searcher_obj.get_names_of_all_py_functions_defined_but_never_used()

*Output:*

.. code-block:: console

    Found functions defined:  31
    --> Printing all never used functions:
    -->  0 )
    ----> Function: check_type_of_arguments(...)
    ----> From file:  c:\users\stanislav\desktop\my_python_projects\code_searcher\src\code_searcher\decorators.py
    Found never used functions:  1

6) To check which modules were imported in the library.
--------------------------------------------------------------------------------------------------

*It can be used in order to have only used packages in the virtual environment*

.. code-block:: python

    code_searcher_obj.get_list_imported_modules_in_the_py_library()

*Output:*

.. code-block:: console

    Imported packages found:
    -->  0 ) __future__
    -->  1 ) code_searcher
    -->  2 ) codecs
    -->  3 ) collections
    -->  4 ) json
    -->  5 ) os
    -->  6 ) pkg_resources
    -->  7 ) re
    -->  8 ) stdlib_list
    -->  9 ) sys
    -->  10 ) time

7) To get dictionary with content of all satisfy files.
--------------------------------------------------------------------------------------------------

*For now on this dictionary structure is*

*{"dir_path_1": {"file_extension_1": {"absosut_file_path_1": str_file_content, ..}, ..}, ..}*

.. code-block:: python

    code_searcher_obj.dict_str_file_by_path_by_ext_by_dir


8) To print places where line length exceeds certain limit
--------------------------------------------------------------------------------------------------

*If you want to search only through .py files but code_searcher_obj was initialized for [".py", "ipynb"]*

*you can give to argument list_str_file_extensions=[".py"]*


.. code-block:: python

    code_searcher_obj.print_places_where_line_length_exceed_N(int_max_length=78, list_str_file_extensions=None,)

*Output:*

.. code-block:: console

    For folder: c:\users\stanislav\desktop\my_python_projects\code_search_engine\project\code_searcher\src\code_searcher

    --> For extension: .py
    ----> Found in:  code_searcher_class.py
    ------> 0) line: 63  Length: 79
    ------> 1) line: 151  Length: 79
    ------> 2) line: 153  Length: 79
    ------> 3) line: 156  Length: 79
    ------> 4) line: 583  Length: 80
    ------> 5) line: 594  Length: 79
    ------> 6) line: 719  Length: 79
    ----> Found in:  decorators.py
    ------> 7) line: 50  Length: 79
    ------> 8) line: 63  Length: 79

    --> For extension: ipynb
    ----> NOTHING FOUND.

9) To get the number of not empty code lines in the library
--------------------------------------------------------------------------------------------------

.. code-block:: python

    code_searcher_obj.get_number_of_lines_in_the_library()

Links
=====

    * `Pypi <https://pypi.org/project/code-searcher/>`_
    * `readthedocs <https://code-searcher.readthedocs.io/en/latest/>`_
    * `GitHub <https://github.com/stas-prokopiev/code_searcher>`_

Releases
========

See `CHANGELOG <https://github.com/stas-prokopiev/code_searcher/blob/master/CHANGELOG.rst>`_.

Contributing
============

- Fork it (<https://github.com/stas-prokopiev/code_searcher/fork>)
- Create your feature branch (`git checkout -b feature/fooBar`)
- Commit your changes (`git commit -am 'Add some fooBar'`)
- Push to the branch (`git push origin feature/fooBar`)
- Create a new Pull Request

Contacts
========

    * Email: stas.prokopiev@gmail.com

    * `vk.com <https://vk.com/stas.prokopyev>`_

    * `Facebook <https://www.facebook.com/profile.php?id=100009380530321>`_

License
=======

This project is licensed under the MIT License.
