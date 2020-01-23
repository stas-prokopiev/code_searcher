# -*- coding: utf-8 -*-
"""
code_searcher.decorators
~~~~~~~~~~~~

This module is consists of decorators for code searching
through your library.
Very UNLIKELY that you will need them.

:copyright: © 2019 by Stanislav Prokopyev stas.prokopiev@gmail.com.
:license: MIT, see LICENSE.rst for more details.
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import sys


def check_with_assert_that_var_given_to_func_has_asked_type(
        str_function_name,
        str_variable_name,
        variable_value,
        tuple_types_variable_can_be,
):
    """Checking with assert that given variable has asked type

    Parameters
    ----------
    str_function_name : str
        function name where variables are checked
    str_variable_name  : str
        name of variable to check
    variable_value  : any
        value of checked variable
    tuple_types_variable_can_be  : tuple or type
        types asked variable can be

    Returns
    -------
    None
    """
    assert isinstance(variable_value, tuple_types_variable_can_be), (
        "ERROR: Incorrect type of variables given to function: " +
        str(str_function_name) + "\n" +
        "---> For variable: " + str(str_variable_name) + "\n" +
        "---> were given value: " + str(variable_value) + "\n" +
        "---> with type: " + str(type(variable_value)) + "\n"
        "---> instead of: " + str(tuple_types_variable_can_be)
    )


def check_type_of_arguments(func_to_check):
    """Decorator to check with assert that function arguments given to function
    have asked types defined argument's name first prefix

    Parameters
    ----------
    func_to_check : str
        Function given to decorator

    Returns
    -------
    None
    """
    list_function_arguments = \
        func_to_check.__code__.co_varnames[:func_to_check.__code__.co_argcount]
    str_function_name = func_to_check.__name__

    def echo_func(*args, **kwargs):
        dict_local_variables = locals()
        tuple_args = dict_local_variables['args']
        dict_kwargs = dict_local_variables['kwargs']
        list_tuples_to_iterate = (
            list(zip(list_function_arguments, tuple_args)) +
            list(dict_kwargs.items())
        )
        #####
        # Check arguments one by one
        for str_variable_name, variable_value in list_tuples_to_iterate:
            # print(str_variable_name, " = ", variable_value)
            # If value is None then do not check this variable
            if variable_value is None:
                continue
            # Checking with assert that given variable has asked type
            if str_variable_name.startswith("str_"):
                if sys.version_info[0] == 2:
                    tuple_types_to_check = (str, bytes, unicode)
                else:
                    tuple_types_to_check = (str, bytes)
                check_with_assert_that_var_given_to_func_has_asked_type(
                    str_function_name,
                    str_variable_name,
                    variable_value,
                    tuple_types_to_check,
                )
            elif str_variable_name.startswith("bool_"):
                check_with_assert_that_var_given_to_func_has_asked_type(
                    str_function_name,
                    str_variable_name,
                    variable_value,
                    bool,
                )
            elif str_variable_name.startswith("int_"):
                check_with_assert_that_var_given_to_func_has_asked_type(
                    str_function_name,
                    str_variable_name,
                    variable_value,
                    int,
                )
            elif str_variable_name.startswith("float_"):
                check_with_assert_that_var_given_to_func_has_asked_type(
                    str_function_name,
                    str_variable_name,
                    variable_value,
                    float,
                )
            elif str_variable_name.startswith("list_"):
                check_with_assert_that_var_given_to_func_has_asked_type(
                    str_function_name,
                    str_variable_name,
                    variable_value,
                    list,
                )
            elif str_variable_name.startswith("dict_"):
                check_with_assert_that_var_given_to_func_has_asked_type(
                    str_function_name,
                    str_variable_name,
                    variable_value,
                    dict,
                )
            elif str_variable_name.startswith("set_"):
                check_with_assert_that_var_given_to_func_has_asked_type(
                    str_function_name,
                    str_variable_name,
                    variable_value,
                    set,
                )
        return func_to_check(*args, **kwargs)
    return echo_func
