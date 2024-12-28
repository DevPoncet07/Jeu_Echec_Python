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
        Label(self, text=str(genre)+str(self.coul)).grid()

