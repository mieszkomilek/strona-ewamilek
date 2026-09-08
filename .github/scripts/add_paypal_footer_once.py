from pathlib import Path
import re

pages=['index.html','vedic-art.html','mandala.html','anioly.html','numerologia.html','tworczosc.html','jedwab-malowany.html','o-mnie.html','kontakt.html','ebooki.html']
block='''<div class="footer-payment" aria-label="Płatność PayPal"><p class="footer-payment-label">Płatność online</p><form action="https://www.paypal.com/ncp/payment/7JL9X24RW64Q8" method="post" target="_blank" rel="noopener" class="paypal-form"><input class="pp-7JL9X24RW64Q8" type="submit" value="Zapłać przez PayPal"><img src="https://www.paypalobjects.com/images/Debit_Credit_APM.svg" alt="Obsługiwane karty płatnicze" loading="lazy"><section>Obsługiwane przez <img src="https://www.paypalobjects.com/paypal-ui/logos/svg/paypal-wordmark-color.svg" alt="PayPal"></section></form></div>'''
for name in pages:
    p=Path(name)
    s=p.read_text(encoding='utf-8')
    if 'class="footer-payment"' in s: continue
    s,n=re.subn(r'(<div class="footer-bottom">[\s\S]*?</div>)(</div></footer>)',r'\1'+block+r'\2',s,count=1)
    if n!=1: raise RuntimeError(f'Footer pattern not found in {name}')
    p.write_text(s,encoding='utf-8')

css=Path('styles.css').read_text(encoding='utf-8')
if '/* PayPal footer payment */' not in css:
    css += '''\n\n/* PayPal footer payment */\n.footer-payment{position:relative;z-index:2;margin-top:26px;padding-top:26px;border-top:1px solid rgba(100,67,123,.12);display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center}.footer-payment-label{margin:0;color:#6d5677;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.16em}.paypal-form{display:inline-grid;justify-items:center;align-content:start;gap:.5rem}.pp-7JL9X24RW64Q8{text-align:center;border:0;border-radius:999px;min-width:13rem;padding:0 2rem;height:2.75rem;font-weight:700;background:linear-gradient(135deg,#FFD140,#f6bf33);color:#261b2e;font-family:"Helvetica Neue",Arial,sans-serif;font-size:1rem;line-height:1.25rem;cursor:pointer;box-shadow:0 10px 26px rgba(127,88,38,.12);transition:transform .2s ease,box-shadow .2s ease}.pp-7JL9X24RW64Q8:hover{transform:translateY(-2px);box-shadow:0 14px 30px rgba(127,88,38,.18)}.paypal-form>img{width:min(310px,78vw);height:auto}.paypal-form section{font-size:.75rem;color:#74657b}.paypal-form section img{height:.875rem;vertical-align:middle;width:auto}\n'''
    Path('styles.css').write_text(css,encoding='utf-8')
