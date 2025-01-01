"""
PartieChess stock les donnee d une partie , les joueurs ,les differents coups joues
"""
from copy import deepcopy

from src.objet_plateau import ObjetPlateau




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
                                        [],
                                        0])
        self.historique_plateau=[]
        self.historique_plateau.append(self.objetplateau)

    def recopy(self):
        return deepcopy(self.plateau_de_base),self.joueur_blanc,self.joueur_noir,self.coup_jouer,self.fin_de_partie