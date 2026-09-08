from pathlib import Path
import json,re,sys
R=Path(__file__).resolve().parents[1]; c=json.loads((R/'site.config.json').read_text(encoding='utf-8')); b=c['baseUrl']; E=[]; W=[]; titles={}
for n in c['indexablePages']:
    p=R/n
    if not p.exists():E.append(n+': brak pliku');continue
    s=p.read_text(encoding='utf-8');u=b if n=='index.html' else b+n
    if 'mieszkomilek.github.io/strona-ewamilek' in s:E.append(n+': stara domena')
    if f'href="{u}" rel="canonical"' not in s:E.append(n+': canonical')
    if len(re.findall(r'<h1\b',s,re.I))!=1:E.append(n+': H1')
    m=re.search(r'<title>(.*?)</title>',s,re.S)
    if not m:E.append(n+': title')
    else:
        t=re.sub(r'\s+',' ',m.group(1)).strip()
        if t in titles:W.append(n+': duplikat title z '+titles[t])
        titles[t]=n
    if 'name="description"' not in s:E.append(n+': description')
    if 'manifest.webmanifest' not in s:E.append(n+': manifest')
    for img in re.findall(r'<img\b[^>]*>',s,re.I):
        if not re.search(r'\balt=',img,re.I):W.append(n+': obraz bez alt')
for n in c['privateOrPreviewPages']:
    p=R/n
    if p.exists() and 'noindex' not in p.read_text(encoding='utf-8').lower():W.append(n+': brak noindex')
print('\n'.join('WARN '+x for x in W));print('\n'.join('ERROR '+x for x in E));print('errors',len(E),'warnings',len(W));sys.exit(1 if E else 0)
