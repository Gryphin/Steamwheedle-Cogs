from typing import Literal
import gspread
import os
import sys
import datetime
import urllib.request
from io import StringIO
from contextlib import redirect_stdout
import discord
from redbot.core import commands, app_commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


class DeckDecoder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='decode', description='Decodes a deck code using deckdecode.py')
    async def decode_deck(self, ctx, *, deck_code: str):
        """Decodes a deck code and displays the result in an embed."""
        try:
            # Run deckdecode.py with the provided deck code
            process = subprocess.Popen(['python', 'deckdecode.py', deck_code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()

            if stderr:
                embed = discord.Embed(
                    title="Deck Decoding Error",
                    description=f"An error occurred during decoding:\n```\n{stderr}\n```",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)
                return

            try:
                 decoded_data = json.loads(stdout)

                 embed = discord.Embed(
                     title="Decoded Deck",
                     color=discord.Color.blue()
                 )

                 embed.add_field(name="Format", value=decoded_data.get("format", "Unknown"), inline=False)
                 embed.add_field(name="Hero", value=decoded_data.get("hero", "Unknown"), inline=False)

                 cards_string = ""
                 for card in decoded_data.get("cards", []):
                     cards_string += f"{card['count']}x {card['name']}\n"
                 if cards_string:
                     embed.add_field(name="Cards", value=cards_string, inline=False)
                 else:
                     embed.add_field(name="Cards", value="No Cards Found", inline=False)
                 await ctx.send(embed=embed)

            except json.JSONDecodeError:
                embed = discord.Embed(
                    title="Deck Decoding Error",
                    description=f"Invalid JSON returned from deckdecode.py:\n```\n{stdout}\n```",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed)

        except FileNotFoundError:
            embed = discord.Embed(
                title="Deck Decoding Error",
                description="deckdecode.py not found. Ensure it is in the same directory as the bot.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(
                title="Unexpected Error",
                description=f"An unexpected error occurred: ```{e}```",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)              