"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[61965],{70073:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>c,contentTitle:()=>o,default:()=>x,frontMatter:()=>d,metadata:()=>i,toc:()=>l});var s=r(74848),n=r(28453),a=r(94331);const d={title:"load",description:"This page provides detailed instructions on how to load a stock ticker to perform analysis, complete with usage examples and parameters. It also provides information on loading Indian tickers and references to data sources.",keywords:["load stock ticker","perform stock analysis","Indian stock ticker","stock analysis parameters","stock data usage","data source","intraday stock minutes","pre/after market hours","load custom file","monthly data","weekly data"]},o=void 0,i={id:"terminal/reference/stocks/ta/load",title:"load",description:"This page provides detailed instructions on how to load a stock ticker to perform analysis, complete with usage examples and parameters. It also provides information on loading Indian tickers and references to data sources.",source:"@site/content/terminal/reference/stocks/ta/load.md",sourceDirName:"terminal/reference/stocks/ta",slug:"/terminal/reference/stocks/ta/load",permalink:"/terminal/reference/stocks/ta/load",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/terminal/reference/stocks/ta/load.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"load",description:"This page provides detailed instructions on how to load a stock ticker to perform analysis, complete with usage examples and parameters. It also provides information on loading Indian tickers and references to data sources.",keywords:["load stock ticker","perform stock analysis","Indian stock ticker","stock analysis parameters","stock data usage","data source","intraday stock minutes","pre/after market hours","load custom file","monthly data","weekly data"]},sidebar:"tutorialSidebar",previous:{title:"kc",permalink:"/terminal/reference/stocks/ta/kc"},next:{title:"macd",permalink:"/terminal/reference/stocks/ta/macd"}},c={},l=[{value:"Usage",id:"usage",level:3},{value:"Parameters",id:"parameters",level:2}];function h(e){const t={a:"a",code:"code",h2:"h2",h3:"h3",hr:"hr",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,n.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(a.A,{title:"stocks/ta/load - Reference | OpenBB Terminal Docs"}),"\n",(0,s.jsxs)(t.p,{children:["Load stock ticker to perform analysis on. When the data source is syf', an Indian ticker can be loaded by using '.NS' at the end, e.g. 'SBIN.NS'. See available market in ",(0,s.jsx)(t.a,{href:"https://help.yahoo.com/kb/exchanges-data-providers-yahoo-finance-sln2310.html",children:"https://help.yahoo.com/kb/exchanges-data-providers-yahoo-finance-sln2310.html"}),"."]}),"\n",(0,s.jsx)(t.h3,{id:"usage",children:"Usage"}),"\n",(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-python",children:"load -t TICKER [-s START] [-e END] [-i {1,5,15,30,60}] [-p] [-f FILEPATH] [-m] [-w] [-r {ytd,1y,2y,5y,6m}]\n"})}),"\n",(0,s.jsx)(t.hr,{}),"\n",(0,s.jsx)(t.h2,{id:"parameters",children:"Parameters"}),"\n",(0,s.jsxs)(t.table,{children:[(0,s.jsx)(t.thead,{children:(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.th,{children:"Name"}),(0,s.jsx)(t.th,{children:"Description"}),(0,s.jsx)(t.th,{children:"Default"}),(0,s.jsx)(t.th,{children:"Optional"}),(0,s.jsx)(t.th,{children:"Choices"})]})}),(0,s.jsxs)(t.tbody,{children:[(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"ticker"}),(0,s.jsx)(t.td,{children:"Stock ticker"}),(0,s.jsx)(t.td,{children:"None"}),(0,s.jsx)(t.td,{children:"False"}),(0,s.jsx)(t.td,{children:"None"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"start"}),(0,s.jsx)(t.td,{children:"The starting date (format YYYY-MM-DD) of the stock"}),(0,s.jsx)(t.td,{children:"2019-11-21"}),(0,s.jsx)(t.td,{children:"True"}),(0,s.jsx)(t.td,{children:"None"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"end"}),(0,s.jsx)(t.td,{children:"The ending date (format YYYY-MM-DD) of the stock"}),(0,s.jsx)(t.td,{children:"2022-11-25"}),(0,s.jsx)(t.td,{children:"True"}),(0,s.jsx)(t.td,{children:"None"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"interval"}),(0,s.jsx)(t.td,{children:"Intraday stock minutes"}),(0,s.jsx)(t.td,{children:"1440"}),(0,s.jsx)(t.td,{children:"True"}),(0,s.jsx)(t.td,{children:"1, 5, 15, 30, 60"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"prepost"}),(0,s.jsx)(t.td,{children:"Pre/After market hours. Only works for 'yf' source, and intraday data"}),(0,s.jsx)(t.td,{children:"False"}),(0,s.jsx)(t.td,{children:"True"}),(0,s.jsx)(t.td,{children:"None"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"filepath"}),(0,s.jsx)(t.td,{children:"Path to load custom file."}),(0,s.jsx)(t.td,{children:"None"}),(0,s.jsx)(t.td,{children:"True"}),(0,s.jsx)(t.td,{children:"None"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"monthly"}),(0,s.jsx)(t.td,{children:"Load monthly data"}),(0,s.jsx)(t.td,{children:"False"}),(0,s.jsx)(t.td,{children:"True"}),(0,s.jsx)(t.td,{children:"None"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"weekly"}),(0,s.jsx)(t.td,{children:"Load weekly data"}),(0,s.jsx)(t.td,{children:"False"}),(0,s.jsx)(t.td,{children:"True"}),(0,s.jsx)(t.td,{children:"None"})]})]})]}),"\n",(0,s.jsx)(t.hr,{})]})}function x(e={}){const{wrapper:t}={...(0,n.R)(),...e.components};return t?(0,s.jsx)(t,{...e,children:(0,s.jsx)(h,{...e})}):h(e)}},94331:(e,t,r)=>{r.d(t,{A:()=>a});r(96540);var s=r(5260),n=r(74848);function a(e){let{title:t}=e;return(0,n.jsx)(s.A,{children:(0,n.jsx)("title",{children:t})})}},28453:(e,t,r)=>{r.d(t,{R:()=>d,x:()=>o});var s=r(96540);const n={},a=s.createContext(n);function d(e){const t=s.useContext(a);return s.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function o(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(n):e.components||n:d(e.components),s.createElement(a.Provider,{value:t},e.children)}}}]);