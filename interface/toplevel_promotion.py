from tkinter import Toplevel, StringVar, ttk, Button


class ToplevelPromotion(Toplevel):
    def __init__(self,boss,coul,coup):
        self.boss=boss
        self.coup=coup
        Toplevel.__init__(self,master=boss)
        self.str_text_black = StringVar()
        self.combobox_black = ttk.Combobox(self, width=15, textvariable=self.str_text_black)
        if coul=='white':
            self.combobox_black["values"] = ('R', 'N','B','Q')
        else:
            self.combobox_black["values"] = ('r', 'n', 'b', 'q')
        self.combobox_black.current(3)
        self.combobox_black.grid(row=0,column=0)

        self.boutton_valider=Button(self,text="Valider",command = self.valider)
        self.boutton_valider.grid(row=1,column=0)

    def valider(self):
        self.boss.sortie_fenetre_promotion([self.coup[0],self.coup[1],self.combobox_black.get()])