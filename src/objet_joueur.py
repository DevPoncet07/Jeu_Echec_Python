from copy import deepcopy

from src.algo_recherche_coup.Objet_AlgorithmeAleatoire import AlgorithmeAleatoire
from src.algo_recherche_coup.Objet_AlgorithmeMinMax import AlgorithmeMinMax
from src.algo_recherche_coup.Objet_AlgorithmeMinMax2 import AlgorithmeMinMax2
from src.algo_recherche_coup.objet_Algorithme_stockfish import AlgorithmeStockfish


class ObjetJoueur:
    def __init__(self,arg):
        self.coul=arg[0]
        self.genre=arg[1]
        self.piece_perdu=arg[2]
        if self.genre=='stockfish':
            self.algo = AlgorithmeStockfish(self)

    def recopy(self):
        return [self.coul,self.genre,deepcopy(self.piece_perdu)]

    def trouve_un_coup(self,obj_parti,profondeur=0):
        obj_plateau=obj_parti.objetplateau
        if self.genre=="aleatoire":
            algo = AlgorithmeAleatoire(self)
            return algo.trouve_un_coup(obj_plateau.coups_possible)
        if self.genre=="minmax":
            algo=AlgorithmeMinMax(self)
            return algo.trouve_un_coup(obj_plateau,profondeur)
        if self.genre=="minmax2":
            algo=AlgorithmeMinMax2(self)
            return algo.trouve_un_coup(obj_plateau,profondeur)
        if self.genre=="stockfish":
            return self.algo.trouve_un_coup(obj_parti)


