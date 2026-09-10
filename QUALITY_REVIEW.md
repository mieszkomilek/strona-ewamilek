# Audyt jakości — 10 września 2026

Przegląd źródeł wersji 1.53, odwołań do plików i procesu publikacji. Nie jest to pomiar Lighthouse ani pełny audyt dostępności.

## Wykonane porządki

Usunięto 21 nieużywanych plików: 9 dawnych WebP, 2 zastępcze SVG, pusty script.js, 7 jednorazowych workflowów i 2 ich skrypty. Sprawdzono brak odwołań z HTML/CSS/JS/konfiguracji i bieżącego procesu publikacji. Usunięto także niedziałający fragment komentarza z literalnymi znakami \n w site_build.py; nie wykonywał żadnego kodu. Uaktualniono instrukcję zdjęć, sprzeczną z decyzją o JPG. Historia Git nadal zawiera wcześniejsze pliki — nie przepisywano historii ani tagów.

## Proponowane usprawnienia

1. **Wysoki priorytet — indeksowanie Twórczości.** Strona ma noindex,follow i figuruje jako privateOrPreviewPages w site.config.json, mimo opublikowanej galerii. Przenieść ją do stron publicznych, usunąć noindex i wygenerować sitemap oraz dane BreadcrumbList.
2. **Wysoki priorytet — sprawdzanie wszystkich zasobów.** Obecne QA sprawdza część stron i 8 zdjęć paralaksy. Dodać kontrolę lokalnych src/href, wszystkich 17 zdjęć galerii, powtórzonych identyfikatorów i menu po buildzie.
3. **Wysoki priorytet — dostęp do materiałów.** Hasło z daty działa tylko w przeglądarce; PDF jest publicznym plikiem. Jeśli materiały mają być faktycznie prywatne lub płatne, wymagają autoryzacji po stronie serwera.
4. **Średni priorytet — wspólne menu i stopka.** Zastąpić kopie w HTML jednym szablonem budowania. Kontakt nadal ma klasę nav-cta i odmienny styl; ujednolicić go z pozostałymi pozycjami zgodnie z wcześniejszą prośbą.
5. **Średni priorytet — stabilność i szybkość galerii.** Dodać width/height do zdjęć, aby rezerwować miejsce podczas ładowania. Rozważyć osobne miniatury dopiero po akceptacji użytkownika; oryginalne JPG zachować. Zmierzyć stronę na telefonie przed dalszą optymalizacją.
6. **Średni priorytet — porządek CSS i JS.** styles.css ma liczne nadpisania i !important; rozdzielić komponenty etapami z porównaniem wyglądu. Ładować numerologię, e-booki i moduły administracyjne tylko tam, gdzie są potrzebne.
7. **Średni priorytet — artefakt publikacji.** Pages publikuje katalog repozytorium. Budować oddzielny katalog wyjściowy zawierający tylko publiczne pliki, bez dokumentacji technicznej i skryptów.
8. **Niższy priorytet — redakcja i wygoda.** W O mnie występują powtórzenia tekstu; uzgodnić korektę z Ewą. Dodać przeglądarkę zdjęć ze strzałkami, Escape i obsługą klawiatury; obecnie powiększenie otwiera sam JPG.

## Zachowane materiały

Pozostawiono wszystkie używane JPG, PDF, dokumenty projektu, konfigurację, skrypty produkcyjne oraz historię wersji. Propozycje powyżej nie zostały wdrożone w ramach usuwania zbędnych plików. Płatności pozostają bez zmian.
