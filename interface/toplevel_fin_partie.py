from tkinter import Toplevel,Label


class ToplevelFinPartie(Toplevel):
    def __init__(self,boss,genre,coul):
        self.boss=boss
        self.genre=genre
        Toplevel.__init__(self,master=boss)
        if coul=='white':
            self.coul="Blanc"
        else:
            self.coul='Noir'
        if self.genre=="plus de coup":
            Label(self,text=str(self.coul)+" na plus de coup").grid()
