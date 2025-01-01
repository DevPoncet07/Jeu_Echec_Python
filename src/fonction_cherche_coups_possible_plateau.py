
from src.fonction_joue_un_coup_plateau import joue_un_coup_plateau
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
def cherche_coups_possible_adverse_plateau(obj_plateau):
    if obj_plateau.joueur_actif.coul=="white":
        obj_plateau.joueur_actif.coul = "black"
        coups=cherche_coups_possible_plateau(obj_plateau,False)
        obj_plateau.joueur_actif.coul = "white"
    else:
        obj_plateau.joueur_actif.coul = "white"
        coups = cherche_coups_possible_plateau(obj_plateau, False)
        obj_plateau.joueur_actif.coul = "black"
    return coups

def cherche_coups_possible_plateau(obj_plateau,recursive=True):
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
                            if y==1:
                                coups_possible.append([[x, y], [x, y - 1],'R'])
                                coups_possible.append([[x, y], [x, y - 1],'N'])
                                coups_possible.append([[x, y], [x, y - 1],'B'])
                                coups_possible.append([[x, y], [x, y - 1],'Q'])
                            else:
                                coups_possible.append([[x,y],[x,y-1]])
                        # empty case double move
                        if y==6 and plateau[y-1][x]=="." and plateau[y-2][x]==".":
                            coups_possible.append([[x, y], [x, y - 2]])

                        #secure pawn border left
                        if x>=1:
                            # take black piece left
                            if plateau[y-1][x-1].islower():
                                if y == 1:
                                    coups_possible.append([[x, y], [x-1, y - 1], 'R'])
                                    coups_possible.append([[x, y], [x-1, y - 1], 'N'])
                                    coups_possible.append([[x, y], [x-1, y - 1], 'B'])
                                    coups_possible.append([[x, y], [x-1, y - 1], 'Q'])
                                else:
                                    coups_possible.append([[x, y], [x-1, y - 1]])
                            # take en passant left
                            if obj_plateau.pion_double_move==[x-1,y-1] and plateau[y-1][x-1].islower():
                                coups_possible.append([[x, y], [x - 1, y - 1]])
                        #secure pawn border right
                        if x<=6:
                            #take black piece right
                            if plateau[y-1][x+1].islower():
                                if y == 1:
                                    coups_possible.append([[x, y], [x+1, y - 1], 'R'])
                                    coups_possible.append([[x, y], [x+1, y - 1], 'N'])
                                    coups_possible.append([[x, y], [x+1, y - 1], 'B'])
                                    coups_possible.append([[x, y], [x+1, y - 1], 'Q'])
                                else:
                                    coups_possible.append([[x, y], [x+1, y - 1]])
                            #take pawn en passant
                            if obj_plateau.pion_double_move==[x+1,y-1] and plateau[y-1][x+1].islower():
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
                    if x==4 and y ==7 and recursive:
                        if obj_plateau.roc_blanc[0] and obj_plateau.roc_blanc[1] and plateau[y][x-1]=="." and plateau[y][x-2]=="." and plateau[y][x-3]=="."  :
                            if obj_plateau.joueur_actif.coul=="white":
                                obj_plateau.joueur_actif=obj_plateau.joueur_noir
                                coup_temp=cherche_coups_possible_plateau(obj_plateau,False)
                                obj_plateau.joueur_actif = obj_plateau.joueur_blanc
                                case_verif=True
                                for elem in coup_temp:
                                    if elem[1]==[x-1,y]:
                                        case_verif=False
                                    if elem[1]==[x-2,y]:
                                        case_verif=False
                                    if elem[1]==[x,y]:
                                        case_verif=False
                                if case_verif:
                                    coups_possible.append([[x, y], [x-2, y]])
                        if obj_plateau.roc_blanc[1] and obj_plateau.roc_blanc[2] and plateau[y][x+1]=="." and plateau[y][x+2]=="." :

                            if obj_plateau.joueur_actif.coul == "white":
                                obj_plateau.joueur_actif = obj_plateau.joueur_noir
                                coup_temp = cherche_coups_possible_plateau(obj_plateau, False)
                                obj_plateau.joueur_actif = obj_plateau.joueur_blanc
                                case_verif=True
                                for elem in coup_temp:
                                    if elem[1]==[x+1,y]:
                                        case_verif=False
                                    if elem[1]==[x+2,y]:
                                        case_verif=False
                                    if elem[1]==[x,y]:
                                        case_verif=False
                                if case_verif:
                                    coups_possible.append([[x, y], [x+2, y]])


            # search black move
            else:
                #if black pawn
                if case == "p":
                    #is in case before end
                    if y <= 6:
                        #empty case
                        if plateau[y + 1][x] == ".":
                            if y==6:
                                coups_possible.append([[x, y], [x, y + 1],'r'])
                                coups_possible.append([[x, y], [x, y + 1],'n'])
                                coups_possible.append([[x, y], [x, y + 1],'b'])
                                coups_possible.append([[x, y], [x, y + 1],'q'])
                            else:
                                coups_possible.append([[x, y], [x, y + 1]])
                        #double move
                        if y==1 and plateau[y+1][x]=="." and plateau[y+2][x]==".":
                            coups_possible.append([[x, y], [x, y + 2]])
                        #secure pawn border left
                        if x>=1:
                            #take white piece left
                            if plateau[y+1][x-1].isupper():
                                if y == 6:
                                    coups_possible.append([[x, y], [x-1, y + 1], 'r'])
                                    coups_possible.append([[x, y], [x-1, y + 1], 'n'])
                                    coups_possible.append([[x, y], [x-1, y + 1], 'b'])
                                    coups_possible.append([[x, y], [x-1, y + 1], 'q'])
                                else:
                                    coups_possible.append([[x, y], [x-1, y + 1]])
                            #take en passant right
                            if obj_plateau.pion_double_move==[x-1,y+1] and plateau[y+1][x-1].isupper():
                                coups_possible.append([[x, y], [x - 1, y + 1]])
                        #secure border right
                        if x<=6:
                            #take white piece right
                            if plateau[y+1][x+1].isupper():
                                if y == 6:
                                    coups_possible.append([[x, y], [x+1, y + 1], 'r'])
                                    coups_possible.append([[x, y], [x+1, y + 1], 'n'])
                                    coups_possible.append([[x, y], [x+1, y + 1], 'b'])
                                    coups_possible.append([[x, y], [x+1, y + 1], 'q'])
                                else:
                                    coups_possible.append([[x, y], [x+1, y + 1]])
                            #take pawn en passant
                            if obj_plateau.pion_double_move==[x+1,y+1] and plateau[y+1][x+1].isupper():
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
                    if x == 4 and y == 0 and recursive:
                        if obj_plateau.roc_noir[0] and obj_plateau.roc_noir[1] and plateau[y][x - 1] == "." and \
                                plateau[y][x - 2] == "." and plateau[y][x - 3] == ".":
                            if obj_plateau.joueur_actif.coul == "black":
                                obj_plateau.joueur_actif = obj_plateau.joueur_blanc
                                coup_temp = cherche_coups_possible_plateau(obj_plateau, False)
                                obj_plateau.joueur_actif = obj_plateau.joueur_noir
                                case_verif = True
                                for elem in coup_temp:
                                    if elem[1] == [x - 1, y]:
                                        case_verif = False
                                    if elem[1] == [x - 2, y]:
                                        case_verif = False
                                    if elem[1] == [x, y]:
                                        case_verif = False
                                if case_verif:
                                    coups_possible.append([[x, y], [x - 2, y]])
                        if obj_plateau.roc_noir[1] and obj_plateau.roc_noir[2] and plateau[y][x + 1] == "." and \
                                plateau[y][x + 2] == ".":
                            if obj_plateau.joueur_actif.coul == "black":
                                obj_plateau.joueur_actif = obj_plateau.joueur_blanc
                                coup_temp = cherche_coups_possible_plateau(obj_plateau, False)
                                obj_plateau.joueur_actif = obj_plateau.joueur_noir
                                case_verif = True
                                for elem in coup_temp:
                                    if elem[1] == [x + 1, y]:
                                        case_verif = False
                                    if elem[1] == [x + 2, y]:
                                        case_verif = False
                                    if elem[1] == [x, y]:
                                        case_verif = False
                                if case_verif:
                                    coups_possible.append([[x, y], [x + 2, y]])

            x += 1
        y += 1
    if recursive:
        new_coup_possible=[]
        for coup in coups_possible:
            plateau_temp=obj_plateau.recopy()
            joue_un_coup_plateau(plateau_temp,coup)
            coups_adverse=cherche_coups_possible_plateau(plateau_temp,False)
            echec = False
            for elem in coups_adverse:
                if obj_plateau.joueur_actif.coul=="white":
                    if plateau_temp.plateau[elem[1][1]][elem[1][0]]=='K' :
                        echec=True


                elif obj_plateau.joueur_actif.coul=="black":
                    if plateau_temp.plateau[elem[1][1]][elem[1][0]]=='k':
                        echec=True

            if not echec:
                new_coup_possible.append(coup)
        coups_possible=new_coup_possible

    return coups_possible