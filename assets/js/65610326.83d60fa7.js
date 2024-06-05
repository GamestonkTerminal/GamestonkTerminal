"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[2039],{39902:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>a,contentTitle:()=>l,default:()=>p,frontMatter:()=>i,metadata:()=>d,toc:()=>c});var s=t(74848),r=t(28453),o=t(94331);const i={title:"polygon",description:"This documentation is about the 'polygon' function in the OpenBB Terminal Python SDK. It details how the function accepts a polygon API key, and settings to persist or show output.",keywords:["OpenBB Terminal SDK","Polygon API key","openbb.keys.polygon function","Python SDK","API key management","Environment variables"]},l=void 0,d={id:"sdk/reference/keys/polygon",title:"polygon",description:"This documentation is about the 'polygon' function in the OpenBB Terminal Python SDK. It details how the function accepts a polygon API key, and settings to persist or show output.",source:"@site/content/sdk/reference/keys/polygon.md",sourceDirName:"sdk/reference/keys",slug:"/sdk/reference/keys/polygon",permalink:"/sdk/reference/keys/polygon",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/sdk/reference/keys/polygon.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"polygon",description:"This documentation is about the 'polygon' function in the OpenBB Terminal Python SDK. It details how the function accepts a polygon API key, and settings to persist or show output.",keywords:["OpenBB Terminal SDK","Polygon API key","openbb.keys.polygon function","Python SDK","API key management","Environment variables"]},sidebar:"tutorialSidebar",previous:{title:"oanda",permalink:"/sdk/reference/keys/oanda"},next:{title:"quandl",permalink:"/sdk/reference/keys/quandl"}},a={},c=[{value:"Parameters",id:"parameters",level:2},{value:"Returns",id:"returns",level:2},{value:"Examples",id:"examples",level:2}];function h(e){const n={a:"a",code:"code",h2:"h2",hr:"hr",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,r.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(o.A,{title:"keys.polygon - Reference | OpenBB SDK Docs"}),"\n",(0,s.jsx)(n.p,{children:"Set Polygon key"}),"\n",(0,s.jsxs)(n.p,{children:["Source Code: [",(0,s.jsx)(n.a,{href:"https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/keys_model.py#L481",children:"link"}),"]"]}),"\n",(0,s.jsx)(n.pre,{children:(0,s.jsx)(n.code,{className:"language-python",children:"openbb.keys.polygon(key: str, persist: bool = False, show_output: bool = False)\n"})}),"\n",(0,s.jsx)(n.hr,{}),"\n",(0,s.jsx)(n.h2,{id:"parameters",children:"Parameters"}),"\n",(0,s.jsxs)(n.table,{children:[(0,s.jsx)(n.thead,{children:(0,s.jsxs)(n.tr,{children:[(0,s.jsx)(n.th,{children:"Name"}),(0,s.jsx)(n.th,{children:"Type"}),(0,s.jsx)(n.th,{children:"Description"}),(0,s.jsx)(n.th,{children:"Default"}),(0,s.jsx)(n.th,{children:"Optional"})]})}),(0,s.jsxs)(n.tbody,{children:[(0,s.jsxs)(n.tr,{children:[(0,s.jsx)(n.td,{children:"key"}),(0,s.jsx)(n.td,{children:"str"}),(0,s.jsx)(n.td,{children:"API key"}),(0,s.jsx)(n.td,{children:"None"}),(0,s.jsx)(n.td,{children:"False"})]}),(0,s.jsxs)(n.tr,{children:[(0,s.jsx)(n.td,{children:"persist"}),(0,s.jsx)(n.td,{children:"bool"}),(0,s.jsxs)(n.td,{children:["If False, api key change will be contained to where it was changed. For example, a Jupyter notebook session.",(0,s.jsx)("br",{}),"If True, api key change will be global, i.e. it will affect terminal environment variables.",(0,s.jsx)("br",{}),"By default, False."]}),(0,s.jsx)(n.td,{children:"False"}),(0,s.jsx)(n.td,{children:"True"})]}),(0,s.jsxs)(n.tr,{children:[(0,s.jsx)(n.td,{children:"show_output"}),(0,s.jsx)(n.td,{children:"bool"}),(0,s.jsx)(n.td,{children:"Display status string or not. By default, False."}),(0,s.jsx)(n.td,{children:"False"}),(0,s.jsx)(n.td,{children:"True"})]})]})]}),"\n",(0,s.jsx)(n.hr,{}),"\n",(0,s.jsx)(n.h2,{id:"returns",children:"Returns"}),"\n",(0,s.jsxs)(n.table,{children:[(0,s.jsx)(n.thead,{children:(0,s.jsxs)(n.tr,{children:[(0,s.jsx)(n.th,{children:"Type"}),(0,s.jsx)(n.th,{children:"Description"})]})}),(0,s.jsx)(n.tbody,{children:(0,s.jsxs)(n.tr,{children:[(0,s.jsx)(n.td,{children:"str"}),(0,s.jsx)(n.td,{children:"Status of key set"})]})})]}),"\n",(0,s.jsx)(n.hr,{}),"\n",(0,s.jsx)(n.h2,{id:"examples",children:"Examples"}),"\n",(0,s.jsx)(n.pre,{children:(0,s.jsx)(n.code,{className:"language-python",children:'from openbb_terminal.sdk import openbb\nopenbb.keys.polygon(key="example_key")\n'})}),"\n",(0,s.jsx)(n.hr,{})]})}function p(e={}){const{wrapper:n}={...(0,r.R)(),...e.components};return n?(0,s.jsx)(n,{...e,children:(0,s.jsx)(h,{...e})}):h(e)}},94331:(e,n,t)=>{t.d(n,{A:()=>o});t(96540);var s=t(5260),r=t(74848);function o(e){let{title:n}=e;return(0,r.jsx)(s.A,{children:(0,r.jsx)("title",{children:n})})}},28453:(e,n,t)=>{t.d(n,{R:()=>i,x:()=>l});var s=t(96540);const r={},o=s.createContext(r);function i(e){const n=s.useContext(o);return s.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function l(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(r):e.components||r:i(e.components),s.createElement(o.Provider,{value:n},e.children)}}}]);