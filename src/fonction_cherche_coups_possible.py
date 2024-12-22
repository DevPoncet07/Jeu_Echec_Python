

def cherche_coups_possible(obj_plateau):
    coups_possible=[]
    plateau=obj_plateau.plateau
    if obj_plateau.joueur_actif=="white":
        y=0
        for ligne in plateau:
            x=0
            for case in ligne:
                if case=="P":
                    if plateau[y-1][x]==".":
                        coups_possible.append([[x,y],[x,y-1]])
                x+=1
            y+=1
    else:
        y = 0
        for ligne in plateau:
            x = 0
            for case in ligne:
                if case == "p":
                    if plateau[y + 1][x] == ".":
                        coups_possible.append([[x, y], [x, y + 1]])
                x += 1
            y += 1


    return coups_possible