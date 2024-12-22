"""
#################################################################################
#   class ObjetJouer                                                            #
#       genre = 'human' or "aleatoire" or ...                                  #
#       save if  player is human or bots                                        #
#           and have a methode to select move to different way                  #
#                                                                               #
#################################################################################
"""

from random import choice


class ObjetJoueur:
    def __init__(self,info):
        self.boss=info[0]
        self.genre=info[1]
        self.coup=[]
        self.coul=info[2]

    def joue_un_coup(self,obj_plateau,liste_coup):
        # entry methode for bots player search move
        if self.genre=="joueur":
            self.coup=[]
        elif self.genre=="aleatoire":
            self.coup=choice(liste_coup)

    def copy(self):
        return self.boss,self.genre,self.coul
