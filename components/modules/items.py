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

__all__ = ['RuneWordItem, SetItem']

class RuneWordItem(BaseItem):
    """A Runeword Item

    This will parse and hold all information
    of a Rune Word item(s) 

    A RuneWord could have multiple types of
    item_type (e.g, Spirit has both Sword and Shield)

    Parameters
    ----------

    item_name : str
        The name of the specific runeword item query

    """
    def __init__(self, item_name):
        super().__init__(item_name)

        for method in dir(self):

            if method.startswith('_add'):
                attr = method.split('add_')[-1]
                self.compiled_attrs[attr] = method

    def _build(self):
        """Build all"""
        for k in sorted(self.build_attrs.keys()):
            self.string_builder += self.build_attrs[k]

    def _add(self, dict_like):
        """Add dict to this object
        
        This can be more that one set of key:value
            and each will be handled independently 
        
        Example of a dict_like object:

            Case 1: Single key-value
            ------------------------
                __dict__ = {'recipe' : ['Tal', 'Thul', 'Ort', 'Amn']}

            Case 2: Many key-value
            ----------------------      
                __dict__ = {'socket_requirement' : ['4 sockets', '4 sockets'],
                                    'item_type' : ['sword', 'shield'],
                            'level_requirement' : ['25']
                }
        
        Parameters
        ----------

        dict_like : dict
            A dictionary as described as above

        """
        for k, v in dict_like.items():
            if k in self.compiled_attrs.keys():
                getattr(self, self.compiled_attrs[k])(v)

    def _add_recipe(self, specs, sep='>>'):
        """get the recipe for this item
        

        
        """
        self.build_attrs[1] = '** Recipe ** : '+sep.join(specs) +'\n'

    def _add_socket_requirement(self, specs):
        """get the number of sockets required"""
        for idx, priority in enumerate(range(3,len(specs)*3+1,3)):
            self.build_attrs[priority] = '** Build with ** : '+specs[idx]

    def _add_level_required(self, specs):
        """get the level requirement"""
        self.build_attrs[2] = '** Level Required ** : '+''.join(specs)
    
    def _add_stats(self, specs):
        """get the stats for the item"""
        for idx, priority in range(5,len(specs)*5+1,3)):
            self.build_attrs[priority] = '\t\t'+specs[idx]+'\n'
    
    def _add_item_type(self, specs):
        """get the items base type"""
        for idx, priority in enumerate(range(3,len(specs)*3+1,3)):
            self.build_attrs[priority+1] = specs[idx]+'\n'

    def __call__(self):
        """callable should be the main handler"""
        self._build()
        return self.string_builder


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
