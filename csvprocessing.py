import csv
import mariageAlgorithm
from array import *
def csvprocessing (filename):
    #creation de deux dictionnaires
    eleves ={} #dictionnaire global contenant toutes les candidatures
    voeux ={} #dictionnaire contenant les voeux des eleves

    ecoles={}
    capacites={}
    with open (filename) as csv_file:
        csv_reader = csv.reader (csv_file, delimiter=',') #ouverture du fichier csv
        donneeetudiant = 0
        for row in csv_reader:#pour chaque ligne du fichier csv:
            if len(row) == 0:
                donneeetudiant += 1
            if donneeetudiant == 0 :
                for k in range (1, len(row)): #pour chaque couple ecole, note : l'ajouter au dictionnaire voeux
                    nomEcole = str(row[k].split(';')[0])
                    note = int(str(row[k].split(';')[1][1]))
                    voeux[str(nomEcole[2:])] = note
                    eleves[str(row[0])] = voeux# pour chaque etudiant, ajout a csvTab le couple {etudiant: {voeux}}
                voeux = {}
            elif donneeetudiant == 1 :
                for k in range (1, len(row)):
                    nomEcole = str(row[k].split(';')[0])
                    note = int(str(row[k].split(';')[1][1]))
                    voeux[str(nomEcole[2:])] = note
                    ecoles[str(row[0])] = voeux
                voeux = {}
            else:
                if (len(row)) > 0 :
                    capacites[str(row[0])] = int(str(row[1]))

        print("Les écoles sont courtisées par les élèves :")
        print(mariageAlgorithm.mariageStableEcoles(eleves,ecoles,capacites))
        print()
        print("Les élèves sont courtisées par les écoles :")
        print(mariageAlgorithm.mariageStableEleves(eleves,ecoles,capacites))
        print()


print("Exemple Simple :\n")
csvprocessing('exampleSimple.csv')

print("Exemple Complet 1 :\n")
csvprocessing('exampleComplet1.csv')

print("Exemple Complet 2 :\n")
csvprocessing('exampleComplet2.csv')

print("Exemple Complet 3 :\n")
csvprocessing('exampleComplet3.csv')