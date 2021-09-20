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

__all__ = ['ItemTokenizer']

class ItemTokenizer:
    """TODO details
    """

    def __init__(self,
                 item_content='span',
                 item_title='h3',
    ):
        #TODO
        self.queries = Map({})
        self.item_content = item_content
        self.item_title = item_title

        for method in dir(self):
            if method.startswith('_get'):
                attr = method.split('_')[-1]
                self.queries[attr] = method

    def _get_recipe(self,
                    item,
                    item_name,
                    item_spec,
                    filter_term='class',
                    class_name='z-recipes',
    ):
        """Pull Recipe information from item"""
        specs = {filter_term:class_name}
        results = Map({})
        tags = []
        for span in item.parent.find_all(self.item_content,specs):
            tags.append(span.text)
        results[item_spec] = tags 
        return results
    
    def _get_stats(self,
                   item,
                   item_name,
                   item_spec,
    ):
    #TODO
        pass
    
    def _get_requirements(self,
                          item,
                          item_name,
                          item_spec,
    ):
    #TODO
        pass
    
    def _get_setbonus(self,
                      item,
                      item_name,
                      item_spec,
    ):
        #TODO
        pass
    
    def _get_all(self,
                 item,
                 item_spec,
    ):
        """Return all attributes of an item"""
        all_attrs = Map({})
        for attr, method in self.queries.items():
            if attr != item_spec:
                all_attrs[attr] = getattr(self,method)(item,
                                                       item_name,
                                                       attr,
                                                       )
        return all_attrs

    def __call__(self,
                 item,
                 item_name,
                 item_spec = 'all',
    ):
        if item_spec in self.queries.keys():
            return getattr(self,self.queries[item_spec])(item,
                                                         item_name,
                                                         item_spec,
                                                         )
        else:
            return self._get_all(item, item_spec)
        
    

