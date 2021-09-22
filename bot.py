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
import sys
import os
import discord
from sanctuary.utils import args
from sanctuary.utils import ItemLookupConfig
from sanctuary.utils import RunewordLogger
from discord.ext import commands

if args.BOT_REQUEST == 'LOOKUP':
    config = ItemLookupConfig(args.BOT_REQUEST, args)
    bot = config._get_bot()

    #TODO
    #@bot.event
    #async def on_ready():

    @bot.command(name='runewords')
    async def runewords(ctx,
                        item_name= None,
                        item_spec= None,
    ):
        
        pprint = config(item_type='runewords',
                        item_name=item_name,
                        item_spec=item_spec)

        logger = RunewordLogger(pprint,
                                item_name,
                                item_spec)
        pprint = str(logger)
        await ctx.send(pprint)


    @bot.command(name='sets')
    async def runewords(ctx,
                        item_name= None,
                        item_spec= None,
    ):
        #TODO
        
        await ctx.send("Sets are still in development RiP...")


    @bot.command(name='uniques')
    async def runewords(ctx,
                        item_name= None,
                        item_spec= None,
    ):
        #TODO
        
        await ctx.send("Uniques are still in development RiP...")

bot.run(config._get_token_id())