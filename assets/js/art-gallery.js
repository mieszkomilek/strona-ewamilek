(() => {
  const items = [...document.querySelectorAll('.art-gallery-item')];
  if (!items.length) return;
  let index = 0;
  const dialog = document.createElement('dialog');
  dialog.className = 'art-gallery-dialog';
  dialog.innerHTML = '<button type="button" class="art-gallery-close" aria-label="Zamknij podgląd">×</button><button type="button" class="art-gallery-prev" aria-label="Poprzednie zdjęcie">‹</button><img alt=""/><button type="button" class="art-gallery-next" aria-label="Następne zdjęcie">›</button>';
  document.body.append(dialog);
  const image = dialog.querySelector('img');
  const show = (next) => { index = (next + items.length) % items.length; image.src = items[index].href; image.alt = items[index].querySelector('img')?.alt || ''; };
  items.forEach((item, i) => item.addEventListener('click', (event) => { event.preventDefault(); show(i); dialog.showModal(); }));
  dialog.querySelector('.art-gallery-close').addEventListener('click', () => dialog.close());
  dialog.querySelector('.art-gallery-prev').addEventListener('click', () => show(index - 1));
  dialog.querySelector('.art-gallery-next').addEventListener('click', () => show(index + 1));
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', (event) => { if (event.key === 'ArrowLeft') show(index - 1); if (event.key === 'ArrowRight') show(index + 1); });
})();
