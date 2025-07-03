def numer(sygnatura : str) -> str:
        return sygnatura[0:5]
    
class ksiazka:
    def __init__(self, list : list[str]):
        self.sygnatura : str = list[0]
        self.autor : str  = list[1]
        self.tytul : str = list[2]

def main():
    from itertools import groupby

    pozycje : list[ksiazka]= []
    
    # Wczytujemy linie z pliku jako listy
    with open("ewidencja.txt") as file:
        for line in file:
            pozycje.append(ksiazka(line.split(sep='\t')))

    # Usuwamy puste tytuły
    pozycje = [x for x in pozycje if x.tytul!='']
    
    # Sortujemy (!!! sortowanie może źle uwzględniać autorów)
    pozycje.sort(key = lambda s : (s.tytul,s.autor))
    
    # Grupujemy pozycje o tych samych tytułach i tych samych autorach
    podejrzani : list[tuple[list[str],tuple[str,str]]]= [([a.sygnatura for a in list(g)],k) for (k, g) in groupby(pozycje,lambda s : (s.tytul,s.autor))]

    # Sprawdzamy istnienie powtórek
    podejrzani = [p for p in podejrzani if numer(p[0][0]) != numer(p[0][len(p[0])-1])]

    # Sortujemy podług kategorii
    podejrzani.sort(key = lambda s : s[0][0])

    # Sprawdzamy, jakie naklejki trzeba dodrukować
    naklejki = []
    for (syg,_) in podejrzani:
        naklejki.append(list(set([syg[0][0:6] + chr(i) for i in range(97,97+len(syg))]) - set(syg)))

    # Wypisujemy wszystkie powtórki
    for (syg,pozycja) in podejrzani:
        print(syg,pozycja[1] + ';', pozycja[0])
        
    # Wypisujemy wszystkie naklejki, które trzeba dodrukować
    for n in naklejki:
        for x in n:
            print(x, end=' ')
        print()
    print()
        
    # Wypisujemy wszystkie naklejki, które trzeba dodrukować, w jednej linii
    for n in naklejki:
        for x in n:
            print(x, end=' ')
    print()

if __name__ == "__main__":
    main()