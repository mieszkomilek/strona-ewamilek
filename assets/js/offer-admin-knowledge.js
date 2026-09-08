/* Oferta 2026 + Admin extensions and knowledge links */
(()=>{
  const REF_NUM={label:'Źródło referencyjne — numerologia (brak jednej oficjalnej normy)',url:'https://www.encyclopedia.com/philosophy-and-religion/other-religious-beliefs-and-general-terms/miscellaneous-religion/numerology'};
  const UOKIK={label:'UOKiK — prawa konsumenta i treści cyfrowe',url:'https://prawakonsumenta.uokik.gov.pl/zmiany-2023/'};
  const UOKIK_INFO={label:'UOKiK — informacje przed zakupem online',url:'https://prawakonsumenta.uokik.gov.pl/pytania-i-odpowiedzi/prawo-do-informacji/'};
  const EU_DIGITAL={label:'Komisja Europejska — zasady dla treści i usług cyfrowych',url:'https://commission.europa.eu/topics/business-and-industry/contract-rules/digital-contracts/digital-contract-rules_en'};
  const EU_CONSUMER={label:'Komisja Europejska — Consumer Rights Directive',url:'https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en'};
  const GOOGLE_PRODUCT={label:'Google Search Central — Product / Offer structured data',url:'https://developers.google.com/search/docs/appearance/structured-data/product'};
  const VEDIC={label:'Vedic Art — oficjalna strona',url:'https://www.vedicart.com/'};
  const VEDIC_TERMS={label:'Vedic Art — oficjalne Terms & Policies',url:'https://www.vedicart.com/en/terms-policies'};
  const VEDIC_ONLINE={label:'Vedic Art — oficjalne zasady kursów online',url:'https://www.vedicart.com/online'};
  const VEDIC_STORY={label:'Vedic Art — historia metody i 17 Zasad',url:'https://www.vedicart.com/en/vedic-art'};

  const esc=s=>String(s||'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
  const knowledgeHtml=(links,note='')=>`<div class="knowledge-links"><div class="knowledge-title">Linki do oficjalnej bazy wiedzy</div>${note?`<p class="knowledge-note">${esc(note)}</p>`:''}<div class="knowledge-list">${links.map(x=>`<a href="${esc(x.url)}" target="_blank" rel="noopener noreferrer">↗ ${esc(x.label)}</a>`).join('')}</div></div>`;

  const style=document.createElement('style');
  style.textContent=`
  .knowledge-links{margin-top:16px;padding:14px 16px;border-radius:16px;background:linear-gradient(145deg,#fff,#fbf7ff);border:1px solid rgba(102,70,155,.16)}
  .knowledge-title{font-weight:800;color:#563884;margin-bottom:6px}.knowledge-note{margin:0 0 8px!important;font-size:.78rem!important;color:#7d7085!important}.knowledge-list{display:flex;gap:8px;flex-wrap:wrap}.knowledge-list a{display:inline-flex;padding:7px 10px;border-radius:999px;background:#f0e8fb;text-decoration:none;color:#5b3b91;font-size:.74rem;font-weight:700}.knowledge-list a:hover{background:#e7dcf8}
  .offer26-new-heading{margin:64px 0 22px}.offer26-new-heading p{color:var(--muted)}
  .admin-auto-tag{display:inline-flex;padding:6px 10px;border-radius:999px;background:#eaf7ee;color:#2f7043;font-size:.74rem;font-weight:800;margin-left:6px}
  `;
  document.head.appendChild(style);

  const numerologyLinks=[REF_NUM,UOKIK_INFO,EU_CONSUMER];
  const digitalLinks=[REF_NUM,UOKIK,EU_DIGITAL];
  const artLinks=[EU_CONSUMER,GOOGLE_PRODUCT];
  const vedicLinks=[VEDIC,VEDIC_TERMS,VEDIC_ONLINE,VEDIC_STORY];

  function linksForTitle(title){
    const t=(title||'').toLowerCase();
    if(t.includes('vedic')) return vedicLinks;
    if(t.includes('e-book')||t.includes('ebook')||t.includes('pdf')||t.includes('kurs z numerologii')) return digitalLinks;
    if(t.includes('numerolog')||t.includes('rok osobisty')||t.includes('droga życia')||t.includes('portret')||t.includes('firma')||t.includes('nazw')||t.includes('partners')||t.includes('dziecka')||t.includes('talent')||t.includes('cykl')||t.includes('data startu')) return numerologyLinks;
    return artLinks;
  }

  // -------- Oferta 2026 --------
  if(document.body.classList.contains('offer26')){
    const products=document.querySelector('#offer26-products');
    if(products && !document.querySelector('#offer26-added-products')){
      const wrap=document.createElement('section');
      wrap.id='offer26-added-products';
      wrap.innerHTML=`<div class="offer26-new-heading"><p class="eyebrow">Nowe kierunki do wdrożenia</p><h2>Produkty, których brakowało w Ofercie 2026</h2><p>Na tym etapie są to pozycje robocze bez nowych płatności. Ceny i zakres wymagają akceptacji Ewy.</p></div>`;
      products.parentNode.insertBefore(wrap,products.nextSibling);
      const list=document.createElement('div');list.className='offer26-products';wrap.appendChild(list);
      const newProducts=[
        ['20','numerologia','Twój Rok Osobisty 2027','69–249 zł','MINI, pełna 12-miesięczna oraz PREMIUM z osobistymi wskazówkami Ewy.','Admin: kalkulator roku i miesięcy'],
        ['21','numerologia','Numerologiczny Plan Roku','129–199 zł','Rok osobisty rozpisany miesiąc po miesiącu z miejscem na intencje i decyzje.','Admin: generator 12 miesięcy'],
        ['22','premium','Portret Partnerski','490–790 zł','Porównanie dwóch osób: podstawowe liczby, różnice, podobieństwa i cykle.','Admin: porównywarka dwóch osób'],
        ['23','numerologia','Numerologia Kariery i Talentów','249–390 zł','Osobny produkt z istniejącego rozszerzenia: predyspozycje, talenty, powołanie i praca.','Admin: profil bazowy do interpretacji'],
        ['24','numerologia','Numerologia dla Firmy — wybór nazwy','290–650 zł','Porównanie do 5 nazw marki lub firmy i daty rozpoczęcia.','Admin: porównywarka nazw'],
        ['25','numerologia','Portret Numerologiczny Dziecka','249–390 zł','Profil bazowy dla rodziców: Droga Życia, liczby z imienia, cykle i predyspozycje.','Admin: profil bazowy dziecka'],
        ['26','numerologia','Prognoza 9-letniego cyklu','290–450 zł','Dziewięć kolejnych lat osobistych przedstawionych w jednym planie.','Admin: generator 9 lat'],
        ['27','numerologia','Numerologiczna data startu firmy / projektu','190–290 zł','Porównanie kilku dat z uwzględnieniem roku osobistego właściciela.','Admin: porównywarka dat'],
        ['28','mandala premium','Mandala Twojej Wibracji','Do wyceny','Produkt premium łączący wybrane liczby numerologiczne z indywidualną Mandalą Ewy.','Zakres do decyzji Ewy'],
        ['29','tworczosc','Warsztaty tematyczne Ewy','Do ustalenia','Mandala Intencji, Kolory Twojego Roku, Moja Droga Życia w obrazie, Kobiecy dzień twórczy.','Autorski format, niezależny od pełnego kursu Vedic Art']
      ];
      newProducts.forEach(([n,cat,title,price,desc,chip])=>{
        const a=document.createElement('article');a.className='offer26-card';a.dataset.cat=cat;
        a.innerHTML=`<div class="offer26-num">${n}</div><div class="offer26-copy"><h2>${esc(title)}</h2><p>${esc(desc)}</p><div class="offer26-meta"><span class="offer26-chip">${esc(cat)}</span><span class="offer26-chip">${esc(chip)}</span></div>${knowledgeHtml(linksForTitle(title),title.includes('Numerolog')||title.includes('Portret')||title.includes('Rok')||title.includes('Firmy')||title.includes('cyklu')||title.includes('data startu')?'Numerologia nie ma jednej oficjalnej normy. Link encyklopedyczny jest punktem referencyjnym, a docelową bazą interpretacji mają być materiały Ewy.':'')}</div><div class="offer26-buy"><strong>${esc(price)}</strong><small>cena / status roboczy</small></div>`;
        list.appendChild(a);
      });
    }
    const addOfferLinks=()=>document.querySelectorAll('.offer26-card').forEach(card=>{
      if(card.querySelector('.knowledge-links'))return;
      const title=card.querySelector('h2')?.textContent||'';
      const target=card.querySelector('.offer26-copy')||card;
      target.insertAdjacentHTML('beforeend',knowledgeHtml(linksForTitle(title),(title.toLowerCase().includes('numerolog')||title.toLowerCase().includes('rok osobisty'))?'Numerologia nie ma jednej oficjalnej normy; do interpretacji nadrzędne będą materiały Ewy.':''));
    });
    addOfferLinks();
    new MutationObserver(addOfferLinks).observe(document.querySelector('#offer26-products')||document.body,{childList:true,subtree:true});
  }

  // -------- Admin --------
  if(document.body.classList.contains('admin-page')){
    const red=n=>{n=Math.abs(Number(n)||0);while(n>9&&![11,22,33].includes(n))n=String(n).split('').reduce((a,b)=>a+Number(b),0);return n};
    const dp=v=>{if(!v)return null;const [y,m,d]=v.split('-').map(Number);return{y,m,d}};
    const life=p=>p?red([...String(p.y),...String(p.m).padStart(2,'0'),...String(p.d).padStart(2,'0')].reduce((a,x)=>a+Number(x),0)):0;
    const py=(p,y)=>p?red(red(p.m)+red(p.d)+red(y)):0;
    const norm=s=>(s||'').toUpperCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/Ł/g,'L').replace(/[^A-Z]/g,'');
    const vv=ch=>((ch.charCodeAt(0)-65)%9)+1;
    const sum=(name,mode='all')=>[...norm(name)].filter(ch=>{const v='AEIOUY'.includes(ch);return mode==='all'||(mode==='v'&&v)||(mode==='c'&&!v)}).reduce((a,ch)=>a+vv(ch),0);
    const profile=name=>{const er=sum(name),sr=sum(name,'v'),pr=sum(name,'c');return{e:red(er),er,s:red(sr),sr,p:red(pr),pr}};
    const fprof=(name,p)=>{const n=profile(name),l=life(p);return`Droga Życia: ${l}\nDzień urodzenia: ${p?red(p.d):'—'}\nEkspresja / Przeznaczenie: ${n.e} (suma ${n.er})\nDążenie Duszy: ${n.s} (suma ${n.sr})\nOsobowość: ${n.p} (suma ${n.pr})\nDojrzałość: ${red(l+n.e)}`};
    const tools=document.querySelector('.admin-tools')||document.querySelector('main .container');
    if(tools && !document.querySelector('#admin-extended-numerology')){
      const ext=document.createElement('section');ext.id='admin-extended-numerology';ext.className='container admin-tools';
      ext.innerHTML=`
      <section class="admin-section" id="admin-year-planner"><div class="admin-badges"><span class="admin-badge offer">Oferta – Numerologiczny Plan Roku</span><span class="admin-auto-tag">można liczyć online</span></div><h2>Plan roku osobistego — 12 miesięcy</h2><div class="admin-grid"><label class="admin-field"><span>Data urodzenia</span><input id="ap-birth" type="date"></label><label class="admin-field"><span>Rok</span><input id="ap-year" type="number"></label></div><div class="admin-actions"><button class="btn btn-primary" id="ap-calc">Generuj plan roku</button></div><div class="admin-output" id="ap-output">Wyniki pojawią się tutaj.</div></section>
      <section class="admin-section" id="admin-nine-year"><div class="admin-badges"><span class="admin-badge offer">Oferta – Prognoza 9-letniego cyklu</span><span class="admin-auto-tag">można liczyć online</span></div><h2>Cykl 9 kolejnych lat osobistych</h2><div class="admin-grid"><label class="admin-field"><span>Data urodzenia</span><input id="a9-birth" type="date"></label><label class="admin-field"><span>Rok początkowy</span><input id="a9-year" type="number"></label></div><div class="admin-actions"><button class="btn btn-primary" id="a9-calc">Generuj 9 lat</button></div><div class="admin-output" id="a9-output">Wyniki pojawią się tutaj.</div></section>
      <section class="admin-section" id="admin-partners"><div class="admin-badges"><span class="admin-badge offer">Oferta – Portret Partnerski</span><span class="admin-auto-tag">porównanie liczb</span><span class="admin-badge warn">Interpretacja: wiedza Ewy później</span></div><h2>Porównanie dwóch osób</h2><div class="admin-grid"><label class="admin-field"><span>Osoba A — imię i nazwisko</span><input id="rel-name-a"></label><label class="admin-field"><span>Osoba A — data urodzenia</span><input id="rel-date-a" type="date"></label><label class="admin-field"><span>Osoba B — imię i nazwisko</span><input id="rel-name-b"></label><label class="admin-field"><span>Osoba B — data urodzenia</span><input id="rel-date-b" type="date"></label></div><div class="admin-actions"><button class="btn btn-primary" id="rel-calc">Porównaj liczby</button></div><div class="admin-output" id="rel-output">Wyniki pojawią się tutaj.</div></section>
      <section class="admin-section" id="admin-child"><div class="admin-badges"><span class="admin-badge offer">Oferta – Portret Numerologiczny Dziecka</span><span class="admin-auto-tag">profil bazowy</span></div><h2>Profil bazowy dziecka</h2><div class="admin-grid"><label class="admin-field"><span>Imię i nazwisko</span><input id="child-name"></label><label class="admin-field"><span>Data urodzenia</span><input id="child-date" type="date"></label></div><div class="admin-actions"><button class="btn btn-primary" id="child-calc">Oblicz profil</button></div><div class="admin-output" id="child-output">Wyniki pojawią się tutaj.</div></section>
      <section class="admin-section" id="admin-career"><div class="admin-badges"><span class="admin-badge offer">Oferta – Numerologia Kariery i Talentów</span><span class="admin-auto-tag">profil bazowy</span></div><h2>Profil kariery — liczby do interpretacji</h2><div class="admin-grid"><label class="admin-field"><span>Imię i nazwisko</span><input id="career-name"></label><label class="admin-field"><span>Data urodzenia</span><input id="career-date" type="date"></label></div><div class="admin-actions"><button class="btn btn-primary" id="career-calc">Oblicz profil kariery</button></div><div class="admin-output" id="career-output">Wyniki pojawią się tutaj.</div></section>
      <section class="admin-section" id="admin-business-names"><div class="admin-badges"><span class="admin-badge offer">Oferta – Numerologia dla Firmy</span><span class="admin-auto-tag">do 5 nazw</span></div><h2>Porównywarka nazw firmy / marki</h2><div class="admin-grid">${[1,2,3,4,5].map(i=>`<label class="admin-field"><span>Nazwa ${i}</span><input class="biz-name"></label>`).join('')}</div><div class="admin-actions"><button class="btn btn-primary" id="biz-calc">Porównaj nazwy</button></div><div class="admin-output" id="biz-output">Wyniki pojawią się tutaj.</div></section>
      <section class="admin-section" id="admin-start-dates"><div class="admin-badges"><span class="admin-badge offer">Oferta – Data startu firmy / projektu</span><span class="admin-auto-tag">porównywarka dat</span></div><h2>Porównanie proponowanych dat</h2><div class="admin-grid"><label class="admin-field"><span>Data urodzenia właściciela</span><input id="start-owner" type="date"></label>${['A','B','C','D'].map(x=>`<label class="admin-field"><span>Data ${x}</span><input class="start-date" type="date"></label>`).join('')}</div><div class="admin-actions"><button class="btn btn-primary" id="start-calc">Porównaj daty</button></div><div class="admin-output" id="start-output">Wyniki pojawią się tutaj.</div></section>`;
      document.querySelector('main').appendChild(ext);
    }
    const y=new Date().getFullYear();document.querySelector('#ap-year')&&(document.querySelector('#ap-year').value=y);document.querySelector('#a9-year')&&(document.querySelector('#a9-year').value=y);
    document.querySelector('#ap-calc')?.addEventListener('click',()=>{const p=dp(document.querySelector('#ap-birth').value),yr=+document.querySelector('#ap-year').value||y,o=document.querySelector('#ap-output');o.textContent=p?`Rok osobisty ${yr}: ${py(p,yr)}\n\n`+Array.from({length:12},(_,i)=>`${String(i+1).padStart(2,'0')}.${yr} — miesiąc osobisty ${red(py(p,yr)+i+1)}`).join('\n'):'Uzupełnij datę urodzenia.'});
    document.querySelector('#a9-calc')?.addEventListener('click',()=>{const p=dp(document.querySelector('#a9-birth').value),yr=+document.querySelector('#a9-year').value||y,o=document.querySelector('#a9-output');o.textContent=p?Array.from({length:9},(_,i)=>`${yr+i} — Rok osobisty ${py(p,yr+i)}`).join('\n'):'Uzupełnij datę urodzenia.'});
    document.querySelector('#rel-calc')?.addEventListener('click',()=>{const na=document.querySelector('#rel-name-a').value,nb=document.querySelector('#rel-name-b').value,da=dp(document.querySelector('#rel-date-a').value),db=dp(document.querySelector('#rel-date-b').value),o=document.querySelector('#rel-output');o.textContent=na&&nb&&da&&db?`OSOBA A\n${fprof(na,da)}\n\nOSOBA B\n${fprof(nb,db)}\n\nInterpretacja relacji: do zasilenia wiedzą Ewy.`:'Uzupełnij dane obu osób.'});
    document.querySelector('#child-calc')?.addEventListener('click',()=>{const n=document.querySelector('#child-name').value,p=dp(document.querySelector('#child-date').value),o=document.querySelector('#child-output');o.textContent=n&&p?fprof(n,p)+'\n\nInterpretacja rozwojowa: do zasilenia wiedzą Ewy.':'Uzupełnij dane.'});
    document.querySelector('#career-calc')?.addEventListener('click',()=>{const n=document.querySelector('#career-name').value,p=dp(document.querySelector('#career-date').value),o=document.querySelector('#career-output');o.textContent=n&&p?fprof(n,p)+'\n\nInterpretacja talentów i powołania: do zasilenia wiedzą Ewy.':'Uzupełnij dane.'});
    document.querySelector('#biz-calc')?.addEventListener('click',()=>{const names=[...document.querySelectorAll('.biz-name')].map(x=>x.value.trim()).filter(Boolean),o=document.querySelector('#biz-output');o.textContent=names.length?names.map((n,i)=>{const x=profile(n);return`${i+1}. ${n}\nEkspresja ${x.e} • Dążenie Duszy ${x.s} • Osobowość ${x.p}`}).join('\n\n')+'\n\nRekomendacja: do zasilenia wiedzą Ewy.':'Wpisz co najmniej jedną nazwę.'});
    document.querySelector('#start-calc')?.addEventListener('click',()=>{const owner=dp(document.querySelector('#start-owner').value),dates=[...document.querySelectorAll('.start-date')].map(x=>dp(x.value)).filter(Boolean),o=document.querySelector('#start-output');o.textContent=dates.length?dates.map((d,i)=>`${String.fromCharCode(65+i)}. ${String(d.d).padStart(2,'0')}.${String(d.m).padStart(2,'0')}.${d.y} — wibracja ${life(d)}${owner?` • rok osobisty właściciela ${py(owner,d.y)}`:''}`).join('\n')+'\n\nWybór najlepszej daty: do zasilenia wiedzą Ewy.':'Wpisz co najmniej jedną datę.'});

    const addAdminLinks=()=>{
      const candidates=[...document.querySelectorAll('.admin-section'),document.querySelector('#wibracja-imienia-nazwiska')].filter(Boolean);
      candidates.forEach(sec=>{
        if(sec.querySelector('.knowledge-links'))return;
        const title=sec.querySelector('h2,h3')?.textContent||'Numerologia';
        sec.insertAdjacentHTML('beforeend',knowledgeHtml(linksForTitle(title),'Dla numerologii brak jednej oficjalnej normy. Źródło encyklopedyczne jest punktem referencyjnym; interpretacje docelowo powinny wynikać z dokumentów Ewy.'));
      });
    };
    addAdminLinks();
  }
})();
