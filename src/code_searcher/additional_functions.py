 # -*- coding: utf-8 -*-
"""

This module is consists of additional functions for code searching
through your library.
"""
# Standard library imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import re
import os

# Third party imports

# Local imports


def search_code_in_the_library_common_processes(
        dict_str_file_by_path_by_ext_by_dir,
        func_check_if_string_is_in_the_line,
        str_code_to_search,
        bool_is_to_search_case_sensitive=True,
):
    """Searching some code inside whole library

    Searching some code inside whole library and
    print all occurrences in nice formatted way

    Parameters
    ----------
    func_check_if_string_is_in_the_line : function
        Function which should check if string is inside another string
    str_code_to_search : str
        Code to search in the library
    bool_is_to_search_case_sensitive : bool, optional
        A flag if to search cas sensitive (default is True)

    Returns
    -------
    int
        times occurrences of code found in whole library
    """
    # 1) If not necessary to search case sensitive, then lower everything
    if not bool_is_to_search_case_sensitive:
        str_code_to_search = str_code_to_search.lower()
    int_occurrences_found = 0
    print("=" * 79)
    # For every folder searching through all files inside folder
    for str_dir in dict_str_file_by_path_by_ext_by_dir:
        dict_str_file_by_path_by_ext = \
            dict_str_file_by_path_by_ext_by_dir[str_dir]
        print("For folder: {folder}".format(folder=str_dir))
        for str_ext in dict_str_file_by_path_by_ext:
            if len(dict_str_file_by_path_by_ext) > 1:
                print("")
            print("--> For extension: {extension}".format(
                extension=str_ext
            ))
            bool_is_entry_found_for_cur_ext = False
            dict_str_file_by_path = dict_str_file_by_path_by_ext[str_ext]
            # For every file search occurrences of asked code
            for str_file_path in dict_str_file_by_path:
                str_rel_path = os.path.relpath(str_file_path, str_dir)
                str_full_file = dict_str_file_by_path[str_file_path]
                if not bool_is_to_search_case_sensitive:
                    str_full_file = str_full_file.lower()
                list_str_file_splitted = enumerate(
                    str_full_file.splitlines()
                )
                #####
                # Line by line searching for asked code
                bool_is_entry_found_for_cur_file = False
                for int_line_num, str_line in list_str_file_splitted:
                    if func_check_if_string_is_in_the_line(
                        str_code_to_search,
                        str_line,
                    ):
                        if not bool_is_entry_found_for_cur_file:
                            bool_is_entry_found_for_cur_file = True
                            bool_is_entry_found_for_cur_ext = True
                            print("----> Found in: ", str_rel_path)
                        print(
                            "------> {})".format(int_occurrences_found),
                            "line:", int_line_num,
                            " Code_line:", str_line.strip()
                        )
                        int_occurrences_found += 1
            #####
            if not bool_is_entry_found_for_cur_ext:
                print("----> NOTHING FOUND.")
        #####
        if int_occurrences_found:
            print("=" * 79)
    print("Overall occurrences found: ", int_occurrences_found)
    return int_occurrences_found


def bool_simple_search_of_code(str_code_to_search, str_where_to_search):
    """Getting names of all modules imported in the python code

    Parameters
    ----------
    str_py_code : str
        code where to search for imported modules

    Returns
    -------
    bool
        If string is inside another string
    """
    bool_is_code_found = str_code_to_search in str_where_to_search
    if not bool_is_code_found:
        return False
    #####
    str_in_quotes_1 = "'{}'".format(str_code_to_search)
    str_in_quotes_2 = '"{}"'.format(str_code_to_search)
    bool_is_code_in_quotes = (
        (str_in_quotes_1 in str_where_to_search) or
        (str_in_quotes_2 in str_where_to_search)
    )
    if bool_is_code_in_quotes:
        return False
    return True


def bool_search_of_code_with_re(str_re_pattern, str_where_to_search):
    """Getting names of all modules imported in the python code

    Parameters
    ----------
    str_py_code : str
        code where to search for imported modules

    Returns
    -------
    bool
        If string is inside another string
    """
    return bool(re.findall(str_re_pattern, str_where_to_search))


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

