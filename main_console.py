from src.main_moteur import MoteurEchec


class MainConsole:
    def __init__(self):
        self.chess=MoteurEchec(self)

    def demarrage(self):
        print("Bienvenue sur PakChess")
        print("version: "+str(self.chess.version))
        print()
        rep = input("Entre reponse :")
        print(rep)
        print()
        input("Press any key to quit")

if __name__=="__main__":
    mainconsole=MainConsole()
    mainconsole.demarrage()