import asyncio
from discord.ext import commands
import discord
import os


async def voice_channel_check(ctx):
    if ctx.author.voice is None:
        return False
    return True


class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description="Play Sounds over discord voice")
    @commands.check(voice_channel_check)
    @commands.guild_only()
    async def vox(self, ctx, *, arg):
        '''This cog command is responsible for playing sounds over discord voice'''
        sound_list = ''
        if arg.lower() == 'list':
            sound_list = []
            for file in os.walk(f'{os.getcwd()}\\sounds\\'):
                sound_list = file[2]
                str_list = '\n'.join(sound_list)
            await ctx.send(f'``` {str_list} ```')
            return

        await ctx.message.delete()
        voice_channel = ctx.author.voice.channel
        if voice_channel != None:
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(source=f"sounds/{arg}",))
            while vc.is_playing():
                await asyncio.sleep(1)
            await vc.disconnect()

    # vox error handling
    @vox.error
    async def vox_error(self, ctx, error):
        # if it fails our check
        if isinstance(error, commands.CheckFailure):
            return
        # if DM
        if isinstance(error, commands.errors.NoPrivateMessage):
            await ctx.send(f"{ctx.author.mention} {error}")
            return


def setup(bot):
    bot.add_cog(voice(bot))
