# Primitives arbres Python

# Fonction créer arbre vide

def CREER_ARBRE_VIDE():
    return []

# e = racine, SAG = sous arbre gauche, SAD = sous arbre droit

def CREER_ARBRE(e,SAG,SAD):
    return [e,SAG,SAD]

# Créer une feuille

def CREER_ARBRE_FEUILLE(e):
    return [e,[],[]]

# Fonction qui renvoie la racine d'un arbre T

def RACINE(T):
    assert not(EST_VIDE(T)), "L'arbre est vide :("
    return T[0]

# Fonction qui renvoie le SAG d'un arbre T

def SAG(T):
    assert not(EST_VIDE(T[1])), "Le sous-arbre gauche est vide :("
    return T[1]

# Fonction qui renvoie le SAD d'un arbre T

def SAD(T):
    assert not(EST_VIDE(T[2])), "Le sous-arbre droit est vide :("
    return T[2]

# Fonction qui renvoie True si l'arbre est vide

def EST_VIDE(T):
    if T==[]:
        return True
    return False

# Fonction qui renvoie la taille d'un arbre T, taille_arbre = 1 + taille_SAG + taille_SAD

def Taille(T):
    if EST_VIDE(T):
        return 0
    return 1 + Taille(T[1]) + Taille(T[2])

# Fonction qui renvoie la hauteur d'un arbre T, hauteur_arbre = 1

def hauteur(T):
    if EST_VIDE(T):
        return 0
    return 1 + max(hauteur(T[1]),hauteur(T[2]))

# Liste représentant un arbre

L=["A",["B",[],[]],["C",["F",[],[]],["G",[],[]]]]

