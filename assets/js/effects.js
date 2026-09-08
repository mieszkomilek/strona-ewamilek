;(()=>{
  const reduced=window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  if(reduced||document.querySelector('.magic-layer'))return;
  const layer=document.createElement('div');
  layer.className='magic-layer'; layer.setAttribute('aria-hidden','true'); document.body.appendChild(layer);
  const items=[{char:'🦋',type:'butterfly'},{char:'✿',type:'flower'},{char:'❀',type:'flower'},{char:'✦',type:'flower'}];
  const palette=['#6f4bc2','#a86ad2','#d67da9','#e8a6c5','#8b70d6'];
  const spawn=(initial=false)=>{
    if(document.hidden)return;
    const pick=items[Math.floor(Math.random()*items.length)], el=document.createElement('span');
    el.className='magic-fly '+pick.type; el.textContent=pick.char;
    const y=5+Math.random()*86, dur=9+Math.random()*8;
    const size=pick.type==='butterfly'?(38+Math.random()*22):(32+Math.random()*20);
    const rot=(-25+Math.random()*50)+'deg';
    const c1=palette[Math.floor(Math.random()*palette.length)], c2=palette[Math.floor(Math.random()*palette.length)];
    el.style.setProperty('--y',y+'vh');el.style.setProperty('--dur',dur+'s');el.style.setProperty('--size',size+'px');el.style.setProperty('--rot',rot);
    el.style.setProperty('--c1',c1);el.style.setProperty('--c2',c2);
    if(initial)el.style.animationDelay=(-Math.random()*dur*.72)+'s';
    layer.appendChild(el);el.addEventListener('animationend',()=>el.remove(),{once:true});
  };
  for(let i=0;i<8;i++)spawn(true);
  setInterval(()=>{for(let i=0;i<2;i++)spawn(false)},2600);
})();
;(()=>{
  const hero=document.querySelector('.hero-photo-bg');
  if(hero && !window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    let ticking=false;
    const move=()=>{
      const section=hero.closest('.hero-photo');
      if(section){
        const rect=section.getBoundingClientRect();
        const travelled=Math.max(0,-rect.top);
        const mobile=window.matchMedia('(max-width:760px)').matches;
        const maxShift=mobile?190:145;
        const speed=mobile?.34:.25;
        const shift=-Math.min(maxShift,travelled*speed);
        const scale=mobile?1.14:1.09;
        hero.style.setProperty('--parallax-shift',shift.toFixed(1)+'px');
        hero.style.setProperty('--parallax-scale',String(scale));
      }
      ticking=false;
    };
    const requestMove=()=>{if(!ticking){ticking=true;requestAnimationFrame(move)}};
    window.addEventListener('scroll',requestMove,{passive:true});
    window.addEventListener('resize',requestMove,{passive:true});
    window.addEventListener('orientationchange',requestMove,{passive:true});
    move();
  }

  const root=document.querySelector('#wibracja-imienia-nazwiska');
  const modal=document.querySelector('#nv-password-modal');
  if(!root||!modal)return;
  const openBtn=document.querySelector('#nv-unlock');
  const form=document.querySelector('#nv-password-form');
  const input=document.querySelector('#nv-password');
  const error=document.querySelector('#nv-password-error');
  const currentPassword=()=>{
    const d=new Date();
    return String(d.getFullYear())+String(d.getMonth()+1).padStart(2,'0');
  };
  const open=()=>{
    modal.classList.add('is-open');modal.setAttribute('aria-hidden','false');
    document.body.classList.add('modal-open');error.textContent='';input.value='';
    setTimeout(()=>input.focus(),80);
  };
  const close=()=>{
    modal.classList.remove('is-open');modal.setAttribute('aria-hidden','true');
    document.body.classList.remove('modal-open');
  };
  const unlock=()=>{
    root.classList.remove('calc-locked');root.classList.add('calc-unlocked');
    sessionStorage.setItem('ewaNumerologyUnlocked','1');close();
    setTimeout(()=>root.scrollIntoView({behavior:'smooth',block:'start'}),100);
  };
  if(sessionStorage.getItem('ewaNumerologyUnlocked')==='1'){
    root.classList.remove('calc-locked');root.classList.add('calc-unlocked');
  }
  openBtn?.addEventListener('click',open);
  root.addEventListener('click',e=>{
    if(root.classList.contains('calc-locked') && !e.target.closest('#nv-unlock')){e.preventDefault();open();}
  });
  form?.addEventListener('submit',e=>{
    e.preventDefault();
    if(input.value.trim()===currentPassword())unlock();
    else{error.textContent='Nieprawidłowe hasło. Spróbuj ponownie.';input.select();}
  });
  modal.querySelectorAll('[data-close-password]').forEach(el=>el.addEventListener('click',close));
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&modal.classList.contains('is-open'))close()});
})();
