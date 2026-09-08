/* E-book library: password + in-page PDF reader */
;(()=>{
  const openBtn=document.querySelector('#ebook-open');
  const modal=document.querySelector('#ebook-password-modal');
  const form=document.querySelector('#ebook-password-form');
  const input=document.querySelector('#ebook-password');
  const error=document.querySelector('#ebook-password-error');
  const reader=document.querySelector('#ebook-reader');
  const frame=document.querySelector('#ebook-frame');
  const readerClose=document.querySelector('#ebook-reader-close');
  if(!openBtn||!modal||!form||!input||!reader||!frame)return;

  const expectedPassword=()=>{
    const d=new Date();
    const y=d.getFullYear();
    const m=String(d.getMonth()+1).padStart(2,'0');
    const day=String(d.getDate()).padStart(2,'0');
    return `${y}${m}${day}`;
  };
  const showModal=()=>{
    modal.classList.add('is-open'); modal.setAttribute('aria-hidden','false');
    document.body.classList.add('modal-open');
    input.value=''; if(error)error.textContent='';
    setTimeout(()=>input.focus(),80);
  };
  const hideModal=()=>{
    modal.classList.remove('is-open'); modal.setAttribute('aria-hidden','true');
    document.body.classList.remove('modal-open');
  };
  const showReader=()=>{
    hideModal();
    frame.src='assets/ebooks/kurs-numerologii-ewa-milek.pdf#toolbar=0&navpanes=0&scrollbar=1&view=FitH';
    reader.classList.add('is-open'); reader.setAttribute('aria-hidden','false');
    document.body.classList.add('ebook-reading');
  };
  const hideReader=()=>{
    reader.classList.remove('is-open'); reader.setAttribute('aria-hidden','true');
    document.body.classList.remove('ebook-reading'); frame.src='';
  };
  openBtn.addEventListener('click',showModal);
  document.querySelectorAll('[data-ebook-close]').forEach(el=>el.addEventListener('click',hideModal));
  readerClose?.addEventListener('click',hideReader);
  form.addEventListener('submit',e=>{
    e.preventDefault();
    if(input.value.trim()===expectedPassword()){showReader();}
    else{if(error)error.textContent='Nieprawidłowe hasło. Spróbuj ponownie.';input.select();}
  });
  document.addEventListener('keydown',e=>{
    if(e.key!=='Escape')return;
    if(reader.classList.contains('is-open'))hideReader();
    else if(modal.classList.contains('is-open'))hideModal();
  });
})();
