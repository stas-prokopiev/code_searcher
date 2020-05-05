# -*- coding: utf-8 -*-
"""

This module is consists of main class for code searching through your
code library.
"""
# Standard library imports
import time
import os
import re
from collections import defaultdict
from collections import OrderedDict

# Third party imports

# Local imports
from code_searcher import working_with_files
from code_searcher import additional_functions


class code_searcher_class:
    """
    A class used to do search operations on whole code of project

    ...

    Attributes
    ----------
    self.list_str_dirs_where_to_look : list
        list most parent folders where to look for code files
    self.list_str_file_extensions : list
        list strings file extensions which files to explore
    self.dict_time_file_changed_by_path : dict
        {"path_to_file_1": float_time_when_last_modified, ...}
    self.dict_list_file_paths_by_ext_by_dir : dict
        dict with pathes of all initialized files
        {"folder_path_1": {"file_extension_1": [file_path_1, ...], ...}, ...}
    self.dict_str_file_content_by_file_path : dict
        {"file_path_1": file_1_content, "file_path_2": file_2_content, ...}
    self.time_when_last_time_downloaded_files : float
        time.time() when last time downloaded files
        (need for not redownloading too often at least after 1 seconds)

    Methods
    -------
    get_file_stats_of_the_code_library(...)
        Getting string with statistics about files in the library

    get_dict_list_file_paths_by_ext_by_dir(...)
        Getting dict with pathes to asked files by ext by dir

    download_all_files(...)
        For all files defined in self.dict_list_file_paths_by_ext_by_dir
        download up to date versions of files (Efficient realization)

    update_files(...)
        Re-search for all files in the folders and download them

    search(...)
        Searching some code inside whole library and
        print all occurrences in nice formatted way

    search_with_re(...)
        Searching some code inside library using regular expressions

    """

    def __init__(
        self,
        list_str_dirs_where_to_look,
        list_str_file_extensions=[".py", "ipynb"],
    ):
        """Init object

        Parameters
        ----------
        list_str_dirs_where_to_look : list
            list most parent folders where to look for code files
        list_str_file_extensions : list, optional
            list strings file extensions which files to explore
            (default is [".py", "ipynb"])
        """
        # 0) Check that as least some arguments are given
        assert list_str_dirs_where_to_look, (
            "ERROR: for initializing code_searcher obj should be given \n"
            "list of folders where to search files with code \n"
            "var list_str_dirs_where_to_look: SHOULD NOT BE EMPTY"
        )
        # 1) Initialize class variables
        # Take absolute path of list folders where to look for code files
        self.list_str_dirs_where_to_look = [
            os.path.abspath(str_dir).lower()
            for str_dir in list_str_dirs_where_to_look
        ]
        # list strings file extensions which files to explore
        self.list_str_file_extensions = list_str_file_extensions
        # {"path_to_file_1": float_time_when_last_modified, ...}
        self.dict_time_file_changed_by_path = defaultdict(float)
        self.dict_str_file_content_by_file_path = {}

        print("Downloading all files (it can be a long process, please wait.)")
        float_time_start = time.time()
        # {"folder_path_1": {"file_extension_1": [file_path_1, ...], ...}, ...}
        self.dict_list_file_paths_by_ext_by_dir = (
            self.get_dict_list_file_paths_by_ext_by_dir()
        )
        self.time_when_last_time_downloaded_files = 0.0
        int_files_downloaded = self.download_all_files()
        print(
            "{} Files were downloaded in {} seconds".format(
                int_files_downloaded,
                round(time.time() - float_time_start, 2)
            )
        )

    def __repr__(self):
        """Representation of obj

        Returns
        -------
        str
            representation of the obj
        """
        self.download_all_files()
        str_obj_repr = ""
        str_obj_repr += (
            "This is an obj that allows you to search through "
            "your project codebase\n"
            "for getting names of available functions "
            "use help() on current obj"
            "\n\n"
        )
        str_obj_repr += "Folders to search in: \n"
        for str_dir in self.list_str_dirs_where_to_look:
            str_obj_repr += "--> " + str_dir + "\n"
        str_obj_repr += "Extensions to check: \n"
        for str_ext in self.list_str_file_extensions:
            str_obj_repr += "--> " + str_ext + "\n"
        str_obj_repr += self.get_file_stats_of_the_code_library()
        return str_obj_repr

    def get_file_stats_of_the_code_library(self):
        """Getting string with statistics about files in the library

        Parameters
        ----------

        Returns
        -------
        str
            File statistic of current obj
        """

        self.download_all_files()
        str_stats = "\n"
        str_stats += "Files Statistic of current code library:\n"
        # Print file statistic for every folder
        for str_dir in self.dict_list_file_paths_by_ext_by_dir:
            str_stats_dir = ""
            str_stats_dir += "--> For folder: " + str(str_dir) + "\n"
            int_files_in_folder = 0
            int_lines_in_folder = 0
            str_stats_dir += "--> Files_found = {int_files_in_dir}  "
            str_stats_dir += "Code_lines = {int_lines_in_dir}\n"
            dict_list_file_paths_by_ext = \
                self.dict_list_file_paths_by_ext_by_dir[str_dir]
            # Count number of files with every extension
            for str_ext in dict_list_file_paths_by_ext:
                list_file_paths = dict_list_file_paths_by_ext[str_ext]
                int_code_lines = 0
                for str_file_path in list_file_paths:
                    str_full_file = \
                        self.dict_str_file_content_by_file_path[str_file_path]
                    int_code_lines += str_full_file.count("\n")
                int_files = len(list_file_paths)
                #####
                int_files_in_folder += int_files
                int_lines_in_folder += int_code_lines
                #####
                # Add number of files with every extension to stats
                str_stats_dir += (
                    "----> {extension}:  "
                    "Files_found = {int_files};  "
                    "Code_lines = {int_lines};  "
                    "\n"
                ).format(
                    extension=str_ext,
                    int_files=int_files,
                    int_lines=int_code_lines,
                )
            str_stats += str_stats_dir.format(
                int_files_in_dir=int_files_in_folder,
                int_lines_in_dir=int_lines_in_folder,
            )
            #####
            str_stats += "=" * 79 + "\n"
        return str_stats

    def get_dict_list_file_paths_by_ext_by_dir(self):
        """Getting dict with pathes to asked files by ext by dir

        Returns
        -------
        dict
            {"folder_path_1": {"file_extension_1": [file_path_1, ..], ..}, ..}
        """
        dict_list_file_paths_by_ext_by_dir = OrderedDict()
        for str_dir_path in self.list_str_dirs_where_to_look:
            dict_list_file_paths_by_ext_by_dir[str_dir_path] = \
                working_with_files.get_dict_list_file_paths_by_ext(
                    str_dir_path,
                    list_str_extensions=self.list_str_file_extensions,
                )
        return dict_list_file_paths_by_ext_by_dir

    def download_one_file(self, str_file_path):
        """"""
        # Check if file was deleted
        if not os.path.exists(str_file_path):
            self.dict_str_file_content_by_file_path[str_file_path] = ""
            return 0
        #####
        # Check if file was modified and if so redownload it
        float_time_file_changed = \
            os.path.getmtime(str_file_path) + os.path.getsize(str_file_path)
        float_time_file_mod_before = \
            self.dict_time_file_changed_by_path[str_file_path]
        if float_time_file_mod_before != float_time_file_changed:
            self.dict_str_file_content_by_file_path[str_file_path] = \
                working_with_files.get_file_as_string(str_file_path)
            self.dict_time_file_changed_by_path[str_file_path] = \
                float_time_file_changed
            return 1
        return 0

    def download_all_files(self):
        """
        For all files defined in self.dict_list_file_paths_by_ext_by_dir
        download up to date versions of files (Efficient realization)

        Returns
        -------
        int
            Number of files for which were loaded new versions of files
        """
        # Check if enough time gone (1 seconds) after last download of files
        if time.time() - self.time_when_last_time_downloaded_files < 1.0:
            return 0
        self.time_when_last_time_downloaded_files = time.time()
        int_files_loaded = 0
        #####
        # For every folder where to look download code files
        # Only if they were updated
        for str_dir_path in self.dict_list_file_paths_by_ext_by_dir:
            dict_list_file_paths_by_ext = \
                self.dict_list_file_paths_by_ext_by_dir[str_dir_path]
            #####
            for str_ext in dict_list_file_paths_by_ext:
                list_str_file_paths = dict_list_file_paths_by_ext[str_ext]
                for str_file_path in list_str_file_paths:
                    int_files_loaded += self.download_one_file(str_file_path)
            #####
        return int_files_loaded

    def update_files(self):
        """Re-search for all files in the folders and download them

        Parameters
        ----------
        Returns
        -------
        """
        print("Updating all files (it can be a long process, please wait.)")
        self.dict_list_file_paths_by_ext_by_dir = (
            self.get_dict_list_file_paths_by_ext_by_dir()
        )
        self.download_all_files()

    def search(
            self,
            str_code_to_search,
            bool_is_to_search_case_sensitive=True,
    ):
        """Searching some code inside whole library and
        print all occurrences in nice formatted way

        Parameters
        ----------
        str_code_to_search : str
            Code to search in the library
        bool_is_to_search_case_sensitive : bool, optional
            A flag if to search cas sensitive (default is True)

        Returns
        -------
        int
            times occurrences of code found in whole library
        """
        self.download_all_files()
        return self.search_processes_common(
            additional_functions.func_simple_search_of_code,
            str_code_to_search,
            bool_is_to_search_case_sensitive=bool_is_to_search_case_sensitive,
        )

    def search_with_re(self, str_re_template,):
        """Searching some code inside library using regular expressions

        Parameters
        ----------
        str_code_to_search : str
            Code to search in the library

        Returns
        -------
        int
            times occurrences of code found in whole library
        """
        self.download_all_files()
        def func_search_of_code_with_re(str_re_pattern, str_where_to_search):
            return bool(re.findall(str_re_pattern, str_where_to_search))
        return self.search_processes_common(
            func_search_of_code_with_re,
            str_re_template,
            bool_is_to_search_case_sensitive=True,
        )

    def search_processes_common_for_one_file(
            self,
            str_file_path,
            func_check_if_string_is_in_the_line,
            str_code_to_search,
            bool_is_to_search_case_sensitive,
    ):
        """Searching some code inside one file

        Searching some code inside one file and
        print all occurrences in nice formatted way

        Parameters
        ----------
        str_file_path : str
            Path to file where to search
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
        int_occurrences_found = 0
        str_full_file = self.dict_str_file_content_by_file_path[str_file_path]
        if not bool_is_to_search_case_sensitive:
            str_full_file = str_full_file.lower()
            str_code_to_search = str_code_to_search.lower()
        #####
        # Line by line searching for asked code
        bool_is_entry_found_for_cur_file = False
        for int_line_num, str_line in enumerate(str_full_file.splitlines()):
            if func_check_if_string_is_in_the_line(
                str_code_to_search,
                str_line,
            ):
                if not bool_is_entry_found_for_cur_file:
                    bool_is_entry_found_for_cur_file = True
                    print("----> Found in: ", str_file_path)
                print(
                    "------> {})".format(int_occurrences_found),
                    "line:", int_line_num,
                    " Code_line:", str_line.strip()
                )
                int_occurrences_found += 1
        return int_occurrences_found


    def search_processes_common(
            self,
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
        int_occurrences_found = 0
        print("=" * 79)
        # For every folder searching through all files inside folder
        for str_dir in self.dict_list_file_paths_by_ext_by_dir:
            dict_list_file_paths_by_ext = \
                self.dict_list_file_paths_by_ext_by_dir[str_dir]

            print("For folder: {folder}".format(folder=str_dir))
            for str_ext in dict_list_file_paths_by_ext:
                if len(dict_list_file_paths_by_ext) > 1:
                    print("")
                print("--> For extension: {extension}".format(
                    extension=str_ext
                ))

                int_found_for_ext = 0
                # For every file search occurrences of asked code
                for str_file_path in dict_list_file_paths_by_ext[str_ext]:
                    int_found_for_ext += \
                        self.search_processes_common_for_one_file(
                            str_file_path,
                            func_check_if_string_is_in_the_line,
                            str_code_to_search,
                            bool_is_to_search_case_sensitive,
                        )
                #####
                if not int_found_for_ext:
                    print("----> NOTHING FOUND.")
            int_occurrences_found += int_found_for_ext
            #####
            if int_occurrences_found:
                print("=" * 79)
        print("Overall occurrences found: ", int_occurrences_found)
        return int_occurrences_found


