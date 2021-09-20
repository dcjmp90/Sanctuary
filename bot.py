# Author(s):
#       Name        Email
#       Jon Perry   dcjmp90@gmail.com
#
#
# Notes:
#
# This bot has been made purely for fun and integration into the
# release of Diablo II: Resurrected. 
# Sanctuary seeks to support players needs from trade, to item lookup,
# and currently seeking ability to support player status tracking.
# ============================================================================
import os
import discord
import args
import ItemLookupConfig
from discord.ext import commands

if args.BOT_REQUEST == 'LOOKUP':
    config = ItemLookupConfig(args.BOT_REQUEST, args)

bot = config._get_bot()


@bot.command(name='runewords')
async def runewords(ctx,
                    item_name = None,
                    item_spec = None,
                    **kwargs,
):
    pprint = config('runewords', item_name, item_spec, **kwargs)
    await ctx.send(pprint)

bot.run(config._get_token_id())