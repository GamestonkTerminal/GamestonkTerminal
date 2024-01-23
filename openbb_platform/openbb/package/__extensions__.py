### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###


from openbb_core.app.static.container import Container


class Extensions(Container):
    # fmt: off
    """
Routers:
    /crypto
    /currency
    /derivatives
    /econometrics
    /economy
    /equity
    /etf
    /fixedincome
    /index
    /news
    /quantitative
    /regulators
    /technical

Extensions:
    - crypto@1.1.1
    - currency@1.1.1
    - derivatives@1.1.1
    - econometrics@1.1.1
    - economy@1.1.1
    - equity@1.1.1
    - etf@1.1.1
    - fixedincome@1.1.1
    - index@1.1.1
    - news@1.1.1
    - openbb_charting@1.1.1
    - quantitative@1.1.1
    - regulators@1.1.1
    - technical@1.1.2

    - alpha_vantage@1.1.1
    - benzinga@1.1.1
    - biztoc@1.1.1
    - cboe@1.1.1
    - ecb@1.1.1
    - federal_reserve@1.1.1
    - finra@1.1.1
    - finviz@1.1.0
    - fmp@1.1.1
    - fred@1.1.1
    - government_us@1.1.1
    - intrinio@1.1.1
    - nasdaq@1.1.2
    - oecd@1.1.1
    - polygon@1.1.1
    - sec@1.1.1
    - seeking_alpha@1.1.1
    - stockgrid@1.1.1
    - tiingo@1.1.1
    - tradingeconomics@1.1.1
    - ultima@1.0.0b0
    - wsj@1.1.1
    - yfinance@1.1.1    """
    # fmt: on

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
    def crypto(self):
        # pylint: disable=import-outside-toplevel
        from . import crypto

        return crypto.ROUTER_crypto(command_runner=self._command_runner)

    @property
    def currency(self):
        # pylint: disable=import-outside-toplevel
        from . import currency

        return currency.ROUTER_currency(command_runner=self._command_runner)

    @property
    def derivatives(self):
        # pylint: disable=import-outside-toplevel
        from . import derivatives

        return derivatives.ROUTER_derivatives(command_runner=self._command_runner)

    @property
    def econometrics(self):
        # pylint: disable=import-outside-toplevel
        from . import econometrics

        return econometrics.ROUTER_econometrics(command_runner=self._command_runner)

    @property
    def economy(self):
        # pylint: disable=import-outside-toplevel
        from . import economy

        return economy.ROUTER_economy(command_runner=self._command_runner)

    @property
    def equity(self):
        # pylint: disable=import-outside-toplevel
        from . import equity

        return equity.ROUTER_equity(command_runner=self._command_runner)

    @property
    def etf(self):
        # pylint: disable=import-outside-toplevel
        from . import etf

        return etf.ROUTER_etf(command_runner=self._command_runner)

    @property
    def fixedincome(self):
        # pylint: disable=import-outside-toplevel
        from . import fixedincome

        return fixedincome.ROUTER_fixedincome(command_runner=self._command_runner)

    @property
    def index(self):
        # pylint: disable=import-outside-toplevel
        from . import index

        return index.ROUTER_index(command_runner=self._command_runner)

    @property
    def news(self):
        # pylint: disable=import-outside-toplevel
        from . import news

        return news.ROUTER_news(command_runner=self._command_runner)

    @property
    def quantitative(self):
        # pylint: disable=import-outside-toplevel
        from . import quantitative

        return quantitative.ROUTER_quantitative(command_runner=self._command_runner)

    @property
    def regulators(self):
        # pylint: disable=import-outside-toplevel
        from . import regulators

        return regulators.ROUTER_regulators(command_runner=self._command_runner)

    @property
    def technical(self):
        # pylint: disable=import-outside-toplevel
        from . import technical

        return technical.ROUTER_technical(command_runner=self._command_runner)
