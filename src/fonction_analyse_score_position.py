


def analyse_score_position(objet_plateau):
    score=0
    for ligne in objet_plateau.plateau:
        for case in ligne:
            if case=="p":score-=1
            if case=="r":score-=5
            if case=='n':score-=3
            if case=='b':score-=3
            if case=='q':score-=9
            if case=='k':score-=100
            if case=="P":score+=1
            if case=="R":score+=5
            if case=='N':score+=3
            if case=='B':score+=3
            if case=='Q':score+=9
            if case=='K':score+=100
    if objet_plateau.joueur_actif.coul=='white':
        score+=len(objet_plateau.coups_possible)
        score-=len(objet_plateau.coups_adverse)
    else:
        score -= len(objet_plateau.coups_possible)
        score += len(objet_plateau.coups_adverse)
    if objet_plateau.joueur_actif.coul=='white':
        for coup in objet_plateau.coups_adverse:
            if objet_plateau.plateau[coup[1][1]][coup[1][0]]=="K":
                score-=100
                print(objet_plateau.coups_possible)
                if len(objet_plateau.coups_possible)==0:
                    score-=1000
    else:
        for coup in objet_plateau.coups_adverse:
            if objet_plateau.plateau[coup[1][1]][coup[1][0]]=="k":
                score+=100
                print(objet_plateau.coups_possible)
                if len(objet_plateau.coups_possible)==0:
                    score+=1000
    return score