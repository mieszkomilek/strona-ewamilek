(() => {
  const form = document.querySelector('#photo-search-form');
  if (!form) return;
  const result = document.querySelector('#photo-search-result');
  form.addEventListener('submit', event => {
    event.preventDefault();
    result.replaceChildren();
    const input = document.querySelector('#photo-search-id').value.trim().toLowerCase();
    const digits = input.replace(/^image_id_/, '');
    const id = /^\d+$/.test(digits) ? 'image_id_' + digits.padStart(3, '0') : '';
    const entry = Object.entries(window.EWA_PHOTO_IDS || {}).find(([, value]) => value === id);
    if (!entry) {
      result.textContent = 'Brak aktywnego zdjęcia o tym ID. Sprawdź numer; zdjęcie mogło zostać usunięte.';
      return;
    }
    const [path] = entry;
    const label = document.createElement('p');
    label.textContent = id;
    const link = document.createElement('a');
    link.href = "/" + path;
    link.target = '_blank';
    link.rel = 'noopener';
    link.textContent = 'Otwórz oryginalne zdjęcie';
    const image = document.createElement('img');
    image.src = "/" + path;
    image.alt = 'Podgląd zdjęcia ' + id;
    image.style.cssText = 'display:block;max-width:100%;max-height:65vh;width:auto;height:auto;margin:1rem auto;object-fit:contain';
    result.append(label, image, link);
  });
})();
