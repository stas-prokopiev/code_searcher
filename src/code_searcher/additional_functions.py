 # -*- coding: utf-8 -*-
# Standard library imports
import logging

# Third party imports

# Local imports

LOGGER = logging.getLogger("local_simple_database")

def func_simple_search_of_code(str_code_to_search, str_where_to_search):
    """Getting names of all modules imported in the python code

    Parameters
    ----------
    str_py_code : str
        code where to search for imported modules

    Returns
    -------
    bool
        If string is inside another string
    """
    return str_code_to_search in str_where_to_search
    # if str_code_to_search not in str_where_to_search:
    #     return False
    # #####
    # # If code found check that it's not in quotes
    # str_in_quotes_1 = "'{}'".format(str_code_to_search)
    # str_in_quotes_2 = '"{}"'.format(str_code_to_search)
    # bool_is_code_in_quotes = (
    #     (str_in_quotes_1 in str_where_to_search) or
    #     (str_in_quotes_2 in str_where_to_search)
    # )
    # if bool_is_code_in_quotes:
    #     return False
    # return True

