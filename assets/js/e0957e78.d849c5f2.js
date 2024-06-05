"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[38547],{27596:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>o,contentTitle:()=>c,default:()=>f,frontMatter:()=>a,metadata:()=>i,toc:()=>l});var s=r(74848),n=r(28453),d=r(94331);const a={title:"dcf",description:"This page covers how to use the 'dcf' function from FMP for stocks analysis with the OpenBB tool. It indicates the parameters required and returns a dataframe of dcf data.",keywords:["dcf","stocks","FMP","fundamental analysis","fmp model","parameters","returns","stock ticker symbol","limit","quarterly","dataframe","dcf data"]},c=void 0,i={id:"sdk/reference/stocks/fa/dcf",title:"dcf",description:"This page covers how to use the 'dcf' function from FMP for stocks analysis with the OpenBB tool. It indicates the parameters required and returns a dataframe of dcf data.",source:"@site/content/sdk/reference/stocks/fa/dcf.md",sourceDirName:"sdk/reference/stocks/fa",slug:"/sdk/reference/stocks/fa/dcf",permalink:"/sdk/reference/stocks/fa/dcf",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/sdk/reference/stocks/fa/dcf.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"dcf",description:"This page covers how to use the 'dcf' function from FMP for stocks analysis with the OpenBB tool. It indicates the parameters required and returns a dataframe of dcf data.",keywords:["dcf","stocks","FMP","fundamental analysis","fmp model","parameters","returns","stock ticker symbol","limit","quarterly","dataframe","dcf data"]},sidebar:"tutorialSidebar",previous:{title:"data",permalink:"/sdk/reference/stocks/fa/data"},next:{title:"divs",permalink:"/sdk/reference/stocks/fa/divs"}},o={},l=[{value:"Parameters",id:"parameters",level:2},{value:"Returns",id:"returns",level:2}];function h(e){const t={a:"a",code:"code",h2:"h2",hr:"hr",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,n.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(d.A,{title:"stocks.fa.dcf - Reference | OpenBB SDK Docs"}),"\n",(0,s.jsx)(t.p,{children:"Get stocks dcf from FMP"}),"\n",(0,s.jsxs)(t.p,{children:["Source Code: [",(0,s.jsx)(t.a,{href:"https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/stocks/fundamental_analysis/fmp_model.py#L173",children:"link"}),"]"]}),"\n",(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-python",children:"openbb.stocks.fa.dcf(symbol: str, limit: int = 5, quarterly: bool = False)\n"})}),"\n",(0,s.jsx)(t.hr,{}),"\n",(0,s.jsx)(t.h2,{id:"parameters",children:"Parameters"}),"\n",(0,s.jsxs)(t.table,{children:[(0,s.jsx)(t.thead,{children:(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.th,{children:"Name"}),(0,s.jsx)(t.th,{children:"Type"}),(0,s.jsx)(t.th,{children:"Description"}),(0,s.jsx)(t.th,{children:"Default"}),(0,s.jsx)(t.th,{children:"Optional"})]})}),(0,s.jsxs)(t.tbody,{children:[(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"symbol"}),(0,s.jsx)(t.td,{children:"str"}),(0,s.jsx)(t.td,{children:"Stock ticker symbol"}),(0,s.jsx)(t.td,{children:"None"}),(0,s.jsx)(t.td,{children:"False"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"limit"}),(0,s.jsx)(t.td,{children:"int"}),(0,s.jsx)(t.td,{children:"Number to get"}),(0,s.jsx)(t.td,{children:"5"}),(0,s.jsx)(t.td,{children:"True"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"quarterly"}),(0,s.jsx)(t.td,{children:"bool"}),(0,s.jsx)(t.td,{children:"Flag to get quarterly data, by default False"}),(0,s.jsx)(t.td,{children:"False"}),(0,s.jsx)(t.td,{children:"True"})]})]})]}),"\n",(0,s.jsx)(t.hr,{}),"\n",(0,s.jsx)(t.h2,{id:"returns",children:"Returns"}),"\n",(0,s.jsxs)(t.table,{children:[(0,s.jsx)(t.thead,{children:(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.th,{children:"Type"}),(0,s.jsx)(t.th,{children:"Description"})]})}),(0,s.jsx)(t.tbody,{children:(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"pd.DataFrame"}),(0,s.jsx)(t.td,{children:"Dataframe of dcf data"})]})})]}),"\n",(0,s.jsx)(t.hr,{})]})}function f(e={}){const{wrapper:t}={...(0,n.R)(),...e.components};return t?(0,s.jsx)(t,{...e,children:(0,s.jsx)(h,{...e})}):h(e)}},94331:(e,t,r)=>{r.d(t,{A:()=>d});r(96540);var s=r(5260),n=r(74848);function d(e){let{title:t}=e;return(0,n.jsx)(s.A,{children:(0,n.jsx)("title",{children:t})})}},28453:(e,t,r)=>{r.d(t,{R:()=>a,x:()=>c});var s=r(96540);const n={},d=s.createContext(n);function a(e){const t=s.useContext(d);return s.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function c(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(n):e.components||n:a(e.components),s.createElement(d.Provider,{value:t},e.children)}}}]);