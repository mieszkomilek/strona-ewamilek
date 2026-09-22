# PROJECT_BRAIN — Strona Ewa Miłek

Ten plik jest **Second Brain projektu**. Ma być pierwszym dokumentem czytanym przy wejściu do repozytorium w nowym czacie AI, przez nowego developera lub podczas powrotu do projektu po przerwie.

> Zasada utrzymania: gdy w projekcie zostaje podjęta nowa trwała decyzja dotycząca produktu, treści, architektury, płatności, SEO, wersjonowania, brandingu, zabezpieczeń lub workflow — **zaktualizuj również ten plik**.

## 1. Cel projektu

Repozytorium `mieszkomilek/strona-ewamilek` zawiera statyczną stronę Ewy Miłek hostowaną przez GitHub Pages pod domeną:

- `https://ewamilek.pl/`

Projekt ma dwa cele:

1. rozwijać stronę Ewy Miłek jako wysokiej jakości stronę sprzedażowo-wizerunkową,
2. służyć jako wzorzec / starter do budowania kolejnych stron o innej tematyce.

## 2. Marka i komunikacja

Aktualny branding nagłówka:

- nazwa: **Ewa Miłek**
- tagline: **Sztuka, która prowadzi do wnętrza**

Stylistyka:

- premium, lekka, kobieca,
- płowy / pudrowy róż,
- lawenda,
- indygo,
- delikatny glassmorphism,
- subtelne motywy: motyle, kwiaty, anioły, liczby numerologiczne, pędzle i znaki twórcze,
- animacje mają być spokojne i respektować `prefers-reduced-motion`,
- obiekty w dynamicznym headerze mają być wyraźnie widoczne: większe niż pierwotnie i w mocniejszym, ale nadal eleganckim różowo-śliwkowym tonie, aby nie ginęły na płowym tle.

Nie zmieniać oryginalnych treści Ewy bez wyraźnej zgody. Można zmieniać układ, prezentację i technologię.

## 3. Architektura

Strona jest statyczna i publikowana przez GitHub Pages.

Najważniejsze pliki:

- `index.html` — strona główna,
- `admin.html` — prywatny panel narzędzi Ewy,
- `oferta-2026.html` — robocza oferta,
- `numerologia.html`, `vedic-art.html`, `mandala.html`, `anioly.html`, `jedwab-malowany.html`, `o-mnie.html`, `ebooki.html`, `kontakt.html` — główne działy,
- `site.config.json` — wspólna konfiguracja domeny i nawigacji,
- `data/catalog.json` — dane katalogowe niezależne od płatności,
- `styles.css` — globalny styl,
- `assets/js/core.js` — podstawowy UI,
- `assets/js/effects.js` — efekty wizualne,
- `assets/js/numerology.js` — obliczenia numerologiczne,
- `assets/js/ebooks.js` — biblioteka e-booków,
- `assets/js/offer-admin-knowledge.js` — rozszerzenia Oferta 2026 / Admin i źródła wiedzy,
- `assets/js/admin-offer-complete.js` — kontrola kompletności modułów,
- `assets/js/site-shell.js` — wspólny branding, artystyczny header i wspólne reguły dostępu,
- `scripts/site_build.py` — build i normalizacja wdrożenia,
- `scripts/site_qa.py` — kontrola jakości,
- `.github/workflows/pages.yml` — główny deployment GitHub Pages.

## 4. Zasada wdrożeń

Nie tworzyć kolejnych jednorazowych workflowów `*-once.yml`, jeśli można wykonać zmianę bezpośrednio w kodzie lub przez główny build.

Historycznie jednorazowe workflowy powodowały błędy YAML i czerwone powiadomienia GitHub Actions.

Aktualny standard:

1. zmiana w `main`,
2. zakończenie `Bump site version` (numer, historia i tag), następnie główny Pages uruchamiany przez `workflow_run`,
3. `scripts/site_build.py`,
4. `scripts/site_qa.py`,
5. upload artefaktu,
6. deploy GitHub Pages.

Główny workflow: `.github/workflows/pages.yml`.

## 5. Wersjonowanie i rollback

Publiczna wersja strony znajduje się w:

- `version.txt`

