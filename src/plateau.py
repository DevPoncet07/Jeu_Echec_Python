"""
#################################################################################
#   class Plateau(                                                              #
#                plateau=[["r","b"...],[],...]                                  #
#                joueur_actif = objet_joueur                                    #
#                                                                               #
#       save actual state of game                                               #
#                                                                               #
#################################################################################
"""

class Plateau:
    def __init__(self,plateau,joueur_actif,joueur_blanc,joueur_noir):
        self.plateau=plateau
        self.joueur_actif=joueur_actif
        self.pion_double_avance=[]
        self.roc_blanc=[True,True,True]
        self.roc_noir=[True,True,True]
        self.joueur_blanc=joueur_blanc
        self.joueur_noir=joueur_noir