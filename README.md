# Ewa Miłek — nowa wersja strony

Statyczna, responsywna strona przygotowana pod GitHub Pages.

## Najpierw przeczytaj — Second Brain projektu

Przy wejściu do projektu w nowym czacie AI albo po dłuższej przerwie zacznij od:

- [`PROJECT_BRAIN.md`](PROJECT_BRAIN.md) — aktualne ustalenia, architektura, branding, wersjonowanie, Admin, Oferta 2026, hasła, SEO, PayPal i zasady dla przyszłych zmian.
- `version.txt` — aktualna wersja publiczna.
- `VERSION_HISTORY.md` — historia punktów przywracania.

`PROJECT_BRAIN.md` jest dokumentem żywym: każda trwała decyzja projektowa powinna być dopisywana również tam.

## Uruchomienie lokalne

Otwórz `index.html` w przeglądarce albo uruchom:

```bash
python3 -m http.server 8080
```

Następnie otwórz `http://localhost:8080`.

## GitHub Pages

Repozytorium: `mieszkomilek/strona-ewamilek`.

Aktualny deployment jest realizowany przez GitHub Actions (`.github/workflows/pages.yml`). Nie należy wracać do starych jednorazowych workflowów `*-once.yml` jako podstawowego mechanizmu zmian.

## Media

Wszystkie media używane przez stronę znajdują się lokalnie w katalogu `assets/`. Strona nie powinna zależeć od zasobów starego Shopify.
