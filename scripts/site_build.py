from pathlib import Path
import json,re
from datetime import date

R=Path(__file__).resolve().parents[1]
c=json.loads((R/'site.config.json').read_text(encoding='utf-8'))
base=c['baseUrl']
VERSION=(R/'version.txt').read_text().strip()
BRAND_NAME='Ewa Miłek'
BRAND_TAGLINE='Sztuka, która prowadzi do wnętrza'

def url(n):
    return base if n=='index.html' else base+n

def ensure_script(s,src):
    marker=f'<script src="{src}"></script>'
    if marker not in s:
        s=s.replace('</body>',marker+'\n</body>',1)
    return s

def ensure_css(s,href):
    marker=f'<link href="{href}" rel="stylesheet"/>'
    if marker not in s:
        s=s.replace('</head>',marker+'\n</head>',1)
    return s

for p in R.glob('*.html'):
    s=p.read_text(encoding='utf-8').replace('https://mieszkomilek.github.io/strona-ewamilek/',base)

    for part in ('header', 'footer'):
        markup=(R/'templates'/f'{part}.html').read_text()
        s=s.replace(f'<!-- site:{part} -->',markup)
        s=re.sub(rf'<{part}\b.*?</{part}>',lambda m: markup,s,flags=re.S)
    s=re.sub(r'<a class="skip-link"[^>]*>.*?</a>','',s,count=1)
    s=re.sub(r'(<body\b[^>]*>)',r'\1<a class="skip-link" href="#main-content">Przejdź do treści</a>',s,count=1)
    s=re.sub(r'<main\b(?![^>]*\bid=)', '<main id="main-content"', s, count=1)
    for module, marker in (('numerology.js','id="wibracja-imienia-nazwiska"'),('ebooks.js','id="ebook-open"')):
        if marker not in s:
            s=re.sub(r'<script src="assets/js/'+re.escape(module)+r'(?:\?[^" ]*)?"></script>','',s)
    s=ensure_css(s,'assets/css/navigation.css')

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

    # Common shell and layout guard. photo-parallax.css also prevents any page
    # from becoming horizontally draggable because of decorative/off-canvas UI.
    s=re.sub(r'<link\s+href="assets/css/photo-parallax\.css(?:\?[^"]*)?"\s+rel="stylesheet"\s*/?>','',s)
    s=ensure_css(s,f'assets/css/photo-parallax.css?v={VERSION}')
    s=ensure_script(s,'assets/js/site-shell.js')

    # Photo storytelling is only needed on the homepage and O mnie.
    if p.name in ('index.html','o-mnie.html'):
        s=re.sub(r'<script src="assets/js/photo-parallax\.js(?:\?[^"]*)?"></script>','',s)
        s=ensure_script(s,f'assets/js/photo-parallax.js?v={VERSION}')

    if p.name=='tworczosc.html':
        s=ensure_css(s,'assets/css/art-gallery-controls.css')
        s=re.sub(r'<script type="application/ld\+json" data-gallery-schema>.*?</script>','',s,flags=re.S)
        images=[]
        for tag in re.findall(r'<img\b[^>]+>',s,re.I):
            src=re.search(r'\bsrc="(facebook-zdjecia-galeria-sztuki-ewa-milek/[^"]+)"',tag)
            alt=re.search(r'\balt="([^"]+)"',tag)
            if src:
                images.append({'@type':'ImageObject','contentUrl':base+src.group(1),'caption':alt.group(1) if alt else BRAND_NAME})
        schema=json.dumps({'@context':'https://schema.org','@type':'ImageGallery','name':'Twórczość Ewy Miłek','url':url(p.name),'image':images},ensure_ascii=False,separators=(',',':'))
        s=s.replace('</head>',f'<script type="application/ld+json" data-gallery-schema>{schema}</script>\n</head>',1)

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
