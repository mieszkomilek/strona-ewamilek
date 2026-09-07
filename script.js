const btn=document.querySelector('.menu-btn');const menu=document.querySelector('#menu');btn?.addEventListener('click',()=>{const open=menu.classList.toggle('open');btn.setAttribute('aria-expanded',open)});document.querySelectorAll('#menu a').forEach(a=>a.addEventListener('click',()=>menu.classList.remove('open')));document.querySelector('#year').textContent=new Date().getFullYear();const io=new IntersectionObserver((entries)=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target)}}),{threshold:.12});document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

;(()=>{
  const reduced=window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  if(reduced||document.querySelector('.magic-layer'))return;
  const layer=document.createElement('div');
  layer.className='magic-layer';
  layer.setAttribute('aria-hidden','true');
  document.body.appendChild(layer);
  const items=[
    {char:'🦋',type:'butterfly'},
    {char:'🦋',type:'butterfly'},
    {char:'✿',type:'flower'},
    {char:'❀',type:'flower'}
  ];
  const spawn=()=>{
    if(document.hidden)return;
    const pick=items[Math.floor(Math.random()*items.length)];
    const el=document.createElement('span');
    el.className='magic-fly '+pick.type;
    el.textContent=pick.char;
    const y=12+Math.random()*70;
    const dur=12+Math.random()*8;
    const size=pick.type==='butterfly'?(18+Math.random()*12):(15+Math.random()*10);
    const rot=(-20+Math.random()*40)+'deg';
    el.style.setProperty('--y',y+'vh');
    el.style.setProperty('--dur',dur+'s');
    el.style.setProperty('--size',size+'px');
    el.style.setProperty('--rot',rot);
    layer.appendChild(el);
    el.addEventListener('animationend',()=>el.remove(),{once:true});
  };
  setTimeout(spawn,3500);
  setInterval(()=>{if(Math.random()>.25)spawn()},9000);
})();