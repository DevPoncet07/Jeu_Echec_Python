
from random import choice

from src.fonction_cherche_coups_possible_plateau import cherche_coups_possible_plateau
from src.fonction_cherche_coups_possible_plateau import cherche_coups_possible_adverse_plateau
from src.fonction_joue_un_coup_plateau import joue_un_coup_plateau
from src.fonction_analyse_score_position import analyse_score_position



class AlgorithmeMinMax:
    def __init__(self,boss):
        self.node_boss = None
        self.boss=boss
        self.objet_plateau =None
        self.liste_node_new = []
        self.liste_node_vue = []

    def trouve_un_coup(self,objet_plateau,profondeur=2):
        profondeur=2

        self.liste_node_new=[]
        self.liste_node_vue=[]
        self.objet_plateau=objet_plateau
        self.node_boss=Node(objet_plateau,[],[],0)
        self.liste_node_new.append(self.node_boss)
        while self.liste_node_new:
            node_temp=self.liste_node_new.pop()
            if node_temp.profondeur==profondeur or len(node_temp.objet_plateau.coups_possible)==1:
                node_temp.score=analyse_score_position(node_temp.objet_plateau)
            else:
                for coup in node_temp.objet_plateau.coups_possible:
                    plateau_temp=self.joue_un_coup(node_temp.objet_plateau.recopy(),coup)
                    node=Node(plateau_temp,node_temp,[],node_temp.profondeur+1)
                    self.liste_node_new.append(node)
                    node_temp.enfants.append(node)
            self.liste_node_vue.append(node_temp)
        index=self.meilleur_index_boss(self.node_boss)
        return self.objet_plateau.coups_possible[index]

    def joue_un_coup(self,obj_plateau,coup):
        objet_plateau = joue_un_coup_plateau(obj_plateau, coup)
        objet_plateau.coups_possible = cherche_coups_possible_plateau(objet_plateau, True)
        objet_plateau.coups_adverse = cherche_coups_possible_adverse_plateau(objet_plateau)
        objet_plateau.score_position = analyse_score_position(objet_plateau)
        return  objet_plateau

    def meilleur_index_boss(self,node):
        liste_score=[]
        meilleur_index=[]
        for enfant in node.enfants:
            liste_score.append(self.pire_index_enfant(enfant))
        meilleur = liste_score[0]
        for index in range(len(liste_score)):
            if liste_score[index] == meilleur:
                meilleur_index.append(index)
            elif liste_score[index] < meilleur:
                meilleur=liste_score[index]
                meilleur_index = [index]
        if len(meilleur_index)!=1:
            coup=choice(meilleur_index)
            return coup
        else:
            return meilleur_index[0]

    def meilleur_index_enfant(self,node):
        if not node.enfants:
            return node.objet_plateau.score_position
        else:
            liste_score=[]
            for enfant in node.enfants:
                liste_score.append(self.pire_index_enfant(enfant))
            meilleur=liste_score[0]
            for index in range(len(liste_score)):
                if liste_score[index]<meilleur:
                    meilleur=liste_score[index]
            return meilleur

    def pire_index_enfant(self,node):
        if not node.enfants:
            return node.objet_plateau.score_position
        else:
            liste_score=[]
            for enfant in node.enfants:
               liste_score.append(self.meilleur_index_enfant(enfant))
            meilleur = liste_score[0]
            for index in range(len(liste_score)):
                if liste_score[index]> meilleur:
                    meilleur=liste_score[index]
            return meilleur



class Node:
    def __init__(self,objet_plateau,parent,enfants,profondeur):
        self.objet_plateau=objet_plateau
        self.parent=parent
        self.enfants=enfants
        self.profondeur=profondeur
        self.score=None