# -*- coding: utf-8 -*-
# Standard library imports
import os
import logging

# Third party imports

# Local imports
import code_searcher
from code_searcher.code_searcher_class import code_searcher_class

logging.basicConfig(level=logging.DEBUG)


def test_code_searcher_class():
    """"""
    str_code_searcher_file = os.path.abspath(code_searcher.__file__)
    str_folder_with_files = os.path.dirname(str_code_searcher_file)
    code_searcher_obj = code_searcher_class(
        [str_folder_with_files],
        list_str_file_extensions=[".py", ".ipynb"],
    )
    #####
    # Test main search functions search
    int_occurrences = \
        code_searcher_obj.search("class code_searcher_class")
    assert int_occurrences == 1, "ERROR: 'search' is not working"
    int_occurrences = code_searcher_obj.search(
        "CLASS code_searcher_class",
        bool_is_to_search_case_sensitive=True,
    )
    assert int_occurrences == 0, \
        "ERROR: 'bool_is_to_search_case_sensitive' is not working"
    code_searcher_obj.search_with_re("^def ")
    #####
    print(code_searcher_obj)
    code_searcher_obj.download_all_files()
    code_searcher_obj.update_files()
    code_searcher_obj.get_dict_list_file_paths_by_ext_by_dir()
    code_searcher_obj.get_file_stats_of_the_code_library()
    #####



    return 0
