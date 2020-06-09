import discord

TOKEN  = ''
bot = None

def launch():
  bot = discord.Client()
  bot.run(TOKEN)
