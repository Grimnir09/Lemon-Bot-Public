import asyncio
from discord.ext import commands
import discord
from google_images_search import GoogleImagesSearch
from settings import gis_project_cx, gis_token

#   cog instanced class


class image_search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description="Query Google Images by typing `!img <your query> without the arrows")
    @commands.guild_only()
    async def img(self, ctx, *, arg):
        '''
        This cog command is responsible for pulling google images
        Input: message context args from discord user
        Output: posts images related to search
        '''
        # send typing to the bot
        async with ctx.typing():
            # set up our search
            gis = GoogleImagesSearch(
                gis_token,
                gis_project_cx,
                validate_images=True
            )
            # join our list of args into a string
            image_query = ''.join(arg)
            # set up our search params
            _search_params = {
                'q': image_query,
                'num': 10,
            }
            # execute first search
            gis.search(search_params=_search_params)

            # put our results in a object
            gis_results = gis.results()

            # embed creation
            embed = discord.Embed(
                title=f'Google Image Results for `{arg}`',
                description=f'{ctx.author.mention} Use `n` for next image, `c` to cancel.',
                color=0xeeff00
            )
            embed.set_author(name=ctx.author.nick,
                             icon_url=ctx.author.avatar_url)
            embed.set_image(url=f'{gis_results[0].url}')

            # send first embed outside of loop
            main_msg = await ctx.send(embed=embed)
            # pop our first result after post
            gis_results.pop(0)

        # wait_for loop
        while gis_results:
            # this try/except is really only for catching the timeout, if we timeout lets end the loop
            try:
                msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author
                                              and message.content.lower() == 'n'
                                              or message.content.lower() == 'c',
                                              timeout=30
                                              )
            except asyncio.TimeoutError:
                embed.set_footer(
                    text="Search timed out, start a new search to continue.", icon_url=self.bot.user.avatar_url)
                await main_msg.edit(embed=embed)
                break

            # if the user cancels, delete the embed and break
            if msg.content.lower() == 'c':
                await main_msg.delete()
                await msg.delete()
                break
            # if the user has passed our wait_for check and has posted a n, we need to delete his message and then set a new embed image
            if msg:
                async with ctx.typing():
                    await msg.delete()
                    embed.set_image(url=gis_results[0].url)
                    await main_msg.edit(embed=embed)
                    gis_results.pop(0)

            # if we are at the end of our page list lets go get another page of images
            if len(gis_results) == 0:
                async with ctx.typing():
                    gis.next_page()
                    gis_results = gis.results()

    # img error handling
    @img.error
    async def img_error(self, ctx, error):
        #error handling for DMs
        if isinstance(error, commands.errors.NoPrivateMessage):
            await ctx.send(f"{ctx.author.mention} {error}")


def setup(bot):
    bot.add_cog(image_search(bot))
