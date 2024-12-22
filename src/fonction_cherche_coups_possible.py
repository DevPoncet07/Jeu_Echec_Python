from copy import deepcopy
from src.fonction_joue_un_coup_plateau import joue_un_coup_plateau
from src.objet_joueur import ObjetJoueur
from src.plateau import Plateau
"""
#################################################################################
#   Function  very important                                                    #
#                                                                               #
#       _ objet_plateau                                                         #
#                                                                               #
#       search all move possible for a player activ                             #
#       return a list of move possible                                          #
#                                                                               #
#################################################################################
"""
def cherche_coups_possible(obj_plateau,recursive=True):
    coups_possible=[]
    plateau=obj_plateau.plateau
    y = 0
    for ligne in plateau:
        x = 0
        for case in ligne:
            #search white move
            if obj_plateau.joueur_actif.coul=="white":
                #white pawn
                if case=="P":
                    #is in case before end
                    if y>=1:
                        #empty case
                        if plateau[y-1][x]==".":
                            coups_possible.append([[x,y],[x,y-1]])
                        # empty case double move
                        if y==6 and plateau[y-1][x]=="." and plateau[y-2][x]==".":
                            coups_possible.append([[x, y], [x, y - 2]])
                        #secure pawn border left
                        if x>=1:
                            # take black piece left
                            if plateau[y-1][x-1].islower():
                                coups_possible.append([[x, y], [x-1, y - 1]])
                            # take en passant left
                            if obj_plateau.pion_double_avance==[x-1,y-1]:
                                coups_possible.append([[x, y], [x - 1, y - 1]])
                        #secure pawn border right
                        if x<=6:
                            #take black piece right
                            if plateau[y-1][x+1].islower():
                                coups_possible.append([[x, y], [x+1, y - 1]])
                            #take pawn en passant
                            if obj_plateau.pion_double_avance==[x+1,y-1]:
                                coups_possible.append([[x, y], [x + 1, y - 1]])
                #if white rook
                if case == 'R':
                    liste_dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                    for d in range(1, 8):
                        for t in range(4):
                            if liste_dir[t]:
                                x1 = x + liste_dir[t][0] * d
                                y1 = y + liste_dir[t][1] * d
                                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                                    if plateau[y1][x1].isupper():
                                        liste_dir[t] = []
                                    if plateau[y1][x1] == ".":
                                        coups_possible.append([[x, y], [x1, y1]])
                                    elif plateau[y1][x1].islower():
                                        coups_possible.append([[x, y], [x1, y1]])
                                        liste_dir[t] = []
                if case == 'B':
                    liste_dir = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
                    for d in range(1, 8):
                        for t in range(4):
                            if liste_dir[t]:
                                x1 = x + liste_dir[t][0] * d
                                y1 = y + liste_dir[t][1] * d
                                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                                    if plateau[y1][x1].isupper():
                                        liste_dir[t] = []
                                    if plateau[y1][x1] == ".":
                                        coups_possible.append([[x, y], [x1, y1]])
                                    elif plateau[y1][x1].islower():
                                        coups_possible.append([[x, y], [x1, y1]])
                                        liste_dir[t] = []
                if case == 'N':
                    liste_dir = [[-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1]]
                    for premove in liste_dir:
                        x1 = x + premove[0]
                        y1 = y + premove[1]
                        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                            if plateau[y1][x1] == ".":
                                coups_possible.append([[x, y], [x1, y1]])
                            elif plateau[y1][x1].islower():
                                coups_possible.append([[x, y], [x1, y1]])
                if case == 'Q':
                    liste_dir = [[1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [1, 0], [-1, 0], [0, -1]]
                    for d in range(1, 8):
                        for t in range(8):
                            if liste_dir[t]:
                                x1 = x + liste_dir[t][0] * d
                                y1 = y + liste_dir[t][1] * d
                                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                                    if plateau[y1][x1].isupper():
                                        liste_dir[t] = []
                                    if plateau[y1][x1] == ".":
                                        coups_possible.append([[x, y], [x1, y1]])
                                    elif plateau[y1][x1].islower():
                                        coups_possible.append([[x, y], [x1, y1]])
                                        liste_dir[t] = []
                if case == 'K':
                    liste_dir = [[1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [1, 0], [-1, 0], [0, -1]]
                    for premove in liste_dir:
                        x1 = x + premove[0]
                        y1 = y + premove[1]
                        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                            if plateau[y1][x1] == ".":
                                coups_possible.append([[x, y], [x1, y1]])
                            if plateau[y1][x1].islower():
                                coups_possible.append([[x, y], [x1, y1]])


            # search black move
            else:
                #if black pawn
                if case == "p":
                    #is in case before end
                    if y <= 6:
                        #empty case
                        if plateau[y + 1][x] == ".":
                            coups_possible.append([[x, y], [x, y + 1]])
                        #double move
                        if y==1 and plateau[y+1][x]=="." and plateau[y+2][x]==".":
                            coups_possible.append([[x, y], [x, y + 2]])
                        #secure pawn border left
                        if x>=1:
                            #take white piece left
                            if plateau[y+1][x-1].isupper():
                                coups_possible.append([[x, y], [x-1, y + 1]])
                            #take en passant right
                            if obj_plateau.pion_double_avance==[x-1,y+1]:
                                coups_possible.append([[x, y], [x - 1, y + 1]])
                        #secure border right
                        if x<=6:
                            #take white piece right
                            if plateau[y+1][x+1].isupper():
                                coups_possible.append([[x, y], [x+1, y + 1]])
                            #take pawn en passant
                            if obj_plateau.pion_double_avance==[x+1,y+1]:
                                coups_possible.append([[x, y], [x + 1, y + 1]])
                if case == 'r':
                    liste_dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
                    for d in range(1, 8):
                        for t in range(4):
                            if liste_dir[t]:
                                x1 = x + liste_dir[t][0] * d
                                y1 = y + liste_dir[t][1] * d
                                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                                    if plateau[y1][x1].islower():
                                        liste_dir[t] = []
                                    if plateau[y1][x1] == ".":
                                        coups_possible.append([[x, y], [x1, y1]])
                                    elif plateau[y1][x1].isupper():
                                        coups_possible.append([[x, y], [x1, y1]])
                                        liste_dir[t] = []
                if case == 'b':
                    liste_dir = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
                    for d in range(1, 8):
                        for t in range(4):
                            if liste_dir[t]:
                                x1 = x + liste_dir[t][0] * d
                                y1 = y + liste_dir[t][1] * d
                                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                                    if plateau[y1][x1].islower():
                                        liste_dir[t] = []
                                    if plateau[y1][x1] == ".":
                                        coups_possible.append([[x, y], [x1, y1]])
                                    elif plateau[y1][x1].isupper():
                                        coups_possible.append([[x, y], [x1, y1]])
                                        liste_dir[t] = []
                if case == 'n':
                    liste_dir = [[-1, -2], [1, -2], [2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1]]
                    for premove in liste_dir:
                        x1 = x + premove[0]
                        y1 = y + premove[1]
                        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                            if plateau[y1][x1] == ".":
                                coups_possible.append([[x, y], [x1, y1]])
                            elif plateau[y1][x1].isupper():
                                coups_possible.append([[x, y], [x1, y1]])
                if case == 'q':
                    liste_dir = [[1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [1, 0], [-1, 0], [0, -1]]
                    for d in range(1, 8):
                        for t in range(8):
                            if liste_dir[t]:
                                x1 = x + liste_dir[t][0] * d
                                y1 = y + liste_dir[t][1] * d
                                if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                                    if plateau[y1][x1].islower():
                                        liste_dir[t] = []
                                    if plateau[y1][x1] == ".":
                                        coups_possible.append([[x, y], [x1, y1]])
                                    elif plateau[y1][x1].isupper():
                                        coups_possible.append([[x, y], [x1, y1]])
                                        liste_dir[t] = []
                if case == 'k':
                    liste_dir = [[1, 1], [1, -1], [-1, -1], [-1, 1], [0, 1], [1, 0], [-1, 0], [0, -1]]
                    for premove in liste_dir:
                        x1 = x + premove[0]
                        y1 = y + premove[1]
                        if 0 <= x1 <= 7 and 0 <= y1 <= 7:
                            if plateau[y1][x1] == ".":
                                coups_possible.append([[x, y], [x1, y1]])
                            if plateau[y1][x1].isupper():
                                coups_possible.append([[x, y], [x1, y1]])



            x += 1
        y += 1
    if recursive:
        new_coup_possible=[]
        for coup in coups_possible:
            plateau_temp=Plateau(deepcopy(plateau),ObjetJoueur(obj_plateau.joueur_actif.copy()),obj_plateau.joueur_blanc,obj_plateau.joueur_noir)
            plateau_temp.pion_double_avance=deepcopy(obj_plateau.pion_double_avance)
            joue_un_coup_plateau(plateau_temp,coup)
            coups_adverse=cherche_coups_possible(plateau_temp,False)
            echec = False
            for elem in coups_adverse:
                if obj_plateau.joueur_actif.coul=="white":
                    if plateau_temp.plateau[elem[1][1]][elem[1][0]]=='K' :
                        echec=True


                elif obj_plateau.joueur_actif.coul=="black":
                    if plateau_temp.plateau[elem[1][1]][elem[1][0]]=='k'or plateau_temp.plateau[elem[1][1]][elem[1][0]]=='k':
                        echec=True

            if not echec:
                new_coup_possible.append(coup)
        coups_possible=new_coup_possible


    return coups_possible