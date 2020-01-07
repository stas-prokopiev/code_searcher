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
    int_occurences = \
        code_searcher_obj.search_all_occurrences_of_the_code_in_the_library(
            "class code_searcher_class"
        )
    assert int_occurences == 1, "ERROR: my_tmp"


# import unittest
# class Test_code_searcher(unittest.TestCase):

#     def test_code_searching(self):
#         """"""
#         str_code_searcher_file = os.path.abspath(code_searcher.__file__)
#         str_folder_with_files = os.path.dirname(str_code_searcher_file)
#         list_str_folders_where_to_look = [str_folder_with_files]
#         code_searcher_obj = code_searcher_class(
#             list_str_folders_where_to_look,
#             list_str_file_extensions=[".py"],
#         )
#         int_occurences = \
#             code_searcher_obj.search_all_occurrences_of_the_code_in_the_library(
#                 "class code_searcher_class"
#             )
#         self.assertEqual(int_occurences, 1)


# if __name__ == "__main__":
#     unittest.main()
