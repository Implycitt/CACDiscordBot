import discord
from discord.ext import commands
import json

with open("config.json", 'r') as configjsonfile:
  configdata = json.load(configjsonfile)
  TOKEN = configdata["TOKEN"]
  CID = configdata["CID"]
  PREFIX = configdata["PREFIX"]

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

def correctPerms(ctx):
  return ctx.channel.id == CID and '@everyone' not in ctx.message.content.lower() and 'here' not in ctx.message.content.lower()

def hasPermission():
  return commands.check(correctPerms)

@bot.event
async def onRead():
  print(f'{bot.user} has connected to Discord!')

@bot.command()
@hasPermission()
async def ping(ctx):
  await ctx.send(f'pong! Latency: {str(round(bot.latency * 1000))}ms')

@bot.command()
@hasPermission()
async def echo(ctx, *args):
  arguments = ' '.join(args)
  await ctx.send(f'{arguments}')

bot.run(TOKEN)