/* Completes the Admin/Oferta 2026 UI without touching payment logic. */
(()=>{
  const adminItems=[
    ['admin-year-planner','Oferta – Numerologiczny Plan Roku','12 miesięcy osobistych'],
    ['admin-nine-year','Oferta – Prognoza 9-letniego cyklu','9 kolejnych lat osobistych'],
    ['admin-partners','Oferta – Portret Partnerski','porównanie dwóch osób'],
    ['admin-child','Oferta – Portret Numerologiczny Dziecka','profil bazowy dziecka'],
    ['admin-career','Oferta – Numerologia Kariery i Talentów','liczby do interpretacji'],
    ['admin-business-names','Oferta – Numerologia dla Firmy','porównanie do 5 nazw'],
    ['admin-start-dates','Oferta – Data startu firmy / projektu','porównanie kilku dat']
  ];

  const run=()=>{
    if(document.body.classList.contains('admin-page')){
      const index=document.querySelector('.module-index');
      if(index){
        adminItems.forEach(([id,title,small])=>{
          if(!index.querySelector(`a[href="#${id}"]`)){
            index.insertAdjacentHTML('beforeend',`<a href="#${id}">${title}<small>${small}</small></a>`);
          }
        });
      }
      const missing=adminItems.filter(([id])=>!document.getElementById(id));
      if(missing.length){
        const warn=document.createElement('div');
        warn.className='container admin-note';
        warn.style.marginTop='24px';
        warn.innerHTML='<strong>Trwa ładowanie modułów dodatkowych.</strong> Jeśli po odświeżeniu nadal ich nie widać, sprawdź najnowszy deployment GitHub Pages.';
        document.querySelector('main')?.appendChild(warn);
      }
    }

    if(document.body.classList.contains('offer26')){
      const list=document.querySelector('#offer26-added-products, #offer26-new-ideas');
      if(list && !document.querySelector('#offer26-complete-label')){
        const label=document.createElement('div');
        label.id='offer26-complete-label';
        label.className='container';
        label.style.marginTop='16px';
        label.innerHTML='<p class="offer26-note"><strong>Uzupełnienie Oferty 2026:</strong> dodane pozycje są robocze i nie zmieniają istniejącej konfiguracji PayPal. Powiązane kalkulatory znajdują się w dziale Admin.</p>';
        list.parentNode.insertBefore(label,list);
      }
    }
  };

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',()=>setTimeout(run,0));
  else setTimeout(run,0);
  setTimeout(run,500);
})();
