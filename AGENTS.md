# Zasady pracy nad stroną Ewy Miłek

- Przed pracą przeczytaj PROJECT_BRAIN.md, VERSION_HISTORY.md i DEPLOYMENT_COSTS.md.
- Każde wdrożenie do main musi mieć identyfikator `Deployment-ID` w treści commita oraz wpis w `tracking/deployments.json`.
- Zapisuj rzeczywiście użyte modele i źródło informacji o modelu. Model wybrany, którego uruchomienie nie powiodło się, oznacz jako nieuruchomiony.
- Oddzielaj budżet, szacunek i pomiar. Nieznane tokeny i koszty zapisuj jako null, nigdy jako zero.
- Koszt API obliczaj wyłącznie z potwierdzonych stawek dla dokładnego modelu i daty. Koszt abonamentu Codex nie jest kosztem API.
- Uwzględniaj osobno generowanie obrazów, narzędzia i ponowne próby. Nie sumuj ponownie tych samych liczników sesji.
- Po publikacji sprawdź commit, version.txt, tag i workflow Pages. Uzupełnij dane wdrożenia, kiedy są dostępne; sam commit nie oznacza udanego deployu.
- Aktualizuj opis projektu i second brain przy trwałych ustaleniach. Zachowuj istniejące zmiany użytkownika.
