"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[18878],{20550:(e,t,l)=>{l.r(t),l.d(t,{assets:()=>c,contentTitle:()=>d,default:()=>o,frontMatter:()=>r,metadata:()=>a,toc:()=>h});var n=l(74848),i=l(28453),s=l(94331);const r={title:"Customization",sidebar_position:4,description:"This documentation page details the functionality of the Settings Menu and the Feature Flags Menu in the OpenBB Terminal. It instructs users how to customize the Terminal, alter its behaviour, and manipulate various environment variables.",keywords:["Settings Menu","Feature Flags Menu","customize Terminal","alter Terminal behaviour","environment variables","Documentation"]},d=void 0,a={id:"terminal/usage/overview/customizing-the-terminal",title:"Customization",description:"This documentation page details the functionality of the Settings Menu and the Feature Flags Menu in the OpenBB Terminal. It instructs users how to customize the Terminal, alter its behaviour, and manipulate various environment variables.",source:"@site/content/terminal/usage/overview/customizing-the-terminal.md",sourceDirName:"terminal/usage/overview",slug:"/terminal/usage/overview/customizing-the-terminal",permalink:"/terminal/usage/overview/customizing-the-terminal",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/terminal/usage/overview/customizing-the-terminal.md",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,sidebarPosition:4,frontMatter:{title:"Customization",sidebar_position:4,description:"This documentation page details the functionality of the Settings Menu and the Feature Flags Menu in the OpenBB Terminal. It instructs users how to customize the Terminal, alter its behaviour, and manipulate various environment variables.",keywords:["Settings Menu","Feature Flags Menu","customize Terminal","alter Terminal behaviour","environment variables","Documentation"]},sidebar:"tutorialSidebar",previous:{title:"Commands and arguments",permalink:"/terminal/usage/overview/commands-and-arguments"},next:{title:"Data",permalink:"/terminal/usage/data/"}},c={},h=[{value:"Settings Menu",id:"settings-menu",level:2},{value:"Style example",id:"style-example",level:3},{value:"Timezone example",id:"timezone-example",level:3},{value:"Feature Flags Menu",id:"feature-flags-menu",level:2},{value:"Interactive example",id:"interactive-example",level:3},{value:"Overwrite",id:"overwrite",level:3},{value:"Exithelp",id:"exithelp",level:3}];function x(e){const t={code:"code",h2:"h2",h3:"h3",p:"p",pre:"pre",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",...(0,i.R)(),...e.components};return(0,n.jsxs)(n.Fragment,{children:[(0,n.jsx)(s.A,{title:"Customization - Overview - Usage | OpenBB Terminal Docs"}),"\n",(0,n.jsx)(t.p,{children:"The OpenBB Terminal contains two menus for altering the behaviour and presentation of the Terminal, Settings and Feature Flags, both of which are accessed from the main menu."}),"\n",(0,n.jsx)("br",{}),"\n",(0,n.jsx)(t.h2,{id:"settings-menu",children:"Settings Menu"}),"\n",(0,n.jsxs)(t.p,{children:["The ",(0,n.jsx)(t.code,{children:"/settings"})," menu provides methods for customizing the look of the Terminal."]}),"\n",(0,n.jsxs)(t.table,{children:[(0,n.jsx)(t.thead,{children:(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.th,{style:{textAlign:"left"},children:"Setting"}),(0,n.jsx)(t.th,{style:{textAlign:"left"},children:"Description"})]})}),(0,n.jsxs)(t.tbody,{children:[(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"chart"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Select the chart style."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"colors"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Sets the color scheme for Terminal fonts."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"dt"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Add or remove date and time from the Terminal command line."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"flair"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Sets the flair emoji to be used."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"height"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Set the default plot height."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"lang"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Select the language for the Terminal menus and commands."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"source"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Use an alternate data sources file. (Not recommended to change.)"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"table"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Select the table style."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"tz"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Select a timezone."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"userdata"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Change the local path to the OpenBBUserData folder."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"width"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Set the default plot width."})]})]})]}),"\n",(0,n.jsx)(t.h3,{id:"style-example",children:"Style example"}),"\n",(0,n.jsx)(t.p,{children:"Set charts and tables styles as light or dark mode."}),"\n",(0,n.jsx)(t.pre,{children:(0,n.jsx)(t.code,{className:"language-console",children:"/settings/table -s light\n"})}),"\n",(0,n.jsx)(t.pre,{children:(0,n.jsx)(t.code,{className:"language-console",children:"/settings/chart -s dark\n"})}),"\n",(0,n.jsx)(t.h3,{id:"timezone-example",children:"Timezone example"}),"\n",(0,n.jsx)(t.p,{children:"Set the local timezone for the Terminal"}),"\n",(0,n.jsx)(t.pre,{children:(0,n.jsx)(t.code,{className:"language-console",children:"/settings/tz Africa/Johannesburg\n"})}),"\n",(0,n.jsx)(t.h2,{id:"feature-flags-menu",children:"Feature Flags Menu"}),"\n",(0,n.jsxs)(t.p,{children:["The ",(0,n.jsx)(t.code,{children:"/featflags"})," menu provides methods for altering the behaviour and responses with environment variables. These configurations are on/off, and the status is indicated by the red/green text of each.  Each parameter is listed below."]}),"\n",(0,n.jsxs)(t.table,{children:[(0,n.jsx)(t.thead,{children:(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.th,{style:{textAlign:"left"},children:"Feature"}),(0,n.jsx)(t.th,{style:{textAlign:"left"},children:"Description"})]})}),(0,n.jsxs)(t.tbody,{children:[(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"cls"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Clear the screen after each command.  Default state is off."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"exithelp"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Automatically print the screen after navigating back one menu.  Default state is off."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"interactive"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Enable/disable interactive tables.  Disabling prints the table directly on the Terminal screen."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"overwrite"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Automatically overwrite exported files with the same name.  Default state is off."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"promptkit"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Enable auto complete and history.  Default state is on."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"rcontext"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Remember loaded tickers while switching menus.  Default state is on."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"retryload"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Retries misspelled commands with the load function first.  Default state is off."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"reporthtml"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Generate reports as HTML files.  Default state is on."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"richpanel"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Displays a border around menus.  Default state is on."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"tbhint"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Display usage hints in the bottom toolbar.  Default state is on."})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:(0,n.jsx)(t.code,{children:"version"})}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"Displays the currently installed version number in the bottom right corner."})]})]})]}),"\n",(0,n.jsx)(t.h3,{id:"interactive-example",children:"Interactive example"}),"\n",(0,n.jsx)(t.p,{children:"When it is off, the Terminal displays all tables directly on the screen instead of opening a window."}),"\n",(0,n.jsx)(t.pre,{children:(0,n.jsx)(t.code,{className:"language-console",children:"/stocks/quote spy\n"})}),"\n",(0,n.jsxs)(t.table,{children:[(0,n.jsx)(t.thead,{children:(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.th,{style:{textAlign:"left"}}),(0,n.jsx)(t.th,{style:{textAlign:"left"},children:"SPY"})]})}),(0,n.jsxs)(t.tbody,{children:[(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"day_low"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"434.87"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"day_high"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"438.09"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"symbol"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"SPY"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"name"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"SPDR S&P 500 ETF Trust"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"price"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"437.25"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"changes_percentage"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"0.0732"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"change"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"0.32"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"year_high"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"459.44"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"year_low"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"373.61"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"market_cap"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"401300183873.0"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"price_avg50"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"433.4872"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"price_avg200"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"424"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"volume"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"56366265"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"avg_volume"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"83194937"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"exchange"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"AMEX"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"open"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"437.55"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"previous_close"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"436.93"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"eps"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"19.851322"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"pe"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"22.03"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"shares_outstanding"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"917782010"})]}),(0,n.jsxs)(t.tr,{children:[(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"date"}),(0,n.jsx)(t.td,{style:{textAlign:"left"},children:"2023-11-08 21:00"})]})]})]}),"\n",(0,n.jsx)(t.h3,{id:"overwrite",children:"Overwrite"}),"\n",(0,n.jsxs)(t.p,{children:["Enable this feature flag to remove the prompt when exporting a file with the same name. This will only overwrite an existing ",(0,n.jsx)(t.code,{children:"XLSX"})," file if the ",(0,n.jsx)(t.code,{children:"--sheet-name"})," is not defined."]}),"\n",(0,n.jsx)(t.h3,{id:"exithelp",children:"Exithelp"}),"\n",(0,n.jsx)(t.p,{children:"Enabling this prints the parent menu on the screen when navigating back from a sub-menu."})]})}function o(e={}){const{wrapper:t}={...(0,i.R)(),...e.components};return t?(0,n.jsx)(t,{...e,children:(0,n.jsx)(x,{...e})}):x(e)}},94331:(e,t,l)=>{l.d(t,{A:()=>s});l(96540);var n=l(5260),i=l(74848);function s(e){let{title:t}=e;return(0,i.jsx)(n.A,{children:(0,i.jsx)("title",{children:t})})}},28453:(e,t,l)=>{l.d(t,{R:()=>r,x:()=>d});var n=l(96540);const i={},s=n.createContext(i);function r(e){const t=n.useContext(s);return n.useMemo((function(){return"function"==typeof e?e(t):{...t,...e}}),[t,e])}function d(e){let t;return t=e.disableParentContext?"function"==typeof e.components?e.components(i):e.components||i:r(e.components),n.createElement(s.Provider,{value:t},e.children)}}}]);