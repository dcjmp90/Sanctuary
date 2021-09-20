import argparse

__all__ = ['Map', 'CommandLineArgs']

class Map(dict):
    """
    Pulled from the ever helpful stackoverflow

    Link
    ----
    https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary

    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]


class CommandLineArgs:
    """Parse da commandzzzz"""

    def parse_args():
        """Okay...actually parse da commandzzz"""
        parser = argparse.ArgumentParser()
        parser.add_argument('--bot-type',
                            dest='BOT_TYPE',
                            type=lambda s: Map({'NAME':token+'_TOKEN' for token in s.split(',')}),
                            default='MUSIC,LOOKUP,FINDER,CHATBOT',
                            )
        parser.add_argument('--config-map',
                            dest='CONFIGS',
                            type=lambda s: Map({token.split('/')[0]:token.split('/')[1] for token in s.split(',')}),
                            default='MUSIC/music.cfg,LOOKUP/lookup.cfg,FINDER/finder.cfg,CHATBOT/chatbot.cfg',
                            )
        parser.add_argument('--search-items',
                            dest='SEARCH_ITEMS',
                            type=lambda s: Map({'NAME':token for token in s.split(',')}),
                            default='runewords,uniques,sets,base',
                            )
        parser.add_argument('--delimiter',
                            dest='DELIM',
                            type=str,
                            default=',',
                            )
        parser.add_argument('--default-config',
                            dest='DEFAULT_CONFIG',
                            type=str,
                            default="CHATBOT",
                            )
        parser.add_argument('--server-id',
                            dest='SERVER_ID',
                            type=str,
                            default="DISCORD_GUILD",
                            )
        parser.add_argument('--base-url',
                            dest='BASE_URL',
                            type=str,
                            default="https://www.diablo2.io/",
                            )
        parser.add_argument('--bs4-parser',
                            dest='PARSER',
                            type=str,
                            default="html.parser",
                            )
        parser.add_argument('--item-tag',
                            dest='ITEM_CONTAINER',
                            type=str,
                            default="article",
                            )
        parser.add_argument('--use-bot',
                            dest='BOT_REQUEST',
                            type=lamda s : str(s).upper(),
                            required=True,
                            help="REQUIRED -- You will need to pass an argument for the bot type you want.",
                            )
        parser.add_argument('--bot-prefix',
                            dest='PREFIX',
                            type=str,
                            required=True,
                            help="REQUIRED -- You will need to pass an argument to tell the bot what the prefix will be. (e.g, ! or ? )",
                            )
                            
        return parser.parse_args()
