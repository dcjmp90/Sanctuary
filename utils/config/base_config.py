# ===================================================================
# Author(s):
#
#       Name        Email
#      Jon Perry    dcjmp90@gmail.com
#
# Notes:
#
#   Base will serve as an abstraction of each class
#   in current package directory Utils. 
# ===================================================================
"""Config base class implementation"""

import os
import abc
from dotenv import load_dotenv
from discord.ext import commands
from sanctuary.utils.config.loaders import load_configs
from sanctuary.utils.parser.cli_arguments import Map

__all__ = ['BaseConfig']


class BaseConfig(metaclass=abc.ABCMeta):
    """A Base Configuration for Config class
    
    Each config implementation should have a relatively 
    simple setup, depending on the type of bot this config
    will be altered with some minor additions.

    Each config will be setup for a more singular design
    and purpose, such as item lookup or join in-game event.
    These will scale and grow as needs present themselves.
    """

    def __init__(self,
                 name,
                 prefix,
                 args,
    ):
        self.name = name
        self.prefix = prefix
        self.args = args
        self.BOT_TYPE = Map({t:t+'_TOKEN' for t in args.BOT_TYPE.split(args.DELIM)})
        self.CONFIGS = Map({t.split('/')[0]:t.split('/')[1] for t in args.CONFIGS.split(args.DELIM)})
        self.SEARCH_ITEMS = Map({t.upper():t for t in args.SEARCH_ITEMS.split(args.DELIM) })
        self.config_name = name
        self._set_config(self.config_name)
        load_dotenv()

    def _get_bot(self):
        """return bot from set config"""
        return commands.Bot(command_prefix=self.prefix)

    def _get_token_id(self):
        """return dot env token id for discord bot"""
        return os.getenv(self.BOT_TYPE[self.config_name])


    def _get_server_id(self):
        """return dot env server id for discord server"""
        return os.getenv(self.args.SERVER_ID)


    def _set_config(self, config_name):
        """Pull config file from provided name

        Parameters
        ----------

        config_name: str
            The configuration name as a string
        
        Returns
        -------

        None: NoneType
            Sets internally and will not return
        
        Notes
        -----

        Will look into possibility of altering this class 
            and having bot isntances instead.
        Right now this will have a configuration set for 
            different event types based on a config name 
            and event name.
        """
        if config_name in self.CONFIGS.keys():
            self.config = load_configs()(self.CONFIGS[config_name])
            print('loaded config',config_name)
        else:
            print('Did not load config:', config_name)
            default = self.args.DEFAULT_CONFIG
            self.config = load_configs()(self.CONFIGS[default])


