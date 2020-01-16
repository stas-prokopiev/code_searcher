=============
CODE_SEARCHER
=============

Overview
========

code_searcher is a simple Python package(**py>=2.7 or py>=3.4**) with the main purpose to
help support changes in any function signature inside your project.

(Currently, fully supported file types are **.py** and **.ipynb**
nonetheless, search functional can be applied to any file extensions which can be read as plain text in utf-8 encoding).

It's becoming quite useful when your project outgrows 1k lines of code and manual replacement becomes too annoying (Too easy to overlook replacement somewhere).

Also, this package allows you to get some statistics about your project. For more info check section: **Typical examples of Usage**

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

    code_searcher_obj.search_all_occurrences_of_the_code_in_the_library(
        str_code_to_search="previous_function_name(",
        bool_is_to_search_case_sensitive=True,
    )

*Output:*

.. code-block:: console

    For folder: c:\users\stanislav\desktop\my_python_projects\code_search_engine\project\code_searcher\src\code_searcher
    --> For extension: .py
    ----> Found in:  additional_functions.py
    ------>  0 ) line: 17  Code_line: def get_names_of_all_functions_defined_in_py_code(str_py_code):
    ------>  1 ) line: 31  Code_line: list_all_defines_start = str_py_code.split("def ")


2) To see some statistics about your library.
------------------------------------------------------

.. code-block:: python

    print(code_searcher_obj)
    
*Output:*

.. code-block:: console

    Folders to search in: 
    --> c:\users\stanislav\desktop\my_python_projects\code_search_engine\project\code_searcher\src\code_searcher
    --> C:/Users/Stanislav/Desktop/websim/ALL_WEBSIM_SCRIPTS/working_with_EXPRESSION_alphas/DASHBOARD
    Extensions to check: 
    --> .py
    --> ipynb

    Files Statistic of current code library:
    --> For folder: c:\users\stanislav\desktop\my_python_projects\code_search_engine\project\code_searcher\src\code_searcher
    --> Files_found = 5  Code_lines = 981
    ----> .py:  Files_found = 5;  Code_lines = 981;  
    ----> ipynb:  Files_found = 0;  Code_lines = 0;  
    ===============================================================================
    --> For folder: C:/Users/Stanislav/Desktop/websim/ALL_WEBSIM_SCRIPTS/working_with_EXPRESSION_alphas/DASHBOARD
    --> Files_found = 4  Code_lines = 175
    ----> .py:  Files_found = 0;  Code_lines = 0;  
    ----> ipynb:  Files_found = 4;  Code_lines = 175;  
    ===============================================================================

3) To add new files to examine.
--------------------------------------------------------------------------------------------------

*You've created a new file inside folder given to code_searcher and want update files for code_searcher so that it will be checked too*

.. code-block:: python

    code_searcher_obj.update_files()
    # Any code

4) To get the number of not empty code lines in the library
--------------------------------------------------------------------------------------------------

*It can be used to measure your everyday performance*

.. code-block:: python

    code_searcher_obj.get_number_of_lines_in_the_library()

5) To check which functions were defined but never used. (NOT STABLE)
--------------------------------------------------------------------------------------------------

*It can be used in order to have your library as short as possible.*

.. code-block:: python

    code_searcher_obj.get_names_of_all_py_functions_defined_but_never_used()

*Output:*

.. code-block:: console

    Found functions defined:  18
    Found never used functions:  4
    ['check_type_of_arguments',
     'echo_func',
     'get_dict_str_full_file_by_rel_path',
     'hello']

6) To check which OUTER modules were imported in the library. (NOT STABLE)
--------------------------------------------------------------------------------------------------

*It can be used in order to have only used packages in the virtual environment*

.. code-block:: python

    code_searcher_obj.get_list_of_all_outer_modules_used_in_the_library()

*Output:*

.. code-block:: console

    Overall unique modules imported:  12
    Overall OUTER unique modules imported:  12
    ['__future__',
     'code_searcher',
     'codecs',
     'collections',
     'init_notebook_mode',
     'json',
     'os',
     'plotly',
     'sys',
     'time',
     'tools',
     'tqdm']


Links
=====

    * `Pypi <https://pypi.org/project/code-searcher/>`_

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
