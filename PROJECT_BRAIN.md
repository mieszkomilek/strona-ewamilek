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

- Wszystkie bramki dostępu przechodzą na `YYYYMMDD`.
- Branding nagłówka: **Ewa Miłek — Sztuka, która prowadzi do wnętrza**.
- Desktopowy header ma dynamiczne płowo-różowe tło z motywami sztuki, motyli, aniołów i numerologii; symbole mają być większe i bardziej kontrastowe niż w pierwszej wersji, ale nadal subtelne i premium.
- Górny indeks Admin ma zawsze pokazywać komplet 13 modułów.
- `VERSION_HISTORY.md` ma zawierać przy każdej nowej wersji krótki opis słowny tego, co zostało zmienione.
- Zdjęcia paralaksy na stronie głównej i „O mnie” używają 9 oryginalnych JPG w `assets/photos/`, bez rekompresji; mapowanie utrzymuje `assets/js/photo-parallax.js`.
- Incydent testowy 1.44 pozostaje w historii z czytelnym opisem; kolejna wersja usuwa plik testowy, bez cofania numerów i przepisywania tagów.
- Nie dotykamy PayPal przy tych zmianach.

---

**Ten plik jest częścią architektury projektu, a nie jednorazową notatką. Aktualizuj go razem z projektem.**