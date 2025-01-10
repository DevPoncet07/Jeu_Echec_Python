from  tkinter import Canvas,PhotoImage,font


# noinspection PyGlobalUndefined
class CanvasPrincipal(Canvas):
    def __init__(self,boss):

        self.boss=boss
        Canvas.__init__(self,master=boss,width=721,height=721,bg='grey20',borderwidth=0,highlightthickness=0)
        self.boutton_press=False
        self.bind('<Button-1>',self.click)
        self.bind('<ButtonRelease-1>',self.declick)
        self.bind('<Motion>',self.motion)

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

        self.colone=[8,7,6,5,4,3,2,1]
        self.ligne=["a","b","c","d","e","f","g","h"]
        self.coord_piece_depart = None
        self.plateau = None
        self.img_piece_motion = None
        self.case_active = None
        self.boutton_press = None
        self.var_motion = False
        self.liste_image_piece=[]
        self.liste_image_case=[]
        self.liste_image_case_focus=[]
        self.img_case_noir=PhotoImage(file="interface/img/case_black.png")
        self.img_case_blanche=PhotoImage(file="interface/img/case_white.png")
        self.image_case_focus=PhotoImage(file="interface/img/case_focus.png")
        self.image_case_possible = PhotoImage(file="interface/img/case_possible.png")

    def click(self,event):
        self.boutton_press=True
        x, y = event.x // 90, event.y // 90
        self.boss.click([x, y])



    def declick(self,event):
        self.boutton_press = False
        x, y = event.x // 90, event.y // 90
        self.boss.declick([x, y])

    def prepare_motion(self,coord):
        x=coord[0]
        y=coord[1]
        self.var_motion=True
        self.coord_piece_depart = [x, y]
        self.img_piece_motion = self.create_image(x * 90, y * 90, image=self.dico_img_piece[self.plateau[y][x]],
                                                  anchor='nw')
    def stop_motion(self):
        self.coord_piece_depart = [-1,-1]
        self.delete(self.img_piece_motion)
        self.var_motion = False

    def motion(self,event):
        if self.boutton_press:
            x,y,=event.x,event.y
            self.tag_raise(self.img_piece_motion)
            self.coords(self.img_piece_motion,[x-45,y-45])
    def motion_manuel(self,x,y):
        self.tag_raise(self.img_piece_motion)
        print("mpotion",x,y)
        self.coords(self.img_piece_motion,[x*90,y*90])

    def afficher_fond(self):
        global coul_font
        compteur=0
        for y in range(8):

            for x in range(8):

                if compteur%2==0:
                    img=self.img_case_blanche
                    coul_font="#6aa15f"
                else:
                    img=self.img_case_noir
                    coul_font = "#c7c7b5"
                self.liste_image_case.append(self.create_image(90*x,90*y,anchor="nw",image=img))
                if y==7:
                    self.liste_image_case.append(self.create_text(80+x*90,710, text=self.ligne[x],font=font.Font(family='arial',size=10,weight='bold'),fill=coul_font))
                compteur+=1
            if coul_font =="#c7c7b5":
                coul_font = "#6aa15f"
            else:
                coul_font = "#c7c7b5"
            self.liste_image_case.append(self.create_text(10, 10 + y * 90, text=self.colone[y],font=font.Font(family='arial',size=10,weight='bold'),fill=coul_font))

            compteur+=1

    def afficher_case_active(self,case,cases_possible):
        self.delete_piece()
        self.liste_image_case=[]
        self.liste_image_case_focus = []
        self.liste_image_piece=[]
        self.afficher_fond()
        self.liste_image_case_focus.append(self.create_image(case[0]*90,case[1]*90,anchor='nw',image=self.image_case_focus))
        liste_save=[]
        if cases_possible:
            for elem in cases_possible:
                if elem not in liste_save:
                   self.liste_image_case_focus.append( self.create_image(elem[0] * 90, elem[1] * 90,anchor='nw',image=self.image_case_possible))
                   liste_save.append(elem)

    def afficher_pieces(self,plateau):
        y=0
        self.plateau=plateau
        for ligne in plateau:
            x=0
            for case in ligne:
                if self.boutton_press and self.coord_piece_depart == [x, y]:
                    pass
                else:
                    if case!=".":
                        self.liste_image_piece.append(self.create_image(45+90*x,45+90*y,image=self.dico_img_piece[case]))
                x+=1
            y+=1

    def delete_piece(self):
        for e in self.liste_image_piece:
            self.delete(e)
        for e in self.liste_image_case_focus:
            self.delete(e)
        for e in self.liste_image_case:
            self.delete(e)