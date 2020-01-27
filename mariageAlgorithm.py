#Permet de récupérer la clé associer à la valeur search
#Elements : Dictionnaire
#Search : Type de la valeur cherché
#Retourne la clé correspondante
def getKey(elements, search): 
    for key, value in elements.items(): 
         if search == value: 
             return key 
    return "no key"

#Algorithme de mariage stable, les eleves sont favorisés par rapport aux écoles
#eleves : Dictionnaire contenant le nom des éléves et un dictionnaire pour chaque éléve contenant le nom des écoles et la note de chaque école
#ecoles : Dictionnaire contenant le nom des écoles et un dictionnaire pour chaque école contenant le nom des éléves et la note de chaque éléve
#nbEleves: Dictionnaire contenant le nom des écoles et le nombres des élèves acceptés dans chaque école
#Retourne un dictionnaire contenant pour chaque éléve, l'école qui lui a été affecté
def mariageStableEleves (eleves, ecoles, nbEleves) :
    #Tableau pour l'algorithme
    balcons = {}
    positions = nbEleves
    #Remplir les cases du tableau
    for key in eleves.keys():
        balcons[key] = []
    for key in ecoles.keys() :
        for nb in range (1, nbEleves[key]+1) :
            student = getKey(ecoles[key],nb)
            if student != "no key" :
                balcons[student].append(key)
    #Tant que l'on a pas atteint l'état stable
    stable = False
    while not stable :
        stable = True
        #On regarde qui, pour chaque balcon, a plusieurs écoles
        for key in balcons.keys() :
            if len(balcons[key]) > 1 :
                stable = False
                minimum = 0
                #On regarde l'école avec la valeur minimale
                for element in balcons[key] :
                    if minimum == 0 or eleves[key][element] < minimum :
                        minimum = eleves[key][element]
                #On replace toutes les écoles avec une valeur plus haute que la valeur minimale
                for element in balcons[key] :
                    if eleves[key][element] > minimum :
                        balcons[key].remove(element)
                        positions[element] += 1
                        #Repositionnement de chaque école précédemment enlevés
                        if positions[element] <= len(eleves.keys()):
                            student = getKey(ecoles[element],positions[element])
                            if student != "no key" :
                                balcons[student].append(element)
    return balcons  

#Algorithme de mariage stable, les écoles sont favorisés par rapport aux éléves
#eleves : Dictionnaire contenant le nom des éléves et un dictionnaire pour chaque éléve contenant le nom des écoles et la note de chaque école
#ecoles : Dictionnaire contenant le nom des écoles et un dictionnaire pour chaque école contenant le nom des éléves et la note de chaque éléve
#nbEleves: Dictionnaire contenant le nom des écoles et le nombres des élèves acceptés dans chaque école
#Retourne un dictionnaire contenant pour chaque école, les éléves qui lui ont été affectés
def mariageStableEcoles (eleves, ecoles, nbEleves) :
    #Tableau pour l'algorithme
    balcons = {}
    #Remplir les cases du tableau
    for key in ecoles.keys():
        balcons[key] = []
    for key in eleves.keys() :
        school = getKey(eleves[key],1)
        if school != "no key" :
            balcons[school].append(key)
    #Tant que l'on a pas atteint l'état stable
    stable = False
    while not stable :
        stable = True
        #On regarde les écoles qui ont plus d'étudiants qu'elles ne peuvent en accueillir
        for key in balcons.keys() :
            if len(balcons[key]) > nbEleves[key] :
                stable = False
                #Tant que l'on a plus d'étudiants que la capacité d'accueil
                while len(balcons[key]) > nbEleves[key] :
                    maximum = 0
                    #On récupère l'école avec la valeur la plus haute
                    for element in balcons[key] :
                        if maximum == 0 or eleves[element][key] > maximum :
                            maximum = eleves[element][key]
                    #On replace l'école avec la valeur la plus haute
                    for element in balcons[key] :
                        if ecoles[key][element] == maximum :
                            balcons[key].remove(element)
                            position = eleves[element][key] + 1
                            ecole = getKey(eleves[element],position)
                            if ecole != "no key" :
                                balcons[ecole].append(element)
    return balcons      
