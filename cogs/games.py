import asyncio
from discord.ext import commands
import discord
from random import randint



class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description="Roll dice, ex. <!roll 1 20> for a 1d20")
    @commands.guild_only()

    async def roll(self, ctx, dice:int, sides:int):
        #idiot rangler
        if dice > 20:
            await ctx.reply("Sorry Limit is `20d`. Thank you Avery.")
            return

        total = 0
        rolls_left = dice
        while rolls_left != 0:
            total += randint(1, sides)
            rolls_left = rolls_left - 1

        await ctx.reply(f':game_die: Rolling a {dice}d{sides}... \n `{total}`', mention_author=False)

    # vox error handling
    @roll.error
    async def roll_error(self, ctx, error):
        # if it fails our check
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply("Dont put a `d` in between your numbers, just a space.",  mention_author=False)
            return
        # if DM
        if isinstance(error, commands.errors.NoPrivateMessage):
            await ctx.send(f"{ctx.author.mention} {error}")
            return


def setup(bot):
    bot.add_cog(games(bot))
