### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###


from openbb_core.app.static.container import Container


class Extensions(Container):
    # fmt: off
    """
Routers:
    /commodity
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
    - commodity@1.0.1
    - crypto@1.1.3
    - currency@1.1.3
    - derivatives@1.1.3
    - econometrics@1.1.3
    - economy@1.1.3
    - equity@1.1.3
    - etf@1.1.3
    - fixedincome@1.1.3
    - index@1.1.3
    - news@1.1.3
    - quantitative@1.1.3
    - regulators@1.1.3
    - technical@1.1.4

    - alpha_vantage@1.1.3
    - benzinga@1.1.3
    - biztoc@1.1.3
    - cboe@1.1.3
    - ecb@1.1.3
    - federal_reserve@1.1.3
    - finra@1.1.3
    - finviz@1.0.2
    - fmp@1.1.3
    - fred@1.1.3
    - government_us@1.1.3
    - intrinio@1.1.3
    - nasdaq@1.1.4
    - oecd@1.1.3
    - polygon@1.1.3
    - sec@1.1.3
    - seeking_alpha@1.1.3
    - stockgrid@1.1.3
    - tiingo@1.1.3
    - tmx@1.0.0
    - tradier@1.0.0
    - tradingeconomics@1.1.3
    - wsj@1.1.3
    - yfinance@1.1.3    """
    # fmt: on

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
    def commodity(self):
        # pylint: disable=import-outside-toplevel
        from . import commodity

        return commodity.ROUTER_commodity(command_runner=self._command_runner)

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
