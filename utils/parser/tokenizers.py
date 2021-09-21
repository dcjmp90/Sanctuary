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
import re

__all__ = ['RunewordItemTokenizer']

class RunewordItemTokenizer:
    """TODO details
    """

    def __init__(self,
                 item_content='span',
                 item_title='h3',
                 filter_term='class',
    ):
        #TODO
        self.queries = Map({})
        self.item_content = item_content
        self.item_title = item_title
        self.filter_term = filter_term

        for method in dir(self):
            if method.startswith('_get'):
                attr = method.split('_')[-1]
                self.queries[attr] = method

    def _get_recipe(self,
                    items,
                    item_name,
                    item_spec,
                    class_name='z-recipes',
    ):
        """Pull Recipe information from item"""
        specs = {self.filter_term:class_name}
        results = Map({})
        tags = []
        for span in items.parent.find_all(self.item_content,specs):
            tags.append(span.text)
        results[item_spec] = tags 
        return results
    
    def _get_stats(self,
                   tag,
                   item_name,
                   item_spec,
                   item_stats='z-smallstats',
    ):
        #TODO
        results = Map({})
        specs_stats = {self.filter_term:item_stats}
        heap = tag.parent.find_all(self.item_content,specs_stats)
        results[item_spec] = [t.text for t in heap]
        return results
    
    def _get_requirements(self,
                          tag,
                          item_name,
                          item_spec,
                          type_filter_term='a',
                          weapon_class='z-white',
                          socket_class='zso_rwsock',
                          level_required='zso_rwlvlrq',
    ):
        results = Map({})
        specs_item_type = {self.filter_term:weapon_class}
        specs_sockets = {self.filter_term:socket_class}
        specs_level = {self.filter_term:level_required}
        item_types = tag.parent.find_all(type_filter_term,specs_item_type)
        socket_rq = tag.parent.find_all(self.item_content,specs_sockets)
        lvl_rq = tag.parent.find_all(self.item_content,specs_level)
        results[item_name] = {'socket_requirement': [t.parent.text.strip() for t in socket_rq]}                   
        results[item_name]['item_types'] = [re.sub(r'\s*','',t.text.strip().split('\n')[-1]) for t in item_types]
        results[item_name]['level_rq'] = [t.text.strip() for t in lvl_rq]
        return results
    
    def _get_all(self,
                 tag,
                 item_name,
                 item_spec,
    ):
        """Return all attributes of an item"""
        all_attrs = Map({})
        for attr, method in self.queries.items():
            if attr != item_spec:
                all_attrs[attr] = getattr(self,method)(tag,
                                                       item_name,
                                                       attr)
        return all_attrs

    def __call__(self,
                 item,
                 item_name,
                 item_spec = 'all',
    ):
        if item_spec in self.queries.keys():
            return getattr(self,self.queries[item_spec])(item,
                                                         item_name,
                                                         item_spec)
        else:
            return {'Error':'Does not exist or query was in error!'}
        
    

