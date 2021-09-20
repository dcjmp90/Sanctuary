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
from sanctuary.utils.parser.tokenizers import ItemTokenizer
import bs4 as bs
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
                 parent_conatiner='article',
                 child_container='span',
                 title_container='h3',
                 filter_term='class',
                 title_class='z-sort-name',
    ):
    self.tokenizer = ItemTokenizer()
    super().__init__(parent_conatiner,
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
                 parent_conatiner,
                 item_name = None,
                 item_spec = None,
                 **kwargs,
    ):
        """TODO: callable details
        """
        if not item_name and not item_spec:
            #TODO
            for link in parent_conatiner.findAll(self.parent_conatiner):
                self.results = []
                tags = link.find_all(self.title_container)
                if tags:
                    self.results.append([''.join(s.text for s in tags)])
        elif not item_spec and item_name:
            #TODO
            for line in parent_conatiner.findAll(self.parent_conatiner):
                self.results = []
                tags = link.find_all(self.title_container,
                                     {self.filter_term:self.title_class},
                                     text=re.compile(item_name),
                                    )
                for tag in tags:
                    if tag:
                        # Find and report all information
                        self.results.append(self.tokenizer(tag.parent, item_name))

        elif item_spec and item_name:
            #TODO
        else:
            self.results.append("No Data!! How did you get here?!")