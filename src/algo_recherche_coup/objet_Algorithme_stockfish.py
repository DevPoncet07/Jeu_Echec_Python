from stockfish import Stockfish
from threading import Thread


class AlgorithmeStockfish:
    def  __init__(self,boss):
        self.stockfish = None
        self.boss=boss


    def trouve_un_coup(self,objet_parti):
        mythread=ThreadStockfish(objet_parti)
        mythread.start()
        return mythread.join()

class ThreadStockfish(Thread):
    def __init__(self,objet_parti):
        Thread.__init__(self)
        self.stockfish = Stockfish(
        path="C:/Users/la famille/Documents/Projet_git/Repository_Chess_Python/src/stockfish/stockfish-windows-x86-64-avx2",parameters={"UCI_Elo":2500})
        self._return=None
        self.objet_parti=objet_parti
        self.liste_colone = ["8","7", "6", "5", "4", "3", "2", "1"]
        self.liste_ligne = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def run(self):
        liste_coup=[]
        for plateau in self.objet_parti.historique_plateau[1:]:
            liste_coup.append(self.traduis_coup(plateau.coup_jouer))
        self.stockfish.set_position(liste_coup)
        best_move=self.retraduis_coup(self.stockfish.get_best_move())
        self._return=best_move

    def join(self, **kwargs):
        Thread.join(self)
        return self._return

    def traduis_coup(self,coup):
        new_coup=self.liste_ligne[coup[0][0]]+self.liste_colone[coup[0][1]]+self.liste_ligne[coup[1][0]]+self.liste_colone[coup[1][1]]
        return new_coup

    def retraduis_coup(self,coup):
        new_coup=[[self.liste_ligne.index(coup[0]),self.liste_colone.index(coup[1])],[self.liste_ligne.index(coup[2]),self.liste_colone.index(coup[3])]]
        return new_coup