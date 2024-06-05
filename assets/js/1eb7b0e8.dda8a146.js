"use strict";(self.webpackChunkdocs=self.webpackChunkdocs||[]).push([[75865],{37152:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>c,contentTitle:()=>s,default:()=>h,frontMatter:()=>r,metadata:()=>l,toc:()=>d});var o=t(74848),i=t(28453),a=t(94331);const r={title:"Authorization and API Keys",sidebar_position:2,description:"An overview for setting up the OpenBB Platform Python client and Fast API with data provider API keys.",keywords:["tutorial","OpenBB Platform","Python client","Fast API","getting started","authorization","data providers","OpenBB Hub","local environment","environment variables"]},s=void 0,l={id:"platform/getting_started/api_keys",title:"Authorization and API Keys",description:"An overview for setting up the OpenBB Platform Python client and Fast API with data provider API keys.",source:"@site/content/platform/getting_started/api_keys.mdx",sourceDirName:"platform/getting_started",slug:"/platform/getting_started/api_keys",permalink:"/platform/getting_started/api_keys",draft:!1,unlisted:!1,editUrl:"https://github.com/OpenBB-finance/OpenBBTerminal/edit/main/website/content/platform/getting_started/api_keys.mdx",tags:[],version:"current",lastUpdatedBy:"montezdesousa",lastUpdatedAt:1717581546e3,sidebarPosition:2,frontMatter:{title:"Authorization and API Keys",sidebar_position:2,description:"An overview for setting up the OpenBB Platform Python client and Fast API with data provider API keys.",keywords:["tutorial","OpenBB Platform","Python client","Fast API","getting started","authorization","data providers","OpenBB Hub","local environment","environment variables"]},sidebar:"tutorialSidebar",previous:{title:"Quickstart",permalink:"/platform/getting_started/quickstart"},next:{title:"Finding Ticker Symbols",permalink:"/platform/getting_started/find_symbols"}},c={},d=[{value:"OpenBB Hub",id:"openbb-hub",level:3},{value:"Local Environment",id:"local-environment",level:3}];function p(e){const n={a:"a",admonition:"admonition",code:"code",h3:"h3",p:"p",pre:"pre",...(0,i.R)(),...e.components};return(0,o.jsxs)(o.Fragment,{children:[(0,o.jsx)(a.A,{title:"API Keys - Usage | OpenBB Platform Docs"}),"\n",(0,o.jsxs)(n.p,{children:["By default, authorization is not required to initialize and use the core services. Most data providers, however, require an API key to access their data. Keys can be stored locally and they can also be securely saved to your OpenBB Hub ",(0,o.jsx)(n.a,{href:"https://my.openbb.co/app/hub",children:"account"})," for convenient remote access."]}),"\n",(0,o.jsx)(n.h3,{id:"openbb-hub",children:"OpenBB Hub"}),"\n",(0,o.jsx)(n.admonition,{type:"info",children:(0,o.jsxs)(n.p,{children:["The OpenBB Hub is only accessible via the Python Interface. For REST API, store credentials and preferences in the ",(0,o.jsx)(n.code,{children:"user_settings.json"})," file ",(0,o.jsx)(n.a,{href:"api_keys#local-environment",children:"local"})," to the deployment."]})}),"\n",(0,o.jsxs)(n.p,{children:["Data provider credentials and user preferences can be securely stored on the OpenBB Hub and accessed in Python using a revokable Personal Access Token (PAT). Login to the ",(0,o.jsx)(n.a,{href:"https://my.openbb.co/",children:"Hub"})," to manage this method of remote authorization."]}),"\n",(0,o.jsxs)(n.p,{children:["The OpenBB Hub is a convenient solution for accessing data in temporary Python environments, like Google Colab (",(0,o.jsx)(n.a,{href:"https://github.com/OpenBB-finance/OpenBBTerminal/blob/develop/examples/googleColab.ipynb",children:"example notebook"}),"). Login with:"]}),"\n",(0,o.jsx)(n.pre,{children:(0,o.jsx)(n.code,{className:"language-python",children:'from openbb import obb\n\n# Login with personal access token\nobb.account.login(pat="my_pat", remember_me=True)\n\n# Alternatively, login with email and password\nobb.account.login(email="my_email", password="my_password", remember_me=True)\n\n# Change a credential\nobb.user.credentials.polygon_api_key = "my_api_key"\n\n# Save account changes to the Hub\nobb.account.save()\n\n# Refresh account with latest changes\nobb.account.refresh()\n\n# Logout\nobb.account.logout()\n'})}),"\n",(0,o.jsxs)(n.p,{children:["Set ",(0,o.jsx)(n.code,{children:"remember_me"})," as ",(0,o.jsx)(n.code,{children:"False"})," to discard all credentials at the end of the session."]}),"\n",(0,o.jsx)(n.admonition,{type:"tip",children:(0,o.jsxs)(n.p,{children:["With ",(0,o.jsx)(n.code,{children:"remember_me=True"}),", credentials will be permanently stored in the environment.\nWrapping this sequence before deploying an API server is one (insecure) way to authorize data providers for remote access."]})}),"\n",(0,o.jsx)(n.h3,{id:"local-environment",children:"Local Environment"}),"\n",(0,o.jsxs)(n.p,{children:["Credentials and user preferences are stored locally, ",(0,o.jsx)(n.code,{children:"~/.openbb_platform/"}),", as a JSON file, ",(0,o.jsx)(n.code,{children:"user_settings.json"}),". It is read upon initializing the Python client, or when the Fast API is authorized. If the file does not exist, it will be created on the first run. The schema below can be copy/pasted as a template:"]}),"\n",(0,o.jsx)(n.pre,{children:(0,o.jsx)(n.code,{className:"language-json",children:'{\n  "credentials": {\n    "fmp_api_key": "REPLACE",\n    "polygon_api_key": "REPLACE",\n    "benzinga_api_key": "REPLACE",\n    "fred_api_key": "REPLACE",\n    "nasdaq_api_key": "REPLACE",\n    "intrinio_api_key": "REPLACE",\n    "alpha_vantage_api_key": "REPLACE",\n    "biztoc_api_key": "REPLACE",\n    "tradier_api_key": "REPLACE",\n    "tradier_account_type": "sandbox OR live",\n    "tradingeconomics_api_key": "REPLACE",\n    "tiingo_token": "REPLACE"\n}\n}\n'})}),"\n",(0,o.jsx)(n.p,{children:"To set keys from the Python client for the current session only, access the Credentials class:"}),"\n",(0,o.jsx)(n.pre,{children:(0,o.jsx)(n.code,{className:"language-python",children:'obb.user.credentials.intrinio_api_key = "my_api_key"\n'})})]})}function h(e={}){const{wrapper:n}={...(0,i.R)(),...e.components};return n?(0,o.jsx)(n,{...e,children:(0,o.jsx)(p,{...e})}):p(e)}},94331:(e,n,t)=>{t.d(n,{A:()=>a});t(96540);var o=t(5260),i=t(74848);function a(e){let{title:n}=e;return(0,i.jsx)(o.A,{children:(0,i.jsx)("title",{children:n})})}},28453:(e,n,t)=>{t.d(n,{R:()=>r,x:()=>s});var o=t(96540);const i={},a=o.createContext(i);function r(e){const n=o.useContext(a);return o.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function s(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(i):e.components||i:r(e.components),o.createElement(a.Provider,{value:n},e.children)}}}]);