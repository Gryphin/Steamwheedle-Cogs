from typing import Literal
import os
import sys
#import urllib.request
#from io import StringIO
from contextlib import redirect_stdout
import discord
from redbot.core import commands, app_commands
from redbot.core.bot import Red
from redbot.core.config import Config
from .dl import dl
RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]
dl.dl()

class recruit(commands.Cog):
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
    @app_commands.command()
    async def recruit(self, interaction: discord.Interaction):
        mypath = os.path.dirname(os.path.abspath(__file__))
        with open(mypath+'/guild.txt', 'r') as g:
                content = g.read()
                embed = discord.Embed(title='Recruiting Guilds', description=f"{content}", color=discord.Color.red())
                await interaction.response.send_message(embed=embed)
