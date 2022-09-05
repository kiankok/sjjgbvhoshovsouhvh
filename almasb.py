import token
import discord
import asyncio
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/',intents=intents) 
token = ('MTAxNTg4MzE2OTgwMDY1MDkwMg.GA9jyc.IQxB39jqRT7MQWXt1YK9IEG2aC1TAHNEs0rnCM')
@bot.event
async def on_ready(ctx):    
    print ("bot run shod")
@bot.command()
async def developer(ctx):
    await ctx.send ("@KIANKOK#0313")
@bot.command()
async def who_is_almasmafor(ctx):
    await ctx.send ("الماس یکی از رپر قدیمی است که متاسفانه زیاد شناخته نشد وی فعالیت خود را در سال 2006 میلادی آغاز کرد اینجانب به کانادا سفر کرد و در کانادا کامپیوتر شروع به کار کرد وی بعد چند سال مغازه خود را زد و شروع به کار کرد و وقتی کرونا اومد وی در شرکت یوبیسافت کار کرد")
@bot.command()
async def level(ctx):
    await ctx.send ("coming soon")

@bot.command()
async def server_info(ctx):
    await ctx.send ("_the offical almasmafor server_developer kiankok_admins MH.RAHMANI sezar braveputak mamad")

@bot.command()
async def owner(ctx):
    await ctx.send ("almasmafor")

@bot.command()
async def bot_info(ctx):
    await ctx.send ("version 1.0.0 | work = orginal almasmafor bot | developer = KIANKOK#0313 | server = almasmafor | private bot")
    
    
    
    
    



bot.run ('MTAxNTg4MzE2OTgwMDY1MDkwMg.GA9jyc.IQxB39jqRT7MQWXt1YK9IEG2aC1TAHNEs0rnCM')