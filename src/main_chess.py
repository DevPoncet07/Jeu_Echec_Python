"""
point d entree du module MoteurEchec:  paramatre: boss=interface

"""

from copy import deepcopy
import re

from src.objet_partie_chess import PartieChess
from src.objet_joueur import ObjetJoueur
from src.fonction_cherche_coups_possible_plateau import cherche_coups_possible_plateau
from src.fonction_cherche_coups_possible_plateau import cherche_coups_possible_adverse_plateau
from src.fonction_joue_un_coup_plateau import joue_un_coup_plateau
from src.fonction_analyse_score_position import analyse_score_position


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
        self.liste_colone = [8,7,6,5,4,3,2,1]
        self.liste_ligne = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def decode_commande(self,commande):
        if commande[0]=='new':
            self.cree_nouvelle_partie(commande[1],commande[2])
        elif commande[0]=="joue":
            self.joue_un_coup(commande[1])
        else:
            commande="".join(commande)

            if re.search("[a-h][1-8][a-h][1-8]",commande):
                self.decode_coup_simple(commande)
            elif re.search("[a-h][1-8]",commande):
                self.decode_coup(commande)

    def decode_coup(self,text):
        print(text)

    def decode_coup_simple(self,text):
        coup=[[self.liste_ligne.index(text[0]),
               self.liste_colone.index(int(text[1]))],
              [self.liste_ligne.index(text[2]),
                self.liste_colone.index(int(text[3]))
                ]]
        print(coup)
        self.joue_un_coup(coup)

    def cree_nouvelle_partie(self,joueur_blanc="joueur",joueur_noir="joueur"):
        joueur_blanc=ObjetJoueur(['white',joueur_blanc,[]])
        joueur_noir=ObjetJoueur(['black',joueur_noir,[]])
        self.partie_en_cours=PartieChess(deepcopy(self.PLATEAU_DE_BASE),joueur_blanc,joueur_noir,[],False)
        self.partie_en_cours.objetplateau.coups_possible=cherche_coups_possible_plateau(self.partie_en_cours.objetplateau,True)
        self.partie_en_cours.objetplateau.coups_adverse=cherche_coups_possible_adverse_plateau(self.partie_en_cours.objetplateau)
        self.partie_en_cours.objetplateau.score_position = analyse_score_position(self.partie_en_cours.objetplateau)


    def joue_un_coup(self,coup):
        if not self.partie_en_cours.fin_de_partie:
            if self.partie_en_cours.objetplateau.joueur_actif.genre != 'joueur':
                coup = self.partie_en_cours.objetplateau.joueur_actif.trouve_un_coup(self.partie_en_cours)
            self.partie_en_cours.objetplateau = self.partie_en_cours.objetplateau.recopy()
            self.partie_en_cours.objetplateau = joue_un_coup_plateau(self.partie_en_cours.objetplateau, coup)
            self.partie_en_cours.historique_plateau.append(self.partie_en_cours.objetplateau)
            self.partie_en_cours.objetplateau.coups_possible = cherche_coups_possible_plateau(self.partie_en_cours.objetplateau, True)
            self.partie_en_cours.objetplateau.coups_adverse = cherche_coups_possible_adverse_plateau(self.partie_en_cours.objetplateau)
            self.partie_en_cours.objetplateau.score_position = analyse_score_position(self.partie_en_cours.objetplateau)
            if not self.partie_en_cours.objetplateau.coups_possible and self.cherche_echec(self.partie_en_cours.objetplateau):
                self.partie_en_cours.fin_de_partie = "Echec et mat , perdu pour le joueur : "
            elif not self.partie_en_cours.objetplateau.coups_possible:
                self.partie_en_cours.fin_de_partie = "Pat,plus de coup pour le joueur : "
            if  self.nul_par_repetition():
                self.partie_en_cours.fin_de_partie = "nul par repetition"
            if len(self.partie_en_cours.objetplateau.joueur_noir.piece_perdu) == 15 and len(
                    self.partie_en_cours.objetplateau.joueur_blanc.piece_perdu) == 15:
                self.partie_en_cours.fin_de_partie = "Egalite , plus de piece pour finir"

    def return_plateau_actuel(self):
        return self.partie_en_cours.objetplateau.plateau

    def demande_case_focus(self,case):
        for coup in self.partie_en_cours.objetplateau.coups_possible:
            if coup[0] == case:
                return True
        return False

    def return_case_arriver(self,case):
        cases = []
        for coup in self.partie_en_cours.objetplateau.coups_possible:
            if coup[0] == case:
                cases.append(coup[1])
        return cases

    def demande_coup(self, coup):
        for elem in self.partie_en_cours.objetplateau.coups_possible:
            if elem[0:2] == coup:
                return True
        return False

    def demande_promotion(self,coup):
        if self.partie_en_cours.objetplateau.joueur_actif.coul=='white':
            if self.partie_en_cours.objetplateau.plateau[coup[0][1]][coup[0][0]]=="P" and coup[1][1]==0:
                return True
        elif self.partie_en_cours.objetplateau.joueur_actif.coul == 'black':
            if self.partie_en_cours.objetplateau.plateau[coup[0][1]][coup[0][0]] == "p" and coup[1][1] == 7:
                return True

        return False

    def cherche_echec(self,obj_plateau):
        if obj_plateau.joueur_actif.coul=='white':
            for coup in obj_plateau.coups_adverse:
                if obj_plateau.plateau[coup[1][1]][coup[1][0]]=="K":
                    return True
        else:
            for coup in obj_plateau.coups_adverse:
                if obj_plateau.plateau[coup[1][1]][coup[1][0]]=="k":
                    return True
        return False

    def nul_par_repetition(self):
        reponse=False
        if len(self.partie_en_cours.historique_plateau)>12:
            reponse=True
            coup_jouer1=self.partie_en_cours.historique_plateau[-1].coup_jouer
            coup_jouer2=self.partie_en_cours.historique_plateau[-2].coup_jouer
            coup_jouer3 = self.partie_en_cours.historique_plateau[-3].coup_jouer
            coup_jouer4 = self.partie_en_cours.historique_plateau[-4].coup_jouer
            for index in range(-12,-0,4):
                if coup_jouer1!=self.partie_en_cours.historique_plateau[index+3].coup_jouer:
                    reponse=False
                if coup_jouer2!=self.partie_en_cours.historique_plateau[index+2].coup_jouer:
                    reponse=False
                if coup_jouer3!=self.partie_en_cours.historique_plateau[index+1].coup_jouer:
                    reponse=False
                if coup_jouer4!=self.partie_en_cours.historique_plateau[index].coup_jouer:
                    reponse=False
        return reponse

