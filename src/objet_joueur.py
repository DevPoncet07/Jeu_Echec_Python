from random import choice
from copy import deepcopy

from src.fonction_analyse_score_position import analyse_score_position


class ObjetJoueur:
    def __init__(self,arg):
        self.coul=arg[0]
        self.genre=arg[1]
        self.piece_perdu=arg[2]
        self.profondeur_max = None

    def recopy(self):
        return [self.coul,self.genre,deepcopy(self.piece_perdu)]

    def joue_un_coup(self,obj_plateau,profondeur=0):
        if self.genre=="aleatoire":
            return choice(obj_plateau.coups_possible)
        if self.genre=="minmax":
            algo=AlgorythmeMinMax(self)
            return algo.trouve_un_coup(obj_plateau,profondeur)


class AlgorythmeMinMax:
    def __init__(self,boss):
        self.boss=boss
        self.objet_plateau =None
        self.coul = None

    def trouve_un_coup(self,objet_plateau,profondeur=0):
        coup=[]
        self.objet_plateau=objet_plateau.recopy()

        return self.objet_plateau.coups_possible[0]

class Node:
    def __init__(self,objet_plateau,parent,enfants):
        self.objet_plateau=objet_plateau
        self.parent=parent
        self.enfants=enfants