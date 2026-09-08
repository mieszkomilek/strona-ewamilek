from pathlib import Path
import re, json

BASE='https://mieszkomilek.github.io/strona-ewamilek/'
PAGES={
'index.html':('Ewa Miłek | Mandale, Vedic Art, Numerologia i sztuka intuicyjna','Autorska przestrzeń Ewy Miłek: mandale osobiste, Anioły Opiekuńcze, warsztaty Vedic Art, numerologia i ręcznie malowany jedwab.','index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'),
'vedic-art.html':('Vedic Art - warsztaty i malowanie intuicyjne | Ewa Miłek','Warsztaty Vedic Art z Ewą Miłek: 17 zasad, malowanie intuicyjne, I i II stopień oraz twórczy proces bez oceniania.','index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'),
'mandala.html':('Mandale osobiste i partnerskie na zamówienie | Ewa Miłek','Autorskie mandale Ewy Miłek: osobiste, partnerskie, ślubne i intencjonalne oraz warsztaty tworzenia mandali.','index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'),
'anioly.html':('Anioł Opiekuńczy - obraz na zamówienie | Ewa Miłek','Indywidualny obraz Anioła Opiekuńczego autorstwa Ewy Miłek, malowany na zamówienie wraz z osobistym opisem.','index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'),
'numerologia.html':('Numerologia i Portret Numerologiczny | Ewa Miłek','Portret numerologiczny Ewy Miłek: Droga Życia, talenty, cykle, wyzwania i autorskie narzędzie do obliczania wibracji imienia i nazwiska.','index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'),
'tworczosc.html':('Twórczość Ewy Miłek | Obrazy i sztuka intuicyjna','Twórczość i autorskie prace Ewy Miłek. Strona w przygotowaniu.','noindex,follow'),
'jedwab-malowany.html':('Malowanie na jedwabiu - kurs i ręcznie malowany jedwab | Ewa Miłek','Kameralny kurs malowania na naturalnym jedwabiu z Ewą Miłek. Poznaj techniki i stwórz własny ręcznie malowany szal.','index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'),
'o-mnie.html':('O mnie - Ewa Miłek | artystka, Vedic Art i numerologia','Poznaj Ewę Miłek: artystkę, nauczycielkę Vedic Art i numerolog. Twórczość, rozwój wewnętrzny, mandale, Anioły i malowanie intuicyjne.','index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'),
'kontakt.html':('Kontakt | Ewa Miłek','Skontaktuj się z Ewą Miłek w sprawie mandali, Aniołów Opiekuńczych, numerologii, Vedic Art, jedwabiu i warsztatów.','index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'),
'ebooki.html':('E-booki o numerologii | Ewa Miłek','E-booki Ewy Miłek. Kurs z Numerologii: praktyczne wskazówki dotyczące Drogi Życia i symboliki liczb.','index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'),
}

HEADER='''<header class="site-header" id="top"><div class="nav-wrap container"><a class="brand" href="index.html"><span class="brand-mark">✦</span><span><strong>EwaMiłek</strong><small>moja autorska strona internetowa</small></span></a><button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Otwórz menu i działy"><span class="menu-icon" aria-hidden="true"><i></i><i></i><i></i></span><span class="menu-label">Menu / Działy</span></button><nav id="menu" class="nav-links" aria-label="Główna nawigacja"><a href="vedic-art.html">Vedic Art</a><a href="mandala.html">Mandala</a><a href="anioly.html">Anioły</a><a href="numerologia.html">Numerologia</a><a href="tworczosc.html">Twórczość</a><a href="jedwab-malowany.html">Jedwab Malowany</a><a href="o-mnie.html">O mnie</a><a href="ebooki.html">E-booki</a><a href="kontakt.html" class="nav-cta">Kontakt</a></nav></div></header>'''

def canonical(name): return BASE if name=='index.html' else BASE+name

def head(name,title,desc,robots):
    url=canonical(name)
    image=BASE+('assets/aniol-opiekunczy.jpg' if name=='anioly.html' else 'assets/ewa-milek-vedic-art.jpg')
    graph=[
      {'@type':'WebSite','@id':BASE+'#website','url':BASE,'name':'EwaMiłek','alternateName':'Ewa Miłek','inLanguage':'pl-PL'},
      {'@type':'Person','@id':BASE+'#ewa-milek','name':'Ewa Miłek','url':BASE+'o-mnie.html','email':'mailto:milekewa@o2.pl','sameAs':['https://www.facebook.com/milekewa','https://www.instagram.com/ewamilek.art']},
      {'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':desc,'inLanguage':'pl-PL','isPartOf':{'@id':BASE+'#website'},'about':{'@id':BASE+'#ewa-milek'}}
    ]
    schema=json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False,separators=(',',':'))
    preload='\n  <link rel="preload" as="image" href="assets/ewa-milek-vedic-art.jpg" fetchpriority="high">' if name=='index.html' else ''
    return f'''<head>\n  <meta charset="utf-8">\n  <meta name="viewport" content="width=device-width,initial-scale=1">\n  <title>{title}</title>\n  <meta name="description" content="{desc}">\n  <meta name="robots" content="{robots}">\n  <meta name="author" content="Ewa Miłek">\n  <meta name="theme-color" content="#f8e9ef">\n  <link rel="canonical" href="{url}">\n  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">{preload}\n  <meta property="og:locale" content="pl_PL">\n  <meta property="og:type" content="website">\n  <meta property="og:site_name" content="EwaMiłek">\n  <meta property="og:title" content="{title}">\n  <meta property="og:description" content="{desc}">\n  <meta property="og:url" content="{url}">\n  <meta property="og:image" content="{image}">\n  <meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:title" content="{title}">\n  <meta name="twitter:description" content="{desc}">\n  <meta name="twitter:image" content="{image}">\n  <script type="application/ld+json">{schema}</script>\n  <link rel="stylesheet" href="styles.css">\n</head>'''

