# ===================================================================
# Author(s):
#
#       Name        Email
#      Jon Perry    dcjmp90@gmail.com
#
# Notes:
#
#   BaseModule will serve as an abstraction of each class
#   in current package subdirectory of Util: modules.
#
#   The idea is to have each query broken down into smaller more
#   managable tasks 
# ===================================================================
"""BaseModule base class implementation"""

import abc
from sanctuary.utils.parser.cli_arguments import Map

__all__ = ['BaseModule']

class BaseModule(metaclass=abc.ABCMeta):
    """A Base Module for Searchables

    Each Module implementation should have json output on a
    callable method of this object.

    This Module class should also implement task and subtask
    of any type of query (specific only to subclasses)
    """

    def __init__(self,
                 config,
                 **kwargs,
    ):
        self.config = config
        self.results = Map({})

    def _get_stats(self):
        """stats information"""

    def _get_requirements(self):
        """get item requirements"""

    def __iter__(self):
        """override iterator"""

    def __call__(self):
        """override callable"""
    
    def _search(self):
        """ensure a searchable query is handled internally"""