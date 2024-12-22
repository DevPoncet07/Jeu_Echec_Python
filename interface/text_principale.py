from tkinter import Text,Frame,Scrollbar,END


class TextPrincipale(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss)

        self.text=Text(self,width=50,height=37,bg='white')
        self.text.grid(row=0,column=0)

        self.scrollbary=Scrollbar(self,command=self.text.yview)
        self.scrollbary.grid(row=0,column=1,sticky="ns")
        self.text["yscrollcommand"]=self.scrollbary.set
        self.text.config(state="disabled")

    def print(self,text):
        self.text.config(state="normal")
        self.text.insert(END,text+"\n")
        self.text.yview_scroll(1,"units")
        self.text.config(state="disabled")