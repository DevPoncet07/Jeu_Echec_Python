from tkinter import *
from src.main_moteur import MoteurEchec


class MainInterface(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.chess=MoteurEchec(self)
        self.demarrage()

    def demarrage(self):
        fenetre1=Toplevel(self)
        fenetre1.attributes("-topmost",True)
        Label(fenetre1,text="Bienvenue sur PakChess").grid(row=0,column=0)
        Label(fenetre1,text="version: "+str(self.chess.version)).grid(row=1,column=0)



if __name__=="__main__":
    maininterface=MainInterface()
    maininterface.mainloop()