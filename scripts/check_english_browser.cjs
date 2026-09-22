const fs=require('fs');const {chromium}=require('playwright');
const root=require('path').resolve(__dirname,'..');
const base=process.env.PREVIEW_URL||'http://127.0.0.1:8767';
(async()=>{const b=await chromium.launch({headless:true,...(process.env.CHROME_EXECUTABLE?{executablePath:process.env.CHROME_EXECUTABLE}:{})});const context=await b.newContext();const all=new Set();const report=[];
for(const file of fs.readdirSync(root+'/en').filter(x=>x.endsWith('.html'))){const p=await context.newPage();const errors=[];p.on('pageerror',e=>errors.push(e.message));p.on('response',r=>{if(r.status()>=400&&r.url().includes('127.0.0.1'))errors.push(r.status()+' '+r.url())});await p.goto(base+'/en/'+file);await p.waitForTimeout(1200);const strings=await p.evaluate(()=>{const a=[];const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);while(w.nextNode()){const n=w.currentNode;if(!n.parentElement.closest('script,style,textarea'))a.push(n.data.replace(/\s+/g,' ').trim())}document.querySelectorAll('[alt],[title],[aria-label],[placeholder]').forEach(e=>['alt','title','aria-label','placeholder'].forEach(k=>{if(e.getAttribute(k))a.push(e.getAttribute(k))}));return a.filter(Boolean)});strings.forEach(s=>all.add(s));report.push({file,errors});await p.close()}
const dictionary=JSON.parse(fs.readFileSync(root+'/data/i18n/en.json','utf8'));
const untranslated=[...all].filter(text=>dictionary[text] && dictionary[text]!==text);
if(untranslated.length)throw new Error('Untranslated UI: '+untranslated.join(' | '));
if(report.some(r=>r.errors.length))throw new Error(JSON.stringify(report));
fs.writeFileSync('/tmp/ewa-rendered.json',JSON.stringify([...all],null,2));fs.writeFileSync('/tmp/ewa-browser-report.json',JSON.stringify(report,null,2));await b.close();console.log(JSON.stringify(report));})()
