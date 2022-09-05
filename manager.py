import token
import discord
import asyncio
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/',intents=intents) 
token = ('MTAxNjI0NDI0OTY1OTk3MzgwMg.GuwIAv.rUNePqxxZN84J7vFf_SuThaB3QLWl5r2D9fAM0')
@bot.event
async def on_ready(ctx):    
    print ("bot run shod")

@bot.command()
async def massage_to_almas(ctx):
    await ctx.send ("almasmafor account |Almasmafor#5949")

@bot.command()
async def info(ctx):
    await ctx.send ("the manager of almasmafor")

@bot.command()
async def bot_info(ctx):
    await ctx.send ("version 1.0.0 | work = manager | developer = KIANKOK#0313 | private bot | server = almasmafor")

bot.run ('MTAxNjI0NDI0OTY1OTk3MzgwMg.GuwIAv.rUNePqxxZN84J7vFf_SuThaB3QLWl5r2D9fAM0')