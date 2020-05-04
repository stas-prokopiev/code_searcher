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
        "ERROR: 'search_code_in_the_library' is not working"
    #####
    return 0
