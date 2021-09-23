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
from sanctuary.components.modules.items import RuneWordItem
import re

__all__ = ['RunewordItemTokenizer']

class RunewordItemTokenizer:
    """Runeword Tokenizer 

    This will parse web based information
    overall/regardless of the type of 
    query made with an item name, this
    will return a Map of values with 
    each key defining a speciifc list
    of information

    Pameters
    --------

    item : sanctuary.components.BaseItem
        This will have the base class of BaseItem, but
            this will be any type of item.

    item_content : str
        A string defaulted to 'span' for what container
            the content will belong to on the site
    
    item_title : str
        A string defaulted to 'h3' for what container
            holds the title for runeword items
    
    filter_term : str
        A string defaulted to 'class' for bs4 filtering usage
            right now we are filtering by class names of containers

    """

    def __init__(self,
                 item_content='span',
                 item_title='h3',
                 filter_term='class',
    ):
        self.queries = Map({})
        self.item_content = item_content
        self.item_title = item_title
        self.filter_term = filter_term

        for method in dir(self):
            if method.startswith('_get'):
                attr = method.split('get_')[-1]
                self.queries[attr] = method

    def _get_recipe(self,
                    tag,
                    item_name,
                    item_spec,
                    class_name='z-recipes',
    ):
        """Pull Recipe information from item
        
        Recipe Example:

            >>> ?runewords Spirit recipe
            ... {'recipe' : ['Tal', 'Thul', 'Ort', 'Amn']}
        
        Parameters
        ----------

        tag : bs4.element.ResultSet
            The result set is a searchable set of strings 
                that pertain to a specific query of a site
        
        item_name : str
            This will be the item from top level search used only 
                to keep a specific pattern to the Map built
        
        item_spec : str
            This will be used to define the list returned as a key value
        
        class_name : str
            A string defaulted to 'z-recipes' for a specific search
                of filter term when using find_all
        """
        specs = {self.filter_term:class_name}
        results = Map({})
        tags = []
        for span in tag.parent.find_all(self.item_content,specs):
            tags.append(span.text)
        results[item_spec] = tags 
        self.item._add(results)
    
    def _get_stats(self,
                   tag,
                   item_name,
                   item_spec,
                   item_stats='z-smallstats',
    ):
        """Pull Stats from item
        
        Stats Example:

            >>> ?runewords Spirit stats
            ... {'stats' : ['+2 to all skills', ...]}
        
        Parameters
        ----------

        tag : bs4.element.ResultSet
            The result set is a searchable set of strings 
                that pertain to a specific query of a site
        
        item_name : str
            This will be the item from top level search used only 
                to keep a specific pattern to the Map built
        
        item_spec : str
            This will be used to define the list returned as a key value
        
        class_name : str
            A string defaulted to 'z-smallstats' for a specific search
                of filter term when using find_all
        """
        results = Map({})
        specs_stats = {self.filter_term:item_stats}
        heap = tag.parent.find_all(self.item_content,specs_stats)
        results[item_spec] = [t.text.strip() for t in heap if len(t.text.strip()) > 1]
        self.item._add(results)
    
    def _get_requirements(self,
                          tag,
                          item_name,
                          item_spec,
                          type_filter_term='a',
                          weapon_class='z-white',
                          socket_class='zso_rwsock',
                          level_required='zso_rwlvlrq',
    ):
        """Pull Requirements from item
        
        Requirements Example:

            >>> ?runewords Spirit requirements
            ... {'requirements' : {
                                    'item'   : ['sword', 'shield'],
                                    'sockets': ['4 sockets', '4 sockets']
                                    'level'  : ['25'],
                                    .
                                    .
                                    .
                                   }
                }
        
        Parameters
        ----------

        tag : bs4.element.ResultSet
            The result set is a searchable set of strings 
                that pertain to a specific query of a site
        
        item_name : str
            This will be the item from top level search used only 
                to keep a specific pattern to the Map built
        
        item_spec : str
            This will be used to define the list returned as a key value
        
        weapon_class : str
            This can be armor or weapon or any type of item, but it
                will be defaulted to 'z-white' as it is unique to 
                the items specified
        
        socket_class : str
            A string that is defaulted to 'zso_rwsock' which
                is intuitively named for a socket requirement class container
        
        level_required : str
            A string that is defaulted to 'zso_rwlvlrq'
                also intuitively name for a lvl requirement class container
        """
        results = Map({})
        specs_item_type = {self.filter_term:weapon_class}
        specs_sockets = {self.filter_term:socket_class}
        specs_level = {self.filter_term:level_required}
        item_types = tag.parent.find_all(type_filter_term,specs_item_type)
        socket_rq = tag.parent.find_all(self.item_content,specs_sockets)
        lvl_rq = tag.parent.find_all(self.item_content,specs_level)
        results['socket_requirement'] = [t.parent.text.strip() for t in socket_rq]
        results['item_type'] = [re.sub(r'\s*','',t.text.strip().split('\n')[-1]) for t in item_types]
        results['level_required'] = [t.text.strip() for t in lvl_rq]
        self.item._add(results)
    
    def _get_all(self,
                 tag,
                 item_name,
                 item_spec,
    ):
        """Pull All details from item
        
        See above for individual examples
        
        Parameters
        ----------

        tag : bs4.element.ResultSet
            The result set is a searchable set of strings 
                that pertain to a specific query of a site
        
        item_name : str
            This will be the item from top level search used only 
                to keep a specific pattern to the Map built
        
        item_spec : str
            This will be used to define the list returned as a key value
        """
        for attr, method in self.queries.items():
            if attr != item_spec:
                getattr(self,method)(tag,
                                     item_name,
                                     attr)

    def __call__(self,
                 item,
                 item_name,
                 item_spec = 'all',
    ):
        """Call override to handle specific query if any"""

        rwitem = RuneWordItem(item_name) 
        self.item = rwitem

        if item_spec in self.queries.keys():
            getattr(self,self.queries[item_spec])(item,
                                                  item_name,
                                                  item_spec)
            return rwitem
        else:
            raise ValueError('Error: Value does not exist or query was in error!')
        
    

