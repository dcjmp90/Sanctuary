import argparse

__all__ = ['Map', 'CommandLineArgs']

class Map(dict):
    """
    Pulled from the ever helpful stackoverflow

    Link
    ----
    https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary

    """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class CommandLineArgs:
    """Parse da commandzzzz"""

    def parse_args():
        """Okay...actually parse da commandzzz"""
        parser = argparse.ArgumentParser()
        parser.add_argument('--bot-type',
                            dest='BOT_TYPE',
                            type=str,
                            default='MUSIC,LOOKUP,FINDER,CHATBOT',
                            )
        parser.add_argument('--config-map',
                            dest='CONFIGS',
                            type=str,
                            default='MUSIC/music.cfg,LOOKUP/lookup.cfg,FINDER/finder.cfg,CHATBOT/chatbot.cfg',
                            )
        parser.add_argument('--search-items',
                            dest='SEARCH_ITEMS',
                            type=str,
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
                            type=lambda s : str(s).upper(),
                            required=True,
                            help="REQUIRED -- You will need to pass an argument for the bot type you want.",
                            )
        
        parser.add_argument('--item-specs',
                            dest='RW_ITEM_SPECS',
                            type=lambda s : [w.strip() for w in s.split(',')],
                            default='stats,requirements,recipe,all',
                            )

        parser.add_argument('--bot-prefix',
                            dest='PREFIX',
                            type=str,
                            required=True,
                            help="REQUIRED -- You will need to pass an argument to tell the bot what the prefix will be. (e.g, ! or ? )",
                            )
                            
        return parser.parse_args()
