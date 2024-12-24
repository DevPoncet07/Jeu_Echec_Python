from copy import deepcopy

from src.objet_joueur import ObjetJoueur

class ObjetPlateau:
    def __init__(self,arg):
        self.partie=arg[0]
        self.plateau=arg[1]
        self.pion_double_move=arg[2]
        self.joueur_actif=arg[3]
        self.joueur_blanc=arg[4]
        self.joueur_noir=arg[5]
        self.roc_blanc=arg[6]
        self.roc_noir=arg[7]
        self.coups_possible=arg[8]
        self.coups_adverse=arg[9]
        self.coup_jouer=arg[10]

    def recopy(self):
        return [self.partie,
                deepcopy(self.plateau),
                self.pion_double_move,
                ObjetJoueur(self.joueur_actif.recopy()),
                ObjetJoueur(self.joueur_blanc.recopy()),
                ObjetJoueur(self.joueur_noir.recopy()),
                deepcopy(self.roc_blanc),
                deepcopy(self.roc_noir),
                self.coups_possible,
                self.coups_adverse,
                self.coup_jouer]