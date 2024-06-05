"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[84163],{81879:(e,o,t)=>{t.r(o),t.d(o,{assets:()=>c,contentTitle:()=>s,default:()=>h,frontMatter:()=>l,metadata:()=>a,toc:()=>d});var n=t(74848),r=t(28453),i=t(94331);const l={title:"regions",description:"This page provides details about the 'regions' function of the OpenBB finance platform. The said function displays the portfolio region allocation in comparison to the benchmark. It includes a brief overview, parameters, return values, and an example usage.",keywords:["OpenBB finance platform","portfolio region allocation","benchmark comparison","portfolio management","portfolio allocation","parameters","example usage"]},s=void 0,a={id:"sdk/reference/portfolio/alloc/regions",title:"regions",description:"This page provides details about the 'regions' function of the OpenBB finance platform. The said function displays the portfolio region allocation in comparison to the benchmark. It includes a brief overview, parameters, return values, and an example usage.",source:"@site/content/sdk/reference/portfolio/alloc/regions.md",sourceDirName:"sdk/reference/portfolio/alloc",slug:"/sdk/reference/portfolio/alloc/regions",permalink:"/sdk/reference/portfolio/alloc/regions",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/sdk/reference/portfolio/alloc/regions.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"regions",description:"This page provides details about the 'regions' function of the OpenBB finance platform. The said function displays the portfolio region allocation in comparison to the benchmark. It includes a brief overview, parameters, return values, and an example usage.",keywords:["OpenBB finance platform","portfolio region allocation","benchmark comparison","portfolio management","portfolio allocation","parameters","example usage"]},sidebar:"tutorialSidebar",previous:{title:"countries",permalink:"/sdk/reference/portfolio/alloc/countries"},next:{title:"sectors",permalink:"/sdk/reference/portfolio/alloc/sectors"}},c={},d=[{value:"Parameters",id:"parameters",level:2},{value:"Returns",id:"returns",level:2},{value:"Examples",id:"examples",level:2}];function p(e){const o={a:"a",code:"code",h2:"h2",hr:"hr",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,r.R)(),...e.components};return(0,n.jsxs)(n.Fragment,{children:[(0,n.jsx)(i.A,{title:"portfolio.alloc.regions - Reference | OpenBB SDK Docs"}),"\n",(0,n.jsx)(o.p,{children:"Display portfolio region allocation compared to the benchmark"}),"\n",(0,n.jsxs)(o.p,{children:["Source Code: [",(0,n.jsx)(o.a,{href:"https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/portfolio/portfolio_model.py#L902",children:"link"}),"]"]}),"\n",(0,n.jsx)(o.pre,{children:(0,n.jsx)(o.code,{className:"language-python",children:"openbb.portfolio.alloc.regions(portfolio_engine: portfolio_engine.PortfolioEngine, limit: int = 10, tables: bool = False, recalculate: bool = False)\n"})}),"\n",(0,n.jsx)(o.hr,{}),"\n",(0,n.jsx)(o.h2,{id:"parameters",children:"Parameters"}),"\n",(0,n.jsxs)(o.table,{children:[(0,n.jsx)(o.thead,{children:(0,n.jsxs)(o.tr,{children:[(0,n.jsx)(o.th,{children:"Name"}),(0,n.jsx)(o.th,{children:"Type"}),(0,n.jsx)(o.th,{children:"Description"}),(0,n.jsx)(o.th,{children:"Default"}),(0,n.jsx)(o.th,{children:"Optional"})]})}),(0,n.jsxs)(o.tbody,{children:[(0,n.jsxs)(o.tr,{children:[(0,n.jsx)(o.td,{children:"portfolio_engine"}),(0,n.jsx)(o.td,{children:"PortfolioEngine"}),(0,n.jsxs)(o.td,{children:["PortfolioEngine class instance, this will hold transactions and perform calculations.",(0,n.jsx)("br",{}),"Use ",(0,n.jsx)(o.code,{children:"portfolio.load"})," to create a PortfolioEngine."]}),(0,n.jsx)(o.td,{children:"None"}),(0,n.jsx)(o.td,{children:"False"})]}),(0,n.jsxs)(o.tr,{children:[(0,n.jsx)(o.td,{children:"tables"}),(0,n.jsx)(o.td,{children:"bool"}),(0,n.jsx)(o.td,{children:"Whether to include separate allocation tables"}),(0,n.jsx)(o.td,{children:"False"}),(0,n.jsx)(o.td,{children:"True"})]}),(0,n.jsxs)(o.tr,{children:[(0,n.jsx)(o.td,{children:"limit"}),(0,n.jsx)(o.td,{children:"int"}),(0,n.jsx)(o.td,{children:"The amount of assets you wish to show, by default this is set to 10"}),(0,n.jsx)(o.td,{children:"10"}),(0,n.jsx)(o.td,{children:"True"})]}),(0,n.jsxs)(o.tr,{children:[(0,n.jsx)(o.td,{children:"recalculate"}),(0,n.jsx)(o.td,{children:"bool"}),(0,n.jsx)(o.td,{children:"Flag to force recalculate allocation if already exists"}),(0,n.jsx)(o.td,{children:"False"}),(0,n.jsx)(o.td,{children:"True"})]})]})]}),"\n",(0,n.jsx)(o.hr,{}),"\n",(0,n.jsx)(o.h2,{id:"returns",children:"Returns"}),"\n",(0,n.jsxs)(o.table,{children:[(0,n.jsx)(o.thead,{children:(0,n.jsxs)(o.tr,{children:[(0,n.jsx)(o.th,{children:"Type"}),(0,n.jsx)(o.th,{children:"Description"})]})}),(0,n.jsx)(o.tbody,{children:(0,n.jsxs)(o.tr,{children:[(0,n.jsx)(o.td,{children:"Union[pd.DataFrame, Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]]"}),(0,n.jsxs)(o.td,{children:["DataFrame with combined allocation plus individual allocation if tables is ",(0,n.jsx)(o.code,{children:"True"}),"."]})]})})]}),"\n",(0,n.jsx)(o.hr,{}),"\n",(0,n.jsx)(o.h2,{id:"examples",children:"Examples"}),"\n",(0,n.jsx)(o.pre,{children:(0,n.jsx)(o.code,{className:"language-python",children:'from openbb_terminal.sdk import openbb\np = openbb.portfolio.load("openbb_terminal/miscellaneous/portfolio_examples/holdings/example.csv")\noutput = openbb.portfolio.alloc.regions(p)\n'})}),"\n",(0,n.jsx)(o.hr,{})]})}function h(e={}){const{wrapper:o}={...(0,r.R)(),...e.components};return o?(0,n.jsx)(o,{...e,children:(0,n.jsx)(p,{...e})}):p(e)}},94331:(e,o,t)=>{t.d(o,{A:()=>i});t(96540);var n=t(5260),r=t(74848);function i(e){let{title:o}=e;return(0,r.jsx)(n.A,{children:(0,r.jsx)("title",{children:o})})}},28453:(e,o,t)=>{t.d(o,{R:()=>l,x:()=>s});var n=t(96540);const r={},i=n.createContext(r);function l(e){const o=n.useContext(i);return n.useMemo((function(){return"function"==typeof e?e(o):{...o,...e}}),[o,e])}function s(e){let o;return o=e.disableParentContext?"function"==typeof e.components?e.components(r):e.components||r:l(e.components),n.createElement(i.Provider,{value:o},e.children)}}}]);