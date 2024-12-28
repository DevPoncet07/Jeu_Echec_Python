"""
#################################################################################
#   Function important                                                          #
#                                                                               #
#       _ objet_plateau                                                         #
#       _ coup                                                                  #
#                                                                               #
#       apply a move and modify information  into an objet plateau              #
#       return obj_plateau modifier                                             #
#                                                                               #
#################################################################################
"""

def joue_un_coup_plateau(obj_plateau,coup):
    depart=coup[0]
    arriver=coup[1]
    plateau=obj_plateau.plateau

    if plateau[arriver[1]][arriver[0]].islower() and obj_plateau.joueur_actif.coul == "white" and plateau[arriver[1]][
        arriver[0]] != ".":
        obj_plateau.joueur_noir.piece_perdu.append(plateau[arriver[1]][arriver[0]])
    if plateau[arriver[1]][arriver[0]].isupper() and obj_plateau.joueur_actif.coul == "black" and plateau[arriver[1]][
        arriver[0]] != ".":
        obj_plateau.joueur_blanc.piece_perdu.append(plateau[arriver[1]][arriver[0]])

    # if the piece is a white pawn
    if plateau[depart[1]][depart[0]]=="P":
        if len(coup)==3:
            plateau[arriver[1]][arriver[0]] = coup[2]
            plateau[depart[1]][depart[0]] = "."
        #if double move
        elif depart[1]-arriver[1]==2:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            obj_plateau.pion_double_move=[depart[0],depart[1]-1]
        # take en passant
        elif depart[1]-arriver[1]==1 and obj_plateau.pion_double_move==[arriver[0],arriver[1]]:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            plateau[arriver[1]+1][arriver[0]] = "."
            obj_plateau.pion_double_move=[]
        # move normally
        else:
            plateau[arriver[1]][arriver[0]]=plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            obj_plateau.pion_double_move = []
    elif plateau[depart[1]][depart[0]]=="K":
        if depart[0]-arriver[0]==2:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            plateau[7][3] = "R"
            plateau[7][0] = "."
        elif arriver[0]-depart[0]==2:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            plateau[7][5] = "R"
            plateau[7][7] = "."
        else:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
        obj_plateau.roc_blanc[1]=False

    #if the piece is a black pawn
    elif plateau[depart[1]][depart[0]]=="p":
        if len(coup)==3:
            plateau[arriver[1]][arriver[0]] = coup[2]
            plateau[depart[1]][depart[0]] = "."
        #if double move
        elif depart[1] - arriver[1] == (-2):
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            obj_plateau.pion_double_move = [depart[0],depart[1] + 1]
        #if take en passant
        elif depart[1]-arriver[1]==(-1) and obj_plateau.pion_double_move==[arriver[0],arriver[1]]:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            plateau[arriver[1]-1][arriver[0]] = "."
            obj_plateau.pion_double_move = []
        #move normally
        else:
            plateau[arriver[1]][arriver[0]]=plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            obj_plateau.pion_double_move = []

    elif plateau[depart[1]][depart[0]]=="k":
        if depart[0]-arriver[0]==2:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            plateau[0][3] = "r"
            plateau[0][0] = "."
        elif arriver[0]-depart[0]==2:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            plateau[0][5] = "r"
            plateau[0][7] = "."
        else:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
    else:
        if plateau[depart[1]][depart[0]] == "R" and depart[0] == 0:
            obj_plateau.roc_blanc[0] = False
        if plateau[depart[1]][depart[0]] == "R" and depart[0] == 7:
            obj_plateau.roc_blanc[2] = False
        if plateau[depart[1]][depart[0]] == "r" and depart[0] == 0:
            obj_plateau.roc_noir[0] = False
        if plateau[depart[1]][depart[0]] == "r" and depart[0] == 7:
            obj_plateau.roc_noir[2] = False
        plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
        plateau[depart[1]][depart[0]] = "."
        obj_plateau.pion_double_move = []

    if obj_plateau.joueur_actif.coul == "white":
        obj_plateau.joueur_actif = obj_plateau.joueur_noir
    else:
        obj_plateau.joueur_actif = obj_plateau.joueur_blanc
    obj_plateau.coup_jouer=coup
    return obj_plateau