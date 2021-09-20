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
    ):
    super().__init__(parent_conatiner,
                     child_container,
    )

    def _search(self):
        """TODO: search details
        """
        pass

    def __iter__(self):
        """TODO: iterator details
        """
        pass
    
    def __call__(self):
        """TODO: callable details
        """
        pass
    
    def __str__(self):
        """TODO: tostring details
        """
        pass