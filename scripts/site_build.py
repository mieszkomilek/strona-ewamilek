from pathlib import Path
import json,re
from datetime import date

R=Path(__file__).resolve().parents[1]
c=json.loads((R/'site.config.json').read_text(encoding='utf-8'))
base=c['baseUrl']
BRAND_NAME='Ewa Miłek'
BRAND_TAGLINE='Sztuka, która prowadzi do wnętrza'

def url(n):
    return base if n=='index.html' else base+n

def ensure_script(s,src):
    marker=f'<script src="{src}"></script>'
    if marker not in s:
        s=s.replace('</body>',marker+'\n</body>',1)
    return s

for p in R.glob('*.html'):
    s=p.read_text(encoding='utf-8').replace('https://mieszkomilek.github.io/strona-ewamilek/',base)

    if 'manifest.webmanifest' not in s:
        s=s.replace('</head>','<link href="manifest.webmanifest" rel="manifest"/>\n</head>',1)

    # Shared public identity. The visual shell also enforces this at runtime,
    # but build-time normalization keeps deployed HTML and crawlers consistent.
    s=re.sub(
        r'<span><strong>EwaMiłek</strong><small>moja autorska strona internetowa</small></span>',
        f'<span><strong>{BRAND_NAME}</strong><small>{BRAND_TAGLINE}</small></span>',
        s
    )
    s=re.sub(
        r'<span><strong>Ewa Miłek</strong><small>moja autorska strona internetowa</small></span>',
        f'<span><strong>{BRAND_NAME}</strong><small>{BRAND_TAGLINE}</small></span>',
        s
    )

    # Common artistic header + shared YYYYMMDD access helper on every page.
    s=ensure_script(s,'assets/js/site-shell.js')

    # Admin and Oferta 2026 receive their specialist modules and knowledge links.
    if p.name in ('admin.html','oferta-2026.html'):
        s=ensure_script(s,'assets/js/offer-admin-knowledge.js')
        s=ensure_script(s,'assets/js/admin-offer-complete.js')

    # Oferta 2026 historically used YYYYMM. Normalize the deployed source to
    # YYYYMMDD as well; site-shell.js also guards submission at runtime.
    if p.name=='oferta-2026.html':
        s=s.replace("const pass=()=>{const d=new Date();return String(d.getFullYear())+String(d.getMonth()+1).padStart(2,'0')};",
                    "const pass=()=>{const d=new Date();return String(d.getFullYear())+String(d.getMonth()+1).padStart(2,'0')+String(d.getDate()).padStart(2,'0')};")
        s=s.replace('maxlength="6" placeholder="••••••"','maxlength="8" placeholder="••••••••"')

    if p.name in c['indexablePages']:
        u=url(p.name)
        s=re.sub(r'<link\s+href="[^"]*"\s+rel="canonical"\s*/?>',f'<link href="{u}" rel="canonical"/>',s,count=1)
        s=re.sub(r'<meta\s+content="[^"]*"\s+property="og:url"\s*/?>',f'<meta content="{u}" property="og:url"/>',s,count=1)
        if p.name!='index.html' and u+'#breadcrumb' not in s:
            h=re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S)
            label=re.sub('<[^>]+>','',h.group(1)).strip() if h else p.stem
            j=json.dumps({
                '@context':'https://schema.org','@type':'BreadcrumbList','@id':u+'#breadcrumb',
                'itemListElement':[
                    {'@type':'ListItem','position':1,'name':BRAND_NAME,'item':base},
                    {'@type':'ListItem','position':2,'name':label,'item':u}
                ]
            },ensure_ascii=False,separators=(',',':'))
            s=s.replace('</head>',f'<script type="application/ld+json">{j}</script>\n</head>',1)

    p.write_text(s,encoding='utf-8')

(R/'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {base}sitemap.xml\n',encoding='utf-8')
d=date.today().isoformat()
rows='\n'.join(f'  <url>\n    <loc>{url(n)}</loc>\n    <lastmod>{d}</lastmod>\n  </url>' for n in c['indexablePages'] if (R/n).exists())
(R/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+rows+'\n</urlset>\n',encoding='utf-8')
