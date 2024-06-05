"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[2884],{92741:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>c,contentTitle:()=>s,default:()=>p,frontMatter:()=>a,metadata:()=>l,toc:()=>d});var n=r(74848),o=r(28453),i=r(94331);const a={title:"calmar",description:"Documentation for the Calmar Ratio function in OpenBB Terminal, a Python library. It includes parameters, type of return, and examples of use. This function is a key tool for risk measurement in portfolio management, calculating the ratio of the portfolio's performance to its downside risk.",keywords:["calmar ratio","OpenBB finance","portfolio metrics","portfolio analysis","portfolio management","risk measurement","Python library","benchmark performance","financial data analysis"]},s=void 0,l={id:"sdk/reference/portfolio/metric/calmar",title:"calmar",description:"Documentation for the Calmar Ratio function in OpenBB Terminal, a Python library. It includes parameters, type of return, and examples of use. This function is a key tool for risk measurement in portfolio management, calculating the ratio of the portfolio's performance to its downside risk.",source:"@site/content/sdk/reference/portfolio/metric/calmar.md",sourceDirName:"sdk/reference/portfolio/metric",slug:"/sdk/reference/portfolio/metric/calmar",permalink:"/sdk/reference/portfolio/metric/calmar",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/sdk/reference/portfolio/metric/calmar.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"calmar",description:"Documentation for the Calmar Ratio function in OpenBB Terminal, a Python library. It includes parameters, type of return, and examples of use. This function is a key tool for risk measurement in portfolio management, calculating the ratio of the portfolio's performance to its downside risk.",keywords:["calmar ratio","OpenBB finance","portfolio metrics","portfolio analysis","portfolio management","risk measurement","Python library","benchmark performance","financial data analysis"]},sidebar:"tutorialSidebar",previous:{title:"maxdd",permalink:"/sdk/reference/portfolio/maxdd"},next:{title:"commonsense",permalink:"/sdk/reference/portfolio/metric/commonsense"}},c={},d=[{value:"Parameters",id:"parameters",level:2},{value:"Returns",id:"returns",level:2},{value:"Examples",id:"examples",level:2}];function m(e){const t={a:"a",code:"code",h2:"h2",hr:"hr",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,o.R)(),...e.components};return(0,n.jsxs)(n.Fragment,{children:[(0,n.jsx)(i.A,{title:"portfolio.metric.calmar - Reference | OpenBB SDK Docs"}),"\n",(0,n.jsx)(t.p,{children:"Get calmar ratio"}),"\n",(0,n.jsxs)(t.p,{children:["Source Code: [",(0,n.jsx)(t.a,{href:"https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/portfolio/portfolio_model.py#L1522",children:"link"}),"]"]}),"\n",(0,n.jsx)(t.pre,{children:(0,n.jsx)(t.code,{className:"language-python",children:"openbb.portfolio.metric.calmar(portfolio_engine: portfolio_engine.PortfolioEngine, window: int = 756)\n"})}),"\n",(0,n.jsx)(t.hr,{}),"\n",(0,n.jsx)(t.h2,{id:"parameters",children:"Parameters"}),"\n",(0,n.jsxs)(t.table,{children:[(0,n.jsx)(t.thead,{children:(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.th,{children:"Name"}),(0,n.jsx)(t.th,{children:"Type"}),(0,n.jsx)(t.th,{children:"Description"}),(0,n.jsx)(t.th,{children:"Default"}),(0,n.jsx)(t.th,{children:"Optional"})]})}),(0,n.jsxs)(t.tbody,{children:[(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{children:"portfolio_engine"}),(0,n.jsx)(t.td,{children:"PortfolioEngine"}),(0,n.jsxs)(t.td,{children:["PortfolioEngine class instance, this will hold transactions and perform calculations.",(0,n.jsx)("br",{}),"Use ",(0,n.jsx)(t.code,{children:"portfolio.load"})," to create a PortfolioEngine."]}),(0,n.jsx)(t.td,{children:"None"}),(0,n.jsx)(t.td,{children:"False"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{children:"window"}),(0,n.jsx)(t.td,{children:"int"}),(0,n.jsx)(t.td,{children:"Interval used for rolling values"}),(0,n.jsx)(t.td,{children:"756"}),(0,n.jsx)(t.td,{children:"True"})]})]})]}),"\n",(0,n.jsx)(t.hr,{}),"\n",(0,n.jsx)(t.h2,{id:"returns",children:"Returns"}),"\n",(0,n.jsxs)(t.table,{children:[(0,n.jsx)(t.thead,{children:(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.th,{children:"Type"}),(0,n.jsx)(t.th,{children:"Description"})]})}),(0,n.jsx)(t.tbody,{children:(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{children:"pd.DataFrame"}),(0,n.jsx)(t.td,{children:"DataFrame of calmar ratio of the benchmark and portfolio during different time periods"})]})})]}),"\n",(0,n.jsx)(t.hr,{}),"\n",(0,n.jsx)(t.h2,{id:"examples",children:"Examples"}),"\n",(0,n.jsx)(t.pre,{children:(0,n.jsx)(t.code,{className:"language-python",children:'from openbb_terminal.sdk import openbb\np = openbb.portfolio.load("openbb_terminal/miscellaneous/portfolio_examples/holdings/example.csv")\noutput = openbb.portfolio.metric.calmar(p)\n'})}),"\n",(0,n.jsx)(t.hr,{})]})}function p(e={}){const{wrapper:t}={...(0,o.R)(),...e.components};return t?(0,n.jsx)(t,{...e,children:(0,n.jsx)(m,{...e})}):m(e)}},94331:(e,t,r)=>{r.d(t,{A:()=>i});r(96540);var n=r(5260),o=r(74848);function i(e){let{title:t}=e;return(0,o.jsx)(n.A,{children:(0,o.jsx)("title",{children:t})})}},28453:(e,t,r)=>{r.d(t,{R:()=>a,x:()=>s});var n=r(96540);const o={},i=n.createContext(o);function a(e){const t=n.useContext(i);return n.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function s(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(o):e.components||o:a(e.components),n.createElement(i.Provider,{value:t},e.children)}}}]);