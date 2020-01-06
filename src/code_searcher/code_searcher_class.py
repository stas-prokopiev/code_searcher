# -*- coding: utf-8 -*-
"""
code_searcher.code_searcher_class
~~~~~~~~~~~~

This module is consists of main class for code searching through your
library

:copyright: © 2019 by Stanislav Prokopyev stas.prokopiev@gmail.com.
:license: MIT, see LICENSE.rst for more details.
"""
from __future__ import print_function
import time

from collections import defaultdict
from collections import OrderedDict
from collections import Counter


from code_searcher.decorators import check_type_of_arguments
from code_searcher.working_with_files import get_dict_str_full_file_by_rel_path
from code_searcher.additional_functions import get_names_of_all_functions_defined_in_py_code
from code_searcher.additional_functions import get_list_modules_imported_in_py_code
from code_searcher.working_with_files import \
    get_list_str_filenames_of_all_files_with_given_extension


class code_searcher_class():
    """
    A class used to do search operations on whole code of project

    ...

    Attributes
    ----------
    list_str_folders_where_to_look : list
        list most parent folders where to look for code files
    list_str_file_extensions : list
        list strings file extensions which files to explore
    dict_dict_str_file_by_filename_by_folder : dict
        {folder_path: {relative_file_path: string_whole_file, ...}, ...}

    Methods
    -------
    search_all_occurrences_of_some_code_in_my_python_library(
    str_code_to_search,
    bool_is_to_search_case_sensitive=True,
    )
        Searching some code inside whole library and
        print all occurences in formatted way

    update_files()
        Redownloading all files if something was changed inside them

    get_file_stats_of_the_code_library(bool_is_to_print=False)
        Getting string statistic about files in the library

    get_dict_times_functions_used()
        Getting {function_name: times_function_used, ...}

    get_names_of_all_functions_defined_but_never_used()
        Getting list of functions defined inside code but never used

    get_number_of_lines_in_the_library()
        Getting number of not empty lines in whole library

    get_list_of_all_outer_modules_used_in_library()
        Getting list of all OUTER modules imported in the library
    """

    @check_type_of_arguments
    def __init__(
            self,
            list_str_folders_where_to_look,
            list_str_file_extensions=[".py", "ipynb"],
    ):
        """
        Parameters
        ----------
        list_str_folders_where_to_look : list
            list most parent folders where to look for code files
        list_str_file_extensions : list, optional
            list strings file extensions which files to explore
            (default is [".py", "ipynb"])
        """
        # 0) Check that as least some arguments are given
        assert list_str_folders_where_to_look is not None, (
            "ERROR: for initializing code_searcher obj should be given \n"
            "list of most parent folders where to search files with code \n"
            "var list_str_folders_where_to_look: SHOULD NOT BE NONE"
        )
        # 1) Initialize class variables
        self.list_str_folders_where_to_look = list_str_folders_where_to_look
        self.list_str_file_extensions = list_str_file_extensions
        # Initialize dict_dict_str_file_by_filename_by_folder
        self.download_files()
        # # Print file statistic
        # self.get_file_stats_of_the_code_library(bool_is_to_print=True)
        # print("Search obj INITIALIZED.")

    @check_type_of_arguments
    def __repr__(self):
        """Representation of obj

        Returns
        -------
        str
            representation of the obj
        """
        str_obj_repr = ""
        str_obj_repr += (
            "This is obj that allows you to search through "
            "your project codebase for code in python and ipynb files\n\n"
        )
        str_obj_repr += "Folders to search in: \n"
        for str_folder in self.list_str_folders_where_to_look:
            str_obj_repr += "--> " + str_folder + "\n"
        str_obj_repr += "Extensions to check: \n"
        for str_extension in self.list_str_file_extensions:
            str_obj_repr += "--> " + str_extension + "\n"
        str_obj_repr += self.get_file_stats_of_the_code_library()
        return str_obj_repr

    @check_type_of_arguments
    def get_file_stats_of_the_code_library(self, bool_is_to_print=False):
        """Getting string statistic about files in the library

        Parameters
        ----------
        bool_is_to_print : bool, optional
            Flag if to print file statistic or just return it
            (default is False)

        Returns
        -------
        str
            File statistic of current obj
        """
        str_stats = ""
        int_code_lines = self.get_number_of_lines_in_the_library()
        str_stats += "Code lines: " + str(int_code_lines) + "\n\n"
        str_stats += "Files Statistic of current code library:\n"
        # Print file statistic for every folder
        for str_folder in self.dict_dict_str_file_by_filename_by_folder:
            counter_int_files_by_extension = Counter()
            dict_str_file_by_filename = \
                self.dict_dict_str_file_by_filename_by_folder[str_folder]
            list_filenames = list(dict_str_file_by_filename.keys())
            str_stats += "--> For folder: " + str(str_folder)
            str_stats += " found files with extensions:\n"
            #####
            # Count number of files with every extension
            for str_extension in self.list_str_file_extensions:
                for str_filename in list_filenames:
                    if str_filename.endswith(str_extension):
                        counter_int_files_by_extension[str_extension] += 1
                        # counter_int_files_by_extension["overall"] += 1
            #####
            # Add number of files with every extension to stats
            for str_extension in counter_int_files_by_extension:
                str_stats += "----> {extension}: {int_files}\n".format(
                    extension=str_extension,
                    int_files=counter_int_files_by_extension[str_extension]
                )
            #####
            str_stats += "=" * 79 + "\n"
        if bool_is_to_print:
            print(str_stats)
        return str_stats

    @check_type_of_arguments
    def download_files(self):
        """Download code files in dict_dict_str_file_by_filename_by_folder"""
        float_time_start = time.time()
        dict_dict_str_file_by_filename_by_folder = OrderedDict()
        # For every folder where to look download code files
        for str_folder_path in self.list_str_folders_where_to_look:
            dict_str_full_file_by_rel_path = OrderedDict()
            for str_extension in self.list_str_file_extensions:
                dict_str_full_file_by_rel_path_tmp = \
                    get_dict_str_full_file_by_rel_path(
                        str_folder_path,
                        str_extension_to_look_for=str_extension,
                    )
                dict_str_full_file_by_rel_path.update(
                    dict_str_full_file_by_rel_path_tmp
                )
            dict_dict_str_file_by_filename_by_folder[str_folder_path] = \
                dict_str_full_file_by_rel_path
        self.dict_dict_str_file_by_filename_by_folder = \
            dict_dict_str_file_by_filename_by_folder
        float_seconds_spent = round(time.time() - float_time_start, 2)
        print(
            "Files were downloaded in {} seconds".format(float_seconds_spent)
        )

    @check_type_of_arguments
    def update_files(self):
        """Redownload code files in dict_dict_str_file_by_filename_by_folder"""
        self.download_files()

    @check_type_of_arguments
    def search_all_occurrences_of_the_code_in_the_library(
            self,
            str_code_to_search,
            bool_is_to_search_case_sensitive=True,
    ):
        """Searching some code inside whole library and
        print all occurences in formatted way

        Parameters
        ----------
        str_code_to_search : str
            Code to search in the library
        bool_is_to_search_case_sensitive : bool, optional
            A flag if to search cas sensitive (default is True)

        Returns
        -------
        int
            times occurences of code found in whole library
        """
        if not bool_is_to_search_case_sensitive:
            str_code_to_search = str_code_to_search.lower()
        int_occurrences_found = 0
        # For every folder searching through all files inside folder
        for str_folder_name in self.dict_dict_str_file_by_filename_by_folder:
            dict_str_full_file_by_rel_path = \
                self.dict_dict_str_file_by_filename_by_folder[str_folder_name]
            print("For folder: {folder}\nFiles found: {int_files}".format(
                folder=str_folder_name,
                int_files=len(dict_str_full_file_by_rel_path)),
            )
            # For every file search occurences of asked code
            for str_filename in dict_str_full_file_by_rel_path:
                str_full_file = dict_str_full_file_by_rel_path[str_filename]
                if not bool_is_to_search_case_sensitive:
                    str_full_file = str_full_file.lower()
                list_str_file_splitted = enumerate(str_full_file.splitlines())
                # Line by line searching for asked code
                for int_line_num, str_line in list_str_file_splitted:
                    if str_code_to_search in str_line:
                        print(
                            "--> ", int_occurrences_found,
                            ") Found in: ", str_filename
                        )
                        print(
                            "----> line: ", int_line_num,
                            " Code_line: ", str_line.strip()
                        )
                        int_occurrences_found += 1
                #####
                if int_occurrences_found:
                    print("#" * 79)
        print("Overall occurrences found: ", int_occurrences_found)
        return int_occurrences_found

    @check_type_of_arguments
    def get_dict_times_functions_used(self):
        """Getting {function_name: times_function_used, ...}

        Returns
        -------
        dict
            {function_name: times_function_used, ...}
        """
        defdict_times_functions_used = defaultdict(int)
        set_str_funcs_defined_in_the_library = \
            self.get_names_of_all_functions_defined_in_the_py_library()
        # For every folder searching through all files inside folder
        for str_folder in self.dict_dict_str_file_by_filename_by_folder:
            dict_str_full_file_by_rel_path = \
                self.dict_dict_str_file_by_filename_by_folder[str_folder]
            # For every file searching all occurences of function definition
            for str_filename in dict_str_full_file_by_rel_path:
                str_full_file = dict_str_full_file_by_rel_path[str_filename]
                for str_func_to_count in set_str_funcs_defined_in_the_library:
                    defdict_times_functions_used[str_func_to_count] += \
                        str_full_file.count(str_func_to_count + "(")
        #####
        # Subtract 1 from times every function used, as its function definition
        for str_func_name in defdict_times_functions_used:
            defdict_times_functions_used[str_func_name] -= 1
        return defdict_times_functions_used

    @check_type_of_arguments
    def get_names_of_all_functions_defined_but_never_used(self):
        """Getting list of functions defined inside code but never used

        Returns
        -------
        list
            list names of never used functions inside the code library
        """
        defdict_times_functions_used = self.get_dict_times_functions_used()
        list_str_never_used_functions = []
        for str_func_name in defdict_times_functions_used:
            if not defdict_times_functions_used[str_func_name]:
                list_str_never_used_functions.append(str_func_name)
        print(
            "Found never used functions: ",
            len(list_str_never_used_functions)
        )
        return sorted(list_str_never_used_functions)

    @check_type_of_arguments
    def get_number_of_lines_in_the_library(self):
        """Getting number of not empty lines in whole library

        Returns
        -------
        int
            Number of Not empty code lines in the library
        """
        int_lines_of_code_already_found = 0
        for str_folder in self.dict_dict_str_file_by_filename_by_folder:
            dict_str_file_by_filename = \
                self.dict_dict_str_file_by_filename_by_folder[str_folder]
            for str_filename in dict_str_file_by_filename:
                str_whole_file = dict_str_file_by_filename[str_filename]
                int_lines_of_code_already_found += \
                    str_whole_file.count('\n') + 1
        return int_lines_of_code_already_found

    @check_type_of_arguments
    def get_names_of_all_functions_defined_in_the_py_library(self):
        """Getting set names of all functions defined in the library

        Returns
        -------
        set
            set names of all functions defined in the library
        """
        list_str_all_functions_defined_in_the_library = []
        for str_folder in self.dict_dict_str_file_by_filename_by_folder:
            dict_str_full_file_by_rel_path = \
                self.dict_dict_str_file_by_filename_by_folder[str_folder]
            for str_filename in dict_str_full_file_by_rel_path:
                str_full_file = dict_str_full_file_by_rel_path[str_filename]
                list_str_all_functions_defined_in_the_library += \
                    get_names_of_all_functions_defined_in_py_code(
                        str_full_file
                    )
        set_str_all_functions_defined_in_the_library = \
            set(list_str_all_functions_defined_in_the_library)
        print(
            "Found functions defined: ",
            len(set_str_all_functions_defined_in_the_library)
        )
        return set_str_all_functions_defined_in_the_library

    @check_type_of_arguments
    def get_set_str_names_of_all_py_files(self):
        """Getting set names of all .py files inside the library

        Returns
        -------
        set
            set names of all .py files inside the library
        """
        list_names_of_all_py_files_in_library = []
        for str_folder_where_to_look in self.list_str_folders_where_to_look:
            list_names_of_all_py_files_in_library += \
                get_list_str_filenames_of_all_files_with_given_extension(
                    str_folder_where_to_look,
                    str_extension_to_look_for=".py"
                )
        return set(list_names_of_all_py_files_in_library)

    @check_type_of_arguments
    def get_all_imported_py_modules_in_the_library(self):
        """Getting list of all modules imported in the library
        Returns
        -------
        list
            list names of all imported modules found
        """
        list_imported_modules_found = []
        for str_folder in self.dict_dict_str_file_by_filename_by_folder:
            dict_my_python_file_by_file_name = \
                self.dict_dict_str_file_by_filename_by_folder[str_folder]
            print(
                "Overall files found: ",
                len(dict_my_python_file_by_file_name)
            )
            #####
            # One by one dealing with every file
            for str_filename in dict_my_python_file_by_file_name:
                str_full_code_of_one_py_file = \
                    dict_my_python_file_by_file_name[str_filename]
                list_imported_modules_found += \
                    get_list_modules_imported_in_py_code(
                        str_full_code_of_one_py_file
                    )
        list_imported_modules_found = list(set(list_imported_modules_found))
        return list_imported_modules_found

    @check_type_of_arguments
    def get_list_of_all_outer_modules_used_in_the_library(self):
        """Getting list of all OUTER modules imported in the library
        Returns
        -------
        list
            list names of all OUTER imported modules found
        """
        print("Getting list of all used outer modules in python library")
        set_str_names_of_all_py_files = \
            self.get_set_str_names_of_all_py_files()
        list_imported_modules_found = \
            self.get_all_imported_py_modules_in_the_library()
        print(
            "Overall unique modules imported: ",
            len(list_imported_modules_found)
        )
        #####
        # Delete inner modules from all modules imported
        list_outer_modules_found = []
        for str_my_py_module in list_imported_modules_found:
            if str_my_py_module not in set_str_names_of_all_py_files:
                list_outer_modules_found.append(str_my_py_module)
        print(
            "Overall OUTER unique modules imported: ",
            len(list_outer_modules_found)
        )
        return sorted(list_outer_modules_found)




