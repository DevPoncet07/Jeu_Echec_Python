from tkinter import Frame, Canvas,ALL

from math import exp,e


class FrameBarreScore(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss,bg='grey20')
        self.can=Canvas(self,width=25,height=721,bg='black',borderwidth=0,highlightthickness=0)
        self.can.grid()
        self.can.create_rectangle(0,360,25,721,fill='white')

    def mise_a_jour(self,score):
        self.can.delete(ALL)
        print(score)
        y=360-score
        self.can.create_rectangle(0,y,25,721,fill='white')