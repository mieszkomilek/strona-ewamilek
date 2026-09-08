# Website Standard

Ten projekt jest bazą dla kolejnych statycznych stron. `site.config.json` jest źródłem domeny i ustawień SEO, `data/catalog.json` przechowuje dane oferty bez płatności, `scripts/site_build.py` generuje techniczne SEO, a `scripts/site_qa.py` kontroluje jakość. Nowy projekt powinien zmieniać konfigurację, treści i assety zamiast wpisywać domenę ręcznie w wielu plikach.

## Zasady
1. Produkcyjna domena jest ustawiana w `site.config.json`.
2. Sitemap, robots, canonical i `og:url` są generowane automatycznie.
3. Strony prywatne i podglądowe nie trafiają do sitemap.
4. Każda indeksowana strona ma jeden H1, title, description i self-canonical.
5. Runtime JS jest dzielony funkcjonalnie na core, effects, numerology i ebooks.
6. PayPal nie jest częścią tej warstwy i nie jest przez nią modyfikowany.
