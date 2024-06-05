"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[78203],{49512:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>o,default:()=>u,frontMatter:()=>s,metadata:()=>c,toc:()=>d});var r=n(74848),a=n(28453),i=n(94331);const s={title:"Quickstart",sidebar_position:1,description:"Get started with the OpenBB Platform by following this quickstart guide.",keywords:["OpenBB Platform","investment research infrastructure","data connectors","financial reports","OpenBB team","quickstart","getting started"]},o=void 0,c={id:"platform/getting_started/quickstart",title:"Quickstart",description:"Get started with the OpenBB Platform by following this quickstart guide.",source:"@site/content/platform/getting_started/quickstart.mdx",sourceDirName:"platform/getting_started",slug:"/platform/getting_started/quickstart",permalink:"/platform/getting_started/quickstart",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/platform/getting_started/quickstart.mdx",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,sidebarPosition:1,frontMatter:{title:"Quickstart",sidebar_position:1,description:"Get started with the OpenBB Platform by following this quickstart guide.",keywords:["OpenBB Platform","investment research infrastructure","data connectors","financial reports","OpenBB team","quickstart","getting started"]},sidebar:"tutorialSidebar",previous:{title:"Getting started",permalink:"/platform/getting_started/"},next:{title:"Authorization and API Keys",permalink:"/platform/getting_started/api_keys"}},l={},d=[];function p(e){const t={a:"a",code:"code",img:"img",p:"p",pre:"pre",...(0,a.R)(),...e.components};return(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(i.A,{title:"Quickstart | OpenBB Platform Docs"}),"\n",(0,r.jsxs)(t.p,{children:["To get started with the OpenBB Platform, all you need to do is to import ",(0,r.jsx)(t.code,{children:"obb"})," and start querying away."]}),"\n",(0,r.jsx)(t.pre,{children:(0,r.jsx)(t.code,{className:"language-python",children:'from openbb import obb\n\n# Get the price of a stock\nquote_data = obb.equity.price.quote(symbol="AAPL", provider="yfinance")\nquote_data\n'})}),"\n",(0,r.jsx)(t.p,{children:"The output will look like this:"}),"\n",(0,r.jsx)(t.pre,{children:(0,r.jsx)(t.code,{className:"language-console",children:"OBBject\n\nid: 06649f4e-896c-7b31-8000-52242b1605f2\nresults: [{'symbol': 'AAPL', 'asset_type': 'EQUITY', 'name': 'Apple Inc.', 'exchang...\nprovider: yfinance\nwarnings: None\nchart: None\nextra: {'metadata': {'arguments': {'provider_choices': {'provider': 'yfinance'}, 's...\n"})}),"\n",(0,r.jsxs)(t.p,{children:["To view the output as a dataframe, you can use the ",(0,r.jsx)(t.code,{children:"to_df()"})," method."]}),"\n",(0,r.jsx)(t.pre,{children:(0,r.jsx)(t.code,{className:"language-python",children:"quote_data.to_df()\n"})}),"\n",(0,r.jsx)(t.p,{children:"Let's try another example. This time, we'll get the historical price of a stock."}),"\n",(0,r.jsx)(t.pre,{children:(0,r.jsx)(t.code,{className:"language-python",children:'obb.equity.price.historical(symbol="AAPL", provider="yfinance").to_df()\n'})}),"\n",(0,r.jsx)(t.p,{children:"To view all the available commands, routers and extensions, you can do:"}),"\n",(0,r.jsx)(t.pre,{children:(0,r.jsx)(t.code,{className:"language-python",children:"obb\n"})}),"\n",(0,r.jsx)(t.p,{children:"You can also keep exploring by accessing each route like this:"}),"\n",(0,r.jsx)(t.pre,{children:(0,r.jsx)(t.code,{className:"language-python",children:"obb.equity\n"})}),"\n",(0,r.jsx)(t.p,{children:"If you see a command you're interested in, to get help on how to use it, you can do:"}),"\n",(0,r.jsx)(t.pre,{children:(0,r.jsx)(t.code,{className:"language-python",children:"help(obb.equity.price.historical)\n"})}),"\n",(0,r.jsxs)(t.p,{children:["Visit our ",(0,r.jsx)(t.a,{href:"/platform/reference",children:"reference"})," documentation to see all the available commands and their parameters."]}),"\n",(0,r.jsx)(t.p,{children:"And that's it! You're now ready to start using the OpenBB Platform."}),"\n",(0,r.jsx)(t.p,{children:(0,r.jsx)(t.img,{src:"https://github.com/OpenBB-finance/OpenBBTerminal/assets/85772166/74520441-5e95-4ba6-9d16-6a2d5c966cf9",alt:"Platform Docs pic"})})]})}function u(e={}){const{wrapper:t}={...(0,a.R)(),...e.components};return t?(0,r.jsx)(t,{...e,children:(0,r.jsx)(p,{...e})}):p(e)}},94331:(e,t,n)=>{n.d(t,{A:()=>i});n(96540);var r=n(5260),a=n(74848);function i(e){let{title:t}=e;return(0,a.jsx)(r.A,{children:(0,a.jsx)("title",{children:t})})}},28453:(e,t,n)=>{n.d(t,{R:()=>s,x:()=>o});var r=n(96540);const a={},i=r.createContext(a);function s(e){const t=r.useContext(i);return r.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function o(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(a):e.components||a:s(e.components),r.createElement(i.Provider,{value:t},e.children)}}}]);