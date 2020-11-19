
def factorielle(n):
    if n <=1:
        return 1

    return n * factorielle(n-1)

def compteAllumettes(tab) :
	s = 0
	for i in tab :
		s += i
	return s

def defineCoupsPossibles(plateau):
    coups = []

    for ligne in range(4):
        for nb in range(1,4):
            if nb <= plateau[ligne]:
                coups.append((ligne,nb))
    return coups


def evaluer(plateau, IA):
    #print ("J'evalue :", plateau, IA)

    if compteAllumettes(plateau) == 0:
        if IA :
            return 1
        return -1

    coups = defineCoupsPossibles(plateau)
    #print(coups)

    if IA :

        best = -1000
        for c in coups:
            ligne = c[0]
            nb = c[1]

            plateau[ligne]-= nb
            #print(plateau)
            resu = evaluer(plateau, not IA)
            if resu > best :
                best = resu

            plateau[ligne]+=nb
    else :
        best = 1000
        for c in coups:
            ligne = c[0]
            nb = c[1]

            plateau[ligne]-= nb
            #print(plateau)
            resu = evaluer(plateau, not IA)
            if resu < best :
                best = resu

            plateau[ligne]+=nb


    #print ("Je viens d'evaluer :", plateau, IA,":",best)

    return best

def choisirIA(plateau):
    coups = defineCoupsPossibles(plateau)

    best = -1000
    bestStrategy = None
    for c in coups:
        ligne = c[0]
        nb = c[1]

        plateau[ligne]-= nb
        #print(plateau)
        resu = evaluer(plateau, False)
        if resu > best :
            best = resu
            bestStrategy = c

        plateau[ligne]+=nb

    if best>0 :
        print("Je vais te ni///er en jouant ",bestStrategy)
    else :
        print ("joue bien sinon, je vais te....")

    return bestStrategy


plateau = [1,3,5,3]
print(plateau)
#resu = evaluer(plateau,IA)
#print ("Pg principal : Evaluation de ",plateau,IA,":", resu)

choix = choisirIA(plateau)
print("l'IA joue ",choix)
