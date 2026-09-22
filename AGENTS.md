# Zasady pracy nad stroną Ewy Miłek

- Przed pracą przeczytaj PROJECT_BRAIN.md, VERSION_HISTORY.md i DEPLOYMENT_COSTS.md.
- Każde wdrożenie do main musi mieć identyfikator `Deployment-ID` w treści commita oraz wpis w `tracking/deployments.json`.
- Zapisuj rzeczywiście użyte modele i źródło informacji o modelu. Model wybrany, którego uruchomienie nie powiodło się, oznacz jako nieuruchomiony.
- Oddzielaj budżet, szacunek i pomiar. Nieznane tokeny i koszty zapisuj jako null, nigdy jako zero.
- Koszt API obliczaj wyłącznie z potwierdzonych stawek dla dokładnego modelu i daty. Koszt abonamentu Codex nie jest kosztem API.
- Uwzględniaj osobno generowanie obrazów, narzędzia i ponowne próby. Nie sumuj ponownie tych samych liczników sesji.
- Po publikacji sprawdź commit, version.txt, tag i workflow Pages. Uzupełnij dane wdrożenia, kiedy są dostępne; sam commit nie oznacza udanego deployu.
- Aktualizuj opis projektu i second brain przy trwałych ustaleniach. Zachowuj istniejące zmiany użytkownika.
- Identyfikatory image_id_NNN w assets/js/photo-ids.js są trwałe. Nie renumeruj ich po zmianie kolejności, nie używaj ponownie wycofanych ID. Przy usunięciu po ID sprawdź wszystkie miejsca użycia. Zasady i mapa: PHOTO_IDS.md.
- Przy każdym wdrożeniu zmieniającym stronę dodaj opisowy wpis do `data/admin-change-history.json`, aby historię wersji można było przeczytać w panelu Admin.
- Strona jest dwujęzyczna: każda zmiana tekstu lub interakcji wymaga odpowiednika PL i EN. Polski HTML jest źródłem; `en/` generuje `python3 scripts/site_build.py` z pełnych fraz w `data/i18n/en.json`.
- Nie edytuj ręcznie plików `en/` ani wygenerowanego `assets/js/english.js`. Teksty dynamiczne obsługuje `scripts/english-runtime.js`; nigdy nie tłumacz kodu przez globalne zamiany słów.
- Przed potwierdzeniem kompletności EN sprawdź wszystkie 13 stron, galerie, formularze i PL→EN→PL. Brakujące tłumaczenia muszą blokować build. Dokumenty PDF i napisy wewnątrz oryginalnych obrazów są osobnymi materiałami, nie tekstem HTML.
