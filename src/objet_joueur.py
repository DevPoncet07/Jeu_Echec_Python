from random import choice


class ObjetJoueur:
    def __init__(self,boss,genre,coul):
        self.boss=boss
        self.genre=genre
        self.coup=[]
        self.coul=coul

    def joue_un_coup(self,obj_plateau,liste_coup):
        if self.genre=="joueur":
            self.coup=[]
        elif self.genre=="aleatoire":
            self.coup=choice(liste_coup)
