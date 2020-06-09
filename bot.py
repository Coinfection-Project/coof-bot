import discord
from discord.ext import commands

TOKEN  = ''
bot = None

def launch():
  bot = commands.Bot()
  bot.run(TOKEN)