Historia punktów przywracania:

- `VERSION_HISTORY.md`

Tagi wersji:

- `site-vX.XX`

Użytkownik może poprosić np.:

> przywróć wersję 1.24

Po każdej zmianie strony w odpowiedzi dla użytkownika należy podać:

- **Wersja: X → Y**

Nie zgadywać numeru po deployu — jeśli to możliwe, sprawdzić `version.txt`.

Każdy nowy wpis w `VERSION_HISTORY.md` ma zawierać również **krótki, zrozumiały opis słowny zmiany**, a nie wyłącznie techniczny punkt przywracania. Workflow `.github/workflows/bump-site-version.yml` pobiera opis z tytułu commita źródłowego i zapisuje go w kolumnie `Opis zmian`. Opisy commitów przy zmianach strony powinny więc być krótkie, konkretne i czytelne dla człowieka.

## 6. SEO

Domena produkcyjna i wszystkie canonicale mają wskazywać:

- `https://ewamilek.pl/`

Nie używać jako canonical adresu GitHub Pages.

`robots.txt` ma wskazywać:

- `https://ewamilek.pl/sitemap.xml`

`admin.html`, `oferta-2026.html` i inne strony robocze/prywatne nie powinny być indeksowane.

Build utrzymuje:

- canonical,
- `og:url`,
- sitemap,
- robots,
- BreadcrumbList.

## 7. Hasła / dostęp

Obowiązujący standard dla wszystkich prostych bramek dostępu na statycznej stronie:

- **YYYYMMDD**

Przykład dla 8 września 2026:

- `20260908`

Nie używać już `YYYYMM`.

Aktualnie dotyczy to co najmniej:

- `Admin`,
- `Oferta 2026`,
- e-booków / prywatnych czytników.

To zabezpieczenie jest wyłącznie lekką ochroną po stronie klienta. GitHub Pages nie zapewnia serwerowego uwierzytelniania. Nie przechowywać w Adminie danych klientów ani innych danych wrażliwych bez wdrożenia prawdziwego backendowego auth.

## 8. Admin — zakres

Admin ma być praktycznym panelem pracy Ewy i zawierać indeks prowadzący do wszystkich modułów.

Aktualny docelowy indeks:

1. Wibracja z Imienia i Nazwiska,
2. Oferta – Portret Numerologiczny,
3. Oferta – Portret MIKRO,
4. Oferta – Rok osobisty,
5. Oferta – Analiza imion / nazw firmy,
6. Generator interpretacji,
7. Oferta – Numerologiczny Plan Roku,
8. Oferta – Prognoza 9-letniego cyklu,
9. Oferta – Portret Partnerski,
10. Oferta – Portret Numerologiczny Dziecka,
11. Oferta – Numerologia Kariery i Talentów,
12. Oferta – Numerologia dla Firmy,
13. Oferta – Data startu firmy / projektu.

Moduły, które mogą być liczone deterministycznie, mogą działać już online. Interpretacje, rekomendacje i łączenie znaczeń mają być zasilone później dokumentami Ewy.

Generator interpretacji pozostaje oznaczony:

- `Do przygotowania`,
- `Wiedza do zasilenia`.

## 9. Źródła wiedzy

Przy produktach i modułach Admin należy pokazywać sekcję:

- **Linki do oficjalnej bazy wiedzy**

Dla numerologii należy jasno zaznaczać, że nie istnieje jedna oficjalna norma. Źródła publiczne są referencyjne, a docelową bazą interpretacji mają być materiały Ewy.

Dla Vedic Art preferować oficjalne źródła `vedicart.com` i nie tworzyć automatycznego nagranego kursu przedstawianego jako pełny oficjalny Vedic Art bez potwierdzenia zasad i uprawnień.

## 10. Oferta 2026

Oferta 2026 jest robocza, chroniona hasłem i `noindex`.

Poza istniejącymi produktami rozwijane są m.in.:

- Twój Rok Osobisty 2027,
- Numerologiczny Plan Roku,
- Portret Partnerski,
- Numerologia Kariery i Talentów,
- Numerologia dla Firmy — wybór nazwy,
- Portret Numerologiczny Dziecka,
- Prognoza 9-letniego cyklu,
- Numerologiczna data startu firmy / projektu,
- Mandala Twojej Wibracji,
- Warsztaty tematyczne Ewy.

