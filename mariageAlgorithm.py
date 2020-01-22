def getKey(elements, search): 
    for key, value in elements.items(): 
         if search == value: 
             return key 
    return "no key"

def mariageStableEleves (eleves, ecoles, nbEleves) :
    balcons = {}
    positions = nbEleves
    for key in eleves.keys():
        balcons[key] = []
    for key in ecoles.keys() :
        for nb in range (1, nbEleves[key]+1) :
            student = getKey(ecoles[key],nb)
            if student != "no key" :
                balcons[student].append(key)
    stable = False
    while not stable :
        stable = True
        for key in balcons.keys() :
            if len(balcons[key]) > 1 :
                stable = False
                minimum = 0
                for element in balcons[key] :
                    if minimum == 0 or eleves[key][element] < minimum :
                        minimum = eleves[key][element]
                for element in balcons[key] :
                    if eleves[key][element] > minimum :
                        balcons[key].remove(element)
                        positions[element] += 1
                        if positions[element] <= len(eleves.keys()):
                            student = getKey(ecoles[element],positions[element])
                            if student != "no key" :
                                balcons[student].append(element)
    return balcons  

def mariageStableEcoles (eleves, ecoles, nbEleves) :
    balcons = {}
    for key in ecoles.keys():
        balcons[key] = []
    for key in eleves.keys() :
        school = getKey(eleves[key],1)
        if school != "no key" :
            balcons[school].append(key)
    stable = False
    while not stable :
        stable = True
        for key in balcons.keys() :
            if len(balcons[key]) > nbEleves[key] :
                stable = False
                while len(balcons[key]) > nbEleves[key] :
                    maximum = 0
                    for element in balcons[key] :
                        if maximum == 0 or eleves[element][key] > maximum :
                            maximum = eleves[element][key]
                    for element in balcons[key] :
                        if ecoles[key][element] == maximum :
                            balcons[key].remove(element)
                            position = eleves[element][key] + 1
                            ecole = getKey(eleves[element],position)
                            if ecole != "no key" :
                                balcons[ecole].append(element)
    return balcons      


eleves = {"Mathieu" : {"ENSEEIHT":1,"ENSIBS":3,"ENSIMAG":2},
         "Ignace": {"ENSEEIHT":1,"ENSIBS":2,"ENSIMAG":3},
         "Thomas": {"ENSEEIHT":3,"ENSIBS":2,"ENSIMAG":1},
         "Tom":  {"ENSEEIHT":1,"ENSIBS":2,"ENSIMAG":3}}

ecoles = {"ENSEEIHT":{"Ignace":1,"Mathieu":2,"Thomas":3, "Tom":4},
          "ENSIMAG": {"Ignace":4,"Mathieu":3,"Thomas":2, "Tom":1},
          "ENSIBS":  {"Ignace":1,"Mathieu":3,"Thomas":2, "Tom":4}}

nbEleves = {"ENSEEIHT": 2, "ENSIMAG" : 1, "ENSIBS" : 3}

print("Eleves favorisés :")
print(mariageStableEleves(eleves, ecoles, nbEleves))
print("Ecoles favorisés :")
print(mariageStableEcoles(eleves, ecoles, nbEleves))