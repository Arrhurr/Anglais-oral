def tri_cv_parbac(liste:list,niveau:int,type:str):
    cvagarder=[]
    type=type.lower()
    for i in range(len(liste)):
        if liste[i][1]>=niveau and liste[i][2].lower()==type:
            cvagarder.append(i)
    return cvagarder

def affichage_bon_cv(liste_cv:list,index:list):
    for i in range(len(index)):
        print(liste_cv[index[i]])

liste=[["Cringe Lord",4,"buveur de bite"],["Arnaud Donou",5,"Informatique"],["Guillaume Puill",2,"Alcoolique annonyme"],["Arthur Donou",8,"Informatique"],["Mr le docteur",9,"Medecine"],["Un pelo random",3,"Informatique"]]

print(tri_cv_parbac(liste,3,"Informatique"))
affichage_bon_cv(liste,tri_cv_parbac(liste,3,"Informatique"))