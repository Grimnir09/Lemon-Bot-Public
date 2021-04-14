from settings import discord_token
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("Lemon Ready")


try:
    bot.load_extension('cogs.image_search')
    bot.load_extension('cogs.voice')
    bot.load_extension('cogs.youtube_search')
    #not really nessesary extentions comment them out if needed.
    bot.load_extension('cogs.intercepts')
    bot.load_extension('cogs.games')
except commands.errors.ExtensionNotFound as e:
    print(f'No Cog named: {e.name}')

bot.run(discord_token)
