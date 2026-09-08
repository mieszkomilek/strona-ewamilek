;(()=>{
  const root=document.querySelector('#wibracja-imienia-nazwiska');
  if(!root)return;

  const vowels={A:1,'Ą':1,E:5,'Ę':5,I:9,O:15,'Ó':15,U:21,Y:25};
  const consonants={B:2,C:3,'Ć':3,D:4,F:6,G:7,H:8,J:10,K:11,L:12,'Ł':12,M:13,N:14,P:16,Q:17,R:18,S:19,'Ś':19,T:20,V:22,W:23,X:24,Z:26,'Ż':26,'Ź':26};
  const ids=['nv-first','nv-second','nv-third','nv-surname','nv-surname2'];
  const labels=['Pierwsze imię','Drugie imię','Trzecie imię','Nazwisko','Drugi człon nazwiska'];

  const clean=value=>value.toLocaleUpperCase('pl-PL').replace(/[^A-ZĄĆĘŁŃÓŚŹŻ]/g,'');
  const sumDigits=n=>String(Math.abs(Number(n)||0)).split('').reduce((a,d)=>a+Number(d),0);
  const reductions=n=>{
    const out=[]; let current=Number(n)||0;
    while(current>9 && out.length<3){current=sumDigits(current);out.push(current);}
    return out;
  };
  const analyze=value=>{
    const word=clean(value);
    let soul=0,personality=0;
    const letters=[...word].map(ch=>{
      const sv=vowels[ch]||0, pv=consonants[ch]||0;
      soul+=sv; personality+=pv;
      return {ch,sv,pv};
    });
    return {word,soul,personality,goals:soul+personality,letters};
  };
  const fmtRed=n=>{
    const r=reductions(n);
    return r.length ? 'LP: '+r.join(' → ') : 'LP: '+(n||0);
  };

  const calculate=()=>{
    const rows=ids.map((id,i)=>({label:labels[i],...analyze(document.getElementById(id).value)})).filter(x=>x.word);
    if(!rows.length){
      document.getElementById('nv-breakdown').innerHTML='<p class="calc-empty">Wprowadź przynajmniej jedno imię lub nazwisko.</p>';
      return;
    }
    const soul=rows.reduce((a,x)=>a+x.soul,0);
    const personality=rows.reduce((a,x)=>a+x.personality,0);
    const goals=soul+personality;

    document.getElementById('nv-soul-total').textContent=soul;
    document.getElementById('nv-personality-total').textContent=personality;
    document.getElementById('nv-goals-total').textContent=goals;
    document.getElementById('nv-soul-reduced').textContent=fmtRed(soul);
    document.getElementById('nv-personality-reduced').textContent=fmtRed(personality);
    document.getElementById('nv-goals-reduced').textContent=fmtRed(goals);

    document.getElementById('nv-breakdown').innerHTML=rows.map(x=>`
      <article class="calc-row">
        <div class="calc-word"><small>${x.label}</small><strong>${x.word}</strong></div>
        <div><small>Dążenie Duszy</small><strong>${x.soul}</strong><span>${fmtRed(x.soul)}</span></div>
        <div><small>Aspekt Osobowości</small><strong>${x.personality}</strong><span>${fmtRed(x.personality)}</span></div>
        <div><small>Cele życiowe</small><strong>${x.goals}</strong><span>${fmtRed(x.goals)}</span></div>
      </article>`).join('');
  };

  document.getElementById('nv-calc').addEventListener('click',calculate);
  document.getElementById('nv-clear').addEventListener('click',()=>{
    ids.forEach(id=>document.getElementById(id).value='');
    ['nv-soul-total','nv-personality-total','nv-goals-total'].forEach(id=>document.getElementById(id).textContent='—');
    ['nv-soul-reduced','nv-personality-reduced','nv-goals-reduced'].forEach(id=>document.getElementById(id).textContent='LP: —');
    document.getElementById('nv-breakdown').innerHTML='<p class="calc-empty">Wprowadź dane i kliknij „Oblicz wibrację”.</p>';
  });
  root.querySelectorAll('input').forEach(el=>el.addEventListener('keydown',e=>{if(e.key==='Enter')calculate()}));
})();
