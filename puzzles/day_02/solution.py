with open('puzzles\\day_02\\input.txt', 'r') as f:
    INPUT = f.read()

WINPOINTS = 6
DRAWPOINTS = 3
LOSSPOINTS = 0

#Rock       (A, X)      1 point
#Paper      (B, Y)      2 points
#Scissors   (C, Z)      3 points

def p1():
    score = 0
    for round in INPUT.split('\n'):
        them = handvalue(round.split(' ')[0])
        us = handvalue(round.split(' ')[1])
        score += us                                 # add the flat value of your played hand
        if them == us:                              # draw condition
            score += DRAWPOINTS
        elif them - us == -1 or them - us == 2:     # win condition
            score += WINPOINTS
        else:                                       # loss condition
            score += LOSSPOINTS
    return score

def handvalue(alphain):
    if alphain == "A" or alphain == "X":
        return 1
    elif alphain == "B" or alphain == "Y":
        return 2
    else:
        return 3

print(f"Your total score is {p1()}.")