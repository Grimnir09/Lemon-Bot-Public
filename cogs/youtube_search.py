
from discord.ext import commands
from youtubesearchpython.__future__ import VideosSearch


class youtube_search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description="Query Youtube by typing `!yt <your query> without the arrows")
    async def yt(self, ctx, *, arg):
        '''This cog command is responsible for searching youtube videos'''
        yt_search = VideosSearch(arg, limit=1)
        yt_result = await yt_search.next()
        yt_title = yt_result["result"][0]["title"]
        yt_description = None
        try:
            yt_description = yt_result["result"][0]["descriptionSnippet"][0]["text"]
        except:
            pass

        yt_link = yt_result["result"][0]["link"]

        await ctx.send(f'**Youtube Result for: ** `{arg}` \n **Title: **  `{yt_title}` \n **Description: ** `{yt_description}` \n {yt_link}')

    @yt.error
    async def yt_error(self, ctx, error):
        await ctx.send(f':no_entry: `{error}`')


def setup(bot):
    bot.add_cog(youtube_search(bot))
