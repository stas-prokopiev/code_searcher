# -*- coding: utf-8 -*-
"""

This module is consists of main class for code searching through your
code library.
"""
# Standard library imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import time
import os
import sys
from collections import defaultdict
from collections import OrderedDict

# Third party imports

# Local imports
# .additional_functions
from code_searcher.additional_functions import \
    get_number_of_lines_in_string

from code_searcher.additional_functions import \
    search_code_in_the_library_common_processes
# .working_with_files
from code_searcher.working_with_files import \
    get_list_str_filenames_of_all_files_with_given_extension
from code_searcher.working_with_files import \
    get_list_str_path_all_files_with_given_extension
from code_searcher.working_with_files import get_file_as_string


class code_searcher_class:
    """
    A class used to do search operations on whole code of project

    ...

    Attributes
    ----------
    list_str_dirs_where_to_look : list
        list most parent folders where to look for code files
    list_str_file_extensions : list
        list strings file extensions which files to explore
    dict_time_file_changed_by_path : dict
        {"path_to_file_1": float_time_when_last_modified, ...}
    dict_list_file_paths_by_ext_by_dir : dict
        dict with pathes of all initialized files
        {"folder_path_1": {"file_extension_1": [file_path_1, ...], ...}, ...}
    dict_str_file_by_path_by_ext_by_dir : dict
        {"dir_path_1": {"file_ext_1": {"file_path_1": whole_file, ..}, ..}, ..}
    dict_str_file_by_full_path : dict
        {"file_path_1": file_1_content, "file_path_2": file_2_content, ...}
    time_when_last_time_downloaded_files : float
        time.time() when last time downloaded files
        (need for not redownloading too often at least after 3 seconds)

    Methods
    -------
    get_file_stats_of_the_code_library(...)
        Getting string with statistics about files in the library

    get_dict_list_file_paths_by_ext_by_dir(...)
        Getting dict with pathes to asked files by ext by dir

    get_dict_list_file_paths_by_ext(...)
        Getting dict with pathes to asked files by extension

    download_files(...)
        For all files defined in self.dict_list_file_paths_by_ext_by_dir
        download up to date versions of files (Efficient realization)

    update_files(...)
        Re-search for all files in the folders and download them

    search_code_in_the_library(...)
        Searching some code inside whole library and
        print all occurrences in nice formatted way

    search_code_in_the_library_with_re(...)
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
        assert list_str_dirs_where_to_look is not None, (
            "ERROR: for initializing code_searcher obj should be given \n"
            "list of most parent folders where to search files with code \n"
            "var list_str_dirs_where_to_look: SHOULD NOT BE NONE"
        )
        # 1) Initialize class variables
        # list most parent folders where to look for code files
        self.list_str_dirs_where_to_look = [
            os.path.abspath(str_dir).lower()
            for str_dir in list_str_dirs_where_to_look
        ]
        # list strings file extensions which files to explore
        self.list_str_file_extensions = list_str_file_extensions
        # {"path_to_file_1": float_time_when_last_modified, ...}
        self.dict_time_file_changed_by_path = defaultdict(float)
        self.dict_str_file_by_full_path = {}

        print("Downloading all files (it can be a long process, please wait.)")
        float_time_start = time.time()
        # {"folder_path_1": {"file_extension_1": [file_path_1, ...], ...}, ...}
        self.dict_list_file_paths_by_ext_by_dir = (
            self.get_dict_list_file_paths_by_ext_by_dir()
        )
        # {"dir_path_1": {"file_ext_1": {"file_path_1": whole_file, ..}, .}, .}
        # Initialize dict_str_file_by_path_by_ext_by_dir
        self.dict_str_file_by_path_by_ext_by_dir = OrderedDict()
        self.time_when_last_time_downloaded_files = 0
        int_files_downloaded = self.download_files()
        float_seconds_spent = round(time.time() - float_time_start, 2)
        print(
            "{} Files were downloaded in {} seconds".format(
                int_files_downloaded, float_seconds_spent
            )
        )
        # # Print file statistic
        # self.get_file_stats_of_the_code_library(bool_is_to_print=True)
        # print("Search obj INITIALIZED.")

    def __repr__(self):
        """Representation of obj

        Returns
        -------
        str
            representation of the obj
        """
        self.download_files()
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

    def get_file_stats_of_the_code_library(self, bool_is_to_print=False):
        """Getting string with statistics about files in the library

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

        self.download_files()
        str_stats = "\n"
        str_stats += "Files Statistic of current code library:\n"
        # Print file statistic for every folder
        for str_dir in self.dict_str_file_by_path_by_ext_by_dir:
            str_stats_dir = ""
            str_stats_dir += "--> For folder: " + str(str_dir) + "\n"
            int_files_in_folder = 0
            int_lines_in_folder = 0
            str_stats_dir += "--> Files_found = {int_files_in_dir}  "
            str_stats_dir += "Code_lines = {int_lines_in_dir}\n"
            dict_str_file_by_path_by_ext = \
                self.dict_str_file_by_path_by_ext_by_dir[str_dir]
            # Count number of files with every extension
            for str_ext in dict_str_file_by_path_by_ext:
                dict_str_file_by_path = dict_str_file_by_path_by_ext[str_ext]
                int_code_lines = 0
                for str_file_path in dict_str_file_by_path:
                    str_full_file = dict_str_file_by_path[str_file_path]
                    int_code_lines += \
                        get_number_of_lines_in_string(str_full_file)

                int_files = len(dict_str_file_by_path)
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
        if bool_is_to_print:
            print(str_stats)
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
            dict_list_file_paths_by_ext = defaultdict(list)
            for str_ext in self.list_str_file_extensions:
                dict_list_file_paths_by_ext[
                    str_ext
                ] = get_list_str_path_all_files_with_given_extension(
                    str_dir_path, str_extension_to_look_for=str_ext
                )
            dict_list_file_paths_by_ext_by_dir[
                str_dir_path
            ] = dict_list_file_paths_by_ext
        return dict_list_file_paths_by_ext_by_dir

    def get_dict_list_file_paths_by_ext(self):
        """Getting dict with pathes to asked files by extension

        Returns
        -------
        dict
            {"file_extension_1": [file_path_1, ..], ..}
        """
        dict_list_file_paths_by_ext_by_dir = \
            self.get_dict_list_file_paths_by_ext_by_dir()
        dict_list_file_paths_by_ext = defaultdict(list)
        for str_dir in dict_list_file_paths_by_ext_by_dir:
            dict_list_file_paths_by_ext_tmp = \
                dict_list_file_paths_by_ext_by_dir[str_dir]
            for str_ext in dict_list_file_paths_by_ext_tmp:
                dict_list_file_paths_by_ext[str_ext] = \
                    dict_list_file_paths_by_ext_tmp[str_ext]
        return dict_list_file_paths_by_ext

    def download_files(self):
        """
        For all files defined in self.dict_list_file_paths_by_ext_by_dir
        download up to date versions of files (Efficient realization)

        Returns
        -------
        int
            Number of files for which were downloaded new versions
        """
        # Check if enough time gone (3 seconds) after last download of files
        if time.time() - self.time_when_last_time_downloaded_files < 3.0:
            return 0
        self.time_when_last_time_downloaded_files = time.time()
        int_new_files_downloaded = 0
        #####
        # For every folder where to look download code files
        # Only if they were updated
        for str_dir_path in self.dict_list_file_paths_by_ext_by_dir:
            dict_list_file_paths_by_ext = \
                self.dict_list_file_paths_by_ext_by_dir[str_dir_path]
            #####
            # Necessary for correct redownloading of library
            if str_dir_path in self.dict_str_file_by_path_by_ext_by_dir:
                dict_str_file_by_path_by_ext = \
                    self.dict_str_file_by_path_by_ext_by_dir[str_dir_path]
            else:
                dict_str_file_by_path_by_ext = OrderedDict()
            #####
            for str_ext in dict_list_file_paths_by_ext:
                list_str_file_paths = dict_list_file_paths_by_ext[str_ext]
                #####
                # Necessary for correct redownloading of library
                if str_ext in dict_str_file_by_path_by_ext:
                    dict_str_file_by_path = \
                        dict_str_file_by_path_by_ext[str_ext]
                else:
                    dict_str_file_by_path = OrderedDict()
                #####
                for str_f_path in list_str_file_paths:
                    # Check if file was deleted
                    # then delete it from dict_str_file_by_path
                    if not os.path.exists(str_f_path):
                        dict_str_file_by_path[str_f_path] = ""
                        continue
                    #####
                    # Check if file was modified and if so redownload it

                    float_time_file_changed = os.path.getmtime(
                        str_f_path
                    ) + os.path.getsize(str_f_path)

                    float_time_file_mod_before = \
                        self.dict_time_file_changed_by_path[str_f_path]

                    if float_time_file_mod_before != float_time_file_changed:

                        str_file_content = get_file_as_string(str_f_path)
                        dict_str_file_by_path[str_f_path] = str_file_content
                        self.dict_str_file_by_full_path[str_f_path] = \
                            str_file_content
                        self.dict_time_file_changed_by_path[
                            str_f_path
                        ] = float_time_file_changed
                        int_new_files_downloaded += 1
                dict_str_file_by_path_by_ext[str_ext] = dict_str_file_by_path
            #####
            self.dict_str_file_by_path_by_ext_by_dir[
                str_dir_path
            ] = dict_str_file_by_path_by_ext
        return int_new_files_downloaded

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
        self.download_files()

    def search_code_in_the_library(
        self, str_code_to_search, bool_is_to_search_case_sensitive=True,
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
        from code_searcher.additional_functions import \
            bool_simple_search_of_code

        self.download_files()
        return search_code_in_the_library_common_processes(
            self.dict_str_file_by_path_by_ext_by_dir,
            bool_simple_search_of_code,
            str_code_to_search,
            bool_is_to_search_case_sensitive=bool_is_to_search_case_sensitive,
        )

    def search_code_in_the_library_with_re(
        self, str_re_template,
    ):
        """Searching some code inside library using regular expressions

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
        from code_searcher.additional_functions import \
            bool_search_of_code_with_re

        self.download_files()
        return search_code_in_the_library_common_processes(
            self.dict_str_file_by_path_by_ext_by_dir,
            bool_search_of_code_with_re,
            str_re_template,
            bool_is_to_search_case_sensitive=True,
        )
