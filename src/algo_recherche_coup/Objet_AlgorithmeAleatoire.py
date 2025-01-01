from random import choice

class AlgorithmeAleatoire:
    def __init__(self,boss):
        self.boss=boss

    def trouve_un_coup(self,coups_possible):
        return choice(coups_possible)