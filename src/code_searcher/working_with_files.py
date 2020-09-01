# -*- coding: utf-8 -*-
"""File with all methods connected to working with files"""
# Standard library imports
import os
import codecs
import json
from collections import defaultdict
import logging

# Third party imports

# Local imports

LOGGER = logging.getLogger("code_searcher")


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


def get_dict_list_file_paths_by_ext(
        str_folder_where_to_look,
        list_str_extensions=[".py"],
):
    """Getting pathes to all files with asked extension in the folder

    Parameters
    ----------
    str_folder_where_to_look : str
        path to most parent folder where to look for files
    list_str_extensions  : list
        Extensions for which to look for

    Returns
    -------
    list
        pathes to all files with given extension inside the given folder
    """
    LOGGER.debug("start get_dict_list_file_paths_by_ext:")
    dict_list_file_paths_by_ext = defaultdict(list)
    # Using os.walk getting all files with asked extension
    for str_parent_dir, _, list_filenames in os.walk(str_folder_where_to_look):
        LOGGER.debug(
            "---> Checking %d files in dir: %s",
            len(list_filenames),
            str_parent_dir
        )
        if os.path.basename(str_parent_dir) == "__pycache__":
            LOGGER.debug("------> Cache folder found so continue")
            continue
        for str_ext in list_str_extensions:
            list_files_of_ext = []
            # Add point before extension name in needed
            if not str_ext.startswith("."):
                str_ext = "." + str_ext
            #####
            # If file is ipynb, then do no take files from folder checkpoints
            if str_ext == ".ipynb":
                str_par_folder_name = os.path.basename(str_parent_dir)
                if str_par_folder_name == ".ipynb_checkpoints":
                    continue
            #####
            for str_filename in list_filenames:
                if str_filename.endswith(str_ext):
                    list_files_of_ext.append(
                        os.path.join(str_parent_dir, str_filename)
                    )
            dict_list_file_paths_by_ext[str_ext] += list_files_of_ext
            LOGGER.debug(
                "------> Found files with ext %s: %d",
                str_ext,
                len(list_files_of_ext)
            )
    return dict_list_file_paths_by_ext


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
    str_file_ext = str(os.path.splitext(str_file_path)[1])
    if str_file_ext == ".ipynb":
        return read_ipynb_file(str_file_path)
    return read_whole_file(str_file_path)
