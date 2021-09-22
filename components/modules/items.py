# ===================================================================
# Author(s):
#
#       Name        Email
#      Jon Perry    dcjmp90@gmail.com
#
# Notes:
#
#   This will hold subclasses of the Base Item class
# ===================================================================
"""Item class for ease of parsing and pretty print"""


import bs4 as bs
from sanctuary.components.modules.base_item import BaseItem
from sanctuary.utils.parser.cli_arguments import Map

__all__ = ['RuneWordItem']

class RuneWordItem(BaseItem):
    """A Runeword Item

    This will parse and hold all information
    of a Rune Word item(s) 

    A RuneWord could have multiple types of
    item_type (e.g, Spirit has both Sword and Shield)

    """
    def __init__(self,
                 item_name,
                 item_specs,
    ):
        #TODO
        super().__init__(item_specs)
        self.results = Map({item_name : Map({})})

    def _get_recipe(self, specs):
        """get the recipe for this item"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')

    def _get_socket_requirement(self, specs)"
        """get the number of sockets required"""

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

    def _add_recipe(self, specs):
        """get the recipe for this item"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')

    def _add_socket_requirement(self, specs)"
        """get the number of sockets required"""

    def _add_level_required(self, specs):
        """get the level requirement"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')
    
    def _add_stats(self, specs):
        """get the stats for the item"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')
    
    def _add_item_type(self, specs):
        """get the items base type"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')

    def __call__(self, specs):
        """callable should be the main handler"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')


class SetItem(BaseItem):
    """A Set Item

    This will parse and hold all information
    of a single Set Item

    A Set could have multiple parts of
    gear (e.g, Tal Rasha's has 5 parts to complete)

    """
    def __init__(self,
                 item_name,
                 item_specs,
    ):
        #TODO
        super().__init__(item_specs)
        self.results = Map({item_name : Map({})})

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

    def _add_level_required(self, specs):
        """get the level requirement"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')
    
    def _add_stats(self, specs):
        """get the stats for the item"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')
    
    def _add_item_type(self, specs):
        """get the items base type"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')

    def __call__(self, specs):
        """callable should be the main handler"""
        #TODO
        raise NotImplementedError('You must implement this in subclass!')