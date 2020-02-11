# -*- coding: utf-8 -*-
import os
import code_searcher
from code_searcher.code_searcher_class import code_searcher_class

__author__ = "stanislav prokopyev"
__copyright__ = "stanislav prokopyev"
__license__ = "mit"


def test_code_searcher_class():
    """"""
    str_code_searcher_file = os.path.abspath(code_searcher.__file__)
    str_folder_with_files = os.path.dirname(str_code_searcher_file)
    list_str_folders_where_to_look = [str_folder_with_files]
    code_searcher_obj = code_searcher_class(
        list_str_folders_where_to_look,
        list_str_file_extensions=[".py"],
    )
    #####
    # Test search_code_in_the_library
    int_occurrences = \
        code_searcher_obj.search_code_in_the_library(
            str("class code_searcher_class")
        )
    assert int_occurrences == 1, \
        "ERROR: 'search_code_in_the_library' not working"
    #####
    # Test get_number_of_lines_in_the_library
    int_lines = code_searcher_obj.get_number_of_lines_in_the_library()
    assert int_lines > 500, \
        "ERROR: 'get_number_of_lines_in_the_library' not working"
    #####
    # Test print_places_where_line_length_exceed_N
    int_times = code_searcher_obj.print_places_where_line_length_exceed_N(
        int_max_length=80,
    )
    assert int_times < 200, \
        "ERROR: 'print_places_where_line_length_exceed_N' not working"
    #####
    # Test get_names_functions_defined_in_the_py_library
    set_names = \
        code_searcher_obj.get_names_functions_defined_in_the_py_library()
    assert len(set_names) > 10, \
        "ERROR: 'get_names_functions_defined_in_the_py_library' not working"
    #####
    # Test get_names_of_all_py_functions_defined_but_never_used
    code_searcher_obj.get_names_of_all_py_functions_defined_but_never_used()
    #####
    # Test get_list_imported_modules_in_the_py_library
    list_mod = \
        code_searcher_obj.get_list_imported_modules_in_the_py_library()
    assert len(list_mod) > 1, \
        "ERROR: 'get_list_imported_modules_in_the_py_library' not working"
    #####
    return 0
