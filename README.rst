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

Also, this package allows you get some statistics about your project.

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
    list_str_folders_where_to_look = ["path_to_folder_1", "path_to_folder_2", ...]
    code_searcher_obj = code_searcher_class(
            list_str_folders_where_to_look,
            list_str_file_extensions=[".py", "ipynb"],
    )



1) To find all occurrences of some code.
--------------------------------------------------------------------------------------------------

*You've changed a function signature and want to do necessary changes in the library.*

*To find all the places where this function was used use the code below*

.. code-block:: python

    code_searcher_obj.search_all_occurrences_of_the_code_in_the_library(
        str_code_to_search="previous_function_name(",
        bool_is_to_search_case_sensitive=True,
    )

2) To see some statistics about your library.
------------------------------------------------------

.. code-block:: python

    print(code_searcher_obj)

3) To reload files to up to date versions before searching.
--------------------------------------------------------------------------------------------------

*You've changed something inside code of your library and want update code for code_searcher*

.. code-block:: python

    code_searcher_obj.update_files()
    ... Code from point 1 ...

4) To get the number of not empty code lines in the library
--------------------------------------------------------------------------------------------------

*It can be used to measure your everyday performance*

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
