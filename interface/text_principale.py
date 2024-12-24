from tkinter import Text, Frame, Scrollbar, END, Entry, StringVar, Button


class TextPrincipale(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss,bg="grey20")
        self.text=Text(self,width=44,height=24,bg='white',font="Helvetica 13")
        self.text.grid(row=0,column=0)

        self.scrollbary=Scrollbar(self,command=self.text.yview)
        self.scrollbary.grid(row=0,column=1,sticky="ns")
        self.text["yscrollcommand"]=self.scrollbary.set
        self.text.config(state="disabled")

        self.frame=Frame(self,bg='grey20')
        self.str_entry=StringVar()
        self.entry=Entry(self.frame,width=38,font="Helvetica 13",textvariable=self.str_entry)
        self.entry.grid(row=0,column=0,pady=5)
        self.entry.bind('<Return>', lambda event: self.valide())
        self.boutton_envoie=Button(self.frame,text="Valide",command=self.valide)
        self.boutton_envoie.grid(row=0,column=1,padx=3)
        self.frame.grid(row=1,column=0,columnspan=2)

    def valide(self):
        commande=self.str_entry.get()
        self.boss.envoie_commande_chess(commande.split(" "))
        self.print(commande,'Commande : ')
        self.str_entry.set('')

    def print(self,text,infos):
        self.text.config(state="normal")
        self.text.insert(END, infos)
        self.text.insert(END,text+"\n")
        self.text.yview_scroll(5,"units")
        self.text.config(state="disabled")

    def clear_console(self):
        self.text.config(state="normal")
        self.text.delete("0.0",END)
        self.text.config(state="disabled")