import csv
from array import *
def csvprocessing (filename):
    #creation de deux dictionnaires
    csvTab ={} #dictionnaire global contenant toutes les candidatures
    voeux ={} #dictionnaire contenant les voeux des eleves
    #nomsEtu=[]
    with open (filename) as csv_file:
        csv_reader = csv.reader (csv_file, delimiter=',') #ouverture du fichier csv


        for row in csv_reader:#pour chaque ligne du fichier csv:

            for k in range (1, len(row)): #pour chaque couple ecole, note : l'ajouter au dictionnaire voeux
                nomEcole = str(row[k].split(';')[0])
                note = int(str(row[k].split(';')[1][1:2]))
                #print(nomEcole[2:])
                voeux[str(nomEcole[2:])] = note
                csvTab[str(row[0])] = voeux# pour chaque etudiant, ajout à csvTab le couple {etudiant: {voeux}}

        print(csvTab)
        #nblignesVoeux=len(csvTab)
        #nbcolonnesVoeux=(len(csvTab[0])-1)
        #voeux = [[]*nblignesVoeux]*nbcolonnesVoeux

        #for i in range (0,len(csvTab)):
        #    nomsEtu.append(csvTab[i][0])
            #for j in range (1, len(csvTab[i])):

        #        voeux.append(csvTab[i][j])
                #print (csvTab[i])
        #print(voeux)
        #for j in range (0,len(nomsEtu)):
            #print (nomsEtu[j])


csvprocessing('example.csv')
