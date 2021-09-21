# ===================================================================
# Author(s):
#
#       Name        Email
#      Jon Perry    dcjmp90@gmail.com
#
# Notes:
#
#   SearchModule will serve as a subclass of BaseModule
#   in current package subdirectory of Util: modules.
#
#   The idea is to have each query broken down into smaller more
#   managable tasks, and search will be handled in a dynamic way
# ===================================================================
"""SearchModule class implementation"""

from sanctuary.utils.modules.base_module import BaseModule
from sanctuary.utils.parser.cli_arguments import Map
import bs4 as bs
from importlib import import_module
import re

__all__ = ['ItemSearchModule']

class ItemSearchModule(BaseModule):
    """An Item Search Module for Searchable Item text

    Each Item Module implementation should have json output on a
    callable method of this object.

    This Item Module class will take in a specific type to search on
    callable, and every query will be handled the exact same way.
    """
    def __init__(self,
                 config,
                 parent_container='article',
                 child_container='span',
                 title_container='h3',
                 filter_term='class',
                 title_class='z-sort-name',
    ):
        self.config = config
        self.tokenizer = getattr(import_module(config.TOKENIZER_PACKAGE), 
                                               config.TOKENIZER_MODULE).__init__()
        super().__init__(parent_container,
                        child_container,
                        title_container,
                        filter_term,
                        title_class,
        )

    def _search(self):
        """TODO: search details
        """
        pass

    def __iter__(self):
        """TODO: iterator details
        """
        return self.results.__iter__()
    
    def __call__(self,
                 parent_container,
                 item_name = None,
                 item_spec = None,
                 **kwargs,
    ):
        """TODO: callable details
        """

        if not item_name and not item_spec:
            #TODO
            results = Map({})
            results['Item Names'] = []

            for link in parent_container:
                tags = link.find_all(self.title_container,{self.filter_term:self.title_class})
                if tags:
                    results['Item Names'].append([s.text for s in tags])
            return results
        elif not item_spec and item_name:
            #TODO
            for link in parent_container:
                tags = link.find_all(self.title_container,
                                     {self.filter_term:self.title_class},
                                     text=re.compile(item_name),
                                    )
                for tag in tags:
                    if tag:
                        # Find and report all information
                        self.results[item_name] = self.tokenizer(tag, item_name)

        elif item_spec and item_name:
            #TODO
            specs = {self.filter_term:self.title_class}
            for link in parent_container:
                tags = link.find_all(self.title_container,
                                     specs,
                                     text=re.compile(item_name))
                for tag in tags:
                    if tag:
                        return self.tokenizer(tag,
                                              item_name,
                                              item_spec=item_spec)
        else:
            self.results.append("No Data!! How did you get here?!")