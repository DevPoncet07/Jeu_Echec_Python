from src.plateau import Plateau
from src.fonction_cherche_coups_possible import cherche_coups_possible
from src.fonction_joue_un_coup_plateau import joue_un_coup_plateau


def print_console(plateau):
    print("\n"+"*"*40)
    print()
    for ligne in plateau.plateau:
        print(" ".join(ligne))
    if plateau.joueur_actif=="white":
        couleur_joueur="Blanc"
    else:
        couleur_joueur="Noir"
    print("\ncoup aux : "+str(couleur_joueur))
    print()


class MoteurEchec:
    def __init__(self,boss):
        self.boss=boss
        self.version=1
        self.joueur_blanc = ""
        self.joueur_noir = ""
        self.plateau = None
        self.coups_possible=[]

        self.PLATEAU_DE_BASE=[["r","n","b","q","k","b","n","r"],
                              ["p","p","p","p","p","p","p","p"],
                              [".",".",".",".",".",".",".","."],
                              [".",".",".",".",".",".",".","."],
                              [".",".",".",".",".",".",".","."],
                              [".",".",".",".",".",".",".","."],
                              ["P","P","P","P","P","P","P","P"],
                              ["R","N","B","Q","K","B","N","R"]]
        self.start_new_game("joueur","joueur")

    def start_new_game(self,joueur_blanc,joueur_noir):
        self.joueur_blanc=joueur_blanc
        self.joueur_noir=joueur_noir
        self.plateau = Plateau(self.PLATEAU_DE_BASE, "white")
        self.coups_possible=cherche_coups_possible(self.plateau)

    def joue_un_coup(self,coup):
        joue_un_coup_plateau(self.plateau,coup)
        if self.plateau.joueur_actif=="white":
            self.plateau.joueur_actif='black'
        else:
            self.plateau.joueur_actif="white"
        self.coups_possible=cherche_coups_possible(self.plateau)
        if self.coups_possible==[]:
            print("Ah ba plus de coup possible")

    def teste_si_case_piece_dans_possibles(self,case):
        existe=False
        for coup in self.coups_possible:
            if case==coup[0]:
                existe=True
        return existe

    def renvoie_les_case_possible_pour_piece(self,case):
        cases=[]
        for coup in self.coups_possible:
            if case==coup[0]:
                cases.append(coup[1])
        return cases

    def teste_si_coup_dans_possibles(self,coup):
        existe=False
        for coups in self.coups_possible:
            if coups==coup:
                existe=True
        return existe


