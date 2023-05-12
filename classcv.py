def tri_cv_parbac(liste:list,niveau:int,etude=None,nbvoulu=None):
    cvagarder=[]
    if type(nbvoulu)!=int:
        max=len(liste)+1
    else:max=nbvoulu
    if etude is not None: etude=etude.lower()
    for i in range(len(liste)):
        if liste[i][1]>=niveau and liste[i][2].lower()==etude: 
            cvagarder.append(i)
    while len(cvagarder)>max:
        min=liste[cvagarder[0]][1]
        mini=0
        for i in range(len(cvagarder)):
            if liste[cvagarder[i]][1]<min:
                min=liste[cvagarder[i]][1]
                mini=i
        cvagarder.pop(mini)
    return cvagarder

def affichage_bon_cv(liste_cv:list,index:list):
    for i in range(len(index)):
        print(liste_cv[index[i]])


liste=[["Cringe Lord",4,"buveur de bite"],["Arnaud Donou",5,"Informatique"],["Guillaume Puill",2,"Alcoolique annonyme"],["Arthur Donou",8,"Informatique"],["Mr le docteur",9,"Medecine"],["Un pelo random",3,"Informatique"]]

affichage_bon_cv(liste,tri_cv_parbac(liste,3,etude="Informatique",nbvoulu=2))