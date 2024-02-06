
# Programowanie w Pythonie - Konwersatoria
## Zadanie domowe #1

 Przygotowanie danych do analizy. W tym wypadku, będzie to
 kompletny tekst streszczenia w j. ang. dostępnego pod tym
 [adresem](https://pubmed.ncbi.nlm.nih.gov/33507760/). Zaznaczyć fragment
 streszczenia od słów "Phospholipid membranes support" do "the
 interfacial region.". Przypisać ten wielowierszowy tekst do obiektu
 abstract. W zadaniach poniżej, odwołujemy się zawsze do abstract jako
 obiektu zawierającego dane do analizy.

 Ilekroć mowa o "programie" poniżej, należy go rozumieć jako skrypt
 zawierający co najmniej jedną funkcję, który można uruchomić przez:
 python script.py (gdzie script.py to nazwa pliku z kodem). Każdy z
 programów powinien zawierać co najmniej jedno wykorzystanie listy
 składanej oraz jednej ze standardowych funkcji wyższego rzędu.

 Zaliczenie zadania będzie polegało na zaprezentowaniu odpowiedniego
 kodu, uruchomienia go i omówienia go we wskazanym
 zakresie.


 1. Napisać program, który wyświetli liczbę zdań, liczbę słów,
 najdłuższe słowo, najczęściej występujące słowo o długości co
 najmniej 5 znaków. UWAGA: analizowane słowa nie mogą zawierać znaków
 interpunkcyjnych (np. przecinek lub kropka na końcu) - dopuszczalne
 jest jednak występowanie znaków innych niż litery alfabetu w środku
 zdania (np. two-diemnsional).

 2. Napisać program, który wyświetli zawartość abstract w taki sposób,
 że każdy wiersz będzie zawierał dokładnie 55 znaków, poszczególne
 słowa nie będą dzielone, każdy wiersz będzie wyrównany do prawej
 strony (na początku każdego wiersza powinna być odpowiednia liczba
 spacji).

 3. Napisać program, który wyświetli abstract w taki sposób, że każde
 słowo w kolejnych zdaniach będzie zapisane wspak (np. "... yet remain
 ..." na " ... tey niamer ...". Najlepiej, aby do wyświetlenia
 odpowiednio przetworzonej zawartości abstract wykorzystać odpowiednią
 funkcję formatującą wydruk z zadania nr 2.

 4. Napisać program, który dla każdego zdania w abstract wygeneruje
 sekwencje długości kolejnych słów, wyświetli ją w jednym wierszu a na
 koniec policzy średnią długość słowa w analizowanym zdaniu.
