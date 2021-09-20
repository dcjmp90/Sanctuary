import json
from sanctuary.utils.parser.cli_arguments import Map

__all__ = ['load_configs']


class load_configs:
    """load_config class for Config class support"""

    def __call__(config_file):
        """load in a json config file"""
        
        with open(config_file, 'r') as openfile:
            config = json.load(openfile)
        return Map(config)