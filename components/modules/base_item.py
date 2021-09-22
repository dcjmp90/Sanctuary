# ===================================================================
# Author(s):
#
#       Name        Email
#      Jon Perry    dcjmp90@gmail.com
#
# Notes:
#
#   Base will serve as an abstraction of each class
#   in current package directory Components/modules. 
# ===================================================================
"""Base class for an Item implementation"""

import os
import abc
from sanctuary.utils.parser.cli_arguments import Map

__all__ = ['BaseItem']

class BaseItem(metaclass=abc.ABCMeta):
    """TODO
    """
    def __init__(self,
                 item_name,
    ):
        self.item_name = item_name
        self.string_builder = '** '+item_name+' ** :\n'
        self.compiled_attrs = Map({})
        self.queries = Map({})

        for method in dir(self):
            if method.startswith('_get'):
                attr = method.split('get_')[-1]
                self.queries[attr] = method
    
    def _get_level_required(self, specs):
        """get the level requirement"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')
    
    def _get_stats(self, specs):
        """get the stats for the item"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')
    
    def _get_item_type(self, specs):
        """get the items base type"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')
    
    def __call__(self, specs):
        """callable should be the main handler"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')