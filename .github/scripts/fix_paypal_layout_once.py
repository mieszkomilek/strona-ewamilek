from pathlib import Path
from bs4 import BeautifulSoup

PAGES=['index.html','mandala.html','anioly.html','numerologia.html','jedwab-malowany.html']

for name in PAGES:
    p=Path(name)
    soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    moved=0
    # Move any PayPal block that was inserted immediately after a visual service card
    # back inside that card so CSS grid treats it as one item.
    for pay in list(soup.select('.paypal-inline')):
        prev=pay.find_previous_sibling()
        if prev and any(c in (prev.get('class') or []) for c in ['card','price-card','price-box','banner-price']):
            prev.append(pay.extract())
            moved+=1
    p.write_text(str(soup),encoding='utf-8')
    print(name,moved)

css=Path('styles.css').read_text(encoding='utf-8')
if '/* PayPal card layout correction */' not in css:
    css += '''\n\n/* PayPal card layout correction */\n.card,.price-card{position:relative}.card>.paypal-inline,.price-card>.paypal-inline{margin-top:18px;margin-bottom:0;display:flex;justify-content:flex-start}.card>.paypal-inline .paypal-inline-form,.price-card>.paypal-inline .paypal-inline-form{width:100%;justify-items:stretch}.card>.paypal-inline .pp-inline-btn,.price-card>.paypal-inline .pp-inline-btn{width:100%}.card>.paypal-inline .paypal-inline-form>img,.price-card>.paypal-inline .paypal-inline-form>img{width:min(220px,100%);justify-self:center}.card>.paypal-inline small,.price-card>.paypal-inline small{text-align:center}.cards>.paypal-inline{display:none!important}@media(max-width:760px){.card>.paypal-inline,.price-card>.paypal-inline{margin-top:16px}}\n'''
    Path('styles.css').write_text(css,encoding='utf-8')
