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

__all__ = ['BaseModule']

class BaseModule(metaclass=abc.ABCMeta):
    """A Base Module for Searchables

    Each Module implementation should have json output on a
    callable method of this object.

    This Module class should also implement task and subtask
    of any type of query (specific only to subclasses)
    """

    def __init__(self,
                 parent_conatiner,
                 child_container,
                 **kwargs,
    ):
    self.parent_conatiner = parent_conatiner
    self.child_container = child_container
    self.results = []

    @abc.abstractmethod
    def __iter__(self):
        """override iterator"""

    @abc.abstractmethod
    def __call__(self):
        """override callable"""
    
    @abc.abstractmethod
    def __str__(self):
        """override to string"""
    
    @abs.abstractmethod
    def _search(self):
        """ensure a searchable query is handled internally"""