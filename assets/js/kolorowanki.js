(() => {
  const clear = () => {
    document.body.classList.remove('print-coloring');
    document.querySelectorAll('.selected-print').forEach(el => el.classList.remove('selected-print'));
  };
  document.querySelectorAll('[data-print]').forEach(button => {
    button.addEventListener('click', async () => {
      const card = document.getElementById(button.dataset.print);
      const img = card.querySelector('img');
      button.disabled = true;
      try {
        await img.decode();
        clear();
        card.classList.add('selected-print');
        document.body.classList.add('print-coloring');
        window.print();
      } catch {
        alert('Nie udało się wczytać obrazka. Spróbuj ponownie lub pobierz PNG.');
      } finally { button.disabled = false; }
    });
  });
  window.addEventListener('afterprint', clear);
})();
