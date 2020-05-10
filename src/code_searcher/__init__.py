# -*- coding: utf-8 -*-
"""
code_searcher
========================
code_searcher is a simple Python module with main purpose to
help support changes in any function signature inside any project or
library.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from code_searcher.code_searcher_class import code_searcher_class





__all__ = [
    # Core classes
    "code_searcher_class",
]



#####
# Prepare basic logger in case user is not setting it itself.
#####
import logging
#STR_LOG_STDOUT_FORMAT = '[%(levelname)s]:  %(message)s'
# DEBUG=10   INFO=20   WARNING=30   ERROR=40   CRITICAL=50
#logging.basicConfig(format=STR_LOG_STDOUT_FORMAT, level=20)

LOGGER = logging.getLogger("local_simple_database")
LOGGER.addHandler(logging.NullHandler())

