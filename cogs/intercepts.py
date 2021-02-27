from discord.ext import commands
from asyncio import TimeoutError
from settings import NotSoBot_id


class intercepts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        '''
        This cog specificly handles command interception from notsobot if notsobot is offline (which is often)
        and invokes the command on the behalf of the user.
        '''
        # TODO check if first word of message.content is a command instead of using startswith()
        # check to see if a user is trying to invoke a command through notsobot
        if message.content.startswith('.img'):
            # get the context of the message
            ctx = await self.bot.get_context(message)
            try:
                # wait for notsobot to respond
                msg = await self.bot.wait_for('message', check=lambda message: message.author.id == NotSoBot_id, timeout=5)
            # not so bot didnt respond
            except TimeoutError:
                # notify user
                await ctx.send(":no_entry: No Response from NotSoBot, invoking command.")
                # invoke command, use split to remove command from content.
                await ctx.invoke(self.bot.get_command('img'), arg=ctx.message.content.split(' ', 1)[1])
                return


def setup(bot):
    bot.add_cog(intercepts(bot))
