from tkinter import Frame,Canvas,font,Scrollbar



class FrameCoupJouer(Frame):
    def __init__(self,boss):
        self.boss=boss
        Frame.__init__(self,master=boss)
        self.can=Canvas(self,width=200,height=300,bg='grey30',scrollregion=(0,0,200,300))
        self.can.grid(row=0,column=0)
        self.can.bind("<Button-1>",self.click_coup)
        self.scrolly=Scrollbar(self,orient='vertical',command=self.can.yview)
        self.scrolly.grid(row=0,column=1,sticky='ns')
        self.can.config(yscrollcommand=self.scrolly.set)
        self.liste_coup=[]
        self.liste_image_can=[]
        self.liste_colone=['a','b','c','d','e','f','g','h']
        self.liste_ligne=['8','7','6','5','4','3','2','1']

    def nouvelle_partie(self):
        self.liste_coup = []
        self.liste_image_can = []
        self.can = Canvas(self, width=200, height=300, bg='grey30',scrollregion=self.can.bbox("ALL"))
        self.can.grid(row=0, column=0)
        self.can.bind("<Button-1>", self.click_coup)
        self.can.config(yscrollcommand=self.scrolly.set)
        self.scrolly.configure(command=self.can.yview)

    def ajoute_coup(self,objet_plateau,coup):
        new_coup=""
        plateau=objet_plateau.plateau
        if (plateau[coup[0][1]][coup[0][0]] == 'p' or plateau[coup[0][1]][coup[0][0]] == 'P') and plateau[coup[1][1]][coup[1][0]]!=".":
            new_coup = str(len(self.liste_coup) + 1) + " " +self.liste_colone[coup[0][0]]+"x"+ self.liste_colone[coup[1][0]] + self.liste_ligne[
                coup[1][1]]
        elif (plateau[coup[0][1]][coup[0][0]] == 'p' or plateau[coup[0][1]][coup[0][0]] == 'P') and coup[1]==objet_plateau.pion_double_move:
            new_coup = str(len(self.liste_coup) + 1) + " " + self.liste_colone[coup[0][0]] + "x" + self.liste_colone[
                coup[1][0]] + self.liste_ligne[
                           coup[1][1]]
        elif plateau[coup[0][1]][coup[0][0]]=='p' or plateau[coup[0][1]][coup[0][0]]=='P':
            new_coup=str(len(self.liste_coup)+1)+" "+self.liste_colone[coup[1][0]]+self.liste_ligne[coup[1][1]]

        if (plateau[coup[0][1]][coup[0][0]] == 'n' or plateau[coup[0][1]][coup[0][0]] == 'N') and plateau[coup[1][1]][coup[1][0]]!=".":
            new_coup = str(len(self.liste_coup) + 1) + " Nx" + self.liste_colone[coup[1][0]] + self.liste_ligne[
                coup[1][1]]
        elif plateau[coup[0][1]][coup[0][0]]=='n' or plateau[coup[0][1]][coup[0][0]]=='N':
            new_coup=str(len(self.liste_coup)+1)+" N"+self.liste_colone[coup[1][0]]+self.liste_ligne[coup[1][1]]

        if (plateau[coup[0][1]][coup[0][0]] == 'b' or plateau[coup[0][1]][coup[0][0]] == 'B') and plateau[coup[1][1]][coup[1][0]]!=".":
            new_coup = str(len(self.liste_coup) + 1) + " Bx" + self.liste_colone[coup[1][0]] + self.liste_ligne[
                coup[1][1]]
        elif plateau[coup[0][1]][coup[0][0]]=='b' or plateau[coup[0][1]][coup[0][0]]=='B':
            new_coup=str(len(self.liste_coup)+1)+" B"+self.liste_colone[coup[1][0]]+self.liste_ligne[coup[1][1]]

        if (plateau[coup[0][1]][coup[0][0]] == 'r' or plateau[coup[0][1]][coup[0][0]] == 'R') and plateau[coup[1][1]][coup[1][0]]!=".":
            new_coup = str(len(self.liste_coup) + 1) + " Rx" + self.liste_colone[coup[1][0]] + self.liste_ligne[
                coup[1][1]]
        elif plateau[coup[0][1]][coup[0][0]]=='r' or plateau[coup[0][1]][coup[0][0]]=='R':
            new_coup=str(len(self.liste_coup)+1)+" R"+self.liste_colone[coup[1][0]]+self.liste_ligne[coup[1][1]]

        if (plateau[coup[0][1]][coup[0][0]] == 'q' or plateau[coup[0][1]][coup[0][0]] == 'Q') and plateau[coup[1][1]][coup[1][0]]!=".":
            new_coup = str(len(self.liste_coup) + 1) + " Qx" + self.liste_colone[coup[1][0]] + self.liste_ligne[
                coup[1][1]]
        elif plateau[coup[0][1]][coup[0][0]]=='q' or plateau[coup[0][1]][coup[0][0]]=='Q':
            new_coup=str(len(self.liste_coup)+1)+" Q"+self.liste_colone[coup[1][0]]+self.liste_ligne[coup[1][1]]

        if (plateau[coup[0][1]][coup[0][0]] == 'k' or plateau[coup[0][1]][coup[0][0]] == 'K') and plateau[coup[1][1]][coup[1][0]]!=".":
            new_coup = str(len(self.liste_coup) + 1) + " Kx" + self.liste_colone[coup[1][0]] + self.liste_ligne[
                coup[1][1]]
        elif plateau[coup[0][1]][coup[0][0]]=='k' or plateau[coup[0][1]][coup[0][0]]=='K':
            new_coup=str(len(self.liste_coup)+1)+" K"+self.liste_colone[coup[1][0]]+self.liste_ligne[coup[1][1]]

        print(new_coup)
        self.liste_coup.append(new_coup)
        self.mise_a_jour_canvas()

    def mise_a_jour_canvas(self):
        index=len(self.liste_coup)
        print("index ====",index)
        if index>=24:
            self.can.configure(scrollregion=(0,0,200,20+index*10))
        if len(self.liste_coup)%2==1:
            x=10
            y=10 +( (index - 1) // 2)*20
        else:
            x = 90
            y = 10 +( (index - 1) // 2)*20
        self.liste_image_can.append(self.can.create_text(x,y,anchor="nw",fill='white',text=self.liste_coup[index-1],font=font.Font(size=12,family='Arial')))
        if index%2==1:
            self.can.yview_moveto(20)

    def click_coup(self,event):

        current=event.widget.find_withtag('current')
        if current:
            self.boss.selectionne_plateau(current[0])