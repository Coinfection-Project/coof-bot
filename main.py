from bot import launch, bot
from stats import on_ready_stats

if bot == None:
  launch()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    on_ready_stats()
