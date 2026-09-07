# Propozycja migracji treści ewamilek.pl

## Zasada nadrzędna — CONTENT LOCK

Treści źródłowe z ewamilek.pl są materiałem nadrzędnym.

Podczas migracji:
- nie przeredagowujemy tekstów,
- nie skracamy tekstów,
- nie dopisujemy nowych twierdzeń, opisów usług, historii ani informacji o Ewie,
- nie zmieniamy cen, terminów, parametrów usług ani danych kontaktowych,
- nie poprawiamy merytoryki „na podstawie wiedzy ogólnej”,
- zachowujemy oryginalne brzmienie tekstów.

Dozwolone zmiany dotyczą wyłącznie prezentacji:
- podział na sekcje,
- nagłówki techniczne/nawigacyjne, o ile nie zmieniają sensu treści,
- kolumny, karty, accordiony, galerie i wyróżnienia,
- typografia, odstępy, kolory i responsywność,
- linkowanie między podstronami,
- zajawki na stronie głównej wyłącznie z treści istniejących w materiale źródłowym.

## Docelowa mapa strony

1. Strona główna — `index.html`
2. Vedic Art — `vedic-art.html`
3. Mandala — `mandala.html`
4. Anioły — `anioly.html`
5. Numerologia — `numerologia.html`
6. Twórczość — `tworczosc.html`
7. Jedwab Malowany — `jedwab-malowany.html`
8. O mnie — `o-mnie.html`
9. Kontakt — `kontakt.html`

## Strona główna

Strona główna pozostanie stroną wejściową. Będzie zawierać krótsze fragmenty istniejących treści oraz wizualne wejścia do pełnych podstron.

Planowane wejścia:
- Vedic Art
- Mandala
- Anioły
- Numerologia
- Twórczość
- Jedwab Malowany
- O mnie
- Kontakt

Zajawki nie będą nowymi tekstami marketingowymi. Będą pochodzić z treści źródłowych.

## Podstrony

Każdy dział otrzyma osobny dokument HTML i zachowa kompletną treść odpowiadającego mu działu z ewamilek.pl.

Długie treści mogą być prezentowane za pomocą:
- sekcji tematycznych,
- kart,
- bloków wyróżnionych,
- elementów `details/summary`,
- tabel lub list,
- galerii.

Zmiana sposobu prezentacji nie może zmieniać kolejności logicznej ani znaczenia tekstu.

## Numerologia

Ze względu na objętość treści podstrona może korzystać z rozwijanych sekcji, m.in. dla opisów liczb. Tekst wewnątrz pozostaje bez zmian względem źródła.

## Media

Wszystkie media docelowo znajdują się w repozytorium w katalogu `assets/`.

Nie korzystamy z:
- Shopify CDN,
- zasobów hostowanych przez Shopify,
- zewnętrznych obrazów starego sklepu.

Jeżeli brakuje oryginalnego medium, nie zastępujemy go materiałem udającym oryginał. Zgłaszamy brak i ustalamy nazwę pliku do ręcznego dodania do `assets/`.

## Proces migracji

Dla każdego działu:
1. pobranie treści źródłowej,
2. zapis kopii treści bez zmian,
3. przypisanie treści do sekcji UI,
4. przygotowanie HTML,
5. kontrola tekstu źródło ↔ nowa podstrona,
6. kontrola mediów,
7. review w Pull Request,
8. dopiero po akceptacji merge do `main`.

## Kryterium akceptacji

Migracja danego działu jest poprawna, jeśli:
- wszystkie treści źródłowe zostały zachowane,
- nic merytorycznego nie zostało dopisane,
- ceny i dane są identyczne ze źródłem,
- media są lokalne,
- podstrona działa desktop/mobile,
- nawigacja prowadzi do właściwych działów,
- zmiany nie trafiają na produkcyjny `main` bez akceptacji Pull Request.
