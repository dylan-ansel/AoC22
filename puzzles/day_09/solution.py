with open('input.txt', 'r') as f:
    INPUT = f.read()

STEPS = [line.split(' ') for line in INPUT.split('\n')]

# start at origin
H = [0, 0]
T = [0, 0]

JOURNEY = [[T[0], T[1]]]


def move_head(step):
    if step[0] == "U":
        H[1] += int(step[1])
    elif step[0] == "D":
        H[1] -= int(step[1])
    elif step[0] == "L":
        H[0] -= int(step[1])
    elif step[0] == "R":
        H[0] += int(step[1])
    else:
        print("error parsing move head input")


def is_adjacent():
    if abs(H[0] - T[0]) >= 2 or abs(H[1] - T[1]) >= 2:
        return False
    else:
        return True


def can_move_straight():
    if H[0] == T[0] or H[1] == T[1]:
        return True
    else:
        return False


def move_straight():
    # determine on which axis to move T
    axis = 0        # seems dangerous but it yells at me if i don't init
    if T[0] != H[0]:
        axis = 0
    elif T[1] != H[1]:
        axis = 1
    else:
        print("How did you get here?")

    # move T along the appropriate axis
    if H[axis] - T[axis] > 0:
        T[axis] += 1
    else:
        T[axis] -= 1


def move_diagonally():
    # define direction (-1 or 1) for each axis
    x = 1 if H[0] > T[0] else -1
    y = 1 if H[1] > T[1] else -1

    # move T diagonally
    T[0] += x
    T[1] += y


def append_journey():
    if [T[0], T[1]] not in JOURNEY:
        JOURNEY.append([T[0], T[1]])  # why can't i append T? dunno


def p1():
    for step in STEPS:
        move_head(step)
        while not is_adjacent():
            append_journey()
            if can_move_straight():
                move_straight()
            else:
                move_diagonally()
    return len(JOURNEY)


def p2():
    pass


if __name__ == '__main__':
    print(f'p1: {p1()}, p2: {p2()}')
