from itertools import groupby

sygnatury : list[tuple[str,int]] = []

# Wczytujemy linie z pliku jako listy
with open("ewidencja.txt") as file:
    for line in file:
        sygnatury.append((line[0],int(line[2:5])))

# Usuwamy powtórki        
sygnatury = list(dict.fromkeys(sygnatury))

# Grupujemy względem działu
tytuly_w_dziale : list[tuple[str,list[int]]] = [ (d,[x for (_,x) in list(t)]) for (d,t) in groupby(sygnatury, lambda s : s[0])]

# Znajdujemy braki
braki : list[tuple[str,list[int]]] = [ (d,list(set(range(1,max(t))) - set(t))) for (d,t) in tytuly_w_dziale]

# Odfiltrowujemy działy bez braków
braki_niepuste = [ (d,t) for (d,t) in braki if t!=[]]
    
def main():
    for (d,t) in braki_niepuste:
        for x in t:
            print(d + '-' + f"{x:03d}" + '-a')
    
if __name__ == "__main__":
    main()
