from typing import Literal
import gspread
import os
import sys
import urllib.request
from io import StringIO
from contextlib import redirect_stdout
import discord
from redbot.core import commands, app_commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


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
###If PermissionError: [Errno 13] Permission denied: 'guild.txt' use absolute path to guild.txt
    @app_commands.command()
    async def recruit(self, interaction: discord.Interaction):
        mypath = os.path.dirname(os.path.abspath(__file__))
        gc = gspread.service_account()
        sh = gc.open("Steamwheedle Recruitment")
        worksheet = sh.worksheet("Recruitment")
        guilds_list = [item for item in worksheet.col_values(1) if item]
        original_stdout = sys.stdout
        with open(mypath+'/guild.txt', 'w') as f:
            with redirect_stdout(f):
                for item in guilds_list:
                    print(item)
                sys.stdout = original_stdout
        with open(mypath+'/guild.txt', 'r') as g:
                content = g.read()
                embed = discord.Embed(title='Recruiting Guilds', description=f"{content}", color=discord.Color.red())
                embed.set_author(icon_url="https://cdn.discordapp.com/attachments/1241482905822298246/1252150852882268170/steamwheedle-cartel.png")
                await interaction.response.send_message(embed=embed)