for name,(title,desc,robots) in PAGES.items():
    p=Path(name)
    s=p.read_text(encoding='utf-8')
    s=re.sub(r'<head>[\s\S]*?</head>',head(name,title,desc,robots),s,count=1,flags=re.I)
    s=re.sub(r'<header\b[\s\S]*?</header>',HEADER,s,count=1,flags=re.I)
    p.write_text(s,encoding='utf-8')

# Sitemap: only indexable HTML pages.
urls=[]
for name,(title,desc,robots) in PAGES.items():
    if robots.startswith('noindex'): continue
    urls.append(canonical(name))
xml=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    xml += ['  <url>',f'    <loc>{u}</loc>','    <lastmod>2026-09-08</lastmod>','  </url>']
xml.append('</urlset>')
Path('sitemap.xml').write_text('\n'.join(xml)+'\n',encoding='utf-8')

# Always-on hamburger / off-canvas menu.
css=Path('styles.css').read_text(encoding='utf-8')
css += r'''

/* ===== Always-on Menu / Działy drawer ===== */
.menu-btn{display:inline-flex!important;align-items:center;gap:10px;min-height:44px;padding:9px 14px!important;border:1px solid rgba(101,65,184,.18)!important;border-radius:999px;background:rgba(255,255,255,.72)!important;color:#4e367e!important;font:700 .82rem/1 DVSans,system-ui,sans-serif;cursor:pointer;z-index:111;position:relative}
.menu-icon{width:20px;height:16px;display:flex;flex-direction:column;justify-content:space-between}.menu-icon i{display:block;width:100%;height:2px;border-radius:4px;background:currentColor;transition:transform .25s ease,opacity .2s ease}.menu-btn[aria-expanded="true"] .menu-icon i:nth-child(1){transform:translateY(7px) rotate(45deg)}.menu-btn[aria-expanded="true"] .menu-icon i:nth-child(2){opacity:0}.menu-btn[aria-expanded="true"] .menu-icon i:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.nav-links{position:fixed!important;z-index:109!important;top:0!important;right:0!important;bottom:0!important;width:min(420px,90vw)!important;height:100dvh!important;padding:108px 34px 38px!important;display:flex!important;flex-direction:column!important;align-items:stretch!important;justify-content:flex-start!important;gap:4px!important;background:linear-gradient(155deg,rgba(255,250,253,.98),rgba(246,239,253,.98))!important;border-left:1px solid rgba(105,72,176,.12)!important;box-shadow:-30px 0 90px rgba(54,31,78,.18)!important;transform:translate3d(105%,0,0)!important;opacity:0!important;pointer-events:none!important;transition:transform .32s cubic-bezier(.2,.8,.2,1),opacity .25s ease!important;overflow:auto!important;white-space:normal!important}
.nav-links.open{transform:translate3d(0,0,0)!important;opacity:1!important;pointer-events:auto!important}.nav-links a{font-family:Fraunces,Georgia,serif!important;font-size:clamp(1.35rem,3vw,1.85rem)!important;font-weight:600!important;padding:13px 4px!important;border-bottom:1px solid rgba(105,72,176,.08)!important;color:#342445!important;transform:none!important}.nav-links a:after{display:none!important}.nav-links .nav-cta{margin-top:12px!important;text-align:center!important;font-family:system-ui,sans-serif!important;font-size:1rem!important;border:0!important;padding:14px 18px!important}
body.menu-open{overflow:hidden}body.menu-open:before{content:"";position:fixed;z-index:108;inset:0;background:rgba(40,25,52,.28);backdrop-filter:blur(5px);-webkit-backdrop-filter:blur(5px)}
@media(max-width:560px){.menu-label{font-size:.76rem}.menu-btn{padding:9px 11px!important}.nav-links{width:94vw!important;padding-left:26px!important;padding-right:26px!important}}
'''
Path('styles.css').write_text(css,encoding='utf-8')

js=Path('script.js').read_text(encoding='utf-8')
old=re.compile(r"const btn=document\.querySelector\('\.menu-btn,\.menu-toggle'\);[\s\S]*?if\(year\)year\.textContent=new Date\(\)\.getFullYear\(\);",re.M)
new="""const btn=document.querySelector('.menu-btn');const menu=document.querySelector('#menu');const closeMenu=()=>{menu?.classList.remove('open');btn?.setAttribute('aria-expanded','false');document.body.classList.remove('menu-open')};btn?.addEventListener('click',()=>{const open=!menu?.classList.contains('open');menu?.classList.toggle('open',open);btn.setAttribute('aria-expanded',String(open));document.body.classList.toggle('menu-open',open)});menu?.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));document.addEventListener('click',e=>{if(document.body.classList.contains('menu-open')&&!e.target.closest('#menu')&&!e.target.closest('.menu-btn'))closeMenu()});document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu()});const year=document.querySelector('#year');if(year)year.textContent=new Date().getFullYear();"""
if old.search(js): js=old.sub(new,js,count=1)
else: js=new+'\n'+js
Path('script.js').write_text(js,encoding='utf-8')
