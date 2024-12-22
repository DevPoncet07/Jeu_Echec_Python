import tkinter.font
from tkinter import *
from src.main_moteur import MoteurEchec
from interface.canvas_principale import CanvasPrincipal
from interface.toplevel_fin_partie import ToplevelFinPartie
from interface.frame_outils import FrameOutils


class MainInterface(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("+0+0")
        self.configure(background="grey30")
        self.chess=MoteurEchec(self)
        self.chess.start_new_game("joueur", "aleatoire")

        self.frame_info=Frame(self,bg='grey20')
        self.font_info=tkinter.font.Font(font="Arial",size=10,weight='bold')
        Label(self.frame_info, text="Bienvenue sur PakChess",bg='grey20',font=self.font_info,fg='white').grid(row=0, column=0)
        Label(self.frame_info, text="version: " + str(self.chess.version),bg='grey20',fg='white').grid(row=1, column=0)
        self.frame_info.grid(row=0,column=0)

        self.can=CanvasPrincipal(self)
        self.can.grid(row=1,column=0,padx=10,pady=10)


        self.frame_outils=FrameOutils(self)
        self.frame_outils.grid(row=1,column=1,padx=10)
        self.text=self.frame_outils.text

        self.case_active =[-1,-1]
        self.case_possible_piece=[]
        self.fenetre_fin_partie=None

        self.can.afficher_case_active(self.case_active, self.case_possible_piece)
        self.can.afficher_pieces(self.chess.plateau.plateau)

    def nouvelle_partie(self,joueur_blanc,joueur_noir):
        self.chess.start_new_game(joueur_blanc, joueur_noir)
        self.case_active = [-1, -1]
        self.case_possible_piece = []
        self.fenetre_fin_partie = None
        self.can.afficher_case_active(self.case_active, self.case_possible_piece)
        self.can.afficher_pieces(self.chess.plateau.plateau)
        if self.chess.plateau.joueur_actif.coul=="white" and self.chess.plateau.joueur_actif.genre!='joueur':
            self.chess.plateau.joueur_actif.joue_un_coup(self.chess.plateau,self.chess.coups_possible)
            self.joue_un_coup(self.chess.plateau.joueur_actif.coup)

    def onclick(self,coord_click):
        if self.chess.teste_si_case_piece_dans_possibles(coord_click):
            if self.case_active==coord_click:
                self.case_active=[-2,-2]
                self.case_possible_piece = []
            else:
                self.case_active=coord_click
                self.case_possible_piece=self.chess.renvoie_les_case_possible_pour_piece(self.case_active)
        elif self.chess.teste_si_coup_dans_possibles([self.case_active,coord_click]):
            self.joue_un_coup([self.case_active,coord_click])
            self.case_active=[-2,-2]
            self.case_possible_piece=[]
            self.text.print("coup jouer  : " + str(self.case_active)+" "+str(coord_click))

        else:
            self.case_active = [-2, -2]
            self.case_possible_piece = []
        self.can.afficher_case_active(self.case_active,self.case_possible_piece)
        self.can.afficher_pieces(self.chess.plateau.plateau)

    def joue_un_coup(self,coup):
        if coup!=[-1]:
            if self.chess.plateau.joueur_actif.genre=="joueur":
                self.chess.joue_un_coup(coup)
        self.can.afficher_case_active(self.case_active, self.case_possible_piece)
        self.can.afficher_pieces(self.chess.plateau.plateau)
        if self.chess.partie_fini:
            self.fenetre_fin_partie = ToplevelFinPartie(self, "plus de coup", self.chess.plateau.joueur_actif.coul)
        else:
            if self.chess.plateau.joueur_actif.coul == "white" and self.chess.joueur_blanc.genre!="joueur":
                self.chess.joue_un_coup(self.chess.plateau.joueur_actif.coup)
                self.can.update()
                #time.sleep(0.1)
                self.joue_un_coup([-1])
            elif self.chess.plateau.joueur_actif.coul == "black" and self.chess.joueur_noir.genre != "joueur":
                self.chess.joue_un_coup(self.chess.plateau.joueur_actif.coup)
                self.can.update()
                #time.sleep(0.1)
                self.joue_un_coup([-1])
            elif self.chess.partie_fini:
                self.fenetre_fin_partie = ToplevelFinPartie(self, "plus de coup", self.chess.plateau.joueur_actif.coul)






if __name__=="__main__":
    maininterface=MainInterface()
    maininterface.mainloop()