from typing import Literal

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


class GuildRecruit(commands.Cog):
    """
    Simple Cog to post image of recruitment info.
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=709671911252164640,
            force_registration=True,
        )

    async def red_delete_data_for_user(
            self, *, requester: RequestType, user_id: int
    ) -> None:
        # TODO: Replace this with the proper end user data removal handling.
        super().red_delete_data_for_user(requester=requester, user_id=user_id)

    @commands.command()
    async def recruit(ctx):
        embed: discord.Embed = discord.Embed(
            title="title", description="description",
            color=discord.Color.red()
        )
file = open("guild.txt", "r")
for line in file.readlines():
    l = line.strip()
    loglist.append(l)
    embed.add_field(name="⠀", value=" `{0}`".format(l), inline=False)
embed.set_author(name="name")

await ctx.send(embed=embed)