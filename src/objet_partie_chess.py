
from copy import deepcopy

from src.objet_plateau import ObjetPlateau
from src.fonction_cherche_coups_possible_plateau import cherche_coups_possible_plateau
from src.fonction_cherche_coups_possible_plateau import cherche_coups_possible_adverse_plateau
from src.fonction_joue_un_coup_plateau import joue_un_coup_plateau



class PartieChess:
    def __init__(self,plateau_de_base,joueur_blanc,joueur_noir,coup_jouer,fin_de_partie):
        self.plateau_de_base=plateau_de_base
        self.joueur_blanc=joueur_blanc
        self.joueur_noir=joueur_noir
        self.coup_jouer=coup_jouer
        self.fin_de_partie=fin_de_partie
        self.objetplateau=ObjetPlateau([self,
                                        deepcopy(self.plateau_de_base),
                                        [],
                                        self.joueur_blanc,
                                        self.joueur_blanc,
                                        self.joueur_noir,
                                        [True,True,True],
                                        [True,True,True],
                                        [],
                                        [],
                                        []])
        self.historique_plateau=[]
        self.historique_plateau.append(self.objetplateau)
        self.objetplateau.coups_possible=cherche_coups_possible_plateau(self.objetplateau,True)
        self.objetplateau.coup_adverse=cherche_coups_possible_adverse_plateau(self.objetplateau)

    def joue_un_coup_actuel(self,coup):
        if not self.fin_de_partie:
            if self.objetplateau.joueur_actif.genre != 'joueur':
                coup = self.objetplateau.joueur_actif.joue_un_coup(self.objetplateau)
            self.objetplateau=ObjetPlateau(self.objetplateau.recopy())
            self.objetplateau=joue_un_coup_plateau(self.objetplateau,coup)
            self.historique_plateau.append(self.objetplateau)
            self.objetplateau.coups_possible = cherche_coups_possible_plateau(self.objetplateau, True)
            self.objetplateau.coups_adverse = cherche_coups_possible_adverse_plateau(self.objetplateau)
            if not self.objetplateau.coups_possible and self.cherche_echec(self.objetplateau):
                self.fin_de_partie = "Echec et mat , perdu pour le joueur : "
            elif not self.objetplateau.coups_possible :
                self.fin_de_partie = "Pat,plus de coup pour le joueur : "
            if len(self.objetplateau.joueur_noir.piece_perdu)==15 and len(self.objetplateau.joueur_blanc.piece_perdu)==15:
                self.fin_de_partie = "Egalite , plus de piece pour finir"

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
    def recopy(self):
        return deepcopy(self.plateau_de_base),self.joueur_blanc,self.joueur_noir,self.coup_jouer,self.fin_de_partie