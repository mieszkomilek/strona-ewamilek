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

## Kolorowanki i wybór zdjęć do zmian

15 kolorowanek z opisami, PNG i drukiem A4 znajduje się w dziale Kolorowanki. Zdjęcia w podglądzie galerii mają stałe identyfikatory i przycisk „Kopiuj ID”; do zlecenia usunięcia wystarczy podać np. image_id_023. Rejestr i zasady: PHOTO_IDS.md.

Dział Mandala ma też osobną galerię „Mandale zamówione przez klientów”: 14 oryginalnych JPG w assets/photos/mandale-klientow/, ID image_id_209–image_id_222. Manifest: data/mandale-klientow.json. Te prace nie są przeznaczone do kolorowanek.

## Usunięcie zdjęć i naprawa publikacji — 2026-09-15

Na prośbę Ewy usunięto 30 unikalnych zdjęć ze wszystkich stron, rejestru aktywnych ID i bieżących plików repozytorium. Wycofane ID i skróty plików: `data/retired-photo-ids.json`; nie wolno ich ponownie używać ani przywracać kopii tych zdjęć bez nowej zgody. Historia Git nie jest przepisywana.

| Galeria | Przed | Po | Usunięte |
|---|---:|---:|---:|
| Twórczość | 101 | 71 | 30 |
| O mnie — zdjęcia w treści | 16 | 9 | 7 |
| Mandala | 23 | 20 | 3 |

Starsza dolna galeria O mnie pozostaje; 14 mandali klientów pozostaje. Pusta sekcja „Blisko natury” została usunięta. Aktualny manifest zawiera 57 zdjęć archiwum; starsza galeria Facebook zawiera 14.

Odtworzono osiem uszkodzonych plików (9 bajtów niepoprawnej zawartości UTF-8): Admin, Mandala, Kolorowanki, second brain, QA, tracking, CSS galerii i skrypt przeglądarki Admin. Dokumenty i strony odzyskano z ostatnich poprawnych wersji w historii; przeglądarkę ID odtworzono w istniejącej bramce Admin. Przywrócono utracone wiersze VERSION_HISTORY (w tym 1.62 i starsze), zachowując obecne 1.63/1.64. Nie cofamy numeru 1.64 ani tagów. QA kontroluje wycofane ID, identyczne kopie JPG i integralność plików tekstowych.

Rejestr kosztów odzyskany z historii nie pozwala odtworzyć brakujących pomiarów wcześniejszych prób; brak danych nie oznacza zerowego kosztu.


## Kolorowanki z obrazów Ewy — 1.67

Dodano trzy zaakceptowane przez użytkownika konturowe opracowania załączonych obrazów: Sowy i róże, Umysł i ocean, Spirale i liście. To nazwy opisowe, nie potwierdzone tytuły oryginałów. Sekcja „Kolorowanki z obrazów Ewy” zawiera pobieranie PNG i druk pojedynczej karty A4, opisy oraz wskazówki kolorów i kredek. PNG zachowano bez rekompresji; podpis Ewa Miłek · ewamilek.pl jest w obrazie. Wcześniejsze 15 wzorów ma osobną sekcję „Kolorowanki Ewy z AI”. Pochodzenie i SHA-256: assets/kolorowanki/obrazy-ewy-manifest.json. Łącznie 18 kolorowanek.
