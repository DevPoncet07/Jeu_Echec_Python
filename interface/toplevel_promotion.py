from tkinter import Toplevel, PhotoImage, Canvas


class ToplevelPromotion(Toplevel):
    def __init__(self,boss,coul,coup):
        self.boss=boss
        self.coup=coup
        self.coul=coul
        Toplevel.__init__(self,master=boss)
        self.wm_overrideredirect(True)
        x=self.boss.winfo_x()+coup[1][0]*90+18
        y = self.boss.winfo_y() + 41
        if coul=='black':
            y+=360
        self.geometry("90x360+"+str(x)+"+"+str(y))
        self.liste_image_blanc = [PhotoImage(file="interface/img/knight_white.png"),
                                  PhotoImage(file="interface/img/bishop_white.png"),
                                  PhotoImage(file="interface/img/rook_white.png"),
                                  PhotoImage(file="interface/img/queen_white.png"),]

        self.liste_image_noir=[ PhotoImage(file="interface/img/knight_black.png"),
                                PhotoImage(file="interface/img/bishop_black.png"),
                                PhotoImage(file="interface/img/rook_black.png"),
                                PhotoImage(file="interface/img/queen_black.png")]
        self.piece_blanc=['N','B','R','Q']
        self.piece_noir = ['n', 'b', 'r', 'q']
        self.can=Canvas(self,width=90,height=360,bg='grey30',borderwidth=0,highlightthickness=0)
        self.can.grid()
        self.can.bind('<Button-1>',self.click)
        if coul=='white':
            for y in range(4):
                self.can.create_image(45,45+90*y,image=self.liste_image_blanc[y])
        else:
            for y in range(4):
                self.can.create_image(45,45+90*y,image=self.liste_image_noir[y])


    def click(self,event):
        y=event.y//90
        if self.coul=='white':
            self.boss.sortie_fenetre_promotion([self.coup[0],self.coup[1],self.piece_blanc[y]])
        else:
            self.boss.sortie_fenetre_promotion([self.coup[0], self.coup[1], self.piece_noir[y]])