# ===================================================================
# Author(s):
#
#       Name        Email
#      Jon Perry    dcjmp90@gmail.com
#
# Notes:
#
#   This will hold subclasses of the Abstract Config class
# ===================================================================
"""A Config class for item lookup"""


import bs4 as bs
import urllib.request as url_request
from sanctuary.utils.config.base_config import BaseConfig
from sanctuary.utils.parser.cli_arguments import Map

__all__ = ['ItemLookupConfig']


class ItemLookupConfig(BaseConfig):
    """A processor for bot data

    Performs various bot tasks like look up 
    of item stats or look up of names of runes.
    Anything that is within the diablo 2 database.

    Parameters
    ----------

    bot_name : str
        The name for the lookup bot
    
    prefix : str
        The type of prefix to filter in discord
    
    args : Values objects from builtin
        This will be all the argsparser arguments

    Notes
    -----

    currently only building a single lookup bot, but this may change
    based on needs, the lookups may need to be delegated to many.

    Usage
    -----

    ?<item_type> -- bs4.BeautifulSoup object parse of <item_type>
            will return an array-like structure of all of this <item_type>
    
    ?<item_type> <item_name> stats -- bs4.BeautifulSoup object parse of <item_name>
            will return stats of <item_name>
    
    ?<item_type> <item_name> requirements -- bs4.BeautifulSoup object parse of <item_name>
            will return requirements of <item_name>
    
    >>> ?runewords spirit requirements
    ... returns: lvl. 25, 4 Socket Sword/Shield, Tal->Thul->Ort->Amn

    >>> ?runewords spirit stats
    ... 
    """
    
    def __init__(self,
                 bot_name,
                 args,
                 prefix='?',
    ):
        self.bot_name = bot_name
        self.prefix = prefix
        self.args = args
        super().__init__(self.bot_name,
                         self.prefix,
                         self.args,
        )
       
        self.searchables = [ v for k, v in self.SEARCH_ITEMS.items() ]
        self.bs_parser = Map({})
        
        for name in self.searchables:
            url = url_request.urlopen(self.args.BASE_URL+name)
            self.bs_parser[name] = bs.BeautifulSoup(url.read(), self.config.PARSER)


    def _item_type(self, item_type):
        """Parser for all of type"""

        if item_type.lower() in self.bs_parser.keys():
            item_names = []
            _bs_parser = self.bs_parser[item_type.lower()]

            for item_container in _bs_parser.find_all(self.config.CONTAINER):
                item_names.append(item_container.a.get_text())

            return item_names

        else:
            return None
    

    def __call__(self,
                 item_type,
                 item_name = None,
                 item_spec = None,
                 **kwargs,
    ):
        """Override of the call method"""

        if not item_name:
            return self._item_type(item_type)
        elif not item_spec and item_name:
            # specific item + details search
            pass
        else:
            # deep search
            pass

            