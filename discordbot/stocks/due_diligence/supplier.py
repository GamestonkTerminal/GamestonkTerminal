import discord
import discordbot.config_discordbot as cfg

from gamestonk_terminal.stocks.due_diligence import csimarket_model


async def supplier_command(ctx, ticker=""):
    """Displays suppliers of the company [CSIMarket]"""

    try:
        # Debug user input
        if cfg.DEBUG:
            print(f"!stocks.dd.supplier {ticker}")

        if ticker == "":
            raise Exception("A ticker is required")

        tickers = csimarket_model.get_suppliers(ticker)

        if tickers == "":
            raise Exception("Enter a valid ticker")

        # Debug user output
        if cfg.DEBUG:
            print(tickers)

        # Output data
        embed = discord.Embed(
            title="Stocks: [CSIMarket] Company Suppliers",
            description=tickers,
            colour=cfg.COLOR,
        )
        embed.set_author(
            name=cfg.AUTHOR_NAME,
            icon_url=cfg.AUTHOR_ICON_URL,
        )

        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(
            title="ERROR Stocks: [CSIMarket] Company Suppliers",
            colour=cfg.COLOR,
            description=e,
        )
        embed.set_author(
            name=cfg.AUTHOR_NAME,
            icon_url=cfg.AUTHOR_ICON_URL,
        )

        await ctx.send(embed=embed)
