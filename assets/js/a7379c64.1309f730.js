"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[85663],{34402:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>l,contentTitle:()=>r,default:()=>h,frontMatter:()=>o,metadata:()=>c,toc:()=>d});var i=n(74848),s=n(28453),a=n(94331);const o={title:"Basics",sidebar_position:2,description:"This page provides an overview of the basics of the OpenBB add-in for Microsoft Excel. It covers the basic usage of the add-in and the available functions.",keywords:["Microsoft Excel","Add-in","Basics","Examples","Functions"]},r=void 0,c={id:"excel/getting-started/basics",title:"Basics",description:"This page provides an overview of the basics of the OpenBB add-in for Microsoft Excel. It covers the basic usage of the add-in and the available functions.",source:"@site/content/excel/getting-started/basics.md",sourceDirName:"excel/getting-started",slug:"/excel/getting-started/basics",permalink:"/excel/getting-started/basics",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/excel/getting-started/basics.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,sidebarPosition:2,frontMatter:{title:"Basics",sidebar_position:2,description:"This page provides an overview of the basics of the OpenBB add-in for Microsoft Excel. It covers the basic usage of the add-in and the available functions.",keywords:["Microsoft Excel","Add-in","Basics","Examples","Functions"]},sidebar:"tutorialSidebar",previous:{title:"Installation",permalink:"/excel/getting-started/installation"},next:{title:"Formula Builder",permalink:"/excel/getting-started/formula_builder"}},l={},d=[{value:"Advanced",id:"advanced",level:2}];function p(e){const t={admonition:"admonition",code:"code",h2:"h2",li:"li",ol:"ol",p:"p",pre:"pre",ul:"ul",...(0,s.R)(),...e.components};return(0,i.jsxs)(i.Fragment,{children:[(0,i.jsx)(a.A,{title:"Basics | OpenBB Add-in for Excel Docs"}),"\n",(0,i.jsx)(t.p,{children:"The OpenBB Add-in for Excel provides direct access to the OpenBB platform, where each function implements the following pattern:"}),"\n",(0,i.jsxs)(t.ul,{children:["\n",(0,i.jsx)(t.li,{children:(0,i.jsx)(t.code,{children:"OBB.[MENU].[SUB_MENU].[COMMAND]"})}),"\n"]}),"\n",(0,i.jsx)(t.admonition,{type:"tip",children:(0,i.jsxs)(t.p,{children:["Use the <TAB> key to autocomplete the function name after typing ",(0,i.jsx)(t.code,{children:"=OBB."})]})}),"\n",(0,i.jsx)(t.p,{children:"Examples:"}),"\n",(0,i.jsxs)(t.ol,{children:["\n",(0,i.jsxs)(t.li,{children:["\n",(0,i.jsx)(t.p,{children:"Getting balance sheet data for a stock:"}),"\n",(0,i.jsx)(t.pre,{children:(0,i.jsx)(t.code,{className:"language-excel",children:'=OBB.EQUITY.FUNDAMENTAL.BALANCE("AAPL")\n'})}),"\n"]}),"\n",(0,i.jsxs)(t.li,{children:["\n",(0,i.jsx)(t.p,{children:"Getting the latest news for a stock:"}),"\n",(0,i.jsx)(t.pre,{children:(0,i.jsx)(t.code,{className:"language-excel",children:'=OBB.NEWS.COMPANY("AAPL")\n'})}),"\n"]}),"\n",(0,i.jsxs)(t.li,{children:["\n",(0,i.jsx)(t.p,{children:"Getting the earnings calendar:"}),"\n",(0,i.jsx)(t.pre,{children:(0,i.jsx)(t.code,{className:"language-excel",children:'=OBB.EQUITY.CALENDAR.IPO(,"2023-11-20")\n'})}),"\n"]}),"\n"]}),"\n",(0,i.jsx)(t.admonition,{type:"tip",children:(0,i.jsx)(t.p,{children:"If you want to skip a parameter use comma (or semi-colon depending on your number separator) without any value. In example iii. we are skipping the first parameter (symbol)."})}),"\n",(0,i.jsx)(t.h2,{id:"advanced",children:"Advanced"}),"\n",(0,i.jsx)("div",{style:{display:"flex",justifyContent:"center"},children:(0,i.jsx)("iframe",{style:{width:"800px",height:"450px",display:"block",margin:"0 auto"},src:"https://www.youtube.com/embed/mk-NDjH8CDE?si=oL1Iqh1yJc24dh-K",title:"YouTube video player",frameBorder:"0",allow:"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"})})]})}function h(e={}){const{wrapper:t}={...(0,s.R)(),...e.components};return t?(0,i.jsx)(t,{...e,children:(0,i.jsx)(p,{...e})}):p(e)}},94331:(e,t,n)=>{n.d(t,{A:()=>a});n(96540);var i=n(5260),s=n(74848);function a(e){let{title:t}=e;return(0,s.jsx)(i.A,{children:(0,s.jsx)("title",{children:t})})}},28453:(e,t,n)=>{n.d(t,{R:()=>o,x:()=>r});var i=n(96540);const s={},a=i.createContext(s);function o(e){const t=i.useContext(a);return i.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function r(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(s):e.components||s:o(e.components),i.createElement(a.Provider,{value:t},e.children)}}}]);