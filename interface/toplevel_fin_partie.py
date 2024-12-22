from tkinter import Toplevel


class ToplevelFinPartie(Toplevel):
    def __init__(self,boss,genre):
        self.boss=boss
        self.genre=genre
        Toplevel.__init__(self,master=boss)
