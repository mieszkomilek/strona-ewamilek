from pathlib import Path
import json,re,sys

R=Path(__file__).resolve().parents[1]
c=json.loads((R/'site.config.json').read_text(encoding='utf-8'))
b=c['baseUrl']
E=[];W=[];titles={}

for n in c['indexablePages']:
    p=R/n
    if not p.exists():
        E.append(n+': brak pliku');continue
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
    if 'assets/js/site-shell.js' not in s:E.append(n+': brak wspólnego site-shell.js')
    if '<strong>Ewa Miłek</strong><small>Sztuka, która prowadzi do wnętrza</small>' not in s:
        W.append(n+': nagłówek brandingu nie został znormalizowany podczas builda')
    for img in re.findall(r'<img\b[^>]*>',s,re.I):
        if not re.search(r'\balt=',img,re.I):W.append(n+': obraz bez alt')

for n in c['privateOrPreviewPages']:
    p=R/n
    if p.exists() and 'noindex' not in p.read_text(encoding='utf-8').lower():W.append(n+': brak noindex')

# Access rules: all lightweight protected areas use YYYYMMDD.
offer=R/'oferta-2026.html'
if offer.exists():
    s=offer.read_text(encoding='utf-8')
    monthly="String(d.getFullYear())+String(d.getMonth()+1).padStart(2,'0')};"
    if monthly in s:E.append('oferta-2026.html: nadal używa YYYYMM zamiast YYYYMMDD')
    if 'maxlength="6"' in s:E.append('oferta-2026.html: pole hasła nadal ma 6 znaków')
    if 'assets/js/offer-admin-knowledge.js' not in s:E.append('oferta-2026.html: brak rozszerzenia oferty')

admin=R/'admin.html'
if admin.exists():
    s=admin.read_text(encoding='utf-8')
    if 'maxlength="8"' not in s:E.append('admin.html: pole hasła nie ma 8 znaków')
    if 'assets/js/offer-admin-knowledge.js' not in s:E.append('admin.html: brak rozszerzeń Admin')
    if 'assets/js/admin-offer-complete.js' not in s:E.append('admin.html: brak kontroli kompletności Admin')

# Both built pages must load the photo runtime and all original photos must exist.
for n in ('index.html', 'o-mnie.html'):
    s=(R/n).read_text(encoding='utf-8')
    if s.count(f'<script src="assets/js/photo-parallax.js?v={(R / "version.txt").read_text().strip()}"></script>') != 1:
        E.append(n+': wymagany dokładnie jeden skrypt photo-parallax.js')
photos=re.findall(r'src="(assets/photos/[^" ]+)"', (R/'assets/js/photo-parallax.js').read_text())
if len(set(photos)) != 8:
    E.append('photo-parallax.js: wymagane 8 zdjęć opublikowanych w galerii')
for photo in photos:
    p=R/photo
    if p.suffix != '.jpg' or not p.is_file() or not p.read_bytes().startswith(b'\xff\xd8\xff'):
        E.append(photo+': brak oryginalnego JPG')
if (R/'assets/photos/test-placeholder.txt').exists():
    E.append('pozostał przypadkowy plik testowy')

print('\n'.join('WARN '+x for x in W))
print('\n'.join('ERROR '+x for x in E))
print('errors',len(E),'warnings',len(W))
sys.exit(1 if E else 0)
