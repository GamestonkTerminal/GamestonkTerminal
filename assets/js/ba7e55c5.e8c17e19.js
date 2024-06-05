"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[48926],{45954:(e,t,r)=>{r.r(t),r.d(t,{assets:()=>h,contentTitle:()=>a,default:()=>x,frontMatter:()=>l,metadata:()=>c,toc:()=>o});var d=r(74848),s=r(28453),n=r(18228),i=r(19365);const l={title:"Yield Curve",description:"Get yield curve data by country and date"},a=void 0,c={id:"platform/data_models/YieldCurve",title:"Yield Curve",description:"Get yield curve data by country and date",source:"@site/content/platform/data_models/YieldCurve.md",sourceDirName:"platform/data_models",slug:"/platform/data_models/YieldCurve",permalink:"/platform/data_models/YieldCurve",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/platform/data_models/YieldCurve.md",tags:[],version:"current",frontMatter:{title:"Yield Curve",description:"Get yield curve data by country and date"},sidebar:"tutorialSidebar",previous:{title:"World News",permalink:"/platform/data_models/WorldNews"},next:{title:"FAQs",permalink:"/platform/faqs/"}},h={},o=[{value:"Implementation details",id:"implementation-details",level:2},{value:"Class names",id:"class-names",level:3},{value:"Import Statement",id:"import-statement",level:3},{value:"Parameters",id:"parameters",level:2},{value:"Data",id:"data",level:2}];function u(e){const t={code:"code",h2:"h2",h3:"h3",hr:"hr",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,s.R)(),...e.components};return(0,d.jsxs)(d.Fragment,{children:[(0,d.jsx)(t.hr,{}),"\n",(0,d.jsx)(t.h2,{id:"implementation-details",children:"Implementation details"}),"\n",(0,d.jsx)(t.h3,{id:"class-names",children:"Class names"}),"\n",(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Model name"}),(0,d.jsx)(t.th,{children:"Parameters class"}),(0,d.jsx)(t.th,{children:"Data class"})]})}),(0,d.jsx)(t.tbody,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:(0,d.jsx)(t.code,{children:"YieldCurve"})}),(0,d.jsx)(t.td,{children:(0,d.jsx)(t.code,{children:"YieldCurveQueryParams"})}),(0,d.jsx)(t.td,{children:(0,d.jsx)(t.code,{children:"YieldCurveData"})})]})})]}),"\n",(0,d.jsx)(t.h3,{id:"import-statement",children:"Import Statement"}),"\n",(0,d.jsx)(t.pre,{children:(0,d.jsx)(t.code,{className:"language-python",children:"from openbb_core.provider.standard_models.yield_curve import (\nYieldCurveData,\nYieldCurveQueryParams,\n)\n"})}),"\n",(0,d.jsx)(t.hr,{}),"\n",(0,d.jsx)(t.h2,{id:"parameters",children:"Parameters"}),"\n",(0,d.jsxs)(n.A,{children:[(0,d.jsx)(i.A,{value:"standard",label:"standard",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"}),(0,d.jsx)(t.th,{children:"Default"}),(0,d.jsx)(t.th,{children:"Optional"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"Union[Union[str, str], List[Union[str, str]]]"}),(0,d.jsx)(t.td,{children:"A specific date to get data for. By default is the current data. Multiple items allowed for provider(s): ecb, econdb, federal_reserve, fmp, fred."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"provider"}),(0,d.jsx)(t.td,{children:"Literal['ecb', 'econdb', 'federal_reserve', 'fmp', 'fred']"}),(0,d.jsx)(t.td,{children:"The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: e, c, b."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]})]})]})}),(0,d.jsx)(i.A,{value:"ecb",label:"ecb",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"}),(0,d.jsx)(t.th,{children:"Default"}),(0,d.jsx)(t.th,{children:"Optional"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"Union[Union[str, str], List[Union[str, str]]]"}),(0,d.jsx)(t.td,{children:"A specific date to get data for. By default is the current data. Multiple items allowed for provider(s): ecb, econdb, federal_reserve, fmp, fred."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"provider"}),(0,d.jsx)(t.td,{children:"Literal['ecb', 'econdb', 'federal_reserve', 'fmp', 'fred']"}),(0,d.jsx)(t.td,{children:"The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: e, c, b."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"rating"}),(0,d.jsx)(t.td,{children:"Literal['aaa', 'all_ratings']"}),(0,d.jsx)(t.td,{children:"The rating type, either 'aaa' or 'all_ratings'."}),(0,d.jsx)(t.td,{children:"aaa"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"yield_curve_type"}),(0,d.jsx)(t.td,{children:"Literal['spot_rate', 'instantaneous_forward', 'par_yield']"}),(0,d.jsx)(t.td,{children:"The yield curve type."}),(0,d.jsx)(t.td,{children:"spot_rate"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"use_cache"}),(0,d.jsx)(t.td,{children:"bool"}),(0,d.jsx)(t.td,{children:"If true, cache the request for four hours."}),(0,d.jsx)(t.td,{children:"True"}),(0,d.jsx)(t.td,{children:"True"})]})]})]})}),(0,d.jsx)(i.A,{value:"econdb",label:"econdb",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"}),(0,d.jsx)(t.th,{children:"Default"}),(0,d.jsx)(t.th,{children:"Optional"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"Union[Union[str, str], List[Union[str, str]]]"}),(0,d.jsx)(t.td,{children:"A specific date to get data for. By default is the current data. Multiple items allowed for provider(s): ecb, econdb, federal_reserve, fmp, fred."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"provider"}),(0,d.jsx)(t.td,{children:"Literal['ecb', 'econdb', 'federal_reserve', 'fmp', 'fred']"}),(0,d.jsx)(t.td,{children:"The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: e, c, b."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"country"}),(0,d.jsx)(t.td,{children:"Literal['australia', 'canada', 'china', 'hong_kong', 'india', 'japan', 'mexico', 'new_zealand', 'russia', 'saudi_arabia', 'singapore', 'south_africa', 'south_korea', 'taiwan', 'thailand', 'united_kingdom', 'united_states']"}),(0,d.jsx)(t.td,{children:"The country to get data. New Zealand, Mexico, Singapore, and Thailand have only monthly data. The nearest date to the requested one will be used."}),(0,d.jsx)(t.td,{children:"united_states"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"use_cache"}),(0,d.jsx)(t.td,{children:"bool"}),(0,d.jsx)(t.td,{children:"If true, cache the request for four hours."}),(0,d.jsx)(t.td,{children:"True"}),(0,d.jsx)(t.td,{children:"True"})]})]})]})}),(0,d.jsx)(i.A,{value:"federal_reserve",label:"federal_reserve",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"}),(0,d.jsx)(t.th,{children:"Default"}),(0,d.jsx)(t.th,{children:"Optional"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"Union[Union[str, str], List[Union[str, str]]]"}),(0,d.jsx)(t.td,{children:"A specific date to get data for. By default is the current data. Multiple items allowed for provider(s): ecb, econdb, federal_reserve, fmp, fred."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"provider"}),(0,d.jsx)(t.td,{children:"Literal['ecb', 'econdb', 'federal_reserve', 'fmp', 'fred']"}),(0,d.jsx)(t.td,{children:"The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: e, c, b."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]})]})]})}),(0,d.jsx)(i.A,{value:"fmp",label:"fmp",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"}),(0,d.jsx)(t.th,{children:"Default"}),(0,d.jsx)(t.th,{children:"Optional"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"Union[Union[str, str], List[Union[str, str]]]"}),(0,d.jsx)(t.td,{children:"A specific date to get data for. By default is the current data. Multiple items allowed for provider(s): ecb, econdb, federal_reserve, fmp, fred."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"provider"}),(0,d.jsx)(t.td,{children:"Literal['ecb', 'econdb', 'federal_reserve', 'fmp', 'fred']"}),(0,d.jsx)(t.td,{children:"The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: e, c, b."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]})]})]})}),(0,d.jsx)(i.A,{value:"fred",label:"fred",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"}),(0,d.jsx)(t.th,{children:"Default"}),(0,d.jsx)(t.th,{children:"Optional"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"Union[Union[str, str], List[Union[str, str]]]"}),(0,d.jsx)(t.td,{children:"A specific date to get data for. By default is the current data. Multiple items allowed for provider(s): ecb, econdb, federal_reserve, fmp, fred."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"provider"}),(0,d.jsx)(t.td,{children:"Literal['ecb', 'econdb', 'federal_reserve', 'fmp', 'fred']"}),(0,d.jsx)(t.td,{children:"The provider to use, by default None. If None, the priority list configured in the settings is used. Default priority: e, c, b."}),(0,d.jsx)(t.td,{children:"None"}),(0,d.jsx)(t.td,{children:"True"})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"yield_curve_type"}),(0,d.jsx)(t.td,{children:"Literal['nominal', 'real', 'breakeven', 'corporate_spot', 'corporate_par']"}),(0,d.jsx)(t.td,{children:"Yield curve type. Nominal and Real Rates are available daily, others are monthly. The closest date to the requested date will be returned."}),(0,d.jsx)(t.td,{children:"nominal"}),(0,d.jsx)(t.td,{children:"True"})]})]})]})})]}),"\n",(0,d.jsx)(t.hr,{}),"\n",(0,d.jsx)(t.h2,{id:"data",children:"Data"}),"\n",(0,d.jsxs)(n.A,{children:[(0,d.jsx)(i.A,{value:"standard",label:"standard",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"The date of the data."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"maturity"}),(0,d.jsx)(t.td,{children:"str"}),(0,d.jsx)(t.td,{children:"Maturity length of the security."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"rate"}),(0,d.jsx)(t.td,{children:"float"}),(0,d.jsx)(t.td,{children:"The yield as a normalized percent (0.05 is 5%)"})]})]})]})}),(0,d.jsx)(i.A,{value:"ecb",label:"ecb",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"The date of the data."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"maturity"}),(0,d.jsx)(t.td,{children:"str"}),(0,d.jsx)(t.td,{children:"Maturity length of the security."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"rate"}),(0,d.jsx)(t.td,{children:"float"}),(0,d.jsx)(t.td,{children:"The yield as a normalized percent (0.05 is 5%)"})]})]})]})}),(0,d.jsx)(i.A,{value:"econdb",label:"econdb",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"The date of the data."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"maturity"}),(0,d.jsx)(t.td,{children:"str"}),(0,d.jsx)(t.td,{children:"Maturity length of the security."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"rate"}),(0,d.jsx)(t.td,{children:"float"}),(0,d.jsx)(t.td,{children:"The yield as a normalized percent (0.05 is 5%)"})]})]})]})}),(0,d.jsx)(i.A,{value:"federal_reserve",label:"federal_reserve",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"The date of the data."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"maturity"}),(0,d.jsx)(t.td,{children:"str"}),(0,d.jsx)(t.td,{children:"Maturity length of the security."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"rate"}),(0,d.jsx)(t.td,{children:"float"}),(0,d.jsx)(t.td,{children:"The yield as a normalized percent (0.05 is 5%)"})]})]})]})}),(0,d.jsx)(i.A,{value:"fmp",label:"fmp",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"The date of the data."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"maturity"}),(0,d.jsx)(t.td,{children:"str"}),(0,d.jsx)(t.td,{children:"Maturity length of the security."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"rate"}),(0,d.jsx)(t.td,{children:"float"}),(0,d.jsx)(t.td,{children:"The yield as a normalized percent (0.05 is 5%)"})]})]})]})}),(0,d.jsx)(i.A,{value:"fred",label:"fred",children:(0,d.jsxs)(t.table,{children:[(0,d.jsx)(t.thead,{children:(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.th,{children:"Name"}),(0,d.jsx)(t.th,{children:"Type"}),(0,d.jsx)(t.th,{children:"Description"})]})}),(0,d.jsxs)(t.tbody,{children:[(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"date"}),(0,d.jsx)(t.td,{children:"The date of the data."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"maturity"}),(0,d.jsx)(t.td,{children:"str"}),(0,d.jsx)(t.td,{children:"Maturity length of the security."})]}),(0,d.jsxs)(t.tr,{children:[(0,d.jsx)(t.td,{children:"rate"}),(0,d.jsx)(t.td,{children:"float"}),(0,d.jsx)(t.td,{children:"The yield as a normalized percent (0.05 is 5%)"})]})]})]})})]})]})}function x(e={}){const{wrapper:t}={...(0,s.R)(),...e.components};return t?(0,d.jsx)(t,{...e,children:(0,d.jsx)(u,{...e})}):u(e)}},19365:(e,t,r)=>{r.d(t,{A:()=>i});r(96540);var d=r(34164);const s={tabItem:"tabItem_Ymn6"};var n=r(74848);function i(e){let{children:t,hidden:r,className:i}=e;return(0,n.jsx)("div",{role:"tabpanel",className:(0,d.A)(s.tabItem,i),hidden:r,children:t})}},18228:(e,t,r)=>{r.d(t,{A:()=>T});var d=r(96540),s=r(34164),n=r(23104),i=r(56347),l=r(205),a=r(57485),c=r(31682),h=r(89466);function o(e){return function(e){return d.Children.toArray(e).filter((e=>"\n"!==e)).map((e=>{if(!e||(0,d.isValidElement)(e)&&function(e){const{props:t}=e;return!!t&&"object"==typeof t&&"value"in t}(e))return e;throw new Error(`Docusaurus error: Bad <Tabs> child <${"string"==typeof e.type?e.type:e.type.name}>: all children of the <Tabs> component should be <TabItem>, and every <TabItem> should have a unique "value" prop.`)}))?.filter(Boolean)??[]}(e).map((e=>{let{props:{value:t,label:r,attributes:d,default:s}}=e;return{value:t,label:r,attributes:d,default:s}}))}function u(e){const{values:t,children:r}=e;return(0,d.useMemo)((()=>{const e=t??o(r);return function(e){const t=(0,c.X)(e,((e,t)=>e.value===t.value));if(t.length>0)throw new Error(`Docusaurus error: Duplicate values "${t.map((e=>e.value)).join(", ")}" found in <Tabs>. Every value needs to be unique.`)}(e),e}),[t,r])}function x(e){let{value:t,tabValues:r}=e;return r.some((e=>e.value===t))}function j(e){let{queryString:t=!1,groupId:r}=e;const s=(0,i.W6)(),n=function(e){let{queryString:t=!1,groupId:r}=e;if("string"==typeof t)return t;if(!1===t)return null;if(!0===t&&!r)throw new Error('Docusaurus error: The <Tabs> component groupId prop is required if queryString=true, because this value is used as the search param name. You can also provide an explicit value such as queryString="my-search-param".');return r??null}({queryString:t,groupId:r});return[(0,a.aZ)(n),(0,d.useCallback)((e=>{if(!n)return;const t=new URLSearchParams(s.location.search);t.set(n,e),s.replace({...s.location,search:t.toString()})}),[n,s])]}function f(e){const{defaultValue:t,queryString:r=!1,groupId:s}=e,n=u(e),[i,a]=(0,d.useState)((()=>function(e){let{defaultValue:t,tabValues:r}=e;if(0===r.length)throw new Error("Docusaurus error: the <Tabs> component requires at least one <TabItem> children component");if(t){if(!x({value:t,tabValues:r}))throw new Error(`Docusaurus error: The <Tabs> has a defaultValue "${t}" but none of its children has the corresponding value. Available values are: ${r.map((e=>e.value)).join(", ")}. If you intend to show no default tab, use defaultValue={null} instead.`);return t}const d=r.find((e=>e.default))??r[0];if(!d)throw new Error("Unexpected error: 0 tabValues");return d.value}({defaultValue:t,tabValues:n}))),[c,o]=j({queryString:r,groupId:s}),[f,p]=function(e){let{groupId:t}=e;const r=function(e){return e?`docusaurus.tab.${e}`:null}(t),[s,n]=(0,h.Dv)(r);return[s,(0,d.useCallback)((e=>{r&&n.set(e)}),[r,n])]}({groupId:s}),b=(()=>{const e=c??f;return x({value:e,tabValues:n})?e:null})();(0,l.A)((()=>{b&&a(b)}),[b]);return{selectedValue:i,selectValue:(0,d.useCallback)((e=>{if(!x({value:e,tabValues:n}))throw new Error(`Can't select invalid tab value=${e}`);a(e),o(e),p(e)}),[o,p,n]),tabValues:n}}var p=r(92303);const b={tabList:"tabList_TRJ7",tabItem:"tabItem_hGfb"};var m=r(74848);function y(e){let{className:t,block:r,selectedValue:d,selectValue:l,tabValues:a}=e;const c=[],{blockElementScrollPositionUntilNextRender:h}=(0,n.a_)(),{pathname:o}=(0,i.zy)(),u=e=>{const t=e.currentTarget,r=c.indexOf(t),s=a[r].value;s!==d&&(h(t),l(s))},x=e=>{let t=null;switch(e.key){case"Enter":u(e);break;case"ArrowRight":{const r=c.indexOf(e.currentTarget)+1;t=c[r]??c[0];break}case"ArrowLeft":{const r=c.indexOf(e.currentTarget)-1;t=c[r]??c[c.length-1];break}}t?.focus()};return(0,m.jsx)("ul",{role:"tablist","aria-orientation":"horizontal",className:(0,s.A)("_group-tab list-none -ml-7 my-6 overflow-auto"),children:a.map((e=>{let{value:t,label:r,attributes:n}=e;return(0,m.jsx)("li",{role:"tab",tabIndex:d===t?0:-1,"aria-selected":d===t,ref:e=>c.push(e),onKeyDown:x,onClick:u,...n,className:(0,s.A)("font-bold tracking-widest w-fit px-3 inline-flex py-1 uppercase border-b text-lg cursor-pointer",b.tabItem,n?.className,{"border-b-2 pointer-events-none":d===t,"border-b-2 text-[#669dcb] border-[#669dcb]":d===t&&o.startsWith("/terminal"),"border-b-2 text-[#FB923C] border-[#FB923C]":d===t&&o.startsWith("/sdk"),"border-grey-400 text-grey-400 hover:text-[#ffd4b1] hover:border-[#ffd4b1]":d!==t&&o.startsWith("/sdk"),"border-b-2 text-[#FB923C] border-[#FB923C]":d===t&&o.startsWith("/platform"),"border-grey-400 text-grey-400 hover:text-[#ffd4b1] hover:border-[#ffd4b1]":d!==t&&o.startsWith("/platform"),"border-grey-400 text-grey-400 hover:text-[#abd2f1] hover:border-[#abd2f1]":d!==t&&o.startsWith("/terminal")}),children:r??t},t)}))})}function v(e){let{lazy:t,children:r,selectedValue:s}=e;if(r=Array.isArray(r)?r:[r],t){const e=r.find((e=>e.props.value===s));return e?(0,d.cloneElement)(e,{className:"margin-top--md"}):null}return(0,m.jsx)("div",{className:"margin-top--md",children:r.map(((e,t)=>(0,d.cloneElement)(e,{key:t,hidden:e.props.value!==s})))})}function g(e){const t=f(e);return(0,m.jsxs)("div",{className:(0,s.A)("tabs-container",b.tabList),children:[(0,m.jsx)(y,{...e,...t}),(0,m.jsx)(v,{...e,...t})]})}function T(e){const t=(0,p.A)();return(0,m.jsx)(g,{...e},String(t))}},28453:(e,t,r)=>{r.d(t,{R:()=>i,x:()=>l});var d=r(96540);const s={},n=d.createContext(s);function i(e){const t=d.useContext(n);return d.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function l(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(s):e.components||s:i(e.components),d.createElement(n.Provider,{value:t},e.children)}}}]);