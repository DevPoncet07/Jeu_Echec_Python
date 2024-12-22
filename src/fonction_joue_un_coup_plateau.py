

def joue_un_coup_plateau(obj_plateau,coup):
    depart=coup[0]
    arriver=coup[1]
    plateau=obj_plateau.plateau
    plateau[arriver[1]][arriver[0]]=plateau[depart[1]][depart[0]]
    plateau[depart[1]][depart[0]] = "."
    return obj_plateau