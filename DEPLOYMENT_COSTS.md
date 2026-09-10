# Historia kosztów wdrożeń

Rejestr: [tracking/deployments.json](tracking/deployments.json). Zestawienie: `python3 scripts/deployment_costs.py`.

Śledzimy koszt przygotowania zmian wdrażanych do main, z podziałem na modele. To nie jest automatyczny odczyt rachunku OpenAI. GitHub Actions nie zna zużycia rozmowy Codex; dane trzeba dostarczyć z wiarygodnego eksportu użycia lub rozliczeń. Procent wykorzystania limitu konta nie jest liczbą tokenów projektu.

Każdy wpis ma stały identyfikator, opis, wersję, SHA źródłowe, URL workflow i wynik deployu. Commit źródłowy zawiera `Deployment-ID: <id>`, dzięki czemu można go powiązać z wpisem bez zapisywania własnego SHA w tym samym commicie. Pola wersji i wyniku pozostają null do weryfikacji. Nie zakładaj sukcesu przed zakończeniem Pages.

Każdy element `usage` opisuje jeden model i rozłączny zakres pracy: tokeny wejściowe (łącznie z cache), cache, wyjściowe, kwotę faktycznie rozliczoną, oszacowanie ekwiwalentu API oraz źródła danych. Nieznane wartości mają null. Zero wolno wpisać tylko przy potwierdzonym zerowym użyciu lub koszcie. Liczniki narastające przeliczaj na różnice; nie dodawaj ponownie poprzednich tur. Rozumowanie wliczone w wyjście nie może być doliczane drugi raz.

Koszt ekwiwalentu API = ((input - cached_input) × stawka_input + cached_input × stawka_cache + output × stawka_output) / 1 000 000 + osobno rozliczane obrazy i narzędzia. Stawki wymagają źródła, daty, waluty USD i zgodności z dokładnym modelem oraz trybem rozliczenia. Brak danych oznacza brak kosztu, nie bezpłatne wdrożenie. Nie używaj cennika innego modelu. Nie sumuj ekwiwalentu API z rzeczywistym rachunkiem.

Zestawienie pokazuje osobno znane sumy i liczbę braków. Przy niepełnych danych suma jest częściowa. Koszt obrazów można zapisać w osobnym elemencie usage z modelem generatora i źródłem rozliczenia. Ponowne próby wliczaj tylko raz do zakresu pracy, również gdy kończą się błędem.

Budżet zaakceptowany dla pięciu kolorowanek i analizy/rozmieszczenia 91 zdjęć: 65 000 tokenów (wcześniejszy szacunek 35 000–65 000). Jest to plan, nie pomiar ani gwarancja twardego limitu platformy. Przed publikacją zdjęć należy pokazać użytkownikowi tabelę wszystkich 91 plików i proponowanych miejsc użycia.

Nie rekonstruujemy kosztów historycznych wdrożeń bez danych źródłowych. Nie publikujemy w repo pełnych rozmów, tokenów dostępu ani danych rachunku.

Źródła zasad rozliczeń: https://learn.chatgpt.com/docs/pricing oraz https://developers.openai.com/api/docs/pricing . Stawki należy sprawdzić ponownie w dniu kalkulacji.
