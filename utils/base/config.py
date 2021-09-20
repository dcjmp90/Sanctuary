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

import abc
from dotenv import load_dotenv
from discord.ext import commands
from sanctuary.utils.config.loaders import load_configs
from sanctuary.utils.parser.cli_arguments import Map

__all__ = ['BaseConfig']


class BaseConfig(abc.ABC):
    """A Base Configuration for Config class
    
    Each config implementation should have a relatively 
    simple setup, depending on the type of bot this config
    will be altered with some minor additions.

    Each config will be setup for a more singular design
    and purpose, such as item lookup or join in-game event.
    These will scale and grow as needs present themselves.
    """

    @abstractmethod
    def __init__(self,
                 name,
                 prefix,
                 args,
                 ):
        """Base class constructor"""
        self.name = name
        self.prefix = prefix
        self.args = args
        self.config_name = args.BOT_TYPE[name].CONFIG
        self._set_config(self.config_name)
        load_dotenv()

    @abstractmethod
    def _get_bot(self):
        """return bot from set config"""
        return commands.Bot(command_prefix=self.prefix)

    @abstractmethod
    def _get_token_id(self):
        """return dot env token id for discord bot"""
        return os.getenv(self.args.BOT_TYPE[self.name].NAME)


    @abstractmethod
    def _get_server_id(self):
        """return dot env server id for discord server"""
        return os.getenv(self.args.SERVER_ID)


    @abstractmethod
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
        configs = self.args.CONFIGS
        if config_name in configs.keys():
            self.config = load_configs(configs[config_name])
        else:
            default = self.args.DEFAULT_CONFIG
            self.config = load_configs(configs[default])


