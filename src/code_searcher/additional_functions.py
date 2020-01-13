# -*- coding: utf-8 -*-
"""
code_searcher.additional_functions
~~~~~~~~~~~~

This module is consists of additional functions for code searching
through your library.
Very UNLIKELY that you will need them.

:copyright: © 2019 by Stanislav Prokopyev stas.prokopiev@gmail.com.
:license: MIT, see LICENSE.rst for more details.
"""
from __future__ import print_function
from code_searcher.decorators import check_type_of_arguments


@check_type_of_arguments
def get_names_of_all_functions_defined_in_py_code(str_py_code):
    """Getting names of all functions defined in the python code

    Parameters
    ----------
    str_py_code : str
        code where to search for functions definitions

    Returns
    -------
    list
        All found function names
    """
    list_names_of_all_functions_defined = []
    list_all_defines_start = str_py_code.split("def ")
    for str_def_start in list_all_defines_start[1:]:
        str_func_name = str_def_start.rstrip().split("(")[0]
        if "(self" in str_def_start:
            continue
        list_names_of_all_functions_defined.append(str_func_name)
    return list_names_of_all_functions_defined


@check_type_of_arguments
def get_list_modules_imported_in_py_code(str_py_code):
    """Getting names of all modules imported in the python code

    Parameters
    ----------
    str_py_code : str
        code where to search for imported modules

    Returns
    -------
    list
        names of all imported modules found
    """

    list_imported_modules_found = []
    # One by one dealing with every code line
    for str_one_code_line in str_py_code.splitlines():
        str_one_code_line = str_one_code_line.strip()
        if str_one_code_line.startswith("from "):
            str_module_name_start = \
                str_one_code_line.split("from ")[1].strip()
            str_module_name = str_module_name_start.split(" ")[0]
            str_module_name = str_module_name.split(",")[0]
            str_module_name = str_module_name.split(".")[0]
            list_imported_modules_found.append(str_module_name)
            # print(str_one_code_line.strip())
            # print("---> ", str_module_name, "\n")
            continue
        #####
        if "import " in str_one_code_line:
            str_module_name_start = \
                str_one_code_line.split("import ")[1].strip()
            str_module_name = str_module_name_start.split(" ")[0]
            str_module_name = str_module_name.split(",")[0]
            str_module_name = str_module_name.split(".")[0]
            list_imported_modules_found.append(str_module_name)
            # print(str_one_code_line.strip())
            # print("---> ", str_module_name, "\n")
            continue
    return list_imported_modules_found


def get_number_of_lines_in_string(str_string):
    """Get number of not empty code lines in the string

    Parameters
    ----------

    Returns
    -------
    int
        Number of not empty code lines in the string
    """
    int_lines = 0
    for str_line in str_string.splitlines():
        if str_line.strip():
            int_lines += 1
    return int_lines





