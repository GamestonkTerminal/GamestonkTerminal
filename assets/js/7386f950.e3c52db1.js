"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[8595],{15187:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>c,contentTitle:()=>s,default:()=>p,frontMatter:()=>a,metadata:()=>l,toc:()=>d});var o=t(74848),i=t(28453),r=t(94331);const a={title:"information",description:"Documentation for the 'information' function of the OpenBB financial library. It calculates the information ratio for different time periods based on portfolio transactions.",keywords:["financial library","information ratio","portfolio transactions","portfolio metrics","PortfolioEngine"]},s=void 0,l={id:"sdk/reference/portfolio/metric/information",title:"information",description:"Documentation for the 'information' function of the OpenBB financial library. It calculates the information ratio for different time periods based on portfolio transactions.",source:"@site/content/sdk/reference/portfolio/metric/information.md",sourceDirName:"sdk/reference/portfolio/metric",slug:"/sdk/reference/portfolio/metric/information",permalink:"/sdk/reference/portfolio/metric/information",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/sdk/reference/portfolio/metric/information.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"information",description:"Documentation for the 'information' function of the OpenBB financial library. It calculates the information ratio for different time periods based on portfolio transactions.",keywords:["financial library","information ratio","portfolio transactions","portfolio metrics","PortfolioEngine"]},sidebar:"tutorialSidebar",previous:{title:"gaintopain",permalink:"/sdk/reference/portfolio/metric/gaintopain"},next:{title:"jensens",permalink:"/sdk/reference/portfolio/metric/jensens"}},c={},d=[{value:"Parameters",id:"parameters",level:2},{value:"Returns",id:"returns",level:2},{value:"Examples",id:"examples",level:2}];function f(e){const n={a:"a",code:"code",h2:"h2",hr:"hr",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,i.R)(),...e.components};return(0,o.jsxs)(o.Fragment,{children:[(0,o.jsx)(r.A,{title:"portfolio.metric.information - Reference | OpenBB SDK Docs"}),"\n",(0,o.jsx)(n.p,{children:"Get information ratio"}),"\n",(0,o.jsxs)(n.p,{children:["Source Code: [",(0,o.jsx)(n.a,{href:"https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/portfolio/portfolio_model.py#L1379",children:"link"}),"]"]}),"\n",(0,o.jsx)(n.pre,{children:(0,o.jsx)(n.code,{className:"language-python",children:"openbb.portfolio.metric.information(portfolio_engine: portfolio_engine.PortfolioEngine)\n"})}),"\n",(0,o.jsx)(n.hr,{}),"\n",(0,o.jsx)(n.h2,{id:"parameters",children:"Parameters"}),"\n",(0,o.jsxs)(n.table,{children:[(0,o.jsx)(n.thead,{children:(0,o.jsxs)(n.tr,{children:[(0,o.jsx)(n.th,{children:"Name"}),(0,o.jsx)(n.th,{children:"Type"}),(0,o.jsx)(n.th,{children:"Description"}),(0,o.jsx)(n.th,{children:"Default"}),(0,o.jsx)(n.th,{children:"Optional"})]})}),(0,o.jsx)(n.tbody,{children:(0,o.jsxs)(n.tr,{children:[(0,o.jsx)(n.td,{children:"portfolio_engine"}),(0,o.jsx)(n.td,{children:"PortfolioEngine"}),(0,o.jsxs)(n.td,{children:["PortfolioEngine class instance, this will hold transactions and perform calculations.",(0,o.jsx)("br",{}),"Use ",(0,o.jsx)(n.code,{children:"portfolio.load"})," to create a PortfolioEngine."]}),(0,o.jsx)(n.td,{children:"None"}),(0,o.jsx)(n.td,{children:"False"})]})})]}),"\n",(0,o.jsx)(n.hr,{}),"\n",(0,o.jsx)(n.h2,{id:"returns",children:"Returns"}),"\n",(0,o.jsxs)(n.table,{children:[(0,o.jsx)(n.thead,{children:(0,o.jsxs)(n.tr,{children:[(0,o.jsx)(n.th,{children:"Type"}),(0,o.jsx)(n.th,{children:"Description"})]})}),(0,o.jsx)(n.tbody,{children:(0,o.jsxs)(n.tr,{children:[(0,o.jsx)(n.td,{children:"pd.DataFrame"}),(0,o.jsx)(n.td,{children:"DataFrame of the information ratio during different time periods"})]})})]}),"\n",(0,o.jsx)(n.hr,{}),"\n",(0,o.jsx)(n.h2,{id:"examples",children:"Examples"}),"\n",(0,o.jsx)(n.pre,{children:(0,o.jsx)(n.code,{className:"language-python",children:'from openbb_terminal.sdk import openbb\np = openbb.portfolio.load("openbb_terminal/miscellaneous/portfolio_examples/holdings/example.csv")\noutput = openbb.portfolio.metric.information(p)\n'})}),"\n",(0,o.jsx)(n.hr,{})]})}function p(e={}){const{wrapper:n}={...(0,i.R)(),...e.components};return n?(0,o.jsx)(n,{...e,children:(0,o.jsx)(f,{...e})}):f(e)}},94331:(e,n,t)=>{t.d(n,{A:()=>r});t(96540);var o=t(5260),i=t(74848);function r(e){let{title:n}=e;return(0,i.jsx)(o.A,{children:(0,i.jsx)("title",{children:n})})}},28453:(e,n,t)=>{t.d(n,{R:()=>a,x:()=>s});var o=t(96540);const i={},r=o.createContext(i);function a(e){const n=o.useContext(r);return o.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function s(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(i):e.components||i:a(e.components),o.createElement(r.Provider,{value:n},e.children)}}}]);