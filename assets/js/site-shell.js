/* Global Ewa Miłek site shell: branding, artistic header, Admin index fallback and YYYYMMDD access guard. */
(()=>{
  const BRAND_NAME='Ewa Miłek';
  const BRAND_TAGLINE='Sztuka, która prowadzi do wnętrza';
  const dailyPassword=()=>{
    const d=new Date();
    return String(d.getFullYear())+String(d.getMonth()+1).padStart(2,'0')+String(d.getDate()).padStart(2,'0');
  };
  window.EwaMilekSite={...(window.EwaMilekSite||{}),dailyPassword,brandName:BRAND_NAME,brandTagline:BRAND_TAGLINE};

  const css=`
  .site-header{position:relative;isolation:isolate;background:linear-gradient(112deg,rgba(255,250,252,.94),rgba(251,236,243,.9) 34%,rgba(246,232,244,.88) 64%,rgba(255,247,250,.94));overflow:visible}
  .site-header:before{content:"";position:absolute;inset:0;z-index:-2;background:radial-gradient(circle at 15% 25%,rgba(212,139,169,.18),transparent 28%),radial-gradient(circle at 62% 0%,rgba(174,122,179,.13),transparent 33%),radial-gradient(circle at 88% 72%,rgba(224,163,184,.17),transparent 30%);background-size:135% 135%;animation:ewaHeaderGlow 15s ease-in-out infinite alternate}
  .site-header:after{content:"";position:absolute;left:0;right:0;bottom:-1px;height:1px;background:linear-gradient(90deg,transparent,rgba(115,72,154,.2),rgba(215,143,174,.32),transparent)}
  .site-header .nav-wrap{position:relative;z-index:3;min-height:94px}
  .brand{max-width:min(760px,68vw)}
  .brand strong{font-size:clamp(1.12rem,1.45vw,1.48rem);line-height:1.08;letter-spacing:-.02em}
  .brand small{margin-top:5px;font-size:.73rem;letter-spacing:.095em;color:rgba(83,59,104,.63)}
  .header-atmosphere{position:absolute;inset:0;z-index:0;pointer-events:none;overflow:hidden}
  .header-motif{position:absolute;display:block;color:rgba(185,111,151,.16);font-family:Georgia,serif;font-weight:700;line-height:1;text-shadow:0 0 20px rgba(235,175,204,.25);animation:ewaHeaderDrift var(--dur,13s) ease-in-out infinite alternate;transform:translate3d(0,0,0) rotate(var(--rot,0deg));will-change:transform,opacity}
  .header-motif.m1{left:3%;top:18%;font-size:1.35rem;--dur:10s;--rot:-12deg}.header-motif.m2{left:25%;top:55%;font-size:1.55rem;--dur:14s;--rot:8deg}.header-motif.m3{left:43%;top:16%;font-size:1.2rem;--dur:12s}.header-motif.m4{left:58%;top:52%;font-size:1.65rem;--dur:16s;--rot:-7deg}.header-motif.m5{left:72%;top:15%;font-size:1.25rem;--dur:11s}.header-motif.m6{left:84%;top:58%;font-size:1.45rem;--dur:15s;--rot:9deg}.header-motif.m7{left:35%;top:8%;font-size:1rem;letter-spacing:.26em;--dur:17s}.header-motif.m8{left:66%;top:68%;font-size:1.15rem;--dur:13s}
  @keyframes ewaHeaderGlow{0%{background-position:0% 45%}100%{background-position:100% 55%}}
  @keyframes ewaHeaderDrift{0%{opacity:.34;transform:translate3d(-7px,-3px,0) rotate(var(--rot,0deg)) scale(.94)}55%{opacity:.74}100%{opacity:.42;transform:translate3d(11px,7px,0) rotate(calc(var(--rot,0deg) + 5deg)) scale(1.08)}}
  @media(max-width:820px){.site-header .nav-wrap{min-height:76px}.brand{max-width:68vw}.brand strong{font-size:1rem}.brand small{font-size:.61rem;letter-spacing:.055em}.header-motif{opacity:.5!important}.header-motif.m2,.header-motif.m4,.header-motif.m6,.header-motif.m7{display:none}}
  @media(prefers-reduced-motion:reduce){.site-header:before,.header-motif{animation:none!important}}
  `;
  const style=document.createElement('style');style.id='ewa-site-shell-style';style.textContent=css;document.head.appendChild(style);

  const decorateHeader=()=>{
    document.querySelectorAll('.site-header').forEach((header,idx)=>{
      const brand=header.querySelector('.brand');
      const strong=brand?.querySelector('strong');
      const small=brand?.querySelector('small');
      if(strong) strong.textContent=BRAND_NAME;
      if(small) small.textContent=BRAND_TAGLINE;
      if(brand) brand.setAttribute('aria-label',`${BRAND_NAME} - ${BRAND_TAGLINE}`);
      if(header.querySelector('.header-atmosphere')) return;
      const layer=document.createElement('div');layer.className='header-atmosphere';layer.setAttribute('aria-hidden','true');
      const motifs=['🦋','✧','❀','1 · 7 · 9','🪽','✦','3 · 11 · 22','🖌'];
      motifs.forEach((symbol,i)=>{const s=document.createElement('span');s.className=`header-motif m${i+1}`;s.textContent=symbol;layer.appendChild(s)});
      header.insertBefore(layer,header.firstChild);
    });
  };

  const ensureAdminIndex=()=>{
    if(!document.body.classList.contains('admin-page')) return;
    const index=document.querySelector('.module-index');
    if(!index) return;
    const items=[
      ['wibracja-imienia-nazwiska','Wibracja z Imienia i Nazwiska','istniejące Narzędzie Ewy'],
      ['oferta-portret','Oferta – Portret Numerologiczny','pełny zestaw liczb bazowych'],
      ['oferta-mikro','Oferta – Portret MIKRO','data urodzenia, cykle, szczyty i wyzwania'],
      ['oferta-rok','Oferta – Rok osobisty','rok, miesiąc i dzień osobisty'],
      ['oferta-nazwy','Oferta – Analiza imion / nazw firmy','porównanie wariantów nazw'],
      ['interpretacje','Generator interpretacji','szkielet do zasilenia wiedzą Ewy'],
      ['admin-year-planner','Oferta – Numerologiczny Plan Roku','12 miesięcy osobistych'],
      ['admin-nine-year','Oferta – Prognoza 9-letniego cyklu','9 kolejnych lat osobistych'],
      ['admin-partners','Oferta – Portret Partnerski','porównanie dwóch osób'],
      ['admin-child','Oferta – Portret Numerologiczny Dziecka','profil bazowy dziecka'],
      ['admin-career','Oferta – Numerologia Kariery i Talentów','liczby do interpretacji'],
      ['admin-business-names','Oferta – Numerologia dla Firmy','porównanie do 5 nazw'],
      ['admin-start-dates','Oferta – Data startu firmy / projektu','porównanie kilku dat']
    ];
    items.forEach(([id,title,small])=>{
      if(index.querySelector(`a[href="#${id}"]`)) return;
      index.insertAdjacentHTML('beforeend',`<a href="#${id}">${title}<small>${small}</small></a>`);
    });
  };

  const enforceOfferDailyPassword=()=>{
    if(!document.body.classList.contains('offer26')) return;
    const form=document.querySelector('#offer26-gate-form');
    const input=document.querySelector('#offer26-password');
    const gate=document.querySelector('#offer26-gate');
    const page=document.querySelector('#offer26-page');
    const error=document.querySelector('#offer26-error');
    if(!form||!input||!gate||!page) return;
    input.maxLength=8;input.placeholder='••••••••';
    form.addEventListener('submit',e=>{
      e.preventDefault();e.stopImmediatePropagation();
      if(input.value.trim()===dailyPassword()){
        gate.classList.add('hidden');page.classList.remove('offer26-locked');sessionStorage.setItem('ewaOffer2026Unlocked','1');
        if(error) error.textContent='';
      }else{
        if(error) error.textContent='Nieprawidłowe hasło. Użyj formatu YYYYMMDD.';
        input.select();
      }
    },true);
  };

  const boot=()=>{decorateHeader();ensureAdminIndex();enforceOfferDailyPassword();setTimeout(ensureAdminIndex,350);setTimeout(ensureAdminIndex,900)};
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot,{once:true}); else boot();
})();
