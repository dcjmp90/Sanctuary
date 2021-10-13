# ===================================================================
# Author(s):
#
#       Name        Email
#      Jon Perry    dcjmp90@gmail.com
#
# Notes:
#
# ===================================================================
"""Logger will handle specific logging needs per type"""

from sanctuary.utils.parser.cli_arguments import Map
import re

__all__ = ['RunewordLogger']


class RunewordLogger:
    """Logger for Runeword tpyes
    """
    def __init__(self,
                 results,
                 item_name,
                 item_spec,
    ):
        self.results = results
        self.item_name = item_name
        self.item_spec = item_spec
    
    def _flatten(self, array_like):
        """Flatten a 1D array_like"""
        string_builder = ''

        if isinstance(array_like, dict):
            for k, v in array_like.items():
                string_builder += '**'+k.upper()+'**:' + ' \n ' + self._flatten(v)
        if isinstance(array_like, list):
            for e in array_like:
                if isinstance(e, str):
                    string_builder += '   ' + e + ' \n '
                else:
                    string_builder += self._flatten(e)

        return string_builder
    
    def __str__(self):
        results = self._flatten(self.results)

        if self.item_name is not None:
            return '> **'+self.item_name+'** \n '+results
        else:
            return results