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

    # if the piece is a white pawn
    if plateau[depart[1]][depart[0]]=="P":
        #if double move
        if depart[1]-arriver[1]==2:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            obj_plateau.pion_double_avance=[depart[0],depart[1]-1]
        # take en passant
        elif depart[1]-arriver[1]==1 and obj_plateau.pion_double_avance==[arriver[0],arriver[1]]:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            plateau[arriver[1]+1][arriver[0]] = "."
            obj_plateau.pion_double_avance=[]
        # move normally
        else:
            plateau[arriver[1]][arriver[0]]=plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            obj_plateau.pion_double_avance = []

    #if the piece is a black pawn
    elif plateau[depart[1]][depart[0]]=="p":
        #if double move
        if depart[1] - arriver[1] == (-2):
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            obj_plateau.pion_double_avance = [depart[0],depart[1] + 1]
        #if take en passant
        elif depart[1]-arriver[1]==(-1) and obj_plateau.pion_double_avance==[arriver[0],arriver[1]]:
            plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            plateau[arriver[1]-1][arriver[0]] = "."
            obj_plateau.pion_double_avance = []
        #move normally
        else:
            plateau[arriver[1]][arriver[0]]=plateau[depart[1]][depart[0]]
            plateau[depart[1]][depart[0]] = "."
            obj_plateau.pion_double_avance = []
    else:
        plateau[arriver[1]][arriver[0]] = plateau[depart[1]][depart[0]]
        plateau[depart[1]][depart[0]] = "."
        obj_plateau.pion_double_avance = []

    if obj_plateau.joueur_actif.coul == obj_plateau.joueur_blanc.coul:
        obj_plateau.joueur_actif = obj_plateau.joueur_noir
    else:
        obj_plateau.joueur_actif = obj_plateau.joueur_blanc

    return obj_plateau