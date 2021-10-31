import asyncio
import discord
import config_discordbot as cfg

# pylint: disable=wrong-import-order
from discordbot import gst_bot

from economy.feargreed import feargreed_command
from economy.overview import overview_command
from economy.indices import indices_command
from economy.futures import futures_command
from economy.usbonds import usbonds_command
from economy.glbonds import glbonds_command
from economy.currencies import currencies_command
from economy.valuation import valuation_command
from economy.performance import performance_command


class EconomyCommands(discord.ext.commands.Cog):
    """Economy Commands menu"""

    def __init__(self, bot: discord.ext.commands.Bot):
        self.bot = bot

    @discord.ext.commands.command(name="economy.feargreed")
    async def feargreed(self, ctx: discord.ext.commands.Context, arg=""):
        """CNN Fear and Greed Index [CNN]"""
        await feargreed_command(ctx, arg)

    @discord.ext.commands.command(name="economy.overview")
    async def overview(self, ctx: discord.ext.commands.Context, arg=""):
        """Market data overview [Wall St. Journal]"""
        await overview_command(ctx, arg)

    @discord.ext.commands.command(name="economy.indices")
    async def indices(self, ctx: discord.ext.commands.Context, arg=""):
        """US indices overview [Wall St. Journal]"""
        await indices_command(ctx, arg)

    @discord.ext.commands.command(name="economy.futures")
    async def futures(self, ctx: discord.ext.commands.Context, arg=""):
        """Futures and commodities overview [Wall St. Journal]"""
        await futures_command(ctx, arg)

    @discord.ext.commands.command(name="economy.usbonds")
    async def usbonds(self, ctx: discord.ext.commands.Context, arg=""):
        """US bonds overview [Wall St. Journal]"""
        await usbonds_command(ctx, arg)

    @discord.ext.commands.command(name="economy.glbonds")
    async def glbonds(self, ctx: discord.ext.commands.Context, arg=""):
        """Global bonds overview [Wall St. Journal]"""
        await glbonds_command(ctx, arg)

    @discord.ext.commands.command(name="economy.currencies")
    async def currencies(self, ctx: discord.ext.commands.Context, arg=""):
        """Currencies overview [Wall St. Journal]"""
        await currencies_command(ctx, arg)

    @discord.ext.commands.command(name="economy.valuation")
    async def valuation(self, ctx: discord.ext.commands.Context, arg=""):
        """Valuation of sectors, industry, country [Finviz]"""
        await valuation_command(ctx, arg)

    @discord.ext.commands.command(name="economy.performance")
    async def performance(self, ctx: discord.ext.commands.Context, arg=""):
        """Performance of sectors, industry, country [Finviz]"""
        await performance_command(ctx, arg)

    @discord.ext.commands.command(name="economy")
    async def economy(self, ctx: discord.ext.commands.Context):
        """Economy Context Menu

        Returns
        -------
        Sends a message to the discord user with the commands from the economy context.
        The user can then select a reaction to trigger a command.
        """

        if cfg.DEBUG:
            print("!economy")

        text = (
            "0️⃣ !economy.overview\n"
            "1️⃣ !economy.futures\n"
            "2️⃣ !economy.usbonds\n"
            "3️⃣ !economy.glbonds\n"
            "4️⃣ !economy.indices\n"
            "5️⃣ !economy.currencies\n"
            "6️⃣ !economy.feargreed\n"
            "7️⃣ !economy.valuation <GROUP>\n"
            "8️⃣ !economy.performance <GROUP>"
        )

        title = "Economy Menu"
        embed = discord.Embed(title=title, description=text, colour=cfg.COLOR)
        embed.set_author(
            name=cfg.AUTHOR_NAME,
            icon_url=cfg.AUTHOR_ICON_URL,
        )
        msg = await ctx.send(embed=embed)

        emoji_list = ["0️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]

        for emoji in emoji_list:
            await msg.add_reaction(emoji)

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in emoji_list

        try:
            reaction, _ = await gst_bot.wait_for(
                "reaction_add", timeout=cfg.MENU_TIMEOUT, check=check
            )
            if reaction.emoji == "0️⃣":
                if cfg.DEBUG:
                    print("Reaction selected: 0")
                await overview_command(ctx)
            elif reaction.emoji == "1️⃣":
                if cfg.DEBUG:
                    print("Reaction selected: 1")
                await futures_command(ctx)
            elif reaction.emoji == "2️⃣":
                if cfg.DEBUG:
                    print("Reaction selected: 2")
                await usbonds_command(ctx)
            elif reaction.emoji == "3️⃣":
                if cfg.DEBUG:
                    print("Reaction selected: 3")
                await glbonds_command(ctx)
            elif reaction.emoji == "4️⃣":
                if cfg.DEBUG:
                    print("Reaction selected: 4")
                await indices_command(ctx)
            elif reaction.emoji == "5️⃣":
                if cfg.DEBUG:
                    print("Reaction selected: 5")
                await currencies_command(ctx)
            elif reaction.emoji == "6️⃣":
                if cfg.DEBUG:
                    print("Reaction selected: 6")
                await feargreed_command(ctx)
            elif reaction.emoji == "7️⃣":
                if cfg.DEBUG:
                    print("Reaction selected: 7")
                await valuation_command(ctx)
            elif reaction.emoji == "8️⃣":
                if cfg.DEBUG:
                    print("Reaction selected: 8")
                await performance_command(ctx)

            for emoji in emoji_list:
                await msg.remove_reaction(emoji, ctx.bot.user)

        except asyncio.TimeoutError:
            text = text + "\n\nCOMMAND TIMEOUT."
            embed = discord.Embed(title=title, description=text)
            await msg.edit(embed=embed)
            for emoji in emoji_list:
                await msg.remove_reaction(emoji, ctx.bot.user)


def setup(bot: discord.ext.commands.Bot):
    gst_bot.add_cog(EconomyCommands(bot))
