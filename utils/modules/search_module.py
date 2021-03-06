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
    def __init__(self, config):
        self.tokenizer = getattr(import_module(config.TOKENIZER_PACKAGE), 
                                               config.TOKENIZER_MODULE)()
        super().__init__(config)

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

            results = Map({})
            results['ITEM_NAME'] = []

            for link in parent_container:
                tags = link.find_all(self.config.TITLE_CONTAINER,
                                     {self.config.FILTER_TERM:self.config.TITLE_CLASS},
                                    )
                if tags:
                    results['ITEM_NAME'].append([s.text for s in tags])
            return results
        elif not item_spec and item_name:
            results = []
            for link in parent_container:
                tags = link.find_all(self.config.TITLE_CONTAINER,
                                     {self.config.FILTER_TERM:self.config.TITLE_CLASS},
                                     text=re.compile(item_name),
                                    )
                for tag in tags:
                    if tag:
                        # Find and report all information
                        results.append(self.tokenizer(tag, item_name))
            return results

        elif item_spec and item_name:
            results = []
            for link in parent_container:
                tags = link.find_all(self.config.TITLE_CONTAINER,
                                     {self.config.FILTER_TERM:self.config.TITLE_CLASS},
                                     text=re.compile(item_name),
                                    )
                for tag in tags:
                    if tag:
                        results.append(self.tokenizer(tag,
                                                      item_name,
                                                      item_spec=item_spec))
            return results
        else:
            msg = 'No Data!! How did you get here with \''+item_name+'\'?!'
            print(msg)
            return Map({'ITEM_NAME':[msg]})