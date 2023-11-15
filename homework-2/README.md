
# Programowanie w Pythonie - Konwersatorium
## Zadanie domowe #2

Tematem przewodnim ostatniego zadania domowego jest programowanie obiektowe w Pythonie, praca z plikami, obsługa sytuacji wyjątkowych (ang. exceptions handling) oraz korzystanie z wybranych modułów biblioteki standardowej Pythona.

Zaliczenie zadania polega na zaprezentowaniu odpowiedniego kodu, uruchomienia go i omówienia go we wskazanym zakresie. Rozwiązanie każdego zadania powinno zawierać się w oddzielnym pliku (np. zad1.py, itp) tak, aby interpreter mógł dany program uruchomić (np. python zad1.py). Zadania można rozwiązywać indywidualnie (zalecany sposób) lub z w większej grupie.

## Literatura uzupełniająca

Oprócz prezentacji konwersatoryjnych w sekcji Pliki, proszę o zapoznanie się z rozdziałami 7-10 samouczka programowania w Pythonie (Python Tutorial) dostępnego pod tym [adresem](https://docs.python.org/3/tutorial/index.html). Przydatne jest również zapoznanie się z opisem [wyrażeń regularnych w Pythonie](https://docs.python.org/3/howto/regex.html) (por. [moduł re](https://docs.python.org/3/library/re.html) w bibliotece standardowej). Niektóre zadania mogą wymagać wykorzystania modułów stat, os, os.path, time oraz datetime ze standardowej biblioteki Pythona.

## Zadania programistyczne

1. W sekcji Pliki znajduje się plik PF00061-seed.fasta zawierający tzw. dopasowanie zalążkowe wielu sekwencji białek ewolucyjnie spokrewnionych ze sobą (tu: lipokaliny). Informacje dot. formatu pliku zawarte są np. w [artykule Wikpiedii](https://pl.wikipedia.org/wiki/FASTA_format). W analizowanym pliku miejsca przerw w dopasowaniu zaznaczone są w sekwencjach znakiem "-". Napisać program, który wczyta zawartość tego pliku i zachowa go w postaci słownika, gdzie kluczem będzie nazwa sekwencji (pierwszy ciąg znaków bez spacji po znaku >) a wartością sama sekwencja aminokwasowa reprezentowana przez jednoliterowe wielkie litery (zachowując sekwencje użytkownik powinien mieć możliwość wyboru czy zachowuje sekwencje ze znakami przerw czy te znaki powinny być usuwane). Następnie dla jednej z wczytanych sekwencji (tj. sekwencja bez przerw) zostanie wyznaczony średni skład aminokwasowy (tj. względny odsetek reszt aminokwasowych jednego typu). Wyniki obliczeń powinny być wydrukowane dla wszystkich 20 rodzajów aminokwasów tworzących białka syntetyzowane rybosomalnie.

2. W sekcji Pliki znajduje się plik 4boe.pdb zawierający informacje o strukturze pewnego białka (lipokaliny) wiążącego cholesterol. Napisać program, który będzie definiował klasę dla pliku PDB. Informacje dotyczące formatu PDB dostępne są na [tej stronie](http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html) (UWAGA: na potrzeby rozwiązania tego zadania wystarczy zapoznać się z opisem pól SEQRES, ATOM oraz HETNAM). Szablon klasy zawarty jest w udostępnianym pliku PDB.py. Proszę odpowiednio rozwinąć definicje metod read, getSequence oraz getAtoms. Jako ilustrację działania programu proszę wczytać analizowany plik 4boe.pdb a następnie zapisać sekwencję aminokwasową białka w formacie FASTA. Program powinien również wyświetlać podstawowe informacje o zawartości wczytanego pliku PDB (tj. liczbę łańcuchów polipeptydowych, liczbę atomów białka, a także: liczbę, nazwy chemiczne i wzory stechiometryczne cząsteczek nie będących białkami a zawartych w analizowanym pliku(por. HETNAM, FORMUL)). Wskazówka: warto tu wykorzystać wyrażenia regularne i moduł re.

3. W sekcji Pliki znajduje się archiwum plikowe bitwy.zip zawierające kilka plików graficznych w różnych formatach rastrowych. Proszę rozkompresować to archiwum i napisać program, który wyświetli (1) wielkość w bajtach największego i najmniejszego pliku, (2) nazwę najnowszego pliku (data ostatniej modyfikacji).

4. Napisać program, który wyznaczy liczbę dni między dwiema datami podanymi przy uruchamianiu programu z linii poleceń w formacie DD-MM-YYYY. W szczególności proszę wyznaczyć liczbę dni między datami bitwy pod Grunwaldem (15. lipca 1410) oraz bitwy warszawskiej (przyjmijmy tu datę 15. sierpnia 1920). Przykładowe polecenie uruchmienia programu (zad4.py) powinno zatem wyglądać następująco:

```python zad4.py 15-07-1410 15-08-1920```
