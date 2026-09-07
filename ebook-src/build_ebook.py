import re, html
from pathlib import Path
src=''.join(Path(f'ebook-src/kurs-numerologii-source-0{i}.txt').read_text(encoding='utf-8') for i in range(1,5))
pages=src.split('\f')
def clean_page(t):
    out=[x.rstrip() for x in t.splitlines() if not re.fullmatch(r'\s*\d{1,2}\s*',x)]
    while out and not out[0].strip():out.pop(0)
    while out and not out[-1].strip():out.pop()
    return '\n'.join(out)
pages=[clean_page(p) for p in pages if clean_page(p)]
butterfly='''<svg class="butterfly deco" viewBox="0 0 100 70"><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6f4bc2"/><stop offset=".55" stop-color="#c173b5"/><stop offset="1" stop-color="#e6a0c5"/></linearGradient></defs><ellipse cx="31" cy="26" rx="25" ry="18" transform="rotate(-22 31 26)" fill="url(#bg)" opacity=".82"/><ellipse cx="69" cy="26" rx="25" ry="18" transform="rotate(22 69 26)" fill="url(#bg)" opacity=".72"/><ellipse cx="35" cy="48" rx="16" ry="12" transform="rotate(20 35 48)" fill="#d889b7" opacity=".62"/><ellipse cx="65" cy="48" rx="16" ry="12" transform="rotate(-20 65 48)" fill="#8b70d6" opacity=".62"/><rect x="47" y="17" width="6" height="40" rx="3" fill="#4a365f"/></svg>'''
flower='''<svg class="flower deco" viewBox="0 0 100 100"><g transform="translate(50 50)"><circle r="10" fill="#6f4bc2"/><g fill="#d889b7" opacity=".65"><ellipse cy="-26" ry="23" rx="12"/><ellipse cy="26" ry="23" rx="12"/><ellipse cx="-26" ry="12" rx="23"/><ellipse cx="26" ry="12" rx="23"/><ellipse transform="rotate(45)" cy="-26" ry="20" rx="10"/><ellipse transform="rotate(135)" cy="-26" ry="20" rx="10"/></g></g></svg>'''
heads=[r'^1\.Kilka słów o mnie$',r'^1\.1\.',r'^2\.Historia',r'^3\. O Numerologii$',r'^3\.1\.',r'^4\.Jak obliczyć',r'^4\.1\.',r'^4\.2\.',r'^Ciekawostki$',r'^Ważne Liczby',r'^MISTRZOSTWO \d+$',r'^KARMICZNA \d+$',r'^Inne ważne',r'^Portret Numerologiczny$']
def esc(s):return html.escape(s)
def format_page(t,i):
    if i==0:return '<div class="cover"><div class="kicker">EWA MIŁEK • NUMEROLOGIA</div><h1>Kurs z<br><em>Numerologii</em></h1><p>Praktyczne wskazówki, jak odczytywać datę urodzenia.</p><div class="author">Ewa Miłek</div></div>'
    if i==1:return '<div class="intro"><div class="kicker">WITAJ</div><h2>Witaj…</h2><p class="big">Dziękuję za zakup mojego ebooka.<br>Cieszę się, że to właśnie Ty chcesz poznać tajniki numerologii.</p><p class="big">Poprowadzę Cię teraz po zakamarkach numerologii.</p><div class="copyright">C O P Y R I G H T © EWA MIŁEK 2 0 2 1<br>Autor: Ewa Miłek<br>Zdjęcia: Ewa Miłek<br>Redakcja i korekta: Mieszko Miłek</div></div>'
    out=[];para=[]
    def flush():
      nonlocal para
      if para:
       x=' '.join(y.strip() for y in para if y.strip())
       if x:out.append('<p>'+esc(x)+'</p>')
       para=[]
    for line in t.splitlines():
      s=line.strip()
      if not s:flush();continue
      if i==2 and s.startswith('Spis Treści'):flush();out+=['<div class="kicker">SPIS TREŚCI</div><h2>Spis treści</h2>'];continue
      if any(re.match(x,s,re.I) for x in heads):flush();out.append('<h2>'+esc(s)+'</h2>');continue
      if re.match(r'^[1-9][\s–-]+Pozytywne aspekty:',s):
       flush();n=s[0];out.append('<div class="num"><b>'+n+'</b><p>'+esc(re.sub(r'^[1-9][\s–-]+','',s))+'</p></div>');continue
      if s.startswith('⇦') or s.startswith('Data Urodzenia to jedyna'):flush();out.append('<div class="callout">'+esc(s)+'</div>');continue
      para.append(s)
    flush();return ''.join(out)
style='''@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;font-family:Arial,"DejaVu Sans",sans-serif;color:#2d213d}.page{position:relative;width:210mm;height:297mm;overflow:hidden;page-break-after:always;padding:20mm 19mm 18mm;background:radial-gradient(120mm 80mm at 8% 0%,rgba(111,75,194,.13),transparent 65%),radial-gradient(110mm 78mm at 100% 12%,rgba(216,137,183,.18),transparent 68%),linear-gradient(180deg,#fffafd,#fbf8ff 50%,#fff9fc)}.page:after{content:"";position:absolute;left:0;right:0;bottom:0;height:5mm;background:linear-gradient(90deg,#6f4bc2,#9b66c9,#d889b7,#e6a0c5)}.content{position:relative;z-index:2}.brand,.no{position:absolute;bottom:9.5mm;font-size:8.5pt;color:#897b96}.brand{left:17mm;font-family:Georgia,serif;font-weight:bold;color:#4b3566}.no{right:17mm}.kicker{display:inline-block;padding:4px 10px;border-radius:99px;background:#f1e9fa;color:#6f4bc2;font-size:8.5pt;font-weight:700;letter-spacing:.11em;margin-bottom:7mm}h1,h2{font-family:Georgia,"DejaVu Serif",serif;color:#2d213d;line-height:1.02;margin:0 0 5mm}h1{font-size:56pt}h1 em{font-weight:normal;color:#9555ae}h2{font-size:22pt;margin-top:2mm}p{font-size:10.5pt;line-height:1.45;margin:0 0 3mm;color:#5e536b}.cover{margin-top:27mm}.cover p{font-size:16pt;max-width:120mm;margin-top:9mm}.author{margin-top:23mm;font-family:Georgia,serif;font-size:20pt;color:#6f4bc2}.intro{margin-top:18mm}.intro h2{font-size:40pt}.big{font-size:14pt}.copyright{margin-top:28mm;padding:8mm;border-radius:6mm;background:#fff9;border:1px solid #ddd0e8;font-size:9pt;line-height:1.7;color:#6d607a}.deco{position:absolute;z-index:1}.butterfly{width:23mm;right:12mm;top:38mm;opacity:.7}.flower{width:18mm;left:10mm;bottom:28mm;opacity:.3}.num{display:grid;grid-template-columns:16mm 1fr;gap:4mm}.num>b{display:grid;place-items:center;width:14mm;height:14mm;border-radius:50%;background:linear-gradient(135deg,#6f4bc2,#d889b7);color:white;font:20pt Georgia}.callout{margin:5mm 0;padding:5mm 6mm;border-radius:4mm;background:linear-gradient(135deg,#eee5fa,#fbe9f4);font-weight:bold;color:#4a365f}.dense p{font-size:9.7pt;line-height:1.37}.very p{font-size:9pt;line-height:1.28}.very h2{font-size:18pt}'''
sections=[]
for i,p in enumerate(pages):
 c='page'+(' very' if len(p)>3400 else ' dense' if len(p)>2500 else '')
 sections.append(f'<section class="{c}">{butterfly}{flower}<div class="content">{format_page(p,i)}</div><div class="brand">EwaMiłek</div><div class="no">{i+1:02d}</div></section>')
doc='<!doctype html><html lang="pl"><head><meta charset="utf-8"><style>'+style+'</style></head><body>'+''.join(sections)+'</body></html>'
Path('ebook-src/kurs-numerologii.html').write_text(doc,encoding='utf-8')
print('Generated ebook-src/kurs-numerologii.html from',len(pages),'source pages.')
