=============
CODE_SEARCHER
=============

Overview
========

code_searcher is a simple Python module with the main purpose is to
help support changes in any function signature inside your project
(Currently supported file types are **.py** and **.ipynb**).
It's becoming quite useful when your project outgrows 1k lines of code and manual replacement becomes too annoying.

Also, this package allows you get some statistics about your project for more info check section: **Typical examples of Usage**

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
    list_str_file_extensions = ["path_to_folder_1", "path_to_folder_2", ...]
    code_searcher_obj = code_searcher_class(
            list_str_folders_where_to_look,
            list_str_file_extensions=[".py", "ipynb"],
    )



1) You've changed a function signature and want to do necessary changes in the library.
--------------------------------------------------------------------------------------------------

.. code-block:: python

    code_searcher_obj.search_all_occurrences_of_the_code_in_the_library(
        str_code_to_search="previous_function_name(",
        bool_is_to_search_case_sensitive=True,
    )

2) To see some statistics about your library.
------------------------------------------------------

.. code-block:: python

    print(code_searcher_obj)

3) You've updated files and want to download up to date versions before searching.
--------------------------------------------------------------------------------------------------

.. code-block:: python

    code_searcher_obj.update_files()
    ... Code from point 1 ...

4) To get the number of not empty code lines in the library
--------------------------------------------------------------------------------------------------

.. code-block:: python

    code_searcher_obj.get_number_of_lines_in_the_library()

5) To check which functions were defined but never used. (NOT STABLE)
--------------------------------------------------------------------------------------------------

*It can be used in order to have your library as short as possible.*

.. code-block:: python

    code_searcher_obj.get_names_of_all_functions_defined_but_never_used()

6) To check which OUTER modules were imported in the library. (NOT STABLE)
--------------------------------------------------------------------------------------------------

*It can be used in order to have only used packages in the virtual environment*

.. code-block:: python

    code_searcher_obj.get_list_of_all_outer_modules_used_in_the_library()

Full elaboration on code_searcher_obj
======================================

code_searcher_obj attributes
----------------------------
    **list_str_folders_where_to_look**: list
        *list most parent folders where to look for code files*

    **list_str_file_extensions** : list
        *list strings file extensions which files to explore*

    **dict_dict_str_file_by_filename_by_folder** : dict
        *{folder_path: {relative_file_path: string_whole_file, ...}, ...}*

code_searcher_obj Methods
-------------------------

    **search_all_occurrences_of_some_code_in_my_python_library**
        *Searching some code inside whole library and print all occurrences in a formatted way*

    **update_files**
        *Redownloading all files if something was changed inside them*

    **get_file_stats_of_the_code_library**
        *Getting string statistic about files in the library*

    **get_dict_times_functions_used**
        *Getting {function_name: times_function_used, ...}*

    **get_names_of_all_functions_defined_but_never_used**
        *Getting the list of functions defined inside code but never used*

    **get_number_of_lines_in_the_library**
        *Getting number of not empty lines in the whole library*

    **get_list_of_all_outer_modules_used_in_library**
        *Getting list of all OUTER modules imported in the library*

Contacts
========

    * email: stas.prokopiev@gmail.com

    * `vk.com <https://vk.com/stas.prokopyev>`_

    * `Facebook <https://www.facebook.com/profile.php?id=100009380530321>`_

License
=======

This project is licensed under the MIT License.
