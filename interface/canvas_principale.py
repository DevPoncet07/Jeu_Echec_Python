from  tkinter import Canvas,ALL,PhotoImage


class CanvasPrincipal(Canvas):
    def __init__(self,boss):
        self.boss=boss
        Canvas.__init__(self,master=boss,width=721,height=721,bg='grey20',borderwidth=0,highlightthickness=0)
        self.boutton_press=False
        self.bind('<Button-1>',self.click)

        self.dico_img_piece= {"r":PhotoImage(file="interface/img/rook_black.png"),
                              "R":PhotoImage(file="interface/img/rook_white.png"),
                              "n":PhotoImage(file="interface/img/knight_black.png"),
                              "N":PhotoImage(file="interface/img/knight_white.png"),
                              "b":PhotoImage(file="interface/img/bishop_black.png"),
                              "B":PhotoImage(file="interface/img/bishop_white.png"),
                              "q":PhotoImage(file="interface/img/queen_black.png"),
                              "Q":PhotoImage(file="interface/img/queen_white.png"),
                              "k":PhotoImage(file="interface/img/king_black.png"),
                              "K":PhotoImage(file="interface/img/king_white.png"),
                              "p":PhotoImage(file="interface/img/pawn_black.png"),
                              "P":PhotoImage(file="interface/img/pawn_white.png")}
        self.img_case_noir=PhotoImage(file="interface/img/case_black.png")
        self.img_case_blanche=PhotoImage(file="interface/img/case_white.png")
        self.image_case_focus=PhotoImage(file="interface/img/case_focus.png")
        self.image_case_possible = PhotoImage(file="interface/img/case_possible.png")

    def click(self,event):
        self.boutton_press=True
        x,y=event.x//90,event.y//90
        self.boss.click([x,y])

    def afficher_fond(self):
        compteur=0
        for y in range(8):
            for x in range(8):

                if compteur%2==0:
                    img=self.img_case_blanche
                else:
                    img=self.img_case_noir
                self.create_image(90*x,90*y,anchor="nw",image=img)
                compteur+=1
            compteur+=1

    def afficher_case_active(self,case,cases_possible):
        self.delete(ALL)
        self.afficher_fond()
        self.create_image(case[0]*90,case[1]*90,anchor='nw',image=self.image_case_focus)
        if cases_possible:
            for elem in cases_possible:
                self.create_image(elem[0] * 90, elem[1] * 90,anchor='nw',image=self.image_case_possible)

    def afficher_pieces(self,plateau):
        y=0
        for ligne in plateau:
            x=0
            for case in ligne:
                if case!=".":
                    self.create_image(45+90*x,45+90*y,image=self.dico_img_piece[case])
                x+=1
            y+=1