/* Photo storytelling for homepage + O mnie. Uses optimized WebP assets from assets/photos/. */
(()=>{
  const reduced=window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  const path=(location.pathname.split('/').pop()||'index.html').toLowerCase();
  const make=(html)=>{const t=document.createElement('template');t.innerHTML=html.trim();return t.content.firstElementChild};

  const setupParallax=()=>{
    if(reduced || window.innerWidth<621) return;
    const items=[...document.querySelectorAll('[data-photo-parallax]')];
    if(!items.length) return;
    let ticking=false;
    const draw=()=>{
      ticking=false;
      const vh=window.innerHeight||1;
      for(const el of items){
        const r=el.getBoundingClientRect();
        if(r.bottom<0||r.top>vh) continue;
        const center=r.top+r.height/2;
        const progress=(center-vh/2)/(vh+r.height);
        const shift=Math.max(-48,Math.min(48,-progress*88));
        el.style.setProperty('--photo-shift',`${shift.toFixed(1)}px`);
      }
    };
    const request=()=>{if(!ticking){ticking=true;requestAnimationFrame(draw)}};
    addEventListener('scroll',request,{passive:true});
    addEventListener('resize',request,{passive:true});
    draw();
  };

  const addHome=()=>{
    if(!['','index.html'].includes(path)) return;
    if(document.querySelector('#home-photo-parallax')) return;
    const intro=document.querySelector('.intro.strip');
    const about=document.querySelector('#o-mnie');
    if(intro){
      intro.insertAdjacentElement('afterend',make(`
        <section class="photo-parallax home-garden" id="home-photo-parallax" aria-label="Ewa Miłek i twórczość Vedic Art">
          <img class="photo-parallax-media" data-photo-parallax src="assets/photos/ewa-milek-vedic-art-ogrod.webp" loading="lazy" decoding="async" alt="Ewa Miłek podczas spotkania Vedic Art w ogrodzie, wśród obrazów i sztalug">
          <div class="container photo-parallax-content"><div class="photo-parallax-copy reveal"><p class="eyebrow">Twórczość w praktyce</p><h2>Sztuka rodzi się w spotkaniu.</h2><p>Kolor, natura, uważność i ludzie — właśnie z takich chwil wyrasta moja droga twórcza.</p></div></div>
        </section>`));
    }
    if(about){
      about.insertAdjacentElement('beforebegin',make(`
        <section class="photo-story" id="home-photo-story"><div class="container photo-story-grid">
          <div class="photo-story-frame reveal"><img data-photo-parallax src="assets/photos/ewa-milek-malowanie-w-ogrodzie.webp" loading="lazy" decoding="async" alt="Ewa Miłek maluje obraz przy sztaludze w ogrodzie"></div>
          <div class="photo-story-copy reveal delay-1"><p class="eyebrow">Proces twórczy</p><h2>Najważniejszy jest moment, w którym zaczynasz słuchać obrazu.</h2><p>Malowanie jest dla mnie drogą do skupienia, intuicji i kontaktu z tym, co wewnętrzne. Nie chodzi tylko o gotowy obraz — liczy się również cały proces jego powstawania.</p><a class="text-link" href="o-mnie.html">Poznaj moją historię →</a></div>
        </div></section>`));
    }
  };

  const addAbout=()=>{
    if(path!=='o-mnie.html') return;
    if(document.querySelector('#about-photo-parallax')) return;
    const hero=document.querySelector('.subpage-hero,.page-hero');
    const content=document.querySelector('.subpage-content');
    if(hero){
      hero.insertAdjacentElement('afterend',make(`
        <section class="photo-parallax about-gallery" id="about-photo-parallax" aria-label="Ewa Miłek na wystawie swoich prac">
          <img class="photo-parallax-media" data-photo-parallax src="assets/photos/ewa-milek-wystawa-malarstwo.webp" loading="eager" fetchpriority="high" decoding="async" alt="Ewa Miłek na wystawie przy swoich obrazach">
          <div class="container photo-parallax-content"><div class="photo-parallax-copy reveal"><p class="eyebrow">Moja droga</p><h2>Tworzę, uczę i pokazuję sztukę, która wyrasta z doświadczenia.</h2><p>Pracownia, warsztaty i wystawy są różnymi odsłonami tej samej potrzeby — tworzenia w zgodzie ze sobą.</p></div></div>
        </section>`));
    }
    if(content){
      content.insertAdjacentElement('afterend',make(`
        <section class="about-photo-gallery" id="about-photo-gallery"><div class="container">
          <div class="section-head reveal"><p class="eyebrow">Z pracowni i wystaw</p><h2>Fragmenty mojej twórczej drogi</h2><p>Zdjęcia z pracy przy sztaludze, przygotowań ekspozycji i spotkań wokół sztuki.</p></div>
          <div class="about-photo-grid">
            <figure class="about-photo-card reveal"><img src="assets/photos/ewa-milek-pracownia-sztaluga.webp" loading="lazy" decoding="async" alt="Ewa Miłek w pracowni obok sztalugi i przyborów malarskich"></figure>
            <figure class="about-photo-card reveal"><img src="assets/photos/ewa-milek-mandala-wystawa.webp" loading="lazy" decoding="async" alt="Ewa Miłek przy czerwonej mandali na wystawie"></figure>
            <figure class="about-photo-card reveal"><img src="assets/photos/ewa-milek-galeria-prace.webp" loading="lazy" decoding="async" alt="Ewa Miłek prezentuje własne obrazy w galerii"></figure>
            <figure class="about-photo-card reveal"><img src="assets/photos/ewa-milek-galeria-instalacja.webp" loading="lazy" decoding="async" alt="Ewa Miłek przy ekspozycji obrazów w galerii"></figure>
            <figure class="about-photo-card reveal"><img src="assets/photos/ewa-milek-wystawa-spotkanie.webp" loading="lazy" decoding="async" alt="Ewa Miłek podczas spotkania na wystawie"></figure>
            <figure class="about-photo-card reveal"><img src="assets/photos/ewa-milek-wystawa-wspomnienie.webp" loading="lazy" decoding="async" alt="Ewa Miłek na wystawie z bliską osobą, w otoczeniu obrazów"></figure>
          </div>
        </div></section>`));
    }
  };

  const boot=()=>{addHome();addAbout();setupParallax();setTimeout(setupParallax,250)};
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot,{once:true}); else boot();
})();
