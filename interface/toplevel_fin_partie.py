from tkinter import Toplevel,Label,Button


class ToplevelFinPartie(Toplevel):
    def __init__(self,boss,genre,coul):
        self.boss=boss
        self.genre=genre
        x=self.boss.winfo_x()+360
        y=self.boss.winfo_y()+360
        Toplevel.__init__(self,master=boss)
        self.geometry('+'+str(x)+'+'+str(y))
        self.wm_overrideredirect(True)
        self.configure(bg='grey30')
        if coul=='white':
            self.coul="Blanc"
        else:
            self.coul='Noir'
        Label(self, text=str(genre)+str(self.coul),fg='white',bg='grey30').grid(padx=20,pady=20)
        Button(self,text='Quit',bg='grey30',fg='white',command=lambda:self.destroy()).grid(row=1,column=0,pady=10)

