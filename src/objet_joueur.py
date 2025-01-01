from random import choice
from copy import deepcopy

from src.algo_recherche_coup.Objet_AlgorithmeAleatoire import AlgorithmeAleatoire
from src.algo_recherche_coup.Objet_AlgorithmeMinMax import AlgorithmeMinMax


class ObjetJoueur:
    def __init__(self,arg):
        self.coul=arg[0]
        self.genre=arg[1]
        self.piece_perdu=arg[2]

    def recopy(self):
        return [self.coul,self.genre,deepcopy(self.piece_perdu)]

    def joue_un_coup(self,obj_plateau,profondeur=0):
        if self.genre=="aleatoire":
            algo = AlgorithmeAleatoire(self)
            return algo.trouve_un_coup(obj_plateau.coups_possible)
        if self.genre=="minmax":
            algo=AlgorithmeMinMax(self)
            return algo.trouve_un_coup(obj_plateau,profondeur)