Ceny nowych koncepcji są robocze do zatwierdzenia przez Ewę.

## 11. PayPal — ważna granica

Aktualne płatności PayPal pozostają bez zmian, dopóki użytkownik wyraźnie nie poprosi o ich modyfikację.

W wielu miejscach używany jest obecnie wspólny link NCP PayPal.

Nie zmieniać istniejących linków, kwot ani formularzy podczas refaktorów SEO/UI/Admin.

Jeżeli w przyszłości tworzone są zasoby PayPal dla tej strony, ich nazwa ma zawierać dokładny ciąg:

- `ewamilek.pl`

Przykład:

- `ewamilek.pl - Portret Numerologiczny MIKRO`

## 12. Kontakt i social media

- email: `milekewa@o2.pl`
- Facebook: `https://www.facebook.com/milekewa`
- Instagram: `https://www.instagram.com/ewamilek.art`

## 13. Zasady dla przyszłego AI

Przy rozpoczęciu nowej sesji:

1. przeczytaj `PROJECT_BRAIN.md`,
2. przeczytaj `version.txt` i `VERSION_HISTORY.md`,
3. sprawdź `.github/workflows/pages.yml`,
4. jeśli praca dotyczy Admin/Oferty, sprawdź `admin.html`, `oferta-2026.html` i pliki `assets/js/*admin*` / `offer-admin-knowledge.js`,
5. nie cofaj ustaleń z tego pliku bez wyraźnego polecenia użytkownika,
6. po trwałej nowej decyzji zaktualizuj `PROJECT_BRAIN.md`,
7. po modyfikacji strony podaj zmianę wersji.

## 14. Ostatnie ustalenia

- Od wdrożenia rejestru kosztów obowiązuje tracking modeli, tokenów i USD dla zmian w main. Każda zmiana otrzymuje Deployment-ID i wpis w tracking/deployments.json. Zasady pomiaru i raportowania: DEPLOYMENT_COSTS.md; obowiązki agentów: AGENTS.md. Nieznane wartości mają null; budżety i ekwiwalent API pozostają oddzielone od rzeczywistego użycia i rachunku. Statystyki: python3 scripts/deployment_costs.py.
- Zaakceptowano budżet roboczy 65 000 tokenów dla kolorowanek i 91 zdjęć. Przed wdrożeniem zdjęć przedstawiamy tabelę nazw i rozmieszczenia. Budżet nie jest pomiarem zużycia.

- Wszystkie bramki dostępu przechodzą na `YYYYMMDD`.
- Branding nagłówka: **Ewa Miłek — Sztuka, która prowadzi do wnętrza**.
- Desktopowy header ma dynamiczne płowo-różowe tło z motywami sztuki, motyli, aniołów i numerologii; symbole mają być większe i bardziej kontrastowe niż w pierwszej wersji, ale nadal subtelne i premium.
- Górny indeks Admin ma zawsze pokazywać komplet 13 modułów.
- `VERSION_HISTORY.md` ma zawierać przy każdej nowej wersji krótki opis słowny tego, co zostało zmienione.
- Zdjęcia paralaksy na stronie głównej i „O mnie” używają 9 oryginalnych JPG w `assets/photos/`, bez rekompresji; mapowanie utrzymuje `assets/js/photo-parallax.js`.
- Incydent testowy 1.44 pozostaje w historii z czytelnym opisem; kolejna wersja usuwa plik testowy, bez cofania numerów i przepisywania tagów.
- Pierwsze zdjęcie „O mnie” ma mocną paralaksę (również na telefonie), kadr wyrównany do góry i nieruchomy wariant dla `prefers-reduced-motion`. Dynamicznie dodane zdjęcia rejestrujemy we własnym obserwatorze ujawniania, po wstawieniu do DOM.
- Build dodaje numer wersji do adresów CSS i JS zdjęć, aby po wdrożeniu przeglądarka pobierała aktualną paralaksę i poprawki galerii.
- Na „O mnie” używamy zdjęcia, na którym jest wyłącznie Ewa; zdjęcie z Czesławem i obrazami zostało usunięte z sekcji oraz repozytorium. Cały blok „Moja droga” pozostaje pod zdjęciem.
- Nie dotykamy PayPal przy tych zmianach.
- Galeria „Twórczość” zawiera 17 JPG dostarczonych przez użytkownika w `facebook-zdjecia-galeria-sztuki-ewa-milek/`, bez rekompresji. Zdjęcia pokazujemy w pełnych proporcjach, z dostępnym podglądem, nawigacją klawiaturą oraz filtrem „Obrazy” / „Pracownia i wystawy”.
- „Twórczość” jest publiczną stroną indeksowaną i znajduje się w sitemapie.
- Wspólne menu i stopka są utrzymywane w `templates/`, a build osadza je we wszystkich stronach. Pozycja „Kontakt” wygląda tak samo jak pozostałe pozycje menu.
- QA sprawdza lokalne `src` i `href`, komplet 17 zdjęć galerii oraz dotychczasowe krytyczne zasoby.
- Skrypty numerologii i e-booków są usuwane podczas buildu ze stron, które nie zawierają odpowiednich modułów.
- Audyt jakości 2026-09-10 usunął nieużywane WebP, zastępcze SVG, pusty `script.js` i zakończone automaty migracyjne. Utrzymujemy tylko workflow wersjonowania i Pages. JPG użytkownika pozostają bez rekompresji. Raport: `QUALITY_REVIEW.md`.
- Rejestracja domeny `ewamilek.pl` pozostaje w OVH. Autorytatywny DNS i zarządzanie strefą domeny są przenoszone do Cloudflare; w Cloudflare utworzono pełną strefę w statusie `pending` z nameserverami `alice.ns.cloudflare.com` i `nile.ns.cloudflare.com`. W OVH przyjęto ich ustawienie, a stare serwery `dns110.ovh.net` i `ns110.ovh.net` są w trakcie usuwania. Nie przenosimy rejestracji domeny do Cloudflare.
- Ochrona PDF pozostaje obecnie bez zmian. Docelowa realna ochrona wymaga autoryzacji po stronie serwera lub podpisywanych czasowo adresów; GitHub Pages nie zapewnia poufności pliku.

---

**Ten plik jest częścią architektury projektu, a nie jednorazową notatką. Aktualizuj go razem z projektem.**

## Kolorowanki i nowe zdjęcia

- Kolorowanki: kolorowanki.html, pięć PNG w assets/kolorowanki/, pobieranie i druk pojedynczego wzoru A4. Wzory wygenerowano AI dla strony, nie są reprodukcjami obrazów Ewy.
- Plan 91 zdjęć: PHOTO_PLACEMENT_PLAN.md. Nie publikować zdjęć przed przedstawieniem planu użytkownikowi; kadry muzealne wymagają rozstrzygnięcia zgodnie z wcześniejszym ograniczeniem publikacji cudzych obrazów.

## Wdrożenie 84 zdjęć z archiwum

- Użytkownik zatwierdził pominięcie zdjęć 003, 029, 039, 041, 048, 087, 090 i publikację pozostałych 84. Pominiętych plików nie dodajemy do repo.
- Oryginalne JPG bez rekompresji: assets/photos/ewa-milek/. Manifest data/photo-library.json zawiera nazwy, kategorie, podstrony i SHA-256. Każdy plik jest wspólny dla wszystkich podstron.
- Twórczość: 84 nowe zdjęcia oraz wcześniejsze 17, filtry według jawnych kategorii. O mnie: 16 zdjęć w czterech grupach między tekstami. Mandala: 9 zdjęć obrazów i procesu tworzenia. Zdjęcia rodzinne mają oddzielną kategorię.
- Plan PHOTO_PLACEMENT_PLAN.md zachowuje informację o wszystkich 91 pozycjach i siedmiu pominięciach. Weryfikacja galerii obejmuje cały zatwierdzony manifest.

## Kolorowanki tematyczne i identyfikatory zdjęć

- Dział Kolorowanki zawiera 15 wzorów: wcześniejsze 5 i 10 nowych (harmonia, szczęście, dobrobyt, miłość, spełnienie, zdrowie, równowaga, pieniądze, przebaczenie, wdzięczność). Wbudowany image_gen; PNG do pobrania i druk pojedynczej karty A4, podpis ewamilek.pl. Prompty: assets/kolorowanki/prompts-10.json. Opisy symboliki są propozycją zabawy kolorami.
- Stałe identyfikatory zdjęć image_id_NNN: rejestr assets/js/photo-ids.js i dokument PHOTO_IDS.md. Podgląd pokazuje ID z przyciskiem kopiowania; obejmuje galerie Twórczość, O mnie, Mandala oraz wcześniejszą dolną galerię O mnie. Ten sam plik zachowuje ID między podstronami.
- Nigdy nie renumerować ani nie używać ponownie usuniętego ID. Przy zleceniu usunięcia po ID znaleźć wszystkie odwołania we wszystkich stronach. Nie usuwać zdjęć bez wskazania użytkownika.

## Mandale zamówione przez klientów

- 14 oryginalnych JPG z archiwum użytkownika w assets/photos/mandale-klientow/, bez rekompresji. Osobna podkategoria w mandala.html: „Mandale zamówione przez klientów”.
- Ewa potwierdziła autorstwo i wykonanie tych mandali na zamówienie w ostatnich latach. Nie używać tych prac jako kolorowanek ani do tworzenia kolorowanek.
- ID image_id_209–image_id_222 są stałe; podpisy opisują wygląd, nie są nadanymi przez Ewę tytułami obrazów. Mapa źródeł, SHA-256 i ograniczenie wykorzystania: data/mandale-klientow.json.

## Kolejne materiały kolorowanek

- Dodano zajawkę do albumu mandali na Facebooku, aby kierować odwiedzających do pełnej galerii.
- Istniejące 15 wzorów należą do tagu „kolorowanki Ewy z AI”. Trzy planowane opracowania z obrazów Ewy otrzymają osobny tag „kolorowanki z obrazów Ewy”; nie wolno używać mandali klientów jako kolorowanek bez osobnej decyzji.

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

## Historia zmian w panelu Admin

- Od wersji 1.66 panel Admin zawiera opisową historię ostatnich zmian, zasilaną przez `data/admin-change-history.json` i wyświetlaną przez `assets/js/admin-change-history.js`.
- Każde kolejne wdrożenie zmieniające stronę musi dodać na początku rejestru zrozumiały dla użytkownika wpis: numer wersji, datę, krótki tytuł i opis faktycznej zmiany.
- W wersji 1.66 usunięto ze wszystkich miejsc i bieżącego repo zdjęcia `image_id_025`, `image_id_040`, `image_id_086` i `image_id_207`. ID pozostają trwale wycofane.


## Kolorowanki z obrazów Ewy — 1.67

Dodano trzy zaakceptowane przez użytkownika konturowe opracowania załączonych obrazów: Sowy i róże, Umysł i ocean, Spirale i liście. To nazwy opisowe, nie potwierdzone tytuły oryginałów. Sekcja „Kolorowanki z obrazów Ewy” zawiera pobieranie PNG i druk pojedynczej karty A4, opisy oraz wskazówki kolorów i kredek. PNG zachowano bez rekompresji; podpis Ewa Miłek · ewamilek.pl jest w obrazie. Wcześniejsze 15 wzorów ma osobną sekcję „Kolorowanki Ewy z AI”. Pochodzenie i SHA-256: assets/kolorowanki/obrazy-ewy-manifest.json. Łącznie 18 kolorowanek.


## Przygotowanie wersji angielskiej — 2026-09-17
Rozpoczęto lokalne przygotowanie pełnej wersji EN według mechanizmu z repozytorium MikeMilekFitness: osobne strony w katalogu `/en/`, wspólny przełącznik języka `assets/js/language.js` oraz linki PL/EN w nagłówku. Wygenerowano lokalne kopie wszystkich podstron jako szkic do dalszej pełnej translacji treści. Każda przyszła zmiana wymaga odpowiednika PL i EN oraz aktualizacji obu wersji przed publikacją.

