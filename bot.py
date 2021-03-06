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
sys.path.append(sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
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
    async def runewords(ctx, *msg):
        msg = list(msg)
        item_name = None
        item_spec = None 
        
        if msg != []:
            if msg[-1] in args.RW_ITEM_SPECS:
                item_spec = msg[-1]
                item_name = ' '.join(msg[:-1])
                item_spec = None
                item_name = ' '.join(msg)

        items = config(item_type='runewords',
                        item_name=item_name,
                        item_spec=item_spec)
        out = ''
        if isinstance(items, dict):
            
            for k, v in items.items():
                out += k 
                print(v)
                if isinstance(v,list):
                    out += ':\n'+'\n'.join([''.join(l) for l in v])
                else:
                    out += ': '+v
        else:
            for rw in items:
                out += rw()

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