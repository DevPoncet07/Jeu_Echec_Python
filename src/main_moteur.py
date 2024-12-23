"""
#################################################################################
#   Fichier d'entre du moteur d echec.
#       class MoteurEchec(boss)  boss= MainInterface or MainConsole
#
#
#
#                                                                               #
#################################################################################
"""
from copy import deepcopy
from src.plateau import Plateau
from src.fonction_cherche_coups_possible import cherche_coups_possible
from src.fonction_joue_un_coup_plateau import joue_un_coup_plateau
from src.objet_joueur import ObjetJoueur


class MoteurEchec:
    def __init__(self,boss):
        self.boss=boss
        self.version=1
        self.joueur_blanc = None
        self.joueur_noir = None
        self.plateau = None
        self.coups_possible=[]
        self.partie_fini=False

        self.PLATEAU_DE_BASE=(["r","n","b","q","k","b","n","r"],
                              ["p","p","p","p","p","p","p","p"],
                              [".",".",".",".",".",".",".","."],
                              [".",".",".",".",".",".",".","."],
                              [".",".",".",".",".",".",".","."],
                              [".",".",".",".",".",".",".","."],
                              ["P","P","P","P","P","P","P","P"],
                              ["R","N","B","Q","K","B","N","R"])

    def start_new_game(self,joueur_blanc,joueur_noir):
        self.joueur_blanc = None
        self.joueur_noir = None
        self.plateau = None
        self.coups_possible = []
        self.partie_fini = False
        self.joueur_blanc=ObjetJoueur((self,joueur_blanc,"white"))
        self.joueur_noir=ObjetJoueur((self,joueur_noir,"black"))
        self.plateau = Plateau(deepcopy(self.PLATEAU_DE_BASE), self.joueur_blanc,self.joueur_blanc,self.joueur_noir)
        self.coups_possible=cherche_coups_possible(self.plateau)

    def joue_un_coup(self,coup):
        joue_un_coup_plateau(self.plateau,coup)
        self.coups_possible=cherche_coups_possible(self.plateau)
        if not self.coups_possible:
            self.partie_fini=True
        else:
            if self.plateau.joueur_actif.coul == "white" and self.joueur_blanc.genre!="joueur":
                self.plateau.joueur_actif.joue_un_coup(self.plateau,self.coups_possible)
            elif self.plateau.joueur_actif.coul == "black" and self.joueur_noir.genre != "joueur":
                self.plateau.joueur_actif.joue_un_coup(self.plateau, self.coups_possible)

    def teste_si_case_piece_dans_possibles(self,case):
        existe=False
        for coup in self.coups_possible:
            if case==coup[0]:
                existe=True
        return existe

    def renvoie_les_case_possible_pour_piece(self,case):
        cases=[]
        for coup in self.coups_possible:
            if case==coup[0]:
                cases.append(coup[1])
        return cases

    def teste_si_coup_dans_possibles(self,coup):
        existe=False
        for coups in self.coups_possible:
            if coups[:2]==coup:
                existe=True
        return existe

    def print_console(self,plateau):
        print("\n" + "*" * 40)
        print()
        for ligne in plateau.plateau:
            print(" ".join(ligne))
        if plateau.joueur_actif.coul == "white":
            couleur_joueur = "Blanc"
        else:
            couleur_joueur = "Noir"
        print("\ncoup aux : " + str(couleur_joueur))
        print()