## Audyt EN — 2026-09-21 (w toku)
- Wersja EN nie jest jeszcze gotowa do publikacji: istnieją mieszane zdania PL/EN oraz teksty generowane przez JS.
- Wycofano uszkodzenia inline JavaScript i CSS w kopiach EN, odtwarzając kod z polskich źródeł; poprawiono względne ścieżki zasobów.
- Nie tłumaczyć kodu globalnymi zamianami słów. Docelowo używać pełnych fraz i osobno lokalizować interfejs dynamiczny.
- Wszystkie przyszłe zmiany treści wymagają PL i EN oraz weryfikacji obu wersji. Nie deklarować kompletności na podstawie samej obecności 13 plików.
- Próba użycia zewnętrznego Google Translate została odrzucona przed uruchomieniem; wymaga świadomej zgody użytkownika na wysłanie tekstów strony.
- Nie wykonano push ani wdrożenia. Dokładne tokeny i koszt USD tej pracy nie są dostępne.

## Wersja EN — wykonane lokalnie 2026-09-21
- Zastąpiono niekompletne kopie EN generowaniem wszystkich 13 stron z polskiego źródła i słownika pełnych fraz `data/i18n/en.json`. Tłumaczenia przygotował asystent bez zewnętrznej usługi tłumaczenia.
- Build odrzuca nowe statyczne teksty bez tłumaczenia. Dynamiczne galerie, opisy oferty, komunikaty i wyniki kalkulatorów, Admin oraz historia zmian są lokalizowane przez `scripts/english-runtime.js`. Nie modyfikować kodu przez globalne zamiany słów.
- Przełącznik PL/EN jest częścią układu nagłówka i zachowuje bieżącą podstronę, query oraz hash. Pierwsza wizyta pokazuje wybór języka, zapisywany w localStorage.
- Poprawiono ścieżki zdjęć, PDF, version.txt i historii zmian dla `/en/`. Identyfikatory i pliki fotografii pozostają wspólne. Oryginalne PDF i tekst w rastrach nie stanowią nowych tłumaczeń dokumentów.
- Wersja lokalna 1.68. Aktualizacja workflow synchronizuje numer ostatniego wpisu Admin podczas automatycznego bumpa, aby uniknąć istniejącego konfliktu version.txt / historii. Nie wykonano push ani deployu; numer lokalny nie potwierdza publikacji.
- Miejsce pracy: `colorings-from-ewa-release` w katalogu projektu Codex. Podgląd: http://127.0.0.1:8767/en/index.html. Zmiany nie zostały przeniesione do Development/Projects/Private/EwaMilek-Strona.
- Wcześniejsze notatki o niegotowości EN opisują stan sprzed tej korekty. Wynik i zakres końcowej weryfikacji: EN_TRANSLATION_AUDIT.md.
- Dokładne tokeny i USD pozostają nieznane; zapisano null, bez pozornego pomiaru.

## Akceptacja publikacji EN — 2026-09-22

- Użytkownik zaakceptował lokalny podgląd pełnej wersji angielskiej i zlecił zapisanie oraz publikację zmian na zdalne `main`.
- Publikacja ma zachować wcześniejsze wydanie 1.67 (kolorowanki z obrazów Ewy) i utworzyć kolejne wydanie 1.68 z pełną wersją EN.
- Po pushu należy potwierdzić identyfikator commitu na remote oraz osobno wynik automatycznego wdrożenia Pages; sam push nie jest potwierdzeniem publikacji strony.

## Dyplomy i certyfikaty — 2026-09-22

W „O mnie” dodano podkategorię „Moje Dyplomy i Certyfikaty” z kotwicą `#moje-dyplomy-i-certyfikaty` i skrótem u góry strony. Ścianka zawiera 17 oryginalnych JPEG z archiwum użytkownika, bez rekompresji, z pełnymi kadrami, opisowymi podpisami i wspólnym podglądem galerii. Stałe ID: image_id_223–image_id_239; działają również w przeglądarce Admin. Mapa pochodzenia i SHA-256: `data/certificates.json`. Galeria i podpisy mają wersję PL/EN. Opublikowano i zweryfikowano wersję 1.70 (2026-09-22): build i deploy Pages zakończone sukcesem; tag site-v1.70. Szczegóły w tracking/deployments.json.
