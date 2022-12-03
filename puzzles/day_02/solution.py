with open('puzzles\\day_02\\input.txt', 'r') as f:
    INPUT = f.read()

WINPOINTS = 6
DRAWPOINTS = 3
LOSSPOINTS = 0

# Rock       (A, X)      1 point
# Paper      (B, Y)      2 points
# Scissors   (C, Z)      3 points

# Expected outcomes (p2)
# Loss   X   1
# Draw   Y   2
# Win    Z   3

wldtable = [
[1,1,2],        # [them, us, outcome]
[1,2,3],
[1,3,1],
[2,1,1],
[2,2,2],
[2,3,3],
[3,1,3],
[3,2,1],
[3,3,2]
]

def p1():
    score = 0
    for round in INPUT.split('\n'):
        them = handvalue(round.split(' ')[0])
        us = handvalue(round.split(' ')[1])
        score += playhand(them, us)
    return score

def p2():
    score = 0
    for round in INPUT.split('\n'):
        them = handvalue(round.split(' ')[0])
        outcome = handvalue(round.split(' ')[1])    # expected outcome
        for k in wldtable:
            if k[0] == them and k[2] == outcome:
                us = k[1]
        score += playhand(them, us)
    return score

def handvalue(alphain):
    if alphain == "A" or alphain == "X":
        return 1
    elif alphain == "B" or alphain == "Y":
        return 2
    else:
        return 3

def playhand(them, us):                         # TODO actually use wldtable for this
    score = 0
    score += us                                 # add the flat value of your played hand
    if them == us:                              # draw condition
        score += DRAWPOINTS
    elif them - us == -1 or them - us == 2:     # win condition
        score += WINPOINTS
    else:                                       # loss condition
        score += LOSSPOINTS
    return score                                

print(f"Your total score is {p1()}.")
print(f"Upon reflection, your score is actually {p2()}.")