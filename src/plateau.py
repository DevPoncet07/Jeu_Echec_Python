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
        self.joueur_blanc=joueur_blanc
        self.joueur_noir=joueur_noir