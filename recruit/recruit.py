from typing import Literal
import sys
import csv
import urllib.request
from io import StringIO
from contextlib import redirect_stdout
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
    async def recruit(self, ctx):
        #replace url with link to your google spreadsheet.
        url = ''
        response = urllib.request.urlopen(url)
        lines = [l.decode('utf-8') for l in response.readlines()]
        cr = csv.reader(lines)

        original_stdout = sys.stdout
        with open('guild.txt', 'w') as f:
            with redirect_stdout(f):
                for row in cr:
                    print(','.join(row))
                sys.stdout = original_stdout
        with open('guild.txt', 'r') as g:
            content = g.read()
            await ctx.send(content)
