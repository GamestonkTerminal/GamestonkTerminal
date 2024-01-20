### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

import datetime
from typing import List, Literal, Optional, Union

from openbb_core.app.model.custom_parameter import OpenBBCustomParameter
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.utils.decorators import validate
from openbb_core.app.static.utils.filters import filter_inputs
from typing_extensions import Annotated


class ROUTER_etf(Container):
    """/etf
    countries
    historical
    holdings
    holdings_date
    holdings_performance
    info
    price_performance
    search
    sectors
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate
    def countries(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for. (ETF)"),
        ],
        provider: Optional[Literal["fmp", "tmx"]] = None,
        **kwargs
    ) -> OBBject:
        """ETF Country weighting.

        Parameters
        ----------
        symbol : str
            Symbol to get data for. (ETF)
        provider : Optional[Literal['fmp', 'tmx']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        use_cache : bool
            Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours. (provider: tmx)

        Returns
        -------
        OBBject
            results : List[EtfCountries]
                Serializable results.
            provider : Optional[Literal['fmp', 'tmx']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EtfCountries
        ------------
        country : str
            The country of the exposure.  Corresponding values are normalized percentage points.

        Example
        -------
        >>> from openbb import obb
        >>> obb.etf.countries(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/etf/countries",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def historical(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for. (ETF)"),
        ],
        start_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="Start date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        end_date: Annotated[
            Union[datetime.date, None, str],
            OpenBBCustomParameter(
                description="End date of the data, in YYYY-MM-DD format."
            ),
        ] = None,
        provider: Optional[Literal["yfinance"]] = None,
        **kwargs
    ) -> OBBject:
        """ETF Historical Market Price.

        Parameters
        ----------
        symbol : str
            Symbol to get data for. (ETF)
        start_date : Optional[datetime.date]
            Start date of the data, in YYYY-MM-DD format.
        end_date : Optional[datetime.date]
            End date of the data, in YYYY-MM-DD format.
        provider : Optional[Literal['yfinance']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'yfinance' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[EtfHistorical]
                Serializable results.
            provider : Optional[Literal['yfinance']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EtfHistorical
        -------------
        date : date
            The date of the data.
        open : float
            The open price.
        high : float
            The high price.
        low : float
            The low price.
        close : float
            The close price.
        volume : Optional[Annotated[int, Ge(ge=0)]]
            The trading volume.
        adj_close : Optional[float]
            The adjusted closing price of the ETF. (provider: yfinance)

        Example
        -------
        >>> from openbb import obb
        >>> obb.etf.historical(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/etf/historical",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                    "start_date": start_date,
                    "end_date": end_date,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def holdings(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for. (ETF)"),
        ],
        provider: Optional[Literal["fmp", "sec", "tmx"]] = None,
        **kwargs
    ) -> OBBject:
        """Get the holdings for an individual ETF.

        Parameters
        ----------
        symbol : str
            Symbol to get data for. (ETF)
        provider : Optional[Literal['fmp', 'sec', 'tmx']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        date : Optional[Union[str, datetime.date]]
            A specific date to get data for. This needs to be _exactly_ the date of the filing. Use the holdings_date command/endpoint to find available filing dates for the ETF. (provider: fmp);
            A specific date to get data for.  The date represents the period ending.  The date entered will return the closest filing. (provider: sec)
        cik : Optional[str]
            The CIK of the filing entity. Overrides symbol. (provider: fmp)
        use_cache : bool
            Whether or not to use cache for the request. (provider: sec);
            Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours. (provider: tmx)

        Returns
        -------
        OBBject
            results : List[EtfHoldings]
                Serializable results.
            provider : Optional[Literal['fmp', 'sec', 'tmx']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EtfHoldings
        -----------
        symbol : Optional[str]
            Symbol representing the entity requested in the data. (ETF)
        name : Optional[str]
            Name of the ETF holding.
        lei : Optional[str]
            The LEI of the holding. (provider: fmp, sec)
        title : Optional[str]
            The title of the holding. (provider: fmp)
        cusip : Optional[str]
            The CUSIP of the holding. (provider: fmp, sec)
        isin : Optional[str]
            The ISIN of the holding. (provider: fmp, sec)
        balance : Optional[float]
            The balance of the holding. (provider: fmp, sec)
        units : Optional[Union[str, float]]
            The units of the holding. (provider: fmp, sec)
        currency : Optional[str]
            The currency of the holding. (provider: fmp, sec, tmx)
        value : Optional[float]
            The value of the holding in USD. (provider: fmp, sec)
        weight : Optional[float]
            The weight of the holding in ETF in %. (provider: fmp, sec);
            The weight of the asset in the portfolio, as a normalized percentage. (provider: tmx)
        payoff_profile : Optional[str]
            The payoff profile of the holding. (provider: fmp, sec)
        asset_category : Optional[str]
            The asset category of the holding. (provider: fmp, sec)
        issuer_category : Optional[str]
            The issuer category of the holding. (provider: fmp, sec)
        country : Optional[str]
            The country of the holding. (provider: fmp, sec, tmx)
        is_restricted : Optional[str]
            Whether the holding is restricted. (provider: fmp, sec)
        fair_value_level : Optional[int]
            The fair value level of the holding. (provider: fmp, sec)
        is_cash_collateral : Optional[str]
            Whether the holding is cash collateral. (provider: fmp, sec)
        is_non_cash_collateral : Optional[str]
            Whether the holding is non-cash collateral. (provider: fmp, sec)
        is_loan_by_fund : Optional[str]
            Whether the holding is loan by fund. (provider: fmp, sec)
        cik : Optional[str]
            The CIK of the filing. (provider: fmp)
        acceptance_datetime : Optional[str]
            The acceptance datetime of the filing. (provider: fmp)
        other_id : Optional[str]
            Internal identifier for the holding. (provider: sec)
        loan_value : Optional[float]
            The loan value of the holding. (provider: sec)
        issuer_conditional : Optional[str]
            The issuer conditions of the holding. (provider: sec)
        asset_conditional : Optional[str]
            The asset conditions of the holding. (provider: sec)
        maturity_date : Optional[date]
            The maturity date of the debt security. (provider: sec)
        coupon_kind : Optional[str]
            The type of coupon for the debt security. (provider: sec)
        rate_type : Optional[str]
            The type of rate for the debt security, floating or fixed. (provider: sec)
        annualized_return : Optional[float]
            The annualized return on the debt security. (provider: sec)
        is_default : Optional[str]
            If the debt security is defaulted. (provider: sec)
        in_arrears : Optional[str]
            If the debt security is in arrears. (provider: sec)
        is_paid_kind : Optional[str]
            If the debt security payments are are paid in kind. (provider: sec)
        derivative_category : Optional[str]
            The derivative category of the holding. (provider: sec)
        counterparty : Optional[str]
            The counterparty of the derivative. (provider: sec)
        underlying_name : Optional[str]
            The name of the underlying asset associated with the derivative. (provider: sec)
        option_type : Optional[str]
            The type of option. (provider: sec)
        derivative_payoff : Optional[str]
            The payoff profile of the derivative. (provider: sec)
        expiry_date : Optional[date]
            The expiry or termination date of the derivative. (provider: sec)
        exercise_price : Optional[float]
            The exercise price of the option. (provider: sec)
        exercise_currency : Optional[str]
            The currency of the option exercise price. (provider: sec)
        shares_per_contract : Optional[float]
            The number of shares per contract. (provider: sec)
        delta : Optional[Union[str, float]]
            The delta of the option. (provider: sec)
        rate_type_rec : Optional[str]
            The type of rate for reveivable portion of the swap. (provider: sec)
        receive_currency : Optional[str]
            The receive currency of the swap. (provider: sec)
        upfront_receive : Optional[float]
            The upfront amount received of the swap. (provider: sec)
        floating_rate_index_rec : Optional[str]
            The floating rate index for reveivable portion of the swap. (provider: sec)
        floating_rate_spread_rec : Optional[float]
            The floating rate spread for reveivable portion of the swap. (provider: sec)
        rate_tenor_rec : Optional[str]
            The rate tenor for reveivable portion of the swap. (provider: sec)
        rate_tenor_unit_rec : Optional[Union[str, int]]
            The rate tenor unit for reveivable portion of the swap. (provider: sec)
        reset_date_rec : Optional[str]
            The reset date for reveivable portion of the swap. (provider: sec)
        reset_date_unit_rec : Optional[Union[str, int]]
            The reset date unit for reveivable portion of the swap. (provider: sec)
        rate_type_pmnt : Optional[str]
            The type of rate for payment portion of the swap. (provider: sec)
        payment_currency : Optional[str]
            The payment currency of the swap. (provider: sec)
        upfront_payment : Optional[float]
            The upfront amount received of the swap. (provider: sec)
        floating_rate_index_pmnt : Optional[str]
            The floating rate index for payment portion of the swap. (provider: sec)
        floating_rate_spread_pmnt : Optional[float]
            The floating rate spread for payment portion of the swap. (provider: sec)
        rate_tenor_pmnt : Optional[str]
            The rate tenor for payment portion of the swap. (provider: sec)
        rate_tenor_unit_pmnt : Optional[Union[str, int]]
            The rate tenor unit for payment portion of the swap. (provider: sec)
        reset_date_pmnt : Optional[str]
            The reset date for payment portion of the swap. (provider: sec)
        reset_date_unit_pmnt : Optional[Union[str, int]]
            The reset date unit for payment portion of the swap. (provider: sec)
        repo_type : Optional[str]
            The type of repo. (provider: sec)
        is_cleared : Optional[str]
            If the repo is cleared. (provider: sec)
        is_tri_party : Optional[str]
            If the repo is tri party. (provider: sec)
        principal_amount : Optional[float]
            The principal amount of the repo. (provider: sec)
        principal_currency : Optional[str]
            The currency of the principal amount. (provider: sec)
        collateral_type : Optional[str]
            The collateral type of the repo. (provider: sec)
        collateral_amount : Optional[float]
            The collateral amount of the repo. (provider: sec)
        collateral_currency : Optional[str]
            The currency of the collateral amount. (provider: sec)
        exchange_currency : Optional[str]
            The currency of the exchange rate. (provider: sec)
        exchange_rate : Optional[float]
            The exchange rate. (provider: sec)
        currency_sold : Optional[str]
            The currency sold in a Forward Derivative. (provider: sec)
        currency_amount_sold : Optional[float]
            The amount of currency sold in a Forward Derivative. (provider: sec)
        currency_bought : Optional[str]
            The currency bought in a Forward Derivative. (provider: sec)
        currency_amount_bought : Optional[float]
            The amount of currency bought in a Forward Derivative. (provider: sec)
        notional_amount : Optional[float]
            The notional amount of the derivative. (provider: sec)
        notional_currency : Optional[str]
            The currency of the derivative's notional amount. (provider: sec)
        unrealized_gain : Optional[float]
            The unrealized gain or loss on the derivative. (provider: sec)
        shares : Optional[Union[str, int]]
            The value of the assets under management. (provider: tmx)
        market_value : Optional[Union[str, float]]
            The market value of the holding. (provider: tmx)
        share_percentage : Optional[float]
            The share percentage of the holding, as a normalized percentage. (provider: tmx)
        share_change : Optional[Union[str, float]]
            The change in shares of the holding. (provider: tmx)
        exchange : Optional[str]
            The exchange code of the holding. (provider: tmx)
        type_id : Optional[str]
            The holding type ID of the asset. (provider: tmx)
        fund_id : Optional[str]
            The fund ID of the asset. (provider: tmx)

        Example
        -------
        >>> from openbb import obb
        >>> obb.etf.holdings(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/etf/holdings",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def holdings_date(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for. (ETF)"),
        ],
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject:
        """Get the holdings filing date for an individual ETF.

        Parameters
        ----------
        symbol : str
            Symbol to get data for. (ETF)
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        cik : Optional[str]
            The CIK of the filing entity. Overrides symbol. (provider: fmp)

        Returns
        -------
        OBBject
            results : List[EtfHoldingsDate]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EtfHoldingsDate
        ---------------
        date : date
            The date of the data.

        Example
        -------
        >>> from openbb import obb
        >>> obb.etf.holdings_date(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/etf/holdings_date",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def holdings_performance(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject:
        """Get the ETF holdings performance.

        Parameters
        ----------
        symbol : str
            Symbol to get data for.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[EtfHoldingsPerformance]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EtfHoldingsPerformance
        ----------------------
        one_day : Optional[float]
            One-day return.
        wtd : Optional[float]
            Week to date return.
        one_week : Optional[float]
            One-week return.
        mtd : Optional[float]
            Month to date return.
        one_month : Optional[float]
            One-month return.
        qtd : Optional[float]
            Quarter to date return.
        three_month : Optional[float]
            Three-month return.
        six_month : Optional[float]
            Six-month return.
        ytd : Optional[float]
            Year to date return.
        one_year : Optional[float]
            One-year return.
        three_year : Optional[float]
            Three-year return.
        five_year : Optional[float]
            Five-year return.
        ten_year : Optional[float]
            Ten-year return.
        max : Optional[float]
            Return from the beginning of the time series.
        symbol : Optional[str]
            The ticker symbol. (provider: fmp)

        Example
        -------
        >>> from openbb import obb
        >>> obb.etf.holdings_performance(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/etf/holdings_performance",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def info(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for. (ETF)"),
        ],
        provider: Optional[Literal["fmp", "tmx"]] = None,
        **kwargs
    ) -> OBBject:
        """ETF Information Overview.

        Parameters
        ----------
        symbol : str
            Symbol to get data for. (ETF)
        provider : Optional[Literal['fmp', 'tmx']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        use_cache : bool
            Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours. (provider: tmx)

        Returns
        -------
        OBBject
            results : List[EtfInfo]
                Serializable results.
            provider : Optional[Literal['fmp', 'tmx']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EtfInfo
        -------
        symbol : str
            Symbol representing the entity requested in the data. (ETF)
        name : Optional[str]
            Name of the ETF.
        inception_date : Optional[str]
            Inception date of the ETF.
        asset_class : Optional[str]
            Asset class of the ETF. (provider: fmp)
        aum : Optional[float]
            Assets under management. (provider: fmp);
            The AUM of the ETF. (provider: tmx)
        avg_volume : Optional[Union[float, int]]
            Average trading volume of the ETF. (provider: fmp);
            The average daily volume of the ETF. (provider: tmx)
        cusip : Optional[str]
            CUSIP of the ETF. (provider: fmp)
        description : Optional[str]
            Description of the ETF. (provider: fmp, tmx)
        domicile : Optional[str]
            Domicile of the ETF. (provider: fmp)
        etf_company : Optional[str]
            Company of the ETF. (provider: fmp)
        expense_ratio : Optional[float]
            Expense ratio of the ETF. (provider: fmp)
        isin : Optional[str]
            ISIN of the ETF. (provider: fmp)
        nav : Optional[float]
            Net asset value of the ETF. (provider: fmp)
        nav_currency : Optional[str]
            Currency of the ETF's net asset value. (provider: fmp)
        website : Optional[str]
            Website link of the ETF. (provider: fmp);
            The website of the ETF. (provider: tmx)
        holdings_count : Optional[int]
            Number of holdings in the ETF. (provider: fmp)
        issuer : Optional[str]
            The issuer of the ETF. (provider: tmx)
        investment_style : Optional[str]
            The investment style of the ETF. (provider: tmx)
        esg : Optional[bool]
            Whether the ETF qualifies as an ESG fund. (provider: tmx)
        currency : Optional[str]
            The currency of the ETF. (provider: tmx)
        unit_price : Optional[float]
            The unit price of the ETF. (provider: tmx)
        close : Optional[float]
            The closing price of the ETF. (provider: tmx)
        prev_close : Optional[float]
            The previous closing price of the ETF. (provider: tmx)
        return_1m : Optional[float]
            The one-month return of the ETF. (provider: tmx)
        return_3m : Optional[float]
            The three-month return of the ETF. (provider: tmx)
        return_6m : Optional[float]
            The six-month return of the ETF. (provider: tmx)
        return_ytd : Optional[float]
            The year-to-date return of the ETF. (provider: tmx)
        return_1y : Optional[float]
            The one-year return of the ETF. (provider: tmx)
        return_3y : Optional[float]
            The three-year return of the ETF. (provider: tmx)
        return_5y : Optional[float]
            The five-year return of the ETF. (provider: tmx)
        return_10y : Optional[float]
            The ten-year return of the ETF. (provider: tmx)
        return_from_inception : Optional[float]
            The return from inception of the ETF. (provider: tmx)
        avg_volume_30d : Optional[int]
            The 30-day average volume of the ETF. (provider: tmx)
        pe_ratio : Optional[float]
            The price-to-earnings ratio of the ETF. (provider: tmx)
        pb_ratio : Optional[float]
            The price-to-book ratio of the ETF. (provider: tmx)
        management_fee : Optional[float]
            The management fee of the ETF. (provider: tmx)
        mer : Optional[float]
            The management expense ratio of the ETF. (provider: tmx)
        distribution_yield : Optional[float]
            The distribution yield of the ETF. (provider: tmx)
        dividend_frequency : Optional[str]
            The dividend payment frequency of the ETF. (provider: tmx)

        Example
        -------
        >>> from openbb import obb
        >>> obb.etf.info(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/etf/info",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def price_performance(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for."),
        ],
        provider: Optional[Literal["fmp"]] = None,
        **kwargs
    ) -> OBBject:
        """Price performance as a return, over different periods.

        Parameters
        ----------
        symbol : str
            Symbol to get data for.
        provider : Optional[Literal['fmp']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.

        Returns
        -------
        OBBject
            results : List[PricePerformance]
                Serializable results.
            provider : Optional[Literal['fmp']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        PricePerformance
        ----------------
        one_day : Optional[float]
            One-day return.
        wtd : Optional[float]
            Week to date return.
        one_week : Optional[float]
            One-week return.
        mtd : Optional[float]
            Month to date return.
        one_month : Optional[float]
            One-month return.
        qtd : Optional[float]
            Quarter to date return.
        three_month : Optional[float]
            Three-month return.
        six_month : Optional[float]
            Six-month return.
        ytd : Optional[float]
            Year to date return.
        one_year : Optional[float]
            One-year return.
        three_year : Optional[float]
            Three-year return.
        five_year : Optional[float]
            Five-year return.
        ten_year : Optional[float]
            Ten-year return.
        max : Optional[float]
            Return from the beginning of the time series.
        symbol : Optional[str]
            The ticker symbol. (provider: fmp)

        Example
        -------
        >>> from openbb import obb
        >>> obb.equity.price.performance(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/etf/price_performance",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def search(
        self,
        query: Annotated[
            Optional[str], OpenBBCustomParameter(description="Search query.")
        ] = "",
        provider: Optional[Literal["fmp", "tmx"]] = None,
        **kwargs
    ) -> OBBject:
        """Search for ETFs.

        An empty query returns the full list of ETFs from the provider.


            Parameters
            ----------
            query : Optional[str]
                Search query.
            provider : Optional[Literal['fmp', 'tmx']]
                The provider to use for the query, by default None.
                If None, the provider specified in defaults is selected or 'fmp' if there is
                no default.
            exchange : Optional[Literal['AMEX', 'NYSE', 'NASDAQ', 'ETF', 'TSX', 'EURONEXT']]
                The exchange code the ETF trades on. (provider: fmp)
            is_active : Optional[Literal[True, False]]
                Whether the ETF is actively trading. (provider: fmp)
            div_freq : Optional[Literal['monthly', 'annually', 'quarterly']]
                The dividend payment frequency. (provider: tmx)
            sort_by : Optional[Literal['nav', 'return_1m', 'return_3m', 'return_6m', 'return_1y', 'return_3y', 'return_ytd', 'beta_1y', 'volume_avg_daily', 'management_fee', 'distribution_yield', 'pb_ratio', 'pe_ratio']]
                The column to sort by. (provider: tmx)
            use_cache : bool
                Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours. (provider: tmx)

            Returns
            -------
            OBBject
                results : List[EtfSearch]
                    Serializable results.
                provider : Optional[Literal['fmp', 'tmx']]
                    Provider name.
                warnings : Optional[List[Warning_]]
                    List of warnings.
                chart : Optional[Chart]
                    Chart object.
                extra: Dict[str, Any]
                    Extra info.

            EtfSearch
            ---------
            symbol : str
                Symbol representing the entity requested in the data.(ETF)
            name : Optional[str]
                Name of the ETF.
            market_cap : Optional[float]
                The market cap of the ETF. (provider: fmp)
            sector : Optional[str]
                The sector of the ETF. (provider: fmp)
            industry : Optional[str]
                The industry of the ETF. (provider: fmp)
            beta : Optional[float]
                The beta of the ETF. (provider: fmp)
            price : Optional[float]
                The current price of the ETF. (provider: fmp)
            last_annual_dividend : Optional[float]
                The last annual dividend paid. (provider: fmp)
            volume : Optional[float]
                The current trading volume of the ETF. (provider: fmp)
            exchange : Optional[str]
                The exchange code the ETF trades on. (provider: fmp)
            exchange_name : Optional[str]
                The full name of the exchange the ETF trades on. (provider: fmp)
            country : Optional[str]
                The country the ETF is registered in. (provider: fmp)
            actively_trading : Optional[Literal[True, False]]
                Whether the ETF is actively trading. (provider: fmp)
            short_name : Optional[str]
                The short name of the ETF. (provider: tmx)
            inception_date : Optional[str]
                The inception date of the ETF. (provider: tmx)
            issuer : Optional[str]
                The issuer of the ETF. (provider: tmx)
            investment_style : Optional[str]
                The investment style of the ETF. (provider: tmx)
            esg : Optional[bool]
                Whether the ETF qualifies as an ESG fund. (provider: tmx)
            currency : Optional[str]
                The currency of the ETF. (provider: tmx)
            unit_price : Optional[float]
                The unit price of the ETF. (provider: tmx)
            close : Optional[float]
                The closing price of the ETF. (provider: tmx)
            prev_close : Optional[float]
                The previous closing price of the ETF. (provider: tmx)
            return_1m : Optional[float]
                The one-month return of the ETF. (provider: tmx)
            return_3m : Optional[float]
                The three-month return of the ETF. (provider: tmx)
            return_6m : Optional[float]
                The six-month return of the ETF. (provider: tmx)
            return_ytd : Optional[float]
                The year-to-date return of the ETF. (provider: tmx)
            return_1y : Optional[float]
                The one-year return of the ETF. (provider: tmx)
            beta_1y : Optional[float]
                The one-year beta of the ETF. (provider: tmx)
            return_3y : Optional[float]
                The three-year return of the ETF. (provider: tmx)
            beta_3y : Optional[float]
                The three-year beta of the ETF. (provider: tmx)
            return_5y : Optional[float]
                The five-year return of the ETF. (provider: tmx)
            beta_5y : Optional[float]
                The five-year beta of the ETF. (provider: tmx)
            return_10y : Optional[float]
                The ten-year return of the ETF. (provider: tmx)
            beta_10y : Optional[float]
                The ten-year beta of the ETF. (provider: tmx)
            beta_15y : Optional[float]
                The fifteen-year beta of the ETF. (provider: tmx)
            return_from_inception : Optional[float]
                The return from inception of the ETF. (provider: tmx)
            avg_volume : Optional[int]
                The average daily volume of the ETF. (provider: tmx)
            avg_volume_30d : Optional[int]
                The 30-day average volume of the ETF. (provider: tmx)
            aum : Optional[float]
                The AUM of the ETF. (provider: tmx)
            pe_ratio : Optional[float]
                The price-to-earnings ratio of the ETF. (provider: tmx)
            pb_ratio : Optional[float]
                The price-to-book ratio of the ETF. (provider: tmx)
            management_fee : Optional[float]
                The management fee of the ETF. (provider: tmx)
            mer : Optional[float]
                The management expense ratio of the ETF. (provider: tmx)
            distribution_yield : Optional[float]
                The distribution yield of the ETF. (provider: tmx)
            dividend_frequency : Optional[str]
                The dividend payment frequency of the ETF. (provider: tmx)

            Example
            -------
            >>> from openbb import obb
            >>> obb.etf.search()
        """  # noqa: E501

        return self._run(
            "/etf/search",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "query": query,
                },
                extra_params=kwargs,
            )
        )

    @validate
    def sectors(
        self,
        symbol: Annotated[
            Union[str, List[str]],
            OpenBBCustomParameter(description="Symbol to get data for. (ETF)"),
        ],
        provider: Optional[Literal["fmp", "tmx"]] = None,
        **kwargs
    ) -> OBBject:
        """ETF Sector weighting.

        Parameters
        ----------
        symbol : str
            Symbol to get data for. (ETF)
        provider : Optional[Literal['fmp', 'tmx']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'fmp' if there is
            no default.
        use_cache : bool
            Whether to use a cached request. All ETF data comes from a single JSON file that is updated daily. To bypass, set to False. If True, the data will be cached for 4 hours. (provider: tmx)

        Returns
        -------
        OBBject
            results : List[EtfSectors]
                Serializable results.
            provider : Optional[Literal['fmp', 'tmx']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EtfSectors
        ----------
        sector : str
            Sector of exposure.
        weight : Optional[float]
            Exposure of the ETF to the sector in normalized percentage points.

        Example
        -------
        >>> from openbb import obb
        >>> obb.etf.sectors(symbol="AAPL")
        """  # noqa: E501

        return self._run(
            "/etf/sectors",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={
                    "symbol": ",".join(symbol) if isinstance(symbol, list) else symbol,
                },
                extra_params=kwargs,
            )
        )
