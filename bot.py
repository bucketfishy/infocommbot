import os
import discord

from random import *
import pickle

from dotenv import load_dotenv
from discord.ext import commands
from datetime import *
import requests

from keep_alive import keep_alive

from small import nya, oo

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='quack ')
bot.remove_command("help")

error = ("sorry, i couldn't understand")

@bot.event
async def on_ready():

    await bot.change_presence(activity=discord.Game('with infocomm :) | quack'))


@bot.command(name="ping")
async def pingpong(ctx):
    try:
        response = "pong, " + ctx.author.nick +"!"
    except:
        response = "pong, " + ctx.author.name +"!"

    await ctx.send(response)

@bot.command(name="help")
async def help(ctx):
    await ctx.send("""
hello! i'm duck. but digital. haha! bet you didn't know that.
there are some useful commands and some fun commands :)
> quack help - shows this
> quack nya [message] - nya's your message
> quack oo [message] - oo's your message
> quack scoreboard - shows the grouping scoreboard!
> quack github - links to the github!

have fun in infocomm discord!
    """)


@bot.command('github')
async def github(ctx):
    e = discord.Embed(title="infocomm bot's github",
                      url="https://github.com/fqdingsky/infocommbot",
                      description="github repository for infocomm bot's code!")
    await ctx.send(embed=e)

@bot.command('test')
async def test(ctx):
    if ctx.author.id == 670962000964354049:
        await ctx.send("tongyu testing :D")


@bot.command('nya')
async def nya_(ctx, *args):
    await ctx.send(nya(" ".join(args[:])))

@bot.command('oo')
async def oo_(ctx, *args):
    await ctx.send(oo(" ".join(args[:])))

@bot.command('scoreboard')
async def scoreboard(ctx):
    scores = requests.get("https://keepthescore.co/api/swpoukgtwjr/players").json()
    response = "__**infocomm group scoreboard!**__\n"
    for i in scores["players"]:
        response += i["player_name"] + ": " + str(i["total"]) + "\n"
    await ctx.send(response)

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    message = ctx.content.lower().split()

    if 'duck' in message:
        await ctx.send("duck? me!")

    await bot.process_commands(ctx)

keep_alive()
bot.run(TOKEN)
