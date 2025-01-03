

from tkinter import *

from interface.canvas_principale import CanvasPrincipal
from interface.frame_right import FrameRight
from interface.toplevel_promotion import ToplevelPromotion
from interface.toplevel_fin_partie import ToplevelFinPartie

from src.main_chess import MoteurEchec


class MainInterface(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.geometry('+0+0')
        self.configure(background="grey30")

        self.case_active = [-1, -1]
        self.case_possible_piece = []
        self.fenetre_fin_partie = None
        self.fenetre_promotion = None
        self.obj_plateau_temp = None


        self.can=CanvasPrincipal(self)
        self.can.grid(row=0,column=0,padx=10,pady=10)
        self.can.afficher_fond()

        self.frame=FrameRight(self)
        self.frame.grid(row=0,column=1,padx=10)

        self.chess=MoteurEchec(self)
        self.nouvelle_partie("joueur","stockfish")


    def click(self,coord):
        if not self.chess.partie_en_cours.fin_de_partie:
            if self.case_active == coord and self.can.boutton_press:
                self.case_active=[-1,-1]
                self.case_possible_piece=[]

                self.can.afficher_case_active(self.case_active, self.case_possible_piece)
                self.can.afficher_pieces(self.chess.partie_en_cours.objetplateau.plateau)



            elif self.chess.demande_case_focus(coord)and self.can.boutton_press:
                self.case_active = coord
                self.case_possible_piece=self.chess.return_case_arriver(coord)
                self.can.afficher_case_active(self.case_active,self.case_possible_piece)
                self.can.prepare_motion(coord)
                self.can.afficher_pieces(self.chess.partie_en_cours.objetplateau.plateau)
            elif self.chess.demande_coup([self.case_active, coord]):
                self.joue_un_coup([self.case_active, coord])
            else:
                self.case_active = [-1, -1]
                self.case_possible_piece = []
                self.can.afficher_case_active(self.case_active, self.case_possible_piece)
                self.can.afficher_pieces(self.chess.partie_en_cours.objetplateau.plateau)

    def nouvelle_partie(self,joueur_blanc,joueur_noir):
        self.envoie_commande_chess(['new',joueur_blanc,joueur_noir])
        if joueur_blanc!='joueur' and joueur_noir=='joueur':
            self.envoie_commande_chess(['joue',None])
            self.case_active = [-1, -1]
            self.case_possible_piece = []
            self.frame.frame_coup_jouer.ajoute_coup(self.chess.partie_en_cours.historique_plateau[-2],
                                                    self.chess.partie_en_cours.historique_plateau[-1].coup_jouer)
            self.can.afficher_case_active(self.case_active, self.case_possible_piece)
            self.can.afficher_pieces(self.chess.return_plateau_actuel())
        elif joueur_blanc!='joueur' and joueur_noir!="joueur":
            self.frame.frame_outils.boutton_nouvelle_partie['state']='disabled'
            while not self.chess.partie_en_cours.fin_de_partie:
                self.envoie_commande_chess(['joue', None])
                self.case_active = [-1, -1]
                self.case_possible_piece = []
                self.can.afficher_case_active(self.case_active, self.case_possible_piece)
                self.can.afficher_pieces(self.chess.return_plateau_actuel())
                self.frame.frame_coup_jouer.ajoute_coup(self.chess.partie_en_cours.historique_plateau[-2],self.chess.partie_en_cours.historique_plateau[-1].coup_jouer)
                self.frame.frame_outils.affichage_piece_perdu(
                    self.chess.partie_en_cours.objetplateau.joueur_blanc.piece_perdu,
                    self.chess.partie_en_cours.objetplateau.joueur_noir.piece_perdu)

                self.update()
            self.frame.frame_outils.boutton_nouvelle_partie['state'] = 'normal'
            self.frame.frame_coup_jouer.mise_a_jour_canvas()
            ToplevelFinPartie(self,self.chess.partie_en_cours.fin_de_partie,self.chess.partie_en_cours.objetplateau.joueur_actif.coul)

    def envoie_commande_chess(self,commande):
        self.chess.decode_commande(commande)

        if commande[0]=="new":
            self.case_active = [-1, -1]
            self.case_possible_piece = []
            self.can.afficher_case_active(self.case_active, self.case_possible_piece)
            self.can.afficher_pieces(self.chess.return_plateau_actuel())
        else:
            self.case_active = [-1, -1]
            self.case_possible_piece = []
            self.can.afficher_case_active(self.case_active, self.case_possible_piece)
            self.can.afficher_pieces(self.chess.partie_en_cours.objetplateau.plateau)




    def joue_un_coup(self,coup):
        if self.chess.demande_promotion(coup) and len(coup)==2:
            self.fenetre_promotion=ToplevelPromotion(self,self.chess.partie_en_cours.objetplateau.joueur_actif.coul,coup)
        elif self.chess.partie_en_cours.objetplateau.joueur_actif.genre=="joueur":
            self.frame.frame_coup_jouer.ajoute_coup(self.chess.partie_en_cours.objetplateau, coup)
            self.envoie_commande_chess(["joue", coup])
            self.frame.frame_outils.affichage_piece_perdu(self.chess.partie_en_cours.objetplateau.joueur_blanc.piece_perdu,self.chess.partie_en_cours.objetplateau.joueur_noir.piece_perdu)
            self.update()
            print(self.chess.partie_en_cours.objetplateau.score_position)
            if self.chess.partie_en_cours.historique_plateau[-1].joueur_actif.genre != "joueur":
                self.envoie_commande_chess(["joue", None])
                self.frame.frame_coup_jouer.ajoute_coup(self.chess.partie_en_cours.historique_plateau[-2],self.chess.partie_en_cours.historique_plateau[-1].coup_jouer)
            self.case_active = [-1, -1]
            self.case_possible_piece = []
            self.can.afficher_case_active(self.case_active, self.case_possible_piece)
            self.can.afficher_pieces(self.chess.partie_en_cours.objetplateau.plateau)

        if self.chess.partie_en_cours.fin_de_partie:
            ToplevelFinPartie(self,self.chess.partie_en_cours.fin_de_partie,self.chess.partie_en_cours.objetplateau.joueur_actif.coul)


    def sortie_fenetre_promotion(self, coup):
        self.joue_un_coup(coup)
        self.fenetre_promotion.destroy()

    def selectionne_plateau(self,index):
        self.obj_plateau_temp=self.chess.partie_en_cours.historique_plateau[index]
        self.case_active = [-1, -1]
        self.case_possible_piece = []
        self.can.afficher_case_active(self.case_active, self.case_possible_piece)
        self.can.afficher_pieces(self.obj_plateau_temp.plateau)




if __name__=='__main__':
    main=MainInterface()
    main.mainloop()

