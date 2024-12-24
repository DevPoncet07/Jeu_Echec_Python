from tkinter import Frame, Button, StringVar, Label, ttk, Text, END


class FrameOutils(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss,bg='grey20')

        self.boutton_nouvelle_partie = Button(self, text="Nouvelle Partie", command=self.nouvelle_partie, bg='grey30',
                                              fg='white')
        self.boutton_nouvelle_partie.grid(row=0, column=1, pady=10)

        Label(self, text="Joueur Blanc", bg='grey20', fg='white').grid(row=1, column=0)
        self.str_text_white = StringVar()
        self.combobox_white = ttk.Combobox(self, width=15, textvariable=self.str_text_white)
        self.combobox_white["values"] = ('joueur', 'aleatoire')
        self.combobox_white.current(0)
        self.combobox_white.grid(row=2, column=0, padx=10, pady=10)

        Label(self, text="Joueur Noir", bg='grey20', fg='white').grid(row=1, column=2)
        self.str_text_black = StringVar()
        self.combobox_black = ttk.Combobox(self, width=15, textvariable=self.str_text_black)
        self.combobox_black["values"] = ('joueur', 'aleatoire')
        self.combobox_black.current(0)
        self.combobox_black.grid(row=2, column=2, padx=10, pady=10)

        self.text=Text(self,width=20,height=3,bg='grey20',relief='solid',fg='white',state='disabled')
        self.text.grid(row=3,column=0,columnspan=3)

    def ajoute_texte_coup(self,index,coup):
        self.text['state']='normal'
        self.text.insert(END,str(index)+" "+str(coup))
        self.text['state'] = 'disabled'

    def nouvelle_partie(self):
        joueur_blanc=self.combobox_white.get()
        joueur_noir=self.combobox_black.get()
        self.boss.nouvelle_partie(joueur_blanc,joueur_noir)