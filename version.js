/* Site version footer renderer */
(()=>{
  const footer=document.querySelector('.site-footer')||document.querySelector('footer');
  if(!footer)return;
  fetch(`version.txt?v=${Date.now()}`,{cache:'no-store'})
    .then(r=>r.ok?r.text():Promise.reject())
    .then(v=>{
      const version=v.trim();
      if(!version)return;
      const el=document.createElement('div');
      el.className='site-version';
      el.textContent=`ver: ${version}`;
      el.style.cssText='text-align:center;font-size:10px;line-height:1;color:rgba(78,57,87,.45);letter-spacing:.08em;padding:10px 0 8px;user-select:none;';
      footer.appendChild(el);
    })
    .catch(()=>{});
})();
