"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[50903],{26522:(t,e,l)=>{l.r(e),l.d(e,{assets:()=>x,contentTitle:()=>d,default:()=>a,frontMatter:()=>r,metadata:()=>h,toc:()=>c});var i=l(74848),n=l(28453),s=l(94331);const r={title:"Forex",description:"This guide introduces the Forex (FX) menu, in the OpenBB Terminal, and provides examples for use.  Features in this menu include historical prices and forward rates.  It also provides entry points to the QA, TA, and Forecast menus.",keywords:["Forex","currency trading","currency pairs","USD/EUR","JPY/GBP","quote","candle","forward rates","fwd","technical analysis","forecasting","Oanda","historical data","real-time currency exchange","terminal","quantitative analysis","seasonality"]},d=void 0,h={id:"terminal/menus/forex",title:"Forex",description:"This guide introduces the Forex (FX) menu, in the OpenBB Terminal, and provides examples for use.  Features in this menu include historical prices and forward rates.  It also provides entry points to the QA, TA, and Forecast menus.",source:"@site/content/terminal/menus/forex.md",sourceDirName:"terminal/menus",slug:"/terminal/menus/forex",permalink:"/terminal/menus/forex",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/terminal/menus/forex.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"Forex",description:"This guide introduces the Forex (FX) menu, in the OpenBB Terminal, and provides examples for use.  Features in this menu include historical prices and forward rates.  It also provides entry points to the QA, TA, and Forecast menus.",keywords:["Forex","currency trading","currency pairs","USD/EUR","JPY/GBP","quote","candle","forward rates","fwd","technical analysis","forecasting","Oanda","historical data","real-time currency exchange","terminal","quantitative analysis","seasonality"]},sidebar:"tutorialSidebar",previous:{title:"Forecast",permalink:"/terminal/menus/forecast"},next:{title:"Futures",permalink:"/terminal/menus/futures"}},x={},c=[{value:"Usage",id:"usage",level:2},{value:"Load",id:"load",level:3},{value:"Quote",id:"quote",level:3},{value:"FWD",id:"fwd",level:3}];function g(t){const e={a:"a",code:"code",h2:"h2",h3:"h3",img:"img",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,n.R)(),...t.components};return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)(s.A,{title:"Forex - Menus | OpenBB Terminal Docs"}),"\n",(0,i.jsxs)(e.p,{children:["The Forex menu includes features for historical prices, forward rates, and real-time exchange rates.  It also provides entry points to the ",(0,i.jsx)(e.a,{href:"/terminal/menus/common/ta",children:(0,i.jsx)(e.code,{children:"/ta/"})}),", ",(0,i.jsx)(e.a,{href:"/terminal/menus/common/qa",children:(0,i.jsx)(e.code,{children:"/qa"})}),", and ",(0,i.jsx)(e.a,{href:"/terminal/menus/forecast",children:(0,i.jsx)(e.code,{children:"/forecast"})})," menus."]}),"\n",(0,i.jsx)(e.h2,{id:"usage",children:"Usage"}),"\n",(0,i.jsxs)(e.p,{children:["The Forex menu is entered by typing ",(0,i.jsx)(e.code,{children:"forex"}),", from the Main menu, or with the absolute path:"]}),"\n",(0,i.jsx)(e.pre,{children:(0,i.jsx)(e.code,{className:"language-console",children:"/forex\n"})}),"\n",(0,i.jsx)(e.p,{children:(0,i.jsx)(e.img,{src:"https://github.com/OpenBB-finance/OpenBBTerminal/assets/85772166/83356fc6-9966-4da3-9bed-64ae7e42ecd0",alt:"Screenshot 2023-11-03 at 12 26 41\u202fPM"})}),"\n",(0,i.jsx)(e.h3,{id:"load",children:"Load"}),"\n",(0,i.jsx)(e.p,{children:'The first step will be to load a pair of currencies.  The pairs are entered as a six-letter symbol, with the former of the pair being "from".'}),"\n",(0,i.jsx)(e.pre,{children:(0,i.jsx)(e.code,{className:"language-console",children:"load JPYUSD\n"})}),"\n",(0,i.jsx)(e.p,{children:"Inversely:"}),"\n",(0,i.jsx)(e.pre,{children:(0,i.jsx)(e.code,{className:"language-console",children:"load USDJPY\n"})}),"\n",(0,i.jsx)(e.h3,{id:"quote",children:"Quote"}),"\n",(0,i.jsxs)(e.p,{children:["A ",(0,i.jsx)(e.code,{children:"quote"})," from YahooFinance displays the last price and a timestamp when it was refreshed."]}),"\n",(0,i.jsx)(e.pre,{children:(0,i.jsx)(e.code,{className:"language-console",children:"/forex/load JPYUSD/quote\n"})}),"\n",(0,i.jsx)(e.pre,{children:(0,i.jsx)(e.code,{className:"language-console",children:"Quote for JPY/USD\n\nLast refreshed : 2023-11-03 19:30:00\nLast value     : 0.006694381590932608\n"})}),"\n",(0,i.jsx)(e.p,{children:"From AlphaVantage, a table is returned that includes a bid and ask."}),"\n",(0,i.jsx)(e.pre,{children:(0,i.jsx)(e.code,{className:"language-console",children:"quote --source AlphaVantage\n"})}),"\n",(0,i.jsxs)(e.table,{children:[(0,i.jsx)(e.thead,{children:(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.th,{style:{textAlign:"left"}}),(0,i.jsx)(e.th,{style:{textAlign:"left"},children:"Realtime Currency Exchange Rate"})]})}),(0,i.jsxs)(e.tbody,{children:[(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"From_Currency Code"}),(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"JPY"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"From_Currency Name"}),(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Japanese Yen"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"To_Currency Code"}),(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"USD"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"To_Currency Name"}),(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"United States Dollar"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Exchange Rate"}),(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"0.00669000"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Last Refreshed"}),(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"2023-11-03 19:34:01"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Time Zone"}),(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"UTC"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Bid Price"}),(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"0.00668900"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Ask Price"}),(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"0.00669000"})]})]})]}),"\n",(0,i.jsx)(e.h3,{id:"fwd",children:"FWD"}),"\n",(0,i.jsxs)(e.p,{children:["The ",(0,i.jsx)(e.code,{children:"fwd"})," command gets a table with the term structure of a currency pair."]}),"\n",(0,i.jsx)(e.pre,{children:(0,i.jsx)(e.code,{className:"language-console",children:"/forex/load USDJPY/fwd\n"})}),"\n",(0,i.jsxs)(e.table,{children:[(0,i.jsx)(e.thead,{children:(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.th,{style:{textAlign:"left"},children:"Expiration"}),(0,i.jsx)(e.th,{style:{textAlign:"right"},children:"Ask"}),(0,i.jsx)(e.th,{style:{textAlign:"right"},children:"Bid"}),(0,i.jsx)(e.th,{style:{textAlign:"right"},children:"Mid"}),(0,i.jsx)(e.th,{style:{textAlign:"right"},children:"Points"})]})}),(0,i.jsxs)(e.tbody,{children:[(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Overnight"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.397"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.368"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.383"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"0"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Tomorrow Next"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.397"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.368"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.382"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-2.33"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Spot Next"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.397"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.368"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.382"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-2.325"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"One Week"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.395"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.366"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.381"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-16.315"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Two Weeks"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.394"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.365"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.379"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-32.59"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Three Weeks"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.392"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.363"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.378"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-48.89"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"One Month"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.39"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.361"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.375"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-70.1505"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Two Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.381"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.352"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.367"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-155.31"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Three Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.375"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.346"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.36"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-222.871"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Four Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.368"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.339"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.353"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-290.68"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Five Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.36"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.331"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.346"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-365.94"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Six Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.354"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.325"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.339"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-431.97"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Seven Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.347"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.318"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.332"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-500.22"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Eight Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.34"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.311"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.326"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-567.58"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Nine Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.334"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.305"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.319"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-630.18"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Ten Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.327"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.298"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.313"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-697.4"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Eleven Months"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.322"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.293"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.307"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-753.2"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"One Year"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.316"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.287"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.301"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-812.9"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Two Years"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.256"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.227"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.242"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-1408.19"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Three Years"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.204"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.173"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.188"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-1943.13"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Four Years"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.158"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.127"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.142"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-2401.05"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Five Years"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.108"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.077"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.092"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-2904.72"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Six Years"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.08"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.048"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.064"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-3185.9"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Seven Years"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.047"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.014"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"149.03"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-3522.5"})]}),(0,i.jsxs)(e.tr,{children:[(0,i.jsx)(e.td,{style:{textAlign:"left"},children:"Ten Years"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"148.948"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"148.912"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"148.93"}),(0,i.jsx)(e.td,{style:{textAlign:"right"},children:"-4527.5"})]})]})]})]})}function a(t={}){const{wrapper:e}={...(0,n.R)(),...t.components};return e?(0,i.jsx)(e,{...t,children:(0,i.jsx)(g,{...t})}):g(t)}},94331:(t,e,l)=>{l.d(e,{A:()=>s});l(96540);var i=l(5260),n=l(74848);function s(t){let{title:e}=t;return(0,n.jsx)(i.A,{children:(0,n.jsx)("title",{children:e})})}},28453:(t,e,l)=>{l.d(e,{R:()=>r,x:()=>d});var i=l(96540);const n={},s=i.createContext(n);function r(t){const e=i.useContext(s);return i.useMemo((function(){return"function"==typeof t?t(e):{...e,...t}}),[e,t])}function d(t){let e;return e=t.disableParentContext?"function"==typeof t.components?t.components(n):t.components||n:r(t.components),i.createElement(s.Provider,{value:e},t.children)}}}]);