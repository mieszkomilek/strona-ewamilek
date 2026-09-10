(() => {
  document.querySelectorAll('.art-gallery').forEach((gallery) => {
  const items = [...gallery.querySelectorAll('.art-gallery-item')];
  if (!items.length) return;
  const controls = document.createElement('div');
  controls.className = 'art-gallery-filters';
  controls.setAttribute('role', 'group');
  controls.setAttribute('aria-label', 'Filtruj galerię');
  const categories = ['all', ...new Set(items.map(item => item.dataset.category).filter(Boolean))];
  categories.forEach(category => {
    const button = document.createElement('button');
    button.type = 'button';
    button.dataset.galleryFilter = category;
    button.textContent = category === 'all' ? 'Wszystkie' : category;
    button.classList.toggle('active', category === 'all');
    button.setAttribute('aria-pressed', String(category === 'all'));
    controls.append(button);
  });
  const counter = document.createElement('span');
  counter.className = 'art-gallery-status';
  counter.setAttribute('aria-live', 'polite');
  const countLabel = n => `${n} ${n === 1 ? 'zdjęcie' : n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 12 || n % 100 > 14) ? 'zdjęcia' : 'zdjęć'}`;
  counter.textContent = countLabel(items.length);
  controls.append(counter);
  if (gallery.dataset.filters !== 'false') gallery.before(controls);
  const filters = [...controls.querySelectorAll('[data-gallery-filter]')];
  const status = controls.querySelector('.art-gallery-status');
  filters.forEach((button) => button.addEventListener('click', () => {
    const filter = button.dataset.galleryFilter;
    let visible = 0;
    items.forEach((item) => {
      const showItem = filter === 'all' || item.dataset.category === filter;
      item.hidden = !showItem;
      if (showItem) visible += 1;
    });
    filters.forEach((candidate) => {
      const active = candidate === button;
      candidate.classList.toggle('active', active);
      candidate.setAttribute('aria-pressed', String(active));
    });
    status.textContent = countLabel(visible);
  }));
  let index = 0;
  const dialog = document.createElement('dialog');
  dialog.className = 'art-gallery-dialog';
  dialog.setAttribute('aria-label', 'Podgląd zdjęcia');
  dialog.innerHTML = '<button type="button" class="art-gallery-close" aria-label="Zamknij podgląd">×</button><button type="button" class="art-gallery-prev" aria-label="Poprzednie zdjęcie">‹</button><img alt=""/><button type="button" class="art-gallery-next" aria-label="Następne zdjęcie">›</button>';
  document.body.append(dialog);
  const image = dialog.querySelector('img');
  const show = (next, direction = 1) => {
    index = (next + items.length) % items.length;
    while (items[index].hidden) index = (index + direction + items.length) % items.length;
    image.src = items[index].href;
    image.alt = items[index].querySelector('img')?.alt || '';
  };
  let opener;
  items.forEach((item, i) => item.addEventListener('click', (event) => {
    if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    if (typeof dialog.showModal !== 'function') return;
    event.preventDefault(); opener = item; show(i); dialog.showModal();
  }));
  dialog.addEventListener('close', () => opener?.focus());
  dialog.querySelector('.art-gallery-close').addEventListener('click', () => dialog.close());
  dialog.querySelector('.art-gallery-prev').addEventListener('click', () => show(index - 1, -1));
  dialog.querySelector('.art-gallery-next').addEventListener('click', () => show(index + 1, 1));
  dialog.addEventListener('click', (event) => { if (event.target === dialog) dialog.close(); });
  dialog.addEventListener('keydown', (event) => { if (event.key === 'ArrowLeft') show(index - 1, -1); if (event.key === 'ArrowRight') show(index + 1, 1); });
  });
})();
