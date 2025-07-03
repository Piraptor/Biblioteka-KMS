from braki import braki, tytuly_w_dziale

def main():
    numery : list[list[int]] = []
    
    # Wczytujemy linie z pliku jako listy
    with open("in_biblioteka.txt") as file:
        for line in file:
            numery.append(list(map(int,line.split())))

    print(end="\t")
    
    pusta_sygnatura : int
    numer : int
    
    for dzial in range(0,len(numery)):
        pusta_sygnatura = 0
        
        # Wypisujemy książki wielokrotne
        for tytul in range(1,len(numery[dzial])):
            # Ustalamy numer tytułu w sygnaturze
            if pusta_sygnatura < len(braki[dzial][1]):
                numer = braki[dzial][1][pusta_sygnatura]
                pusta_sygnatura+=1
            elif pusta_sygnatura == len(braki[dzial][1]):
                numer = max(tytuly_w_dziale[dzial][1]) + 1
                pusta_sygnatura+=1
            else:
                numer+=1
                
            for k in range(0,numery[dzial][tytul]):
                print(chr(65+dzial),'-',f"{numer:03d}",'-',chr(97+k),end="\t",sep="")
                
        zrobione : int = sum(numery[dzial][1:])
        
        # Wypisujemy książki pojedyncze
        for _ in range(0,numery[dzial][0]-zrobione):
            # Ustalamy numer tytułu w sygnaturze
            if pusta_sygnatura < len(braki[dzial][1]):
                numer = braki[dzial][1][pusta_sygnatura]
                pusta_sygnatura+=1
            elif pusta_sygnatura == len(braki[dzial][1]):
                numer = max(tytuly_w_dziale[dzial][1]) + 1
                pusta_sygnatura+=1
            else:
                numer+=1
                
            print(chr(65+dzial),'-',f"{numer:03d}",'-','a',end="\t",sep="")
            
    print()

if __name__ == "__main__":
    main()