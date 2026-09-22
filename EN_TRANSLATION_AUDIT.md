# Weryfikacja EN — 2026-09-21

Status: teksty stron i interakcje przetłumaczone, sprawdzone lokalnie. Podgląd 1.68, bez push i bez publikacji.

| Strona | Treść EN i wspólny nagłówek | JS / lokalne zasoby |
| --- | --- | --- |
| index.html | OK | 0 błędów |
| kontakt.html | OK | 0 błędów |
| vedic-art.html | OK | 0 błędów |
| mandala.html | OK | 0 błędów |
| anioly.html | OK | 0 błędów |
| numerologia.html | OK | 0 błędów |
| tworczosc.html | OK | 0 błędów |
| kolorowanki.html | OK | 0 błędów |
| jedwab-malowany.html | OK | 0 błędów |
| o-mnie.html | OK | 0 błędów |
| ebooki.html | OK | 0 błędów |
| admin.html | OK | 0 błędów |
| oferta-2026.html | OK | 0 błędów |

Sprawdzono teksty DOM, także zamkniętych sekcji, opisy dostępności i teksty dodane przez skrypty. Kontrola porównuje frazy z lokalnym słownikiem; dodatkowo przejrzano pozostałe frazy po renderowaniu. Nazwy własne, ID i adresy plików zachowują oryginalną pisownię.

Testy interakcji przeszły: błędne hasła i wejście do lokalnego Admina, puste oraz poprawne dane we wszystkich kalkulatorach, aktywne i wycofane ID, otwarcie/nawigacja/zamknięcie galerii, filtry, próbki oferty, błąd hasła e-booka, przygotowanie druku A4 (bez fizycznego wydruku), pierwsza wizyta i zapamiętanie wyboru, PL→EN→PL. Użyto wyłącznie danych testowych; nie wysyłano płatności.

Przełącznik nie nakłada się na branding i menu przy 1365, 820, 390 i 320 px. Sprawdzono zrzuty strony głównej na desktopie i telefonie. Wbudowana przeglądarka pokazuje aktualny podgląd EN.

Kontrole projektu: `python3 scripts/site_build.py` i `python3 scripts/site_qa.py` — 0 błędów i 0 ostrzeżeń. Build nie korzysta z Google Translate ani innych usług tłumaczenia; nowa fraza statyczna bez odpowiednika EN przerywa generowanie.

## Powtórzenie testów

Uruchom lokalny serwer `python3 -m http.server 8767 --bind 127.0.0.1` z katalogu repo. Mając Playwright dostępny dla Node, uruchom:

```sh
node scripts/check_english_browser.cjs
node scripts/check_english_interactions.cjs
```

Opcjonalne `CHROME_EXECUTABLE` wskazuje zainstalowany Chrome zamiast Chromium Playwright. Pierwszy test obsługuje również `PREVIEW_URL` (domyślnie http://127.0.0.1:8767). Raporty zapisuje w /tmp/ewa-browser-report.json i /tmp/ewa-interaction-text.txt.

## Granice tej zmiany

Przetłumaczono strony HTML i interfejs, nie przygotowano nowych wydań oryginalnych PDF ani nie przemalowywano napisów w obrazach/kolorowankach. W EN zaznaczono język oryginalnego e-booka. To kontrola funkcjonalna tłumaczenia, nie redakcja merytoryczna twierdzeń autorki ani test zewnętrznego procesu płatności.

Zmiany są w lokalnym repo `colorings-from-ewa-release`, nie w repo Development. Wersja 1.68 była numerem podglądu do chwili akceptacji. Użytkownik zatwierdził publikację 2026-09-22; status remote i wdrożenia zostanie zapisany po ich weryfikacji. Dokładne tokeny i koszt USD: niedostępne (null w trackingu).
