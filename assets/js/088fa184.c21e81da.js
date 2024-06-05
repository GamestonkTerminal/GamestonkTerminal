"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[75723],{22394:(e,t,n)=>{n.r(t),n.d(t,{assets:()=>c,contentTitle:()=>d,default:()=>p,frontMatter:()=>i,metadata:()=>l,toc:()=>o});var r=n(74848),s=n(28453),a=n(94331);const i={title:"clean",description:"This documentation details how to use OpenBBTerminal's 'clean' function to clean up NaNs in a pandas DataFrame. It outlines the parameters, return values, and available methods for filling and dropping NaN values.",keywords:["econometrics","clean data","NaN handling","machine learning","dataset cleaning","fill method","drop method","data pre-processing"]},d=void 0,l={id:"sdk/reference/econometrics/clean",title:"clean",description:"This documentation details how to use OpenBBTerminal's 'clean' function to clean up NaNs in a pandas DataFrame. It outlines the parameters, return values, and available methods for filling and dropping NaN values.",source:"@site/content/sdk/reference/econometrics/clean.md",sourceDirName:"sdk/reference/econometrics",slug:"/sdk/reference/econometrics/clean",permalink:"/sdk/reference/econometrics/clean",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/sdk/reference/econometrics/clean.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"clean",description:"This documentation details how to use OpenBBTerminal's 'clean' function to clean up NaNs in a pandas DataFrame. It outlines the parameters, return values, and available methods for filling and dropping NaN values.",keywords:["econometrics","clean data","NaN handling","machine learning","dataset cleaning","fill method","drop method","data pre-processing"]},sidebar:"tutorialSidebar",previous:{title:"bpag",permalink:"/sdk/reference/econometrics/bpag"},next:{title:"coint",permalink:"/sdk/reference/econometrics/coint"}},c={},o=[{value:"Parameters",id:"parameters",level:2},{value:"Returns",id:"returns",level:2}];function h(e){const t={a:"a",code:"code",h2:"h2",hr:"hr",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,s.R)(),...e.components};return(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(a.A,{title:"econometrics.clean - Reference | OpenBB SDK Docs"}),"\n",(0,r.jsx)(t.p,{children:"Clean up NaNs from the dataset"}),"\n",(0,r.jsxs)(t.p,{children:["Source Code: [",(0,r.jsx)(t.a,{href:"https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/econometrics/econometrics_model.py#L65",children:"link"}),"]"]}),"\n",(0,r.jsx)(t.pre,{children:(0,r.jsx)(t.code,{className:"language-python",children:'openbb.econometrics.clean(dataset: pd.DataFrame, fill: str = "", drop: str = "", limit: Optional[int] = None)\n'})}),"\n",(0,r.jsx)(t.hr,{}),"\n",(0,r.jsx)(t.h2,{id:"parameters",children:"Parameters"}),"\n",(0,r.jsxs)(t.table,{children:[(0,r.jsx)(t.thead,{children:(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.th,{children:"Name"}),(0,r.jsx)(t.th,{children:"Type"}),(0,r.jsx)(t.th,{children:"Description"}),(0,r.jsx)(t.th,{children:"Default"}),(0,r.jsx)(t.th,{children:"Optional"})]})}),(0,r.jsxs)(t.tbody,{children:[(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"dataset"}),(0,r.jsx)(t.td,{children:"pd.DataFrame"}),(0,r.jsx)(t.td,{children:"The dataset you wish to clean"}),(0,r.jsx)(t.td,{children:"None"}),(0,r.jsx)(t.td,{children:"False"})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"fill"}),(0,r.jsx)(t.td,{children:"str"}),(0,r.jsxs)(t.td,{children:["The method of filling NaNs. Choose from:",(0,r.jsx)("br",{}),"rfill, cfill, rbfill, cbfill, rffill, cffill"]}),(0,r.jsx)(t.td,{}),(0,r.jsx)(t.td,{children:"True"})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"drop"}),(0,r.jsx)(t.td,{children:"str"}),(0,r.jsxs)(t.td,{children:["The method of dropping NaNs. Choose from:",(0,r.jsx)("br",{}),"rdrop, cdrop"]}),(0,r.jsx)(t.td,{}),(0,r.jsx)(t.td,{children:"True"})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"limit"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"The maximum limit you wish to apply that can be forward or backward filled"}),(0,r.jsx)(t.td,{children:"None"}),(0,r.jsx)(t.td,{children:"True"})]})]})]}),"\n",(0,r.jsx)(t.hr,{}),"\n",(0,r.jsx)(t.h2,{id:"returns",children:"Returns"}),"\n",(0,r.jsxs)(t.table,{children:[(0,r.jsx)(t.thead,{children:(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.th,{children:"Type"}),(0,r.jsx)(t.th,{children:"Description"})]})}),(0,r.jsx)(t.tbody,{children:(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"pd.DataFrame"}),(0,r.jsx)(t.td,{children:"Dataframe with cleaned up data"})]})})]}),"\n",(0,r.jsx)(t.hr,{})]})}function p(e={}){const{wrapper:t}={...(0,s.R)(),...e.components};return t?(0,r.jsx)(t,{...e,children:(0,r.jsx)(h,{...e})}):h(e)}},94331:(e,t,n)=>{n.d(t,{A:()=>a});n(96540);var r=n(5260),s=n(74848);function a(e){let{title:t}=e;return(0,s.jsx)(r.A,{children:(0,s.jsx)("title",{children:t})})}},28453:(e,t,n)=>{n.d(t,{R:()=>i,x:()=>d});var r=n(96540);const s={},a=r.createContext(s);function i(e){const t=r.useContext(a);return r.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function d(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(s):e.components||s:i(e.components),r.createElement(a.Provider,{value:t},e.children)}}}]);