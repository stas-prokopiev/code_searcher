
Full elaboration on code_searcher_obj
======================================

code_searcher_obj attributes
----------------------------
    **list_str_folders_where_to_look**: list
        *list most parent folders where to look for code files*

    **list_str_file_extensions** : list
        *list strings file extensions which files to explore*

    **dict_dict_str_file_by_filename_by_folder** : dict
        *{folder_path: {relative_file_path: string_whole_file, ...}, ...}*

code_searcher_obj Methods
-------------------------

    **search_all_occurrences_of_the_code_in_the_library**
        *Searching some code inside whole library and print all occurrences in a formatted way*

    **update_files**
        *Redownloading all files if something was changed inside them*

    **get_file_stats_of_the_code_library**
        *Getting string statistic about files in the library*

    **get_dict_times_functions_used**
        *Getting {function_name: times_function_used, ...}*

    **get_names_of_all_functions_defined_but_never_used**
        *Getting the list of functions defined inside code but never used*

    **get_number_of_lines_in_the_library**
        *Getting number of not empty lines in the whole library*

    **get_list_of_all_outer_modules_used_in_library**
        *Getting the list of all OUTER modules imported in the library*
