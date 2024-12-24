from copy import deepcopy

from src.objet_partie_chess import PartieChess
from src.objet_joueur import ObjetJoueur



class MoteurEchec:
    def __init__(self,boss):
        self.boss=boss
        self.version=1

        self.PLATEAU_DE_BASE=(["r","n","b","q","k","b","n","r"],
                              ["p","p","p","p","p","p","p","p"],
                              [".",".",".",".",".",".",".","."],
                              [".",".",".",".",".",".",".","."],
                              [".",".",".",".",".",".",".","."],
                              [".",".",".",".",".",".",".","."],
                              ["P","P","P","P","P","P","P","P"],
                              ["R","N","B","Q","K","B","N","R"])

        self.partie_en_cours=None

    def decode_commande(self,commande):
        if commande[0]=='new':
            self.cree_nouvelle_partie(commande[1],commande[2])
        if commande[0]=="joue":
            self.joue_un_coup(commande[1])

    def cree_nouvelle_partie(self,joueur_blanc="joueur",joueur_noir="joueur"):
        joueur_blanc=ObjetJoueur(['white',joueur_blanc,[]])
        joueur_noir=ObjetJoueur(['black',joueur_noir,[]])
        self.partie_en_cours=PartieChess(deepcopy(self.PLATEAU_DE_BASE),joueur_blanc,joueur_noir,[],False)

    def joue_un_coup(self,coup):
        self.partie_en_cours.joue_un_coup_actuel(coup)

    def return_plateau_actuel(self):
        return self.partie_en_cours.objetplateau.plateau

    def demande_case_focus(self,case):
        return self.teste_case_depart_dans_case_possible(self.partie_en_cours.objetplateau,case)

    def return_case_arriver(self,case):
        return self.return_case_arriver_de_case_depart(self.partie_en_cours.objetplateau,case)

    def demande_coup(self, coup):
        return self.teste_coup_in_coup_possible(self.partie_en_cours.objetplateau,coup)

    def teste_case_depart_dans_case_possible(self,obj_plateau,case):
        for coup in obj_plateau.coups_possible:
            if coup[0]==case:
                return True
        return False

    def teste_coup_in_coup_possible(self,obj_plateau,coup):
        for elem in obj_plateau.coups_possible:
            if elem[0:2]==coup:
                return True
        return False

    def return_case_arriver_de_case_depart(self,obj_plateau,case):
        cases = []
        for coup in obj_plateau.coups_possible:
            if coup[0] == case:
                cases.append(coup[1])
        return cases

    def demande_promotion(self,coup):
        if self.partie_en_cours.objetplateau.joueur_actif.coul=='white':
            if self.partie_en_cours.objetplateau.plateau[coup[0][1]][coup[0][0]]=="P" and coup[1][1]==0:
                return True
        elif self.partie_en_cours.objetplateau.joueur_actif.coul == 'black':
            if self.partie_en_cours.objetplateau.plateau[coup[0][1]][coup[0][0]] == "p" and coup[1][1] == 7:
                return True

        return False









