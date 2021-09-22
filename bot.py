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
from sanctuary.components import RuneWordItem
from discord.ext import commands

if args.BOT_REQUEST == 'LOOKUP':
    config = ItemLookupConfig(args.BOT_REQUEST, args)
    bot = config._get_bot()

    #TODO
    #@bot.event
    #async def on_ready():

    @bot.command(name='runewords', aliases=['runeword', 'runes', 'rw'])
    async def runewords(ctx,
                        item_name= None,
                        item_spec= None,
    ):
        
        item = config(item_type='runewords',
                        item_name=item_name,
                        item_spec=item_spec)

        if isinstance(item, dict):
            out = ''
            for k, v in item.items():
                out += k 
                if isinstance(v,list):
                    out += ':\n'+'\n'.join(v)
                else:
                    out += ': '+v
        else:
            out = item()
        
        await ctx.send(out)


    @bot.command(name='sets', aliases=['set','setitem','itemset'])
    async def runewords(ctx,
                        item_name= None,
                        item_spec= None,
    ):
        #TODO
        
        await ctx.send("Sets are still in development RiP...")


    @bot.command(name='uniques', aliases=['unique', 'uniqueitem'])
    async def runewords(ctx,
                        item_name= None,
                        item_spec= None,
    ):
        #TODO
        
        await ctx.send("Uniques are still in development RiP...")

bot.run(config._get_token_id())