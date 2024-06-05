"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[37646],{45307:(e,r,t)=>{t.r(r),t.d(r,{assets:()=>l,contentTitle:()=>d,default:()=>u,frontMatter:()=>a,metadata:()=>o,toc:()=>c});var s=t(74848),n=t(28453),i=t(94331);const a={title:"plot",description:"The plot page allows users to select and plot charts for various portfolios, using a range of parameters and offering several optional features. It includes different types of charts such as pie, histogram, drawdown, and risk contribution charts. Different risk measures can be optimized, and users can control various other factors such as the calculation frequency, the max percentage of accepted NaN values, and the risk-free rate.",keywords:["plot","charts","portfolios","risk measures","drawdown chart","risk contribution chart","correlation matrix","heatmap","CVaR","EVaR","Maximum Drawdown","risk-free rate","significance level"]},d=void 0,o={id:"terminal/reference/portfolio/po/plot",title:"plot",description:"The plot page allows users to select and plot charts for various portfolios, using a range of parameters and offering several optional features. It includes different types of charts such as pie, histogram, drawdown, and risk contribution charts. Different risk measures can be optimized, and users can control various other factors such as the calculation frequency, the max percentage of accepted NaN values, and the risk-free rate.",source:"@site/content/terminal/reference/portfolio/po/plot.md",sourceDirName:"terminal/reference/portfolio/po",slug:"/terminal/reference/portfolio/po/plot",permalink:"/terminal/reference/portfolio/po/plot",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/terminal/reference/portfolio/po/plot.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"plot",description:"The plot page allows users to select and plot charts for various portfolios, using a range of parameters and offering several optional features. It includes different types of charts such as pie, histogram, drawdown, and risk contribution charts. Different risk measures can be optimized, and users can control various other factors such as the calculation frequency, the max percentage of accepted NaN values, and the risk-free rate.",keywords:["plot","charts","portfolios","risk measures","drawdown chart","risk contribution chart","correlation matrix","heatmap","CVaR","EVaR","Maximum Drawdown","risk-free rate","significance level"]},sidebar:"tutorialSidebar",previous:{title:"set",permalink:"/terminal/reference/portfolio/po/parameters/set"},next:{title:"property",permalink:"/terminal/reference/portfolio/po/property"}},l={},c=[{value:"Usage",id:"usage",level:3},{value:"Parameters",id:"parameters",level:2},{value:"Examples",id:"examples",level:2}];function h(e){const r={code:"code",h2:"h2",h3:"h3",hr:"hr",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,n.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(i.A,{title:"portfolio/po/plot - Reference | OpenBB Terminal Docs"}),"\n",(0,s.jsx)(r.p,{children:"Plot selected charts for portfolios"}),"\n",(0,s.jsx)(r.h3,{id:"usage",children:"Usage"}),"\n",(0,s.jsx)(r.pre,{children:(0,s.jsx)(r.code,{className:"language-python",children:"plot [-pf PORTFOLIOS] [-pi] [-hi] [-dd] [-rc] [-he] [-rm {MV,MAD,MSV,FLPM,SLPM,CVaR,EVaR,WR,ADD,UCI,CDaR,EDaR,MDD}] [-mt METHOD] [-ct CATEGORIES] [-p PERIOD] [-s START_PERIOD] [-e END_PERIOD] [-lr] [--freq {d,w,m}] [-mn MAX_NAN] [-th THRESHOLD_VALUE] [-r RISK_FREE] [-a SIGNIFICANCE_LEVEL] [-v LONG_ALLOCATION]\n"})}),"\n",(0,s.jsx)(r.hr,{}),"\n",(0,s.jsx)(r.h2,{id:"parameters",children:"Parameters"}),"\n",(0,s.jsxs)(r.table,{children:[(0,s.jsx)(r.thead,{children:(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.th,{children:"Name"}),(0,s.jsx)(r.th,{children:"Description"}),(0,s.jsx)(r.th,{children:"Default"}),(0,s.jsx)(r.th,{children:"Optional"}),(0,s.jsx)(r.th,{children:"Choices"})]})}),(0,s.jsxs)(r.tbody,{children:[(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"portfolios"}),(0,s.jsx)(r.td,{children:"Selected portfolios that will be plotted"}),(0,s.jsx)(r.td,{}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"pie"}),(0,s.jsx)(r.td,{children:"Display a pie chart for weights"}),(0,s.jsx)(r.td,{children:"False"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"hist"}),(0,s.jsx)(r.td,{children:"Display a histogram with risk measures"}),(0,s.jsx)(r.td,{children:"False"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"dd"}),(0,s.jsx)(r.td,{children:"Display a drawdown chart with risk measures"}),(0,s.jsx)(r.td,{children:"False"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"rc_chart"}),(0,s.jsx)(r.td,{children:"Display a risk contribution chart for assets"}),(0,s.jsx)(r.td,{children:"False"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"heat"}),(0,s.jsx)(r.td,{children:"Display a heatmap of correlation matrix with dendrogram"}),(0,s.jsx)(r.td,{children:"False"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"risk_measure"}),(0,s.jsx)(r.td,{children:"Risk measure used to optimize the portfolio. Possible values are: 'MV' : Variance 'MAD' : Mean Absolute Deviation 'MSV' : Semi Variance (Variance of negative returns) 'FLPM' : First Lower Partial Moment 'SLPM' : Second Lower Partial Moment 'CVaR' : Conditional Value at Risk 'EVaR' : Entropic Value at Risk 'WR' : Worst Realization 'ADD' : Average Drawdown of uncompounded returns 'UCI' : Ulcer Index of uncompounded returns 'CDaR' : Conditional Drawdown at Risk of uncompounded returns 'EDaR' : Entropic Drawdown at Risk of uncompounded returns 'MDD' : Maximum Drawdown of uncompounded returns"}),(0,s.jsx)(r.td,{children:"MV"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"MV, MAD, MSV, FLPM, SLPM, CVaR, EVaR, WR, ADD, UCI, CDaR, EDaR, MDD"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"nan_fill_method"}),(0,s.jsx)(r.td,{children:"Method used to fill nan values in time series, by default time. Possible values are: 'linear': linear interpolation 'time': linear interpolation based on time index 'nearest': use nearest value to replace nan values 'zero': spline of zeroth order 'slinear': spline of first order 'quadratic': spline of second order 'cubic': spline of third order 'barycentric': builds a polynomial that pass for all points"}),(0,s.jsx)(r.td,{children:"time"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"linear, time, nearest, zero, slinear, quadratic, cubic, barycentric"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"categories"}),(0,s.jsx)(r.td,{children:"Show selected categories"}),(0,s.jsx)(r.td,{children:"ASSET_CLASS, COUNTRY, SECTOR, INDUSTRY"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"historic_period"}),(0,s.jsx)(r.td,{children:"Period to get yfinance data from. Possible frequency strings are: 'd': means days, for example '252d' means 252 days 'w': means weeks, for example '52w' means 52 weeks 'mo': means months, for example '12mo' means 12 months 'y': means years, for example '1y' means 1 year 'ytd': downloads data from beginning of year to today 'max': downloads all data available for each asset"}),(0,s.jsx)(r.td,{children:"3y"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"start_period"}),(0,s.jsx)(r.td,{children:"Start date to get yfinance data from. Must be in 'YYYY-MM-DD' format"}),(0,s.jsx)(r.td,{}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"end_period"}),(0,s.jsx)(r.td,{children:"End date to get yfinance data from. Must be in 'YYYY-MM-DD' format"}),(0,s.jsx)(r.td,{}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"log_returns"}),(0,s.jsx)(r.td,{children:"If use logarithmic or arithmetic returns to calculate returns"}),(0,s.jsx)(r.td,{children:"False"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"return_frequency"}),(0,s.jsx)(r.td,{children:"Frequency used to calculate returns. Possible values are: 'd': for daily returns 'w': for weekly returns 'm': for monthly returns"}),(0,s.jsx)(r.td,{children:"d"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"d, w, m"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"max_nan"}),(0,s.jsx)(r.td,{children:"Max percentage of nan values accepted per asset to be considered in the optimization process"}),(0,s.jsx)(r.td,{children:"0.05"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"threshold_value"}),(0,s.jsx)(r.td,{children:"Value used to replace outliers that are higher to threshold in absolute value"}),(0,s.jsx)(r.td,{children:"0.3"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"risk_free"}),(0,s.jsx)(r.td,{children:"Risk-free rate of borrowing/lending. The period of the risk-free rate must be annual"}),(0,s.jsx)(r.td,{children:"0.02924"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"significance_level"}),(0,s.jsx)(r.td,{children:"Significance level of CVaR, EVaR, CDaR and EDaR"}),(0,s.jsx)(r.td,{children:"0.05"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]}),(0,s.jsxs)(r.tr,{children:[(0,s.jsx)(r.td,{children:"long_allocation"}),(0,s.jsx)(r.td,{children:"Amount to allocate to portfolio"}),(0,s.jsx)(r.td,{children:"1"}),(0,s.jsx)(r.td,{children:"True"}),(0,s.jsx)(r.td,{children:"None"})]})]})]}),"\n",(0,s.jsx)(r.hr,{}),"\n",(0,s.jsx)(r.h2,{id:"examples",children:"Examples"}),"\n",(0,s.jsx)(r.pre,{children:(0,s.jsx)(r.code,{className:"language-python",children:"2022 Apr 26, 02:19 (\ud83e\udd8b) /portfolio/po/ $ plot -pf maxsharpe_0 -pi -hi -dd -rc -he\n"})}),"\n",(0,s.jsx)(r.hr,{})]})}function u(e={}){const{wrapper:r}={...(0,n.R)(),...e.components};return r?(0,s.jsx)(r,{...e,children:(0,s.jsx)(h,{...e})}):h(e)}},94331:(e,r,t)=>{t.d(r,{A:()=>i});t(96540);var s=t(5260),n=t(74848);function i(e){let{title:r}=e;return(0,n.jsx)(s.A,{children:(0,n.jsx)("title",{children:r})})}},28453:(e,r,t)=>{t.d(r,{R:()=>a,x:()=>d});var s=t(96540);const n={},i=s.createContext(n);function a(e){const r=s.useContext(i);return s.useMemo((function(){return"function"==typeof e?e(r):{...r,...e}}),[r,e])}function d(e){let r;return r=e.disableParentContext?"function"==typeof e.components?e.components(n):e.components||n:a(e.components),s.createElement(i.Provider,{value:r},e.children)}}}]);