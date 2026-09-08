from pathlib import Path
import json,re
from datetime import date
R=Path(__file__).resolve().parents[1]; c=json.loads((R/'site.config.json').read_text(encoding='utf-8')); base=c['baseUrl']
def url(n): return base if n=='index.html' else base+n
for p in R.glob('*.html'):
    s=p.read_text(encoding='utf-8').replace('https://mieszkomilek.github.io/strona-ewamilek/',base)
    if 'manifest.webmanifest' not in s:s=s.replace('</head>','<link href="manifest.webmanifest" rel="manifest"/>\n</head>',1)
    if p.name in ('admin.html','oferta-2026.html'):
        if 'assets/js/offer-admin-knowledge.js' not in s:
            s=s.replace('</body>','<script src="assets/js/offer-admin-knowledge.js"></script>\n</body>',1)
        if 'assets/js/admin-offer-complete.js' not in s:
            s=s.replace('</body>','<script src="assets/js/admin-offer-complete.js"></script>\n</body>',1)
    if p.name in c['indexablePages']:
        u=url(p.name)
        s=re.sub(r'<link\s+href="[^"]*"\s+rel="canonical"\s*/?>',f'<link href="{u}" rel="canonical"/>',s,count=1)
        s=re.sub(r'<meta\s+content="[^"]*"\s+property="og:url"\s*/?>',f'<meta content="{u}" property="og:url"/>',s,count=1)
        if p.name!='index.html' and u+'#breadcrumb' not in s:
            h=re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S); label=re.sub('<[^>]+>','',h.group(1)).strip() if h else p.stem
            j=json.dumps({'@context':'https://schema.org','@type':'BreadcrumbList','@id':u+'#breadcrumb','itemListElement':[{'@type':'ListItem','position':1,'name':'EwaMiłek','item':base},{'@type':'ListItem','position':2,'name':label,'item':u}]},ensure_ascii=False,separators=(',',':'))
            s=s.replace('</head>',f'<script type="application/ld+json">{j}</script>\n</head>',1)
    p.write_text(s,encoding='utf-8')
(R/'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {base}sitemap.xml\n',encoding='utf-8')
d=date.today().isoformat(); rows='\n'.join(f'  <url>\n    <loc>{url(n)}</loc>\n    <lastmod>{d}</lastmod>\n  </url>' for n in c['indexablePages'] if (R/n).exists())
(R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+rows+'\n</urlset>\n',encoding='utf-8')
