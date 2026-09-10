# Ewa Miłek — nowa wersja strony

Statyczna, responsywna strona przygotowana pod GitHub Pages.

Projekt prowadzi historię modeli AI, zużycia tokenów i kosztów USD przypisanych do wdrożeń na main. Zasady: [DEPLOYMENT_COSTS.md](DEPLOYMENT_COSTS.md), dane: [tracking/deployments.json](tracking/deployments.json), instrukcje dla agentów: [AGENTS.md](AGENTS.md). Brak pomiaru jest oznaczany jawnie; szacunki nie są rachunkiem.

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

Zdjęcia są przechowywane w repozytorium. Nowy zestaw 84 oryginalnych JPG znajduje się w `assets/photos/ewa-milek/`, a wcześniejsze 17 w `facebook-zdjecia-galeria-sztuki-ewa-milek/`. Strona nie powinna zależeć od zasobów starego Shopify.

`data/photo-library.json` opisuje nazwy, kategorie, miejsca użycia i sumy SHA-256 nowego zestawu. Twórczość pokazuje wszystkie 101 zdjęć; wybrane 16 wzbogaca O mnie, a 9 dział Mandala. Podstrony korzystają z tych samych plików bez rekompresji. Siedem zdjęć muzealnych pominięto zgodnie z decyzją użytkownika; pełny plan zawiera `PHOTO_PLACEMENT_PLAN.md`.
