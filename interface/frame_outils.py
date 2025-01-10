from tkinter import Frame, Button, StringVar, Label, ttk, Canvas,PhotoImage,ALL

class FrameOutils(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss,bg='grey20')

        self.dico_img_piece = {"r": PhotoImage(file="interface/img/rook_black_mini.png"),
                               "R": PhotoImage(file="interface/img/rook_white_mini.png"),
                               "n": PhotoImage(file="interface/img/knight_black_mini.png"),
                               "N": PhotoImage(file="interface/img/knight_white_mini.png"),
                               "b": PhotoImage(file="interface/img/bishop_black_mini.png"),
                               "B": PhotoImage(file="interface/img/bishop_white_mini.png"),
                               "q": PhotoImage(file="interface/img/queen_black_mini.png"),
                               "Q": PhotoImage(file="interface/img/queen_white_mini.png"),
                               "p": PhotoImage(file="interface/img/pawn_black_mini.png"),
                               "P": PhotoImage(file="interface/img/pawn_white_mini.png")}
        self.boutton_nouvelle_partie = Button(self, text="Nouvelle Partie", command=self.nouvelle_partie, bg='grey30',
                                              fg='white')
        self.boutton_nouvelle_partie.grid(row=0, column=1, pady=10)

        Label(self, text="Joueur Blanc", bg='grey20', fg='white').grid(row=1, column=0)
        self.str_text_white = StringVar()
        self.combobox_white = ttk.Combobox(self, width=15, textvariable=self.str_text_white)
        self.combobox_white["values"] = ('joueur', 'aleatoire','minmax')
        self.combobox_white.current(0)
        self.combobox_white.grid(row=2, column=0, padx=10, pady=10)

        Label(self, text="Joueur Noir", bg='grey20', fg='white').grid(row=1, column=2)
        self.str_text_black = StringVar()
        self.combobox_black = ttk.Combobox(self, width=15, textvariable=self.str_text_black)
        self.combobox_black["values"] = ('joueur', 'aleatoire','minmax','stockfish')
        self.combobox_black.current(0)
        self.combobox_black.grid(row=2, column=2, padx=10, pady=10)

        self.can=Canvas(self,width=350,height=100,bg='grey30')
        self.can.grid(row=3,column=0,columnspan=3)


    def nouvelle_partie(self):
        joueur_blanc=self.combobox_white.get()
        joueur_noir=self.combobox_black.get()
        self.boss.nouvelle_partie(joueur_blanc,joueur_noir)

    def affichage_piece_perdu(self,piece_blanc,piece_noir):
        self.can.delete(ALL)
        for index in range(len(piece_blanc)):
            self.can.create_image(10+index*20,10,anchor='nw',image=self.dico_img_piece[piece_blanc[index]])
        for index in range(len(piece_noir)):
            self.can.create_image(10+index*20,50,anchor='nw',image=self.dico_img_piece[piece_noir[index]])
