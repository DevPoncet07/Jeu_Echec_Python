
from tkinter import Frame, Label, font


class FrameInfoTop(Frame):
    def __init__(self,boss,version):
        self.boss=boss
        Frame.__init__(self,master=boss,bg='grey20')
        self.font_info=font.Font(font="Arial",size=10,weight='bold')
        Label(self, text="Bienvenue sur PakChess",bg='grey20',font=self.font_info,fg='white').grid(row=0, column=0)
        Label(self, text="version: " + str(version),bg='grey20',fg='white').grid(row=1, column=0)