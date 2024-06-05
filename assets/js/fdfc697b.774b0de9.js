"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[39680],{86519:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>u,contentTitle:()=>d,default:()=>x,frontMatter:()=>l,metadata:()=>c,toc:()=>h});var s=r(74848),n=r(28453),a=r(94331),i=r(18228),o=r(19365);const l={title:"prom",description:"This page provides a detailed explanation of two important functions in FINRA ATS data analysis offered by our tool: 'prom' and 'Chart'. 'prom' fetches and processes the most promising stocks based on linear regression while 'Chart' aids in visualizing the dark pool data for improving trading decisions.",keywords:["FINRA ATS data","Trading tool","Linear regression","Dark pool data","Dark pool trades activity","Stocks analysis","Data visualization","Promising stocks"]},d=void 0,c={id:"sdk/reference/stocks/dps/prom",title:"prom",description:"This page provides a detailed explanation of two important functions in FINRA ATS data analysis offered by our tool: 'prom' and 'Chart'. 'prom' fetches and processes the most promising stocks based on linear regression while 'Chart' aids in visualizing the dark pool data for improving trading decisions.",source:"@site/content/sdk/reference/stocks/dps/prom.md",sourceDirName:"sdk/reference/stocks/dps",slug:"/sdk/reference/stocks/dps/prom",permalink:"/sdk/reference/stocks/dps/prom",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/sdk/reference/stocks/dps/prom.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,frontMatter:{title:"prom",description:"This page provides a detailed explanation of two important functions in FINRA ATS data analysis offered by our tool: 'prom' and 'Chart'. 'prom' fetches and processes the most promising stocks based on linear regression while 'Chart' aids in visualizing the dark pool data for improving trading decisions.",keywords:["FINRA ATS data","Trading tool","Linear regression","Dark pool data","Dark pool trades activity","Stocks analysis","Data visualization","Promising stocks"]},sidebar:"tutorialSidebar",previous:{title:"pos",permalink:"/sdk/reference/stocks/dps/pos"},next:{title:"psi_q",permalink:"/sdk/reference/stocks/dps/psi_q"}},u={},h=[{value:"Parameters",id:"parameters",level:2},{value:"Returns",id:"returns",level:2},{value:"Parameters",id:"parameters-1",level:2},{value:"Returns",id:"returns-1",level:2}];function p(e){const t={a:"a",code:"code",h2:"h2",hr:"hr",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,n.R)(),...e.components};return(0,s.jsxs)(s.Fragment,{children:[(0,s.jsx)(a.A,{title:"stocks.dps.prom - Reference | OpenBB SDK Docs"}),"\n","\n",(0,s.jsxs)(i.A,{children:[(0,s.jsxs)(o.A,{value:"model",label:"Model",default:!0,children:[(0,s.jsx)(t.p,{children:"Get all FINRA ATS data, and parse most promising tickers based on linear regression"}),(0,s.jsxs)(t.p,{children:["Source Code: [",(0,s.jsx)(t.a,{href:"https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/stocks/dark_pool_shorts/finra_model.py#L214",children:"link"}),"]"]}),(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-python",children:'openbb.stocks.dps.prom(limit: int = 1000, tier_ats: str = "T1")\n'})}),(0,s.jsx)(t.hr,{}),(0,s.jsx)(t.h2,{id:"parameters",children:"Parameters"}),(0,s.jsxs)(t.table,{children:[(0,s.jsx)(t.thead,{children:(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.th,{children:"Name"}),(0,s.jsx)(t.th,{children:"Type"}),(0,s.jsx)(t.th,{children:"Description"}),(0,s.jsx)(t.th,{children:"Default"}),(0,s.jsx)(t.th,{children:"Optional"})]})}),(0,s.jsxs)(t.tbody,{children:[(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"limit"}),(0,s.jsx)(t.td,{children:"int"}),(0,s.jsx)(t.td,{children:"Number of tickers to filter from entire ATS data based on the sum of the total weekly shares quantity"}),(0,s.jsx)(t.td,{children:"1000"}),(0,s.jsx)(t.td,{children:"True"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"tier_ats"}),(0,s.jsx)(t.td,{children:"int"}),(0,s.jsx)(t.td,{children:"Tier to process data from: T1, T2 or OTCE"}),(0,s.jsx)(t.td,{children:"T1"}),(0,s.jsx)(t.td,{children:"True"})]})]})]}),(0,s.jsx)(t.hr,{}),(0,s.jsx)(t.h2,{id:"returns",children:"Returns"}),(0,s.jsxs)(t.table,{children:[(0,s.jsx)(t.thead,{children:(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.th,{children:"Type"}),(0,s.jsx)(t.th,{children:"Description"})]})}),(0,s.jsx)(t.tbody,{children:(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"Tuple[pd.DataFrame, Dict]"}),(0,s.jsx)(t.td,{children:"Dark Pools (ATS) Data, Tickers from Dark Pools with better regression slope"})]})})]}),(0,s.jsx)(t.hr,{})]}),(0,s.jsxs)(o.A,{value:"view",label:"Chart",children:[(0,s.jsx)(t.p,{children:"Display dark pool (ATS) data of tickers with growing trades activity. [Source: FINRA]"}),(0,s.jsxs)(t.p,{children:["Source Code: [",(0,s.jsx)(t.a,{href:"https://github.com/OpenBB-finance/OpenBBTerminal/tree/main/openbb_terminal/stocks/dark_pool_shorts/finra_view.py#L188",children:"link"}),"]"]}),(0,s.jsx)(t.pre,{children:(0,s.jsx)(t.code,{className:"language-python",children:'openbb.stocks.dps.prom_chart(input_limit: int = 1000, limit: int = 10, tier: str = "T1", export: str = "", external_axes: Optional[List[matplotlib.axes._axes.Axes]] = None)\n'})}),(0,s.jsx)(t.hr,{}),(0,s.jsx)(t.h2,{id:"parameters-1",children:"Parameters"}),(0,s.jsxs)(t.table,{children:[(0,s.jsx)(t.thead,{children:(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.th,{children:"Name"}),(0,s.jsx)(t.th,{children:"Type"}),(0,s.jsx)(t.th,{children:"Description"}),(0,s.jsx)(t.th,{children:"Default"}),(0,s.jsx)(t.th,{children:"Optional"})]})}),(0,s.jsxs)(t.tbody,{children:[(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"input_limit"}),(0,s.jsx)(t.td,{children:"int"}),(0,s.jsxs)(t.td,{children:["Number of tickers to filter from entire ATS data based on",(0,s.jsx)("br",{}),"the sum of the total weekly shares quantity"]}),(0,s.jsx)(t.td,{children:"1000"}),(0,s.jsx)(t.td,{children:"True"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"limit"}),(0,s.jsx)(t.td,{children:"int"}),(0,s.jsxs)(t.td,{children:["Number of tickers to display from most promising with",(0,s.jsx)("br",{}),"better linear regression slope"]}),(0,s.jsx)(t.td,{children:"10"}),(0,s.jsx)(t.td,{children:"True"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"tier"}),(0,s.jsx)(t.td,{children:"str"}),(0,s.jsx)(t.td,{children:"Tier to process data from: T1, T2 or OTCE"}),(0,s.jsx)(t.td,{children:"T1"}),(0,s.jsx)(t.td,{children:"True"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"export"}),(0,s.jsx)(t.td,{children:"str"}),(0,s.jsx)(t.td,{children:"Export dataframe data to csv,json,xlsx file"}),(0,s.jsx)(t.td,{}),(0,s.jsx)(t.td,{children:"True"})]}),(0,s.jsxs)(t.tr,{children:[(0,s.jsx)(t.td,{children:"external_axes"}),(0,s.jsx)(t.td,{children:"Optional[List[plt.Axes]]"}),(0,s.jsx)(t.td,{children:"External axes (1 axis is expected in the list), by default None"}),(0,s.jsx)(t.td,{children:"None"}),(0,s.jsx)(t.td,{children:"True"})]})]})]}),(0,s.jsx)(t.hr,{}),(0,s.jsx)(t.h2,{id:"returns-1",children:"Returns"}),(0,s.jsx)(t.p,{children:"This function does not return anything"}),(0,s.jsx)(t.hr,{})]})]})]})}function x(e={}){const{wrapper:t}={...(0,n.R)(),...e.components};return t?(0,s.jsx)(t,{...e,children:(0,s.jsx)(p,{...e})}):p(e)}},19365:(e,t,r)=>{r.d(t,{A:()=>i});r(96540);var s=r(34164);const n={tabItem:"tabItem_Ymn6"};var a=r(74848);function i(e){let{children:t,hidden:r,className:i}=e;return(0,a.jsx)("div",{role:"tabpanel",className:(0,s.A)(n.tabItem,i),hidden:r,children:t})}},94331:(e,t,r)=>{r.d(t,{A:()=>a});r(96540);var s=r(5260),n=r(74848);function a(e){let{title:t}=e;return(0,n.jsx)(s.A,{children:(0,n.jsx)("title",{children:t})})}},18228:(e,t,r)=>{r.d(t,{A:()=>y});var s=r(96540),n=r(34164),a=r(23104),i=r(56347),o=r(205),l=r(57485),d=r(31682),c=r(89466);function u(e){return function(e){return s.Children.toArray(e).filter((e=>"\n"!==e)).map((e=>{if(!e||(0,s.isValidElement)(e)&&function(e){const{props:t}=e;return!!t&&"object"==typeof t&&"value"in t}(e))return e;throw new Error(`Docusaurus error: Bad <Tabs> child <${"string"==typeof e.type?e.type:e.type.name}>: all children of the <Tabs> component should be <TabItem>, and every <TabItem> should have a unique "value" prop.`)}))?.filter(Boolean)??[]}(e).map((e=>{let{props:{value:t,label:r,attributes:s,default:n}}=e;return{value:t,label:r,attributes:s,default:n}}))}function h(e){const{values:t,children:r}=e;return(0,s.useMemo)((()=>{const e=t??u(r);return function(e){const t=(0,d.X)(e,((e,t)=>e.value===t.value));if(t.length>0)throw new Error(`Docusaurus error: Duplicate values "${t.map((e=>e.value)).join(", ")}" found in <Tabs>. Every value needs to be unique.`)}(e),e}),[t,r])}function p(e){let{value:t,tabValues:r}=e;return r.some((e=>e.value===t))}function x(e){let{queryString:t=!1,groupId:r}=e;const n=(0,i.W6)(),a=function(e){let{queryString:t=!1,groupId:r}=e;if("string"==typeof t)return t;if(!1===t)return null;if(!0===t&&!r)throw new Error('Docusaurus error: The <Tabs> component groupId prop is required if queryString=true, because this value is used as the search param name. You can also provide an explicit value such as queryString="my-search-param".');return r??null}({queryString:t,groupId:r});return[(0,l.aZ)(a),(0,s.useCallback)((e=>{if(!a)return;const t=new URLSearchParams(n.location.search);t.set(a,e),n.replace({...n.location,search:t.toString()})}),[a,n])]}function m(e){const{defaultValue:t,queryString:r=!1,groupId:n}=e,a=h(e),[i,l]=(0,s.useState)((()=>function(e){let{defaultValue:t,tabValues:r}=e;if(0===r.length)throw new Error("Docusaurus error: the <Tabs> component requires at least one <TabItem> children component");if(t){if(!p({value:t,tabValues:r}))throw new Error(`Docusaurus error: The <Tabs> has a defaultValue "${t}" but none of its children has the corresponding value. Available values are: ${r.map((e=>e.value)).join(", ")}. If you intend to show no default tab, use defaultValue={null} instead.`);return t}const s=r.find((e=>e.default))??r[0];if(!s)throw new Error("Unexpected error: 0 tabValues");return s.value}({defaultValue:t,tabValues:a}))),[d,u]=x({queryString:r,groupId:n}),[m,f]=function(e){let{groupId:t}=e;const r=function(e){return e?`docusaurus.tab.${e}`:null}(t),[n,a]=(0,c.Dv)(r);return[n,(0,s.useCallback)((e=>{r&&a.set(e)}),[r,a])]}({groupId:n}),b=(()=>{const e=d??m;return p({value:e,tabValues:a})?e:null})();(0,o.A)((()=>{b&&l(b)}),[b]);return{selectedValue:i,selectValue:(0,s.useCallback)((e=>{if(!p({value:e,tabValues:a}))throw new Error(`Can't select invalid tab value=${e}`);l(e),u(e),f(e)}),[u,f,a]),tabValues:a}}var f=r(92303);const b={tabList:"tabList_TRJ7",tabItem:"tabItem_hGfb"};var j=r(74848);function v(e){let{className:t,block:r,selectedValue:s,selectValue:o,tabValues:l}=e;const d=[],{blockElementScrollPositionUntilNextRender:c}=(0,a.a_)(),{pathname:u}=(0,i.zy)(),h=e=>{const t=e.currentTarget,r=d.indexOf(t),n=l[r].value;n!==s&&(c(t),o(n))},p=e=>{let t=null;switch(e.key){case"Enter":h(e);break;case"ArrowRight":{const r=d.indexOf(e.currentTarget)+1;t=d[r]??d[0];break}case"ArrowLeft":{const r=d.indexOf(e.currentTarget)-1;t=d[r]??d[d.length-1];break}}t?.focus()};return(0,j.jsx)("ul",{role:"tablist","aria-orientation":"horizontal",className:(0,n.A)("_group-tab list-none -ml-7 my-6 overflow-auto"),children:l.map((e=>{let{value:t,label:r,attributes:a}=e;return(0,j.jsx)("li",{role:"tab",tabIndex:s===t?0:-1,"aria-selected":s===t,ref:e=>d.push(e),onKeyDown:p,onClick:h,...a,className:(0,n.A)("font-bold tracking-widest w-fit px-3 inline-flex py-1 uppercase border-b text-lg cursor-pointer",b.tabItem,a?.className,{"border-b-2 pointer-events-none":s===t,"border-b-2 text-[#669dcb] border-[#669dcb]":s===t&&u.startsWith("/terminal"),"border-b-2 text-[#FB923C] border-[#FB923C]":s===t&&u.startsWith("/sdk"),"border-grey-400 text-grey-400 hover:text-[#ffd4b1] hover:border-[#ffd4b1]":s!==t&&u.startsWith("/sdk"),"border-b-2 text-[#FB923C] border-[#FB923C]":s===t&&u.startsWith("/platform"),"border-grey-400 text-grey-400 hover:text-[#ffd4b1] hover:border-[#ffd4b1]":s!==t&&u.startsWith("/platform"),"border-grey-400 text-grey-400 hover:text-[#abd2f1] hover:border-[#abd2f1]":s!==t&&u.startsWith("/terminal")}),children:r??t},t)}))})}function g(e){let{lazy:t,children:r,selectedValue:n}=e;if(r=Array.isArray(r)?r:[r],t){const e=r.find((e=>e.props.value===n));return e?(0,s.cloneElement)(e,{className:"margin-top--md"}):null}return(0,j.jsx)("div",{className:"margin-top--md",children:r.map(((e,t)=>(0,s.cloneElement)(e,{key:t,hidden:e.props.value!==n})))})}function k(e){const t=m(e);return(0,j.jsxs)("div",{className:(0,n.A)("tabs-container",b.tabList),children:[(0,j.jsx)(v,{...e,...t}),(0,j.jsx)(g,{...e,...t})]})}function y(e){const t=(0,f.A)();return(0,j.jsx)(k,{...e},String(t))}},28453:(e,t,r)=>{r.d(t,{R:()=>i,x:()=>o});var s=r(96540);const n={},a=s.createContext(n);function i(e){const t=s.useContext(a);return s.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function o(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(n):e.components||n:i(e.components),s.createElement(a.Provider,{value:t},e.children)}}}]);