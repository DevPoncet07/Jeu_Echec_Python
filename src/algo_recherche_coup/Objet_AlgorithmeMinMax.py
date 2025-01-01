
from random import choice

from src.fonction_cherche_coups_possible_plateau import cherche_coups_possible_plateau
from src.fonction_cherche_coups_possible_plateau import cherche_coups_possible_adverse_plateau
from src.fonction_joue_un_coup_plateau import joue_un_coup_plateau
from src.fonction_analyse_score_position import analyse_score_position


class AlgorithmeMinMax:
    def __init__(self,boss):
        self.boss=boss
        self.objet_plateau =None

    def trouve_un_coup(self,objet_plateau,profondeur=0):
        liste_score=[]
        self.objet_plateau=objet_plateau.recopy()
        for coup_possible in objet_plateau.coups_possible:
            plateau_temp=self.objet_plateau.recopy()
            plateau_temp=self.joue_un_coup(plateau_temp,coup_possible)
            liste_score.append(plateau_temp.score_position)
        if self.objet_plateau.joueur_actif.coul=='white':
            index=self.meilleur_index(liste_score)
        else:
            index = self.pire_index(liste_score)
        if len(index)==1:
            index=index[0]
        elif len(index)>1:
            index=choice(index)
        else:
            pass
        return self.objet_plateau.coups_possible[index]

    def joue_un_coup(self,obj_plateau,coup):
        objet_plateau = joue_un_coup_plateau(obj_plateau, coup)
        objet_plateau.coups_possible = cherche_coups_possible_plateau(objet_plateau, True)
        objet_plateau.coups_adverse = cherche_coups_possible_adverse_plateau(objet_plateau)
        objet_plateau.score_position = analyse_score_position(objet_plateau)
        return  objet_plateau

    def meilleur_index(self,liste):
        meilleur=liste[0]
        index_meilleur=[]
        index=0
        for elem in liste:
            if elem==meilleur:
                index_meilleur.append(index)
            elif elem>meilleur:
                index_meilleur=[index]
                meilleur=elem
            index+=1
        return index_meilleur

    def pire_index(self,liste):
        meilleur=liste[0]
        index_meilleur=[]
        index=0
        for elem in liste:
            if elem==meilleur:
                index_meilleur.append(index)
            elif elem<meilleur:
                index_meilleur=[index]
                meilleur=elem
            index+=1
        return index_meilleur


class Node:
    def __init__(self,objet_plateau,parent,enfants):
        self.objet_plateau=objet_plateau
        self.parent=parent
        self.enfants=enfants