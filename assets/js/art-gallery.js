(() => {
  const items = [...document.querySelectorAll('.art-gallery-item')];
  if (!items.length) return;
  const gallery = document.querySelector('.art-gallery');
  const controls = document.createElement('div');
  controls.className = 'art-gallery-filters';
  controls.setAttribute('role', 'group');
  controls.setAttribute('aria-label', 'Filtruj galerię');
  controls.innerHTML = '<button type="button" class="active" data-gallery-filter="all" aria-pressed="true">Wszystkie</button><button type="button" data-gallery-filter="obrazy" aria-pressed="false">Obrazy</button><button type="button" data-gallery-filter="pracownia" aria-pressed="false">Pracownia i wystawy</button><span class="art-gallery-status" aria-live="polite">17 zdjęć</span>';
  gallery.before(controls);
  const filters = [...controls.querySelectorAll('[data-gallery-filter]')];
  const status = controls.querySelector('.art-gallery-status');
  const studioWords = ['pracowni', 'wystawie', 'prezentuje', 'praca nad'];
  filters.forEach((button) => button.addEventListener('click', () => {
    const filter = button.dataset.galleryFilter;
    let visible = 0;
    items.forEach((item) => {
      const label = item.getAttribute('aria-label').toLocaleLowerCase('pl-PL');
      const studio = studioWords.some((word) => label.includes(word));
      const showItem = filter === 'all' || (filter === 'pracownia' ? studio : !studio);
      item.hidden = !showItem;
      if (showItem) visible += 1;
    });
    filters.forEach((candidate) => {
      const active = candidate === button;
      candidate.classList.toggle('active', active);
      candidate.setAttribute('aria-pressed', String(active));
    });
    status.textContent = `${visible} ${visible === 1 ? 'zdjęcie' : visible < 5 ? 'zdjęcia' : 'zdjęć'}`;
  }));
  let index = 0;
  const dialog = document.createElement('dialog');
  dialog.className = 'art-gallery-dialog';
  dialog.innerHTML = '<button type="button" class="art-gallery-close" aria-label="Zamknij podgląd">×</button><button type="button" class="art-gallery-prev" aria-label="Poprzednie zdjęcie">‹</button><img alt=""/><button type="button" class="art-gallery-next" aria-label="Następne zdjęcie">›</button>';
  document.body.append(dialog);
  const image = dialog.querySelector('img');
  const show = (next, direction = 1) => {
    index = (next + items.length) % items.length;
    while (items[index].hidden) index = (index + direction + items.length) % items.length;
    image.src = items[index].href;
    image.alt = items[index].querySelector('img')?.alt || '';
  };
  items.forEach((item, i) => item.addEventListener('click', (event) => { event.preventDefault(); show(i); dialog.showModal(); }));
  dialog.querySelector('.art-gallery-close').addEventListener('click', () => dialog.close());
  dialog.querySelector('.art-gallery-prev').addEventListener('click', () => show(index - 1, -1));
  dialog.querySelector('.art-gallery-next').addEventListener('click', () => show(index + 1, 1));
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', (event) => { if (event.key === 'ArrowLeft') show(index - 1, -1); if (event.key === 'ArrowRight') show(index + 1, 1); });
})();
