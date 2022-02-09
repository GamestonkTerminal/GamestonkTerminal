import os
from datetime import datetime, timedelta

import disnake
from matplotlib import pyplot as plt
from PIL import Image

import discordbot.config_discordbot as cfg
import discordbot.helpers
from discordbot.config_discordbot import gst_imgur, logger
from gamestonk_terminal.common.technical_analysis import volatility_model
from gamestonk_terminal.config_plot import PLOT_DPI
from gamestonk_terminal.helper_funcs import plot_autoscale


async def donchian_command(
    ctx, ticker="", upper_length="25", lower_length="100", start="", end=""
):
    """Displays chart with donchian channel [Yahoo Finance]"""

    try:

        # Debug
        if cfg.DEBUG:
            logger.debug(
                "!stocks.ta.donchian %s %s %s %s %s",
                ticker,
                upper_length,
                lower_length,
                start,
                end,
            )

        # Check for argument
        if ticker == "":
            raise Exception("Stock ticker is required")

        if start == "":
            start = datetime.now() - timedelta(days=365)
        else:
            start = datetime.strptime(start, cfg.DATE_FORMAT)

        if end == "":
            end = datetime.now()
        else:
            end = datetime.strptime(end, cfg.DATE_FORMAT)

        if not upper_length.lstrip("-").isnumeric():
            raise Exception("Number has to be an integer")
        upper_length = float(upper_length)
        if not lower_length.lstrip("-").isnumeric():
            raise Exception("Number has to be an integer")
        lower_length = float(lower_length)

        ticker = ticker.upper()
        df_stock = discordbot.helpers.load(ticker, start)
        if df_stock.empty:
            raise Exception("Stock ticker is invalid")

        # Retrieve Data
        df_stock = df_stock.loc[(df_stock.index >= start) & (df_stock.index < end)]

        df_ta = volatility_model.donchian(
            df_stock["High"], df_stock["Low"], upper_length, lower_length
        )

        # Output Data
        plt.style.use("seaborn")
        fig, ax = plt.subplots(figsize=plot_autoscale(), dpi=PLOT_DPI)
        ax.plot(df_stock.index, df_stock["Adj Close"].values, color="k", lw=3)
        ax.plot(df_ta.index, df_ta.iloc[:, 0].values, "b", lw=1.5, label="upper")
        ax.plot(df_ta.index, df_ta.iloc[:, 1].values, "b", lw=1.5, ls="--")
        ax.plot(df_ta.index, df_ta.iloc[:, 2].values, "b", lw=1.5, label="lower")
        ax.set_title(f"{ticker} donchian")
        ax.set_xlim(df_stock.index[0], df_stock.index[-1])
        ax.set_xlabel("Time")
        ax.set_ylabel("Price ($)")

        ax.legend([ticker, df_ta.columns[0], df_ta.columns[1], df_ta.columns[2]])
        ax.fill_between(
            df_ta.index,
            df_ta.iloc[:, 0].values,
            df_ta.iloc[:, 2].values,
            alpha=0.1,
            color="b",
        )
        ax.grid(b=True, which="major", color="#666666", linestyle="-")

        plt.gcf().autofmt_xdate()
        fig.tight_layout(pad=1)

        plt.legend()

        plt.savefig("ta_donchian.png")
        imagefile = "ta_donchian.png"

        img = Image.open(imagefile)
        print(img.size)
        im_bg = Image.open(cfg.IMG_BG)
        h = img.height + 240
        w = img.width + 520

        img = img.resize((w, h), Image.ANTIALIAS)
        x1 = int(0.5 * im_bg.size[0]) - int(0.5 * img.size[0])
        y1 = int(0.5 * im_bg.size[1]) - int(0.5 * img.size[1])
        x2 = int(0.5 * im_bg.size[0]) + int(0.5 * img.size[0])
        y2 = int(0.5 * im_bg.size[1]) + int(0.5 * img.size[1])
        img = img.convert("RGB")
        im_bg.paste(img, box=(x1 - 5, y1, x2 - 5, y2))
        im_bg.save(imagefile, "PNG", quality=100)

        image = Image.open(imagefile)
        image = discordbot.helpers.autocrop_image(image, 0)
        image.save(imagefile, "PNG", quality=100)

        uploaded_image = gst_imgur.upload_image("ta_donchian.png", title="something")
        image_link = uploaded_image.link
        if cfg.DEBUG:
            logger.debug("Image URL: %s", image_link)
        title = "Stocks: Donchian-Channels " + ticker
        embed = disnake.Embed(title=title, colour=cfg.COLOR)
        embed.set_author(
            name=cfg.AUTHOR_NAME,
            icon_url=cfg.AUTHOR_ICON_URL,
        )
        embed.set_image(url=image_link)
        os.remove("ta_donchian.png")

        await ctx.send(embed=embed)

    except Exception as e:
        embed = disnake.Embed(
            title="ERROR Stocks: Donchian-Channels",
            colour=cfg.COLOR,
            description=e,
        )
        embed.set_author(
            name=cfg.AUTHOR_NAME,
            icon_url=cfg.AUTHOR_ICON_URL,
        )

        await ctx.send(embed=embed, delete_after=30.0)
