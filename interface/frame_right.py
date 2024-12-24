from tkinter import Frame, Button, ttk, StringVar, Label
from interface.frame_info_top import FrameInfoTop
from interface.frame_outils import FrameOutils
from interface.text_principale import TextPrincipale


class FrameRight(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss,bg='grey20')

        self.frame_info_top=FrameInfoTop(self,"1")
        self.frame_info_top.grid(row=0,column=0)

        self.frame_outils=FrameOutils(self)
        self.frame_outils.grid(row=1,column=0,pady=10)

        self.text=TextPrincipale(self)
        self.text.grid(row=2,column=0,padx=10)

    def print(self, text, infos):
        self.text.print(text,infos)

    def envoie_commande_chess(self, commande):
        self.boss.envoie_commande_chess(commande)

    def nouvelle_partie(self,joueur_blanc,joueur_noir):
        self.boss.nouvelle_partie(joueur_blanc,joueur_noir)

    def clear_console(self):
        self.text.clear_console()