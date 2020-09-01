# -*- coding: utf-8 -*-
"""
code_searcher
========================
code_searcher is a simple Python module with main purpose to
help support changes in any function signature inside any project or
library.
"""
import logging

from code_searcher.code_searcher_class import CodeSearcher

__all__ = ["CodeSearcher",]


#####
# Prepare basic logger in case user is not setting it itself.
#####
#STR_LOG_STDOUT_FORMAT = '[%(levelname)s]:  %(message)s'
# DEBUG=10   INFO=20   WARNING=30   ERROR=40   CRITICAL=50
#logging.basicConfig(format=STR_LOG_STDOUT_FORMAT, level=20)

LOGGER = logging.getLogger("code_searcher")
LOGGER.addHandler(logging.NullHandler())
