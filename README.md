# Skrypty do obsługi ewidencji książek należących do biblioteki KMS UJ
To repozytorium zawiera skrypty, które mają być pomocą przede wszystkim dla bibliotekarza. Poniżej znajduje się opis poszczególnych plików.

## ewidencja.txt
Pierwsze 3 kolumny z ewidencji (czyli: sygnatura, autor, tytuł) oddzielone tabulatorami.

## braki.py
Sprawdza, czy w ewidencji znajdują się ,,dziury'', czyli np. istnieją sygnatury A-010-a oraz A-012-a, ale nie ma A-011-a. Korzysta do tego z ewidencja.txt.

## biblioteka.py
Generuje listę potrzebnych do wydrukowania naklejek z odpowiednimi sygnaturami dla określonej liczby książek z pliku in_biblioteka.txt. Korzysta do tego ze znalezionych przez skrypt braki.py ,,dziur''.

## in_biblioteka.txt
W kolejnych liniach zawiera książki z poszczeególnych działów, dla których trzeba wydrukować naklejki (i których analogiczne egzemplarze jeszcze nie występują w ewidencji!). Przykładowo linia o treści
10 2 3
oznacza, że do działu dodamy 10 książek, z czego 2 są egzemplarzami jednego tytułu, 3 są egzemplarzami drugiego, a pozostałe 10-2-3=5 to pojedyncze tytuły.

## powtórki.py
Znajduje powtó©ki w ewidencji, czyli egzemplarze tego samego tytułu (i autorów) o różniących się sygnaturach. Generuje listę nowych naklejek, które należałoby wydrukować, aby tę sprawę naprawić.
