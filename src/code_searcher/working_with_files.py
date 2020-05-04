# -*- coding: utf-8 -*-
"""

This module is consists of additional functions for code searching
through your library.
"""
# Standard library imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os
import codecs
import json

# Third party imports

# Local imports


def read_whole_file(str_path_to_file):
    """read the whole file with encoding

    Parameters
    ----------
    str_path_to_file : str
        path to file which to read
    str_encoding : str
        encoding type to use

    Returns
    -------
    str
        whole file as one string
    """
    with codecs.open(str_path_to_file, "r", "utf-8", errors="ignore") as file:
        str_whole_file = file.read()
    return str_whole_file  # .encode("utf-8")


def read_ipynb_file(str_path_to_file):
    """read the ipynb file as string

    Parameters
    ----------
    str_path_to_file : str
        path to file which to read
    Returns
    -------
    str
        whole ipynb file as one string
    """
    str_whole_file = read_whole_file(str_path_to_file)
    dict_ipynb_file = json.loads(str_whole_file)
    if "cells" not in dict_ipynb_file:
        return ""
    str_full_ipynb_file = ""
    for int_cell_num, dict_cell in enumerate(dict_ipynb_file["cells"]):
        str_cell_num = "In [{}] ".format(int_cell_num)
        str_cell_full_code = ""
        for str_one_line_of_code in dict_cell["source"]:
            if not str_one_line_of_code.strip():
                continue
            str_cell_full_code += str_cell_num + str_one_line_of_code
        str_full_ipynb_file += str_cell_full_code + "\n"
    # print(str_full_ipynb_file)
    return str_full_ipynb_file


def get_list_str_path_all_files_with_given_extension(
    str_folder_where_to_look, str_extension_to_look_for=".py",
):
    """Getting pathes to all files with asked extension in the folder

    Parameters
    ----------
    str_folder_where_to_look : str
        path to most parent folder where to look for files
    str_extension_to_look_for  : str
        extension of file which to look for

    Returns
    -------
    list
        pathes to all files with given extension inside the given folder
    """
    # Add point before extension for the sake of getting only right files
    if not str_extension_to_look_for.startswith("."):
        str_extension_to_look_for = "." + str_extension_to_look_for
    # Using os.walk getting all files with asked extension
    list_str_path_all_files_with_given_extension = []
    for str_parent_folder, _, list_str_child_filenames in os.walk(
        str_folder_where_to_look
    ):
        #####
        # If file is ipynb, then do no take files from folder checkpoints
        if str_extension_to_look_for == ".ipynb":
            str_par_folder_name = os.path.basename(str_parent_folder)
            if ".ipynb_checkpoints" == str_par_folder_name:
                continue
        #####
        for str_filename in list_str_child_filenames:
            if str_filename.endswith(str_extension_to_look_for):
                list_str_path_all_files_with_given_extension.append(
                    os.path.join(str_parent_folder, str_filename)
                )
    return list_str_path_all_files_with_given_extension


def get_list_str_filenames_of_all_files_with_given_extension(
    str_folder_where_to_look, str_extension_to_look_for=".py",
):
    """Getting names of all files with asked extension in the folder

    Parameters
    ----------
    str_folder_where_to_look : str
        path to most parent folder where to look for files
    str_extension_to_look_for  : str
        extension of file which to look for

    Returns
    -------
    list
        names of all files with given extension inside the given folder
    """
    # Add point before extension for the sake of getting only right files
    if not str_extension_to_look_for.startswith("."):
        str_extension_to_look_for = "." + str_extension_to_look_for
    # Getting all filenames via os.walk
    list_str_filenames = []
    for _, _, list_str_ch_filenames in os.walk(str_folder_where_to_look):
        for str_filename in list_str_ch_filenames:
            if str_filename.endswith(str_extension_to_look_for):
                list_str_filenames.append(str_filename)
    # Clear filenames from extension .py
    list_str_filenames_cleared = [
        str_filename.replace(str_extension_to_look_for, "")
        for str_filename in list_str_filenames
    ]
    return list_str_filenames_cleared


def get_file_extension(str_file_path):
    """Get file extension by file path

    Parameters
    ----------
    str_file_path : str
        path to file which extension to return

    Returns
    -------
    str
        string file extension for given file
    """
    return str(os.path.splitext(str_file_path)[1])


def get_file_as_string(str_file_path):
    """Get content of file as string for any type of file

    Parameters
    ----------
    str_file_path : str
        path to file which to return as string

    Returns
    -------
    str
        string content inside file
    """
    str_ext = get_file_extension(str_file_path)
    if str_ext == ".ipynb":
        return read_ipynb_file(str_file_path)
    else:
        return read_whole_file(str_file_path)

