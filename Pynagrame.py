## ANAGRAMME
## liste des fonction :
### 1. Choix ds joueur 1/2 - return nombre, je ne passe pas d'information
### 2. génération des lettre - return lettres et stock le mots d'origine, doit passé un nombre de lettre saisi par le joueur solo
### 3. Vérification - passage de la var. qui contient lettre, et var qui contient le/les mots
### 4. systéme de point - compte le nombre de mots, puis de lettre lettre puis additionne
#Import néccéssaire
from random import choice,shuffle

try: # importation du dictionnaire avec gestion d'erreur simple
    with open('./dicoFR.txt', 'r') as f:
        frdico = f.read().split('\n')
except FileNotFoundError:
    print("Erreur : le fichier n'a pas été trouvé.")
    exit()


# Fonctions :
def NbrJoueur():
    test = 1 
    while test == 1:
        try:
            nombre = int(input("Choisir lr nombre de joueur; 1 ou 2 : "))
        except ValueError:
            print("Raté ce n'ai pas un chiffre")
        else: return nombre 


def GenLettr(tab, NbrLettr):
    filtreMots = [mot for mot in tab if len(mot) == NbrLettr]  # je filtre mon tableau pour chercher le bon nombre de lettre

    if not filtreMots:
        return 0

    mot = choice(filtreMots)
    lettres = list(mot)
    shuffle(lettres)

    return ' '.join(lettres)



def VerifLettre(Lttr, Mots,):
    motValide = []
    for mot in Mots:
        motLettr = sorted(mot)
        triLettr = sorted(list(Lttr))
        for lettre in motLettr:
            if lettre in triLettr:
                triLettr.remove(lettre)  # enleve des lettres disponibles
            else:
                print(f"Mot '{mot}' impossible à former avec les lettres disponibles.")
                break  # Si lettre  pas disponible -> arrête la vérification du mot
        else:
            # Si toutes les lettres sont trouvées et utilisées, on ajoute le mot à la liste des mots valides
            motValide.append(mot)
    return motValide

def VerifExist(Checkmot,tab):
    motsValide =  []
    invalid = []
    Mots = list(set(Checkmot))
    for mot in Mots:
        if mot in tab:
            motsValide.append(mot)
        else:
            invalid.append(mot)
    print("Liste de mot non répertorié et ignoré :")
    for mot in invalid:
        print(f"- {mot}")
    print("Mots validé :")
    for mot in motsValide:
        print(f"- {mot}")
    return motsValide


def sysPoint(mots):
    point=0
    for mot in mots:
        point+=1
        for lttr in mot:
            point+=1
    print(f"Votre total de point s'élève a : {point}")
    return point



# variable :
INTRO = "###############\n## PYNAGRAME ##\n###############"
var = 0
lettreGencheck = 0


# Programme Principale

while var == 0:
    nbrJoueur = NbrJoueur()
    
    if nbrJoueur == 1:
        var = 1
        print(INTRO)

        name = str(input("Saisisez votre prénom:\n"))
        print(f"~~~ bienvenu-e dans PYNAGRAMME {name} anagramme~~~\n choissisez un nombre de lettre :")
        
        while lettreGencheck == 0:
            nbrlettre = int(input())
            lettreGen = GenLettr(frdico,nbrlettre)

            if lettreGen == 0:
                print(f"il n'y a pas de mots qui contient {nbrlettre} lettres, entrées une nouvelles valeur : ")
            else : lettreGencheck = 1
        
        print(f"voici les lettres : {lettreGen}\n former le ou les mots possible ( séparer par espace EX: Bois soi bis si)")
        mots = str(input()).split(" ")
        print("ce que vous avez saisi: ")
        for i in mots:
            print("-",end=" ")
            for j in i:
                print(j,end="")
            print(" ")
        checklist=VerifLettre(lettreGen, mots)
        motsValides=VerifExist(checklist,frdico)
        points=sysPoint(motsValides)


    elif nbrJoueur == 2:
        var = 1
        print(INTRO)
        
        nameJ1 = str(input("Joueur 1, entrer votre prénom:\n"))
        nameJ2 = str(input("Joueur 2, entrer votre prénom:\n"))
        # J1 entre lettre, J2 mot
        print(f"~~~ Bienvenus dans PYGRAMME {nameJ1} et {nameJ2} ~~~")
        lettrJ1 = str(input(f"{nameJ1}, entrée les lettres :"))
        print(f"les lettre choisie par {nameJ1} : {lettrJ1}")
        motsJ2 = str(input(f"{nameJ2}, saisissez un ou des mots (séparé par un espace): ")).split(" ")
        print("ce que vous avez saisi: ")
        for i in motsJ2:
            print("-",end=" ")
            for j in i:
                print(j,end="")
            print(" ") 
        #J2 entre lettre et J1 mot
        lttrenbrCheck=0
        while lttrenbrCheck==0:
            lettrJ2 = str(input(f"{nameJ2}, entrée les lettres :"))
            if len(lettrJ1)==len(lettrJ2):
                lttrenbrCheck=1
            else:
                print(f"veuillez entré le meme nombre de lettre que {nameJ1}, {len(lettrJ1)}")
        
        print(f"les lettre choisie par {nameJ2} : {lettrJ2}")
        motsJ1 = str(input(f"{nameJ1}, saisissez un ou des mots (séparé par un espace): ")).split(" ")
        print("ce que vous avez saisi: ")
        for i in motsJ1:
            print("-",end=" ")
            for j in i:
                print(j,end="")
            print(" ")
        checklistJ1=VerifLettre(lettrJ2, motsJ1)
        motsValidesJ1=VerifExist(checklistJ1,frdico)
        pointsJ1=sysPoint(motsValidesJ1)
        checklistJ2=VerifLettre(lettrJ1, motsJ2)
        motsValidesJ2=VerifExist(checklistJ2,frdico)
        pointsJ2=sysPoint(motsValidesJ2)
        
    else : print("il semble que vous soyez trop nombreux, ou pas assez nombreux ?? pour jouer, veuillez selectionnez maximum 2 joueur")
