# ===================================================================
# Author(s):
#
#       Name        Email
#      Jon Perry    dcjmp90@gmail.com
#
# Notes:
#
# ===================================================================
"""Tokenizers will handle specific data pulls"""

from sanctuary.utils.parser.cli_arguments import Map

__all__ = ['']

class ItemTokenizer:
    """TODO details
    """

    def __init__(self,
    ):
    #TODO
    self.queries = Map({})

    for method in dir(self):
        if method.startswith('_get'):
            attr = method.split('_')[-1]
            self.queries[attr] = method


    def _get_recipe(self, item):
        #TODO
        pass
    
    def _get_stats(self, item):
        #TODO
        pass
    
    def _get_requirements(self, item):
        #TODO
        pass
    
    def _get_setbonus(self, item):
        #TODO
        pass
    
    def _get_all(self, item):
        #TODO
        pass

    def __call__(self,
                 item,
                 item_spec = None,
    ):

    if item_spec is not None:
        if item_spec in self.queries.keys():
            return self.queries.item_spec(item)
        else:
            return _get_all(item)
    

