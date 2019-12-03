import random

# création de la carte

Map1 = [
    [],[],[],[],[],[],[],[],[],[]
    ]

Map2 = [
    [],[],[],[],[],[],[],[],[],[]
    ]

abcs =["a","b","c","d","e","f","g","h","i","j"]
ordo =[0,1,2,3,4,5,6,7,8,9]

for i in range(len(ordo)):
    for j in range(len(abcs)):
        Map1[i].append(abcs[j]+str(ordo[i]))

for i in range(len(ordo)):
    for j in range(len(abcs)):
        Map2[i].append(abcs[j]+str(ordo[i]))

def show_map(x):
    print(x[0])  
    print(x[1])  
    print(x[2])  
    print(x[3])  
    print(x[4]) 
    print(x[5]) 
    print(x[6]) 
    print(x[7]) 
    print(x[8]) 
    print(x[9])


# placement des bateaux du joueur

bateaux = {
    "porte-avion" : 5,
    "croiseur" : 4,
    "sous-marin" : 3,
    "destroyer1" : 2,
    "destroyer2" : 2
    }

bateaux_list = ["porte-avion","croiseur","sous-marin","destroyer1","destroyer2"]

pos1 = []
pos2 = []
bas = []

for i in bateaux:
    while True:
    #for i in bateaux:
        pcoo = input(f"quelles coordonnées de la première case du {i} ? ")
        ori = input(f"quelle orientation pour le {i}, droite ou bas ? ")
        if ori == "droite":
            if bateaux[i] <= len(abcs[abcs.index(pcoo[0]):]):
                if "X" in Map1[int(pcoo[1])][abcs.index(pcoo[0]):abcs.index(pcoo[0])+bateaux[i]]:
                    print("il y a déjà un tas de merde dans ce coin")
                    #continue
                else:
                    for j in Map1[int(pcoo[1])][abcs.index(pcoo[0]):abcs.index(pcoo[0])+bateaux[i]]:
                        Map1[int(pcoo[1])][abcs.index(j[0])] = "X"
                        pos1.append(j) 
                    show_map(Map1)
                    break
            else:
                print("ton tas de merde est trop long")
                #continue
        elif ori =="bas":
            if bateaux[i] <= len(ordo[int(pcoo[1]):]):
                for j in Map1[int(pcoo[1]):int(pcoo[1])+bateaux[i]]:
                    if "X" in Map1[Map1.index(j)][abcs.index(pcoo[0])]:
                        print("il y a déjà un tas de merde dans ce coin")
                        break                       
                    else:
                        bas.append(j[abcs.index(pcoo[0])])
                        if len(bas) == bateaux[i]:
                            for u in Map1[int(pcoo[1]):int(pcoo[1])+bateaux[i]]:
                                pos1.append(u[abcs.index(pcoo[0])])
                                Map1[Map1.index(u)][abcs.index(pcoo[0])] = "X"
                                bas=[] 
                            if bateaux_list.index(i) == 4:
                                break
                            else:
                                i = bateaux_list[bateaux_list.index(i)+1]    
                            
                        else:
                            continue                       
                    show_map(Map1)  
                #break
            else:
                print("ton tas de merde est trop long")

print(bas)               
# placement des bateaux de l'ordinateur
                
rand_abcs = {
        0 : "a",
        1 : "b",
        2 : "c",
        3 : "d",
        4 : "e",
        5 : "f",
        6 : "g",
        7 : "h",
        8 : "i",
        9 : "j"
        }

rand_ori = {
        1 : "bas",
        2 : "droite"
        }
          
for i in bateaux:
    while True:
        #pcoo = rand_abcs[random.randint(0,9)]+str(random.randint(0,10))
        #ori = rand_ori[random.randint(1,2)]
        pcoo = input(f"quelles coordonnées de la première case du {i} ? ")
        ori = input(f"quelle orientation pour le {i}, droite ou bas ? ")
        print(pcoo)
        if ori == "droite":
            if bateaux[i] <= len(abcs[abcs.index(pcoo[0]):]):
                if "X" in Map2[int(pcoo[1])][abcs.index(pcoo[0]):abcs.index(pcoo[0])+bateaux[i]]:
                    print("croisement droite " + pcoo)
                    print(bateaux[i])
                    continue
                else:
                    for j in Map2[int(pcoo[1])][abcs.index(pcoo[0]):abcs.index(pcoo[0])+bateaux[i]]:
                        Map2[int(pcoo[1])][abcs.index(j[0])] = "X"
                        pos2.append(j)
                    break  
            else:
                print("trop long droite " + pcoo)
                print(bateaux[i])
                continue
        if ori =="bas":
            if bateaux[i] <= len(ordo[int(pcoo[1]):]):
                for j in Map2[int(pcoo[1]):int(pcoo[1])+bateaux[i]]:
                    if "X" in Map2[Map2.index(j)][abcs.index(pcoo[0])]:
                        print("croisement bas " + pcoo)
                        print(print(bateaux[i]))
                    else:
                        bas.append(j[abcs.index(pcoo[0])])
                        if len(bas) == bateaux[i]:
                            for u in Map2[int(pcoo[1]):int(pcoo[1])+bateaux[i]]:
                                pos2.append(u[abcs.index(pcoo[0])])
                                Map2[Map2.index(u)][abcs.index(pcoo[0])] = "X"
                                bas=[]
                        else:
                            continue
                    print(bas)
                break
            else:
                print("trop long bas " + pcoo)
                print(bateaux[i])
                continue
"""                 
show_map(Map1)   
print("")
print(pos1)
print("")
"""
show_map(Map2)   
print("")
print(pos2)
print(bas)

Map3 = [
    [],[],[],[],[],[],[],[],[],[]
    ]

Tirord = []

for i in range(len(ordo)):
    for j in range(len(abcs)):
        Map3[i].append(abcs[j]+str(ordo[i]))
"""
i=1

while True:
    if i%2 == 0:
        #if i == 2:
        Tir = rand_abcs[random.randint(0,9)]+str(random.randint(0,10))
        if Tir in pos1:
            pos1.remove(Tir)
            Map1[int(Tir[1])][abcs.index(Tir[0])] = "O"
            Tirord.append(Tir)
            i+=1
            show_map(Map1) 
            print("Il t'a touché gros naze ! " + Tir +"\n ")
            if pos1 == []:
                print("Tu as perdu pauvre merde\n ")
                break
        else:
            if Tir in Tirord:
                continue
            else:
                Map1[int(Tir[1])][abcs.index(Tir[0])] = "E"
                Tirord.append(Tir)
                i+=1
                show_map(Map1) 
                print("Tu t'es faux-filet comme un plat de côte ! " + Tir +"\n ")
     
    else:
        Tir = input("A toi de tirer (ton coup) ! ")
        if Tir in pos2:
            pos2.remove(Tir)
            Map3[int(Tir[1])][abcs.index(Tir[0])] = "O"
            i+=1
            show_map(Map3) 
            print("T'as touché, salaud ! Epstein !\n ")
            if pos2 == []:
                print("Tu as gagné")
                break
            else:
                continue
        else:
            Map3[int(Tir[1])][abcs.index(Tir[0])] = "E"
            show_map(Map3)   
            print("Ton tir est raté comme ta vie !\n ")
            i+=1
"""
    











