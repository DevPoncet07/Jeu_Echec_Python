from src.main_moteur import *


class MainConsole:
    def __init__(self):
        self.chess=MoteurEchec(self)
        self.reponse = ""
    def demarrage(self):
        print("Bienvenue sur PakChess")
        print("version: "+str(self.chess.version))

        while self.reponse!="q":
            self.reponse=input("Entre commande : ")
            if self.reponse=="print":
                print_console(self.chess.plateau)
            if self.reponse=="listecoup":
                print(self.chess.coups_possible)
        input("Press any key to quit")

if __name__=="__main__":
    mainconsole=MainConsole()
    mainconsole.demarrage()