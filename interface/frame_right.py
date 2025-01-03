from tkinter import Frame
from interface.frame_info_top import FrameInfoTop
from interface.frame_outils import FrameOutils
from interface.frame_coup_jouer import FrameCoupJouer


class FrameRight(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss,bg='grey20')

        self.frame_info_top=FrameInfoTop(self,"1")
        self.frame_info_top.grid(row=0,column=0)

        self.frame_outils=FrameOutils(self)
        self.frame_outils.grid(row=1,column=0,pady=10)

        self.frame_coup_jouer=FrameCoupJouer(self)
        self.frame_coup_jouer.grid(row=2,column=0)

    def nouvelle_partie(self,joueur_blanc,joueur_noir):
        self.boss.nouvelle_partie(joueur_blanc,joueur_noir)
        self.frame_coup_jouer.nouvelle_partie()

    def selectionne_plateau(self,index):
        self.boss.selectionne_plateau(index)