from random import choice
from copy import deepcopy

class ObjetJoueur:
    def __init__(self,arg):
        self.coul=arg[0]
        self.genre=arg[1]
        self.piece_perdu=arg[2]

    def recopy(self):
        return [self.coul,self.genre,deepcopy(self.piece_perdu)]

    def joue_un_coup(self,obj_plateau):
        if self.genre=="aleatoire":
            return choice(obj_plateau.coups_possible)

