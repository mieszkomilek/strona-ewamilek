(() => {
  const list = document.querySelector('#admin-change-history-list');
  if (!list) return;

  fetch('/data/admin-change-history.json', { cache: 'no-store' })
    .then(response => {
      if (!response.ok) throw new Error('Nie udało się pobrać historii zmian.');
      return response.json();
    })
    .then(data => {
      list.replaceChildren();
      for (const item of data.versions || []) {
        const article = document.createElement('article');
        article.className = 'admin-output';
        const heading = document.createElement('h3');
        heading.textContent = `Wersja ${item.version} — ${item.title}`;
        const date = document.createElement('small');
        date.textContent = item.date;
        const description = document.createElement('p');
        description.textContent = item.description;
        article.append(heading, date, description);
        list.append(article);
      }
      if (!list.children.length) list.textContent = 'Brak zapisanych zmian.';
    })
    .catch(() => {
      list.textContent = 'Historia zmian jest chwilowo niedostępna.';
    });
})();
