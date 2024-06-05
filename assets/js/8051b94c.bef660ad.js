"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[83285],{58419:(e,t,s)=>{s.r(t),s.d(t,{assets:()=>h,contentTitle:()=>a,default:()=>j,frontMatter:()=>l,metadata:()=>c,toc:()=>o});var r=s(74848),n=s(28453),d=s(18228),i=s(19365);const l={title:"Analyst Estimates",description:"Get historical analyst estimates for earnings and revenue"},a=void 0,c={id:"platform/data_models/AnalystEstimates",title:"Analyst Estimates",description:"Get historical analyst estimates for earnings and revenue",source:"@site/content/platform/data_models/AnalystEstimates.md",sourceDirName:"platform/data_models",slug:"/platform/data_models/AnalystEstimates",permalink:"/platform/data_models/AnalystEstimates",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/platform/data_models/AnalystEstimates.md",tags:[],version:"current",frontMatter:{title:"Analyst Estimates",description:"Get historical analyst estimates for earnings and revenue"},sidebar:"tutorialSidebar",previous:{title:"Ameribor",permalink:"/platform/data_models/AMERIBOR"},next:{title:"Analyst Search",permalink:"/platform/data_models/AnalystSearch"}},h={},o=[{value:"Implementation details",id:"implementation-details",level:2},{value:"Class names",id:"class-names",level:3},{value:"Import Statement",id:"import-statement",level:3},{value:"Parameters",id:"parameters",level:2},{value:"Data",id:"data",level:2}];function x(e){const t={code:"code",h2:"h2",h3:"h3",hr:"hr",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,n.R)(),...e.components};return(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(t.hr,{}),"\n",(0,r.jsx)(t.h2,{id:"implementation-details",children:"Implementation details"}),"\n",(0,r.jsx)(t.h3,{id:"class-names",children:"Class names"}),"\n",(0,r.jsxs)(t.table,{children:[(0,r.jsx)(t.thead,{children:(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.th,{children:"Model name"}),(0,r.jsx)(t.th,{children:"Parameters class"}),(0,r.jsx)(t.th,{children:"Data class"})]})}),(0,r.jsx)(t.tbody,{children:(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:(0,r.jsx)(t.code,{children:"AnalystEstimates"})}),(0,r.jsx)(t.td,{children:(0,r.jsx)(t.code,{children:"AnalystEstimatesQueryParams"})}),(0,r.jsx)(t.td,{children:(0,r.jsx)(t.code,{children:"AnalystEstimatesData"})})]})})]}),"\n",(0,r.jsx)(t.h3,{id:"import-statement",children:"Import Statement"}),"\n",(0,r.jsx)(t.pre,{children:(0,r.jsx)(t.code,{className:"language-python",children:"from openbb_core.provider.standard_models.analyst_estimates import (\nAnalystEstimatesData,\nAnalystEstimatesQueryParams,\n)\n"})}),"\n",(0,r.jsx)(t.hr,{}),"\n",(0,r.jsx)(t.h2,{id:"parameters",children:"Parameters"}),"\n",(0,r.jsxs)(d.A,{children:[(0,r.jsx)(i.A,{value:"standard",label:"standard",children:(0,r.jsxs)(t.table,{children:[(0,r.jsx)(t.thead,{children:(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.th,{children:"Name"}),(0,r.jsx)(t.th,{children:"Type"}),(0,r.jsx)(t.th,{children:"Description"}),(0,r.jsx)(t.th,{children:"Default"}),(0,r.jsx)(t.th,{children:"Optional"})]})}),(0,r.jsxs)(t.tbody,{children:[(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"symbol"}),(0,r.jsx)(t.td,{children:"Union[str, List[str]]"}),(0,r.jsx)(t.td,{children:"Symbol to get data for. Multiple items allowed for provider(s): fmp."}),(0,r.jsx)(t.td,{}),(0,r.jsx)(t.td,{children:"False"})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"provider"}),(0,r.jsx)(t.td,{children:"Literal['fmp']"}),(0,r.jsx)(t.td,{children:"The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: f, m, p."}),(0,r.jsx)(t.td,{children:"None"}),(0,r.jsx)(t.td,{children:"True"})]})]})]})}),(0,r.jsx)(i.A,{value:"fmp",label:"fmp",children:(0,r.jsxs)(t.table,{children:[(0,r.jsx)(t.thead,{children:(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.th,{children:"Name"}),(0,r.jsx)(t.th,{children:"Type"}),(0,r.jsx)(t.th,{children:"Description"}),(0,r.jsx)(t.th,{children:"Default"}),(0,r.jsx)(t.th,{children:"Optional"})]})}),(0,r.jsxs)(t.tbody,{children:[(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"symbol"}),(0,r.jsx)(t.td,{children:"Union[str, List[str]]"}),(0,r.jsx)(t.td,{children:"Symbol to get data for. Multiple items allowed for provider(s): fmp."}),(0,r.jsx)(t.td,{}),(0,r.jsx)(t.td,{children:"False"})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"provider"}),(0,r.jsx)(t.td,{children:"Literal['fmp']"}),(0,r.jsx)(t.td,{children:"The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: f, m, p."}),(0,r.jsx)(t.td,{children:"None"}),(0,r.jsx)(t.td,{children:"True"})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"period"}),(0,r.jsx)(t.td,{children:"Literal['quarter', 'annual']"}),(0,r.jsx)(t.td,{children:"Time period of the data to return."}),(0,r.jsx)(t.td,{children:"annual"}),(0,r.jsx)(t.td,{children:"True"})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"limit"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"The number of data entries to return."}),(0,r.jsx)(t.td,{children:"None"}),(0,r.jsx)(t.td,{children:"True"})]})]})]})})]}),"\n",(0,r.jsx)(t.hr,{}),"\n",(0,r.jsx)(t.h2,{id:"data",children:"Data"}),"\n",(0,r.jsxs)(d.A,{children:[(0,r.jsx)(i.A,{value:"standard",label:"standard",children:(0,r.jsxs)(t.table,{children:[(0,r.jsx)(t.thead,{children:(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.th,{children:"Name"}),(0,r.jsx)(t.th,{children:"Type"}),(0,r.jsx)(t.th,{children:"Description"})]})}),(0,r.jsxs)(t.tbody,{children:[(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"symbol"}),(0,r.jsx)(t.td,{children:"str"}),(0,r.jsx)(t.td,{children:"Symbol representing the entity requested in the data."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"date"}),(0,r.jsx)(t.td,{children:"date"}),(0,r.jsx)(t.td,{children:"The date of the data."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_revenue_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated revenue low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_revenue_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated revenue high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_revenue_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated revenue average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_sga_expense_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated SGA expense low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_sga_expense_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated SGA expense high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_sga_expense_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated SGA expense average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebitda_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBITDA low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebitda_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBITDA high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebitda_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBITDA average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebit_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBIT low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebit_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBIT high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebit_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBIT average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_net_income_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated net income low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_net_income_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated net income high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_net_income_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated net income average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_eps_avg"}),(0,r.jsx)(t.td,{children:"float"}),(0,r.jsx)(t.td,{children:"Estimated EPS average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_eps_high"}),(0,r.jsx)(t.td,{children:"float"}),(0,r.jsx)(t.td,{children:"Estimated EPS high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_eps_low"}),(0,r.jsx)(t.td,{children:"float"}),(0,r.jsx)(t.td,{children:"Estimated EPS low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"number_analyst_estimated_revenue"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Number of analysts who estimated revenue."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"number_analysts_estimated_eps"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Number of analysts who estimated EPS."})]})]})]})}),(0,r.jsx)(i.A,{value:"fmp",label:"fmp",children:(0,r.jsxs)(t.table,{children:[(0,r.jsx)(t.thead,{children:(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.th,{children:"Name"}),(0,r.jsx)(t.th,{children:"Type"}),(0,r.jsx)(t.th,{children:"Description"})]})}),(0,r.jsxs)(t.tbody,{children:[(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"symbol"}),(0,r.jsx)(t.td,{children:"str"}),(0,r.jsx)(t.td,{children:"Symbol representing the entity requested in the data."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"date"}),(0,r.jsx)(t.td,{children:"date"}),(0,r.jsx)(t.td,{children:"The date of the data."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_revenue_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated revenue low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_revenue_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated revenue high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_revenue_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated revenue average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_sga_expense_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated SGA expense low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_sga_expense_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated SGA expense high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_sga_expense_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated SGA expense average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebitda_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBITDA low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebitda_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBITDA high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebitda_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBITDA average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebit_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBIT low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebit_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBIT high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_ebit_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated EBIT average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_net_income_low"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated net income low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_net_income_high"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated net income high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_net_income_avg"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Estimated net income average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_eps_avg"}),(0,r.jsx)(t.td,{children:"float"}),(0,r.jsx)(t.td,{children:"Estimated EPS average."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_eps_high"}),(0,r.jsx)(t.td,{children:"float"}),(0,r.jsx)(t.td,{children:"Estimated EPS high."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"estimated_eps_low"}),(0,r.jsx)(t.td,{children:"float"}),(0,r.jsx)(t.td,{children:"Estimated EPS low."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"number_analyst_estimated_revenue"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Number of analysts who estimated revenue."})]}),(0,r.jsxs)(t.tr,{children:[(0,r.jsx)(t.td,{children:"number_analysts_estimated_eps"}),(0,r.jsx)(t.td,{children:"int"}),(0,r.jsx)(t.td,{children:"Number of analysts who estimated EPS."})]})]})]})})]})]})}function j(e={}){const{wrapper:t}={...(0,n.R)(),...e.components};return t?(0,r.jsx)(t,{...e,children:(0,r.jsx)(x,{...e})}):x(e)}},19365:(e,t,s)=>{s.d(t,{A:()=>i});s(96540);var r=s(34164);const n={tabItem:"tabItem_Ymn6"};var d=s(74848);function i(e){let{children:t,hidden:s,className:i}=e;return(0,d.jsx)("div",{role:"tabpanel",className:(0,r.A)(n.tabItem,i),hidden:s,children:t})}},18228:(e,t,s)=>{s.d(t,{A:()=>y});var r=s(96540),n=s(34164),d=s(23104),i=s(56347),l=s(205),a=s(57485),c=s(31682),h=s(89466);function o(e){return function(e){return r.Children.toArray(e).filter((e=>"\n"!==e)).map((e=>{if(!e||(0,r.isValidElement)(e)&&function(e){const{props:t}=e;return!!t&&"object"==typeof t&&"value"in t}(e))return e;throw new Error(`Docusaurus error: Bad <Tabs> child <${"string"==typeof e.type?e.type:e.type.name}>: all children of the <Tabs> component should be <TabItem>, and every <TabItem> should have a unique "value" prop.`)}))?.filter(Boolean)??[]}(e).map((e=>{let{props:{value:t,label:s,attributes:r,default:n}}=e;return{value:t,label:s,attributes:r,default:n}}))}function x(e){const{values:t,children:s}=e;return(0,r.useMemo)((()=>{const e=t??o(s);return function(e){const t=(0,c.X)(e,((e,t)=>e.value===t.value));if(t.length>0)throw new Error(`Docusaurus error: Duplicate values "${t.map((e=>e.value)).join(", ")}" found in <Tabs>. Every value needs to be unique.`)}(e),e}),[t,s])}function j(e){let{value:t,tabValues:s}=e;return s.some((e=>e.value===t))}function u(e){let{queryString:t=!1,groupId:s}=e;const n=(0,i.W6)(),d=function(e){let{queryString:t=!1,groupId:s}=e;if("string"==typeof t)return t;if(!1===t)return null;if(!0===t&&!s)throw new Error('Docusaurus error: The <Tabs> component groupId prop is required if queryString=true, because this value is used as the search param name. You can also provide an explicit value such as queryString="my-search-param".');return s??null}({queryString:t,groupId:s});return[(0,a.aZ)(d),(0,r.useCallback)((e=>{if(!d)return;const t=new URLSearchParams(n.location.search);t.set(d,e),n.replace({...n.location,search:t.toString()})}),[d,n])]}function m(e){const{defaultValue:t,queryString:s=!1,groupId:n}=e,d=x(e),[i,a]=(0,r.useState)((()=>function(e){let{defaultValue:t,tabValues:s}=e;if(0===s.length)throw new Error("Docusaurus error: the <Tabs> component requires at least one <TabItem> children component");if(t){if(!j({value:t,tabValues:s}))throw new Error(`Docusaurus error: The <Tabs> has a defaultValue "${t}" but none of its children has the corresponding value. Available values are: ${s.map((e=>e.value)).join(", ")}. If you intend to show no default tab, use defaultValue={null} instead.`);return t}const r=s.find((e=>e.default))??s[0];if(!r)throw new Error("Unexpected error: 0 tabValues");return r.value}({defaultValue:t,tabValues:d}))),[c,o]=u({queryString:s,groupId:n}),[m,p]=function(e){let{groupId:t}=e;const s=function(e){return e?`docusaurus.tab.${e}`:null}(t),[n,d]=(0,h.Dv)(s);return[n,(0,r.useCallback)((e=>{s&&d.set(e)}),[s,d])]}({groupId:n}),b=(()=>{const e=c??m;return j({value:e,tabValues:d})?e:null})();(0,l.A)((()=>{b&&a(b)}),[b]);return{selectedValue:i,selectValue:(0,r.useCallback)((e=>{if(!j({value:e,tabValues:d}))throw new Error(`Can't select invalid tab value=${e}`);a(e),o(e),p(e)}),[o,p,d]),tabValues:d}}var p=s(92303);const b={tabList:"tabList_TRJ7",tabItem:"tabItem_hGfb"};var f=s(74848);function v(e){let{className:t,block:s,selectedValue:r,selectValue:l,tabValues:a}=e;const c=[],{blockElementScrollPositionUntilNextRender:h}=(0,d.a_)(),{pathname:o}=(0,i.zy)(),x=e=>{const t=e.currentTarget,s=c.indexOf(t),n=a[s].value;n!==r&&(h(t),l(n))},j=e=>{let t=null;switch(e.key){case"Enter":x(e);break;case"ArrowRight":{const s=c.indexOf(e.currentTarget)+1;t=c[s]??c[0];break}case"ArrowLeft":{const s=c.indexOf(e.currentTarget)-1;t=c[s]??c[c.length-1];break}}t?.focus()};return(0,f.jsx)("ul",{role:"tablist","aria-orientation":"horizontal",className:(0,n.A)("_group-tab list-none -ml-7 my-6 overflow-auto"),children:a.map((e=>{let{value:t,label:s,attributes:d}=e;return(0,f.jsx)("li",{role:"tab",tabIndex:r===t?0:-1,"aria-selected":r===t,ref:e=>c.push(e),onKeyDown:j,onClick:x,...d,className:(0,n.A)("font-bold tracking-widest w-fit px-3 inline-flex py-1 uppercase border-b text-lg cursor-pointer",b.tabItem,d?.className,{"border-b-2 pointer-events-none":r===t,"border-b-2 text-[#669dcb] border-[#669dcb]":r===t&&o.startsWith("/terminal"),"border-b-2 text-[#FB923C] border-[#FB923C]":r===t&&o.startsWith("/sdk"),"border-grey-400 text-grey-400 hover:text-[#ffd4b1] hover:border-[#ffd4b1]":r!==t&&o.startsWith("/sdk"),"border-b-2 text-[#FB923C] border-[#FB923C]":r===t&&o.startsWith("/platform"),"border-grey-400 text-grey-400 hover:text-[#ffd4b1] hover:border-[#ffd4b1]":r!==t&&o.startsWith("/platform"),"border-grey-400 text-grey-400 hover:text-[#abd2f1] hover:border-[#abd2f1]":r!==t&&o.startsWith("/terminal")}),children:s??t},t)}))})}function _(e){let{lazy:t,children:s,selectedValue:n}=e;if(s=Array.isArray(s)?s:[s],t){const e=s.find((e=>e.props.value===n));return e?(0,r.cloneElement)(e,{className:"margin-top--md"}):null}return(0,f.jsx)("div",{className:"margin-top--md",children:s.map(((e,t)=>(0,r.cloneElement)(e,{key:t,hidden:e.props.value!==n})))})}function g(e){const t=m(e);return(0,f.jsxs)("div",{className:(0,n.A)("tabs-container",b.tabList),children:[(0,f.jsx)(v,{...e,...t}),(0,f.jsx)(_,{...e,...t})]})}function y(e){const t=(0,p.A)();return(0,f.jsx)(g,{...e},String(t))}},28453:(e,t,s)=>{s.d(t,{R:()=>i,x:()=>l});var r=s(96540);const n={},d=r.createContext(n);function i(e){const t=r.useContext(d);return r.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function l(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(n):e.components||n:i(e.components),r.createElement(d.Provider,{value:t},e.children)}}}]);