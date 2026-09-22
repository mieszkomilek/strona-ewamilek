(() => {
  if (document.documentElement.lang !== 'en') return;
  const normal = s => s.replace(/\s+/g, ' ').trim();
  const translate = s => {
    const key = normal(s);
    if (Object.hasOwn(EWA_EN, key)) return s.slice(0,s.length-s.trimStart().length)+EWA_EN[key]+s.slice(s.trimEnd().length);
    if (s.includes('\n')) return s.split('\n').map(translate).join('\n');
    if (key.startsWith('Enlarge: ')) return 'Enlarge: '+translate(key.slice(9));
    if (key.startsWith('Podgląd zdjęcia ')) return 'Photo preview '+key.slice(16);
    const version=key.match(/^Wersja ([\d.]+) — (.+)$/);
    if(version)return 'Version '+version[1]+' — '+translate(version[2]);
    const numeric=[
      [/^Rok osobisty (\d+)(.*)$/, 'Personal year'],
      [/^suma (\d+)$/, 'sum'],
      [/^(\d+) zł$/, 'PLN'],
    ];
    for(const [re,label] of numeric){const m=key.match(re);if(m)return label+' '+m[1]+(m[2]||'');}
    const labels={'Droga Życia':'Life Path','Dzień urodzenia':'Birthday','Ekspresja / Przeznaczenie':'Expression / Destiny','Dążenie Duszy':'Soul Urge','Osobowość':'Personality','Dojrzałość':'Maturity','Szczyty':'Pinnacles','Wyzwania':'Challenges','Szczyty życiowe':'Life Pinnacles','Wyzwania życiowe':'Life Challenges','Wariant A':'Option A','Wariant B':'Option B','Ekspresja':'Expression','Data rozpoczęcia / zmiany':'Starting / change date'};
    for(const [pl,en] of Object.entries(labels)) {
      if(key.startsWith(pl+': '))return en+': '+key.slice(pl.length+2).replace(/\(suma (\d+)\)/g,'(sum $1)').replace(/^brak$/,'not provided').replace(' → wibracja daty ',' → date vibration ');
    }
    let m=key.match(/^(\d{2}\.\d{4}) — miesiąc osobisty (\d+)$/);if(m)return m[1]+' — personal month '+m[2];
    m=key.match(/^(\d{4}) — Rok osobisty (\d+)$/);if(m)return m[1]+' — Personal year '+m[2];
    m=key.match(/^Ekspresja (\d+) • Dążenie Duszy (\d+) • Osobowość (\d+)$/);if(m)return `Expression ${m[1]} • Soul Urge ${m[2]} • Personality ${m[3]}`;
    m=key.match(/^([A-D]\. [\d.]+) — wibracja (\d+)(?: • rok osobisty właściciela (\d+))?$/);if(m)return m[1]+' — vibration '+m[2]+(m[3]?' • owner’s personal year '+m[3]:'');
    const count = key.match(/^(\d+) zdję(?:cie|cia|ć)$/);
    if (count) return `${count[1]} photo${count[1] === '1' ? '' : 's'}`;
    if (key.startsWith('Powiększ: ')) return 'Enlarge: '+translate(key.slice(10));
    return s;
  };
  window.EwaTranslate = translate;
  const reverse=new Map(Object.entries(EWA_EN).map(([pl,en])=>[en,pl]));
  window.EwaOriginalText=s=>reverse.get(normal(s))||s;
  const attrs = ['alt','title','aria-label','placeholder','value'];
  function visit(el) {
    if(el.nodeType===3) {
      if(el.parentElement?.closest('script,style,textarea,[contenteditable]'))return;
      const next=translate(el.data);if(next!==el.data)el.data=next;return;
    }
    if(el.nodeType!==1 && el.nodeType!==9)return;
    if(el.nodeType===1){
      for(const attr of attrs){if(el.hasAttribute(attr) && (attr!=='value'||['submit','button'].includes(el.type))){const old=el.getAttribute(attr),next=translate(old);if(next!==old)el.setAttribute(attr,next);}}
      // Shared scripts use paths relative to the Polish root; keep original assets shared.
      for(const attr of ['src','href']) {
        const v=el.getAttribute(attr);
        if(v && /^(assets\/|data\/|facebook-zdjecia)/.test(v))el.setAttribute(attr,'../'+v);
      }
    }
    for(const child of el.childNodes)visit(child);
  }
  const observer=new MutationObserver(records=>{
    for(const r of records){if(r.type==='childList')r.addedNodes.forEach(visit);else visit(r.target);}
  });
  observer.observe(document.documentElement,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:attrs.concat(['src','href'])});
  document.addEventListener('DOMContentLoaded',()=>visit(document.documentElement));
  const nativeAlert=window.alert.bind(window);window.alert=s=>nativeAlert(translate(String(s)));
})();
