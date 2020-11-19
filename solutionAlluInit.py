import random

def compteAllumettes(tab) :
	s = 0
	for i in tab :
		s += i
	return s

def changerJoueur(currentp) :
	if currentp == 1:
		return 2
	else:
		return 1

def afficherPlateau(tab):
	for i in range(len(tab)):
		print("Ligne n°",i+1,":",end="")
		for a in range(tab[i]):
				print("|",end="")
		print("\n")

def retirerAllumettes(tab, numLI, numAL):
	tab[numLI]=tab[numLI]-numAL
	if tab[numLI] < 0 :
			tab[numLI] = 0

def saisieValide(tab,lig,nb):

	if lig < 0 or nb > len(tab):
		return False

	if nb<1 or nb> 3 or tab[lig]<nb:
		return False

	return True

def choisirStrategie(tab,joueur):
	print("Joueur",joueur,", veuillez choisir la ligne")
	numLI = int(input())-1
	print("Combien d'allumettes voulez-vous retirer ?")
	numAL = int(input())

	while saisieValide(tab,numLI,numAL) == False:
			print("Saisie invalide")
			print("Joueur",tour,", veuillez choisir la ligne")
			numLI = int(input())-1
			print("Combien d'allumettes voulez-vous retirer ?")
			numAL = int(input())

	return numLI, numAL

def machineStrategie(tab):
	# determination des lignes possibles :
	lignes = []
	for i in range(len(tab)):
		if tab[i]>0:
			lignes.append(i)

	# choix d'une ligne
	lig = random.choice(lignes)

	# choix d'un nombre d'allumettes
	nb=random.randint(1,min(3,tab[lig]))

	print("La machine retire",nb,"allumettes de la ligne n°",lig+1)
	return lig,nb



plateau = [1,3,5,7]
numJoueur = 1

while (compteAllumettes(plateau) > 0 ) :
	afficherPlateau(plateau)

	if numJoueur == 1:
		numLigne, nbAllu = choisirStrategie(plateau, numJoueur)
	else :
		numLigne, nbAllu = machineStrategie(plateau)

	retirerAllumettes(plateau, numLigne, nbAllu)
	print("\n===================================\n")
	numJoueur = changerJoueur(numJoueur)


	print("\n===================================\n")

print("\n    Le joueur",numJoueur, "gagne la partie.\n\n")
