from pathlib import Path
import re
from bs4 import BeautifulSoup

PAGES=['index.html','vedic-art.html','mandala.html','anioly.html','numerologia.html','tworczosc.html','jedwab-malowany.html','o-mnie.html','kontakt.html','ebooki.html']
PRICE_RE=re.compile(r'\b\d[\d\s.,]*\s*(?:zł|PLN)\b',re.I)
PAYPAL='''<div class="paypal-inline" aria-label="Płatność PayPal"><form action="https://www.paypal.com/ncp/payment/7JL9X24RW64Q8" method="post" target="_blank" rel="noopener" class="paypal-inline-form"><input class="pp-inline-btn" type="submit" value="Zapłać przez PayPal"><img src="https://www.paypalobjects.com/images/Debit_Credit_APM.svg" alt="Obsługiwane karty płatnicze" loading="lazy"><small>Obsługiwane przez <img src="https://www.paypalobjects.com/paypal-ui/logos/svg/paypal-wordmark-color.svg" alt="PayPal"></small></form></div>'''

def has_price(tag):
    return bool(PRICE_RE.search(tag.get_text(' ',strip=True)))

def in_footer(tag):
    return tag.find_parent('footer') is not None

def already_paid(target):
    if target.select_one(':scope > .paypal-inline'):
        return True
    nxt=target.find_next_sibling()
    return bool(nxt and 'paypal-inline' in (nxt.get('class') or []))

def add_after(target,soup):
    if target is None or already_paid(target): return False
    frag=BeautifulSoup(PAYPAL,'html.parser').div
    target.insert_after(frag)
    return True

for name in PAGES:
    path=Path(name)
    soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
    targets=[]

    # Purpose-built price areas on the homepage and any future cards.
    for node in soup.select('.price-card,.card,.price-box,.banner-price'):
        if not in_footer(node) and has_price(node):
            targets.append(node)

    # Explicit price paragraphs and price lists on migrated subpages.
    for node in soup.select('main p, main li'):
        if in_footer(node) or not has_price(node):
            continue
        txt=node.get_text(' ',strip=True).lower()
        # Shipping-only information is not a separate service purchase.
        if ('wysyłk' in txt or 'przesyłk' in txt) and not ('cena' in txt or 'dodatkowo' in txt):
            if node.name=='li' and node.parent and has_price(node.parent):
                targets.append(node.parent)
            continue
        if node.name=='li' and node.parent:
            targets.append(node.parent)
        else:
            targets.append(node)

    # De-duplicate nested candidates: prefer service cards over their internal price node.
    unique=[]
    seen=set()
    for t in targets:
        if t is None: continue
        card=t.find_parent(class_='price-card') or t.find_parent(class_='card')
        if card and has_price(card): t=card
        key=id(t)
        if key not in seen:
            seen.add(key); unique.append(t)

    added=0
    for t in unique:
        if add_after(t,soup): added+=1
    path.write_text(str(soup),encoding='utf-8')
    print(name,added)

css=Path('styles.css').read_text(encoding='utf-8')
if '/* Inline PayPal near prices */' not in css:
    css += '''\n\n/* Inline PayPal near prices */\n.paypal-inline{margin:14px 0 24px;display:flex;justify-content:flex-start}.paypal-inline-form{display:inline-grid;justify-items:center;gap:.38rem}.pp-inline-btn{border:0;border-radius:999px;min-width:12.6rem;height:2.6rem;padding:0 1.5rem;background:linear-gradient(135deg,#FFD140,#f6bf33);color:#24192b;font:700 .92rem/1 "Helvetica Neue",Arial,sans-serif;cursor:pointer;box-shadow:0 9px 24px rgba(127,88,38,.12);transition:transform .2s ease,box-shadow .2s ease}.pp-inline-btn:hover{transform:translateY(-2px);box-shadow:0 13px 28px rgba(127,88,38,.18)}.paypal-inline-form>img{width:min(235px,68vw);height:auto}.paypal-inline-form small{color:var(--muted);font-size:.68rem}.paypal-inline-form small img{height:.76rem;width:auto;vertical-align:middle}.dark .paypal-inline-form small{color:rgba(255,255,255,.68)}.price-card>.paypal-inline,.card>.paypal-inline{margin-top:18px;margin-bottom:0}.price-card>.paypal-inline+.paypal-inline,.card>.paypal-inline+.paypal-inline{display:none}@media(max-width:560px){.paypal-inline{justify-content:stretch}.paypal-inline-form{width:100%}.pp-inline-btn{width:100%}}\n'''
    Path('styles.css').write_text(css,encoding='utf-8')
