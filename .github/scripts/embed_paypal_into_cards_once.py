from pathlib import Path
from bs4 import BeautifulSoup

PAGES=['index.html','vedic-art.html','mandala.html','anioly.html','numerologia.html','tworczosc.html','jedwab-malowany.html','o-mnie.html','kontakt.html','ebooki.html']

for name in PAGES:
    p=Path(name)
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    moved=0

    for pay in list(soup.select('main .paypal-inline')):
        # 1) Homepage / product grids: payment block sits directly after a card.
        prev=pay.find_previous_sibling()
        if prev and prev.name in ('article','div') and any(c in (prev.get('class') or []) for c in ('card','price-card','price-box')):
            prev.append(pay.extract())
            moved+=1
            continue

        # 2) If payment belongs to content inside a nearby card, move it into that card.
        prev_el=pay.find_previous()
        card=prev_el.find_parent(class_='price-card') if prev_el else None
        if not card and prev_el:
            card=prev_el.find_parent(class_='card')
        if card:
            card.append(pay.extract())
            moved+=1
            continue

        # 3) Long-form service sections: group previous price/list content and payment visually.
        prev=pay.find_previous_sibling()
        if prev and prev.name in ('p','ul','ol','div'):
            wrap=soup.new_tag('div',attrs={'class':'service-payment-block'})
            prev.insert_before(wrap)
            wrap.append(prev.extract())
            wrap.append(pay.extract())
            moved+=1

    p.write_text(str(soup),encoding='utf-8')
    print(name,'moved',moved)

css=Path('styles.css').read_text(encoding='utf-8')
marker='/* Integrated PayPal product cards */'
if marker not in css:
    css += '''\n\n/* Integrated PayPal product cards */\n.cards>.paypal-inline{display:none!important}\n.card,.price-card{display:flex;flex-direction:column}\n.card>.paypal-inline,.price-card>.paypal-inline{display:flex!important;margin:20px 0 0!important;padding-top:18px;border-top:1px solid rgba(105,72,176,.10);justify-content:center}\n.card>.paypal-inline .paypal-inline-form,.price-card>.paypal-inline .paypal-inline-form{width:100%;max-width:270px}\n.card>.paypal-inline .pp-inline-btn,.price-card>.paypal-inline .pp-inline-btn{width:100%;min-width:0}\n.card>.paypal-inline .paypal-inline-form>img,.price-card>.paypal-inline .paypal-inline-form>img{width:min(190px,80%)}\n.card>.paypal-inline small,.price-card>.paypal-inline small{font-size:.62rem}\n.service-payment-block{margin:20px 0 28px;padding:18px;border:1px solid rgba(105,72,176,.10);border-radius:18px;background:linear-gradient(145deg,rgba(255,255,255,.74),rgba(249,242,251,.70));box-shadow:0 12px 36px rgba(77,50,107,.06)}\n.service-payment-block>.paypal-inline{margin:14px 0 0!important;padding-top:14px;border-top:1px solid rgba(105,72,176,.09)}\n@media(max-width:760px){.card>.paypal-inline,.price-card>.paypal-inline{justify-content:stretch}.card>.paypal-inline .paypal-inline-form,.price-card>.paypal-inline .paypal-inline-form{max-width:none}}\n'''
    Path('styles.css').write_text(css,encoding='utf-8')
