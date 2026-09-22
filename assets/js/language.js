(() => {
  const en=location.pathname.startsWith('/en/');
  const file=location.pathname.split('/').pop()||'index.html';
  const suffix=location.search+location.hash;
  const plUrl=(file==='index.html'?'/':'/'+file)+suffix;
  const enUrl='/en/'+file+suffix;
  const host=document.querySelector('.nav-wrap');
  if(!host)return;
  const nav=document.createElement('nav');nav.className='language-switcher';nav.setAttribute('aria-label',en?'Language selection':'Wybór języka');
  nav.innerHTML=`<a href="/" lang="pl" hreflang="pl" ${!en?'aria-current="page"':''}>🇵🇱 PL</a><a href="/en/" lang="en" hreflang="en" ${en?'aria-current="page"':''}>🇬🇧 EN</a>`;
  nav.querySelector('[lang=pl]').href=plUrl;nav.querySelector('[lang=en]').href=enUrl;
  host.append(nav);
  const remember=lang=>{try{localStorage.setItem('ewa-language',lang)}catch{}};
  nav.addEventListener('click',e=>{const a=e.target.closest('a');if(a)remember(a.lang)});
  let pref;try{pref=localStorage.getItem('ewa-language')}catch{}
  if(pref)return;
  const dialog=document.createElement('div');dialog.className='language-choice';dialog.setAttribute('role','dialog');dialog.setAttribute('aria-modal','true');dialog.setAttribute('aria-labelledby','language-choice-title');
  dialog.innerHTML=en?'<div class="language-choice-card"><h2 id="language-choice-title">Choose your language</h2><p>You can change it at any time in the header.</p><button data-lang="en">🇬🇧 English</button><button data-lang="pl">🇵🇱 Polish</button></div>':'<div class="language-choice-card"><h2 id="language-choice-title">Wybierz język / Choose your language</h2><p>Wybór możesz później zmienić w nagłówku.</p><button data-lang="en">🇬🇧 English</button><button data-lang="pl">🇵🇱 Polski</button></div>';
  dialog.addEventListener('click',e=>{const b=e.target.closest('[data-lang]');if(!b)return;const lang=b.dataset.lang;remember(lang);if((lang==='en')===en){dialog.remove();nav.querySelector('[aria-current]')?.focus()}else location.href=lang==='en'?enUrl:plUrl});
  dialog.addEventListener('keydown',e=>{if(e.key==='Tab'){const buttons=[...dialog.querySelectorAll('button')];if(e.shiftKey&&document.activeElement===buttons[0]){e.preventDefault();buttons[1].focus()}else if(!e.shiftKey&&document.activeElement===buttons[1]){e.preventDefault();buttons[0].focus()}}if(e.key==='Escape'){remember(en?'en':'pl');dialog.remove();nav.querySelector('[aria-current]')?.focus()}});
  document.body.append(dialog);dialog.querySelector('button').focus();
})();
