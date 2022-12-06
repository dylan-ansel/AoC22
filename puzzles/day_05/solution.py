with open('input.txt', 'r') as f:
    INPUT = f.read()

RAW_CRATE = INPUT.split('\n\n')[0]
RAW_INSTRUCTIONS = INPUT.split('\n\n')[1]


def p1(crat, inst):
    width = len(crat[0])
    for i in range(len(inst)):
        move_count = inst[i][0]
        move_from = inst[i][1] - 1             # get ahead of any off-by-one errors here
        move_to = inst[i][2] - 1               # and here

        for movement in range(move_count):
            letter = \
                find_top_letter_in_stack(crat, move_from)[2]
            previous_home = [
                find_top_letter_in_stack(crat, move_from)[0],
                find_top_letter_in_stack(crat, move_from)[1]]
            new_home = \
                find_first_available_space_in_stack(crat, move_to)

            expected_height = new_home[0] + 1
            current_height = len(crat)
            # DEBUG PRINTING
            # print(f"move {letter} from {previous_home} to {new_home}, "
            #       f"expected: {expected_height}, current: {current_height}")

            if expected_height > current_height:
                crat.append([" " for i in range(width)])
                # DEBUG PRINTING
                # print("new row created")

            crat[new_home[0]][new_home[1]] = letter
            crat[previous_home[0]][previous_home[1]] = " "

        # DEBUG PRINTING
        # for line in crat:
        #     print(line)
        # print('\n')

    message = ""
    transposed = [list(i) for i in zip(*crat)]
    for row in transposed:
        topmost = ""
        for item in row:
            if item.isalpha():
                topmost = item
        message += topmost
    return message


def p2():
    pass


def build_crate():
    crat = []                                       # init crate
    flipped = RAW_CRATE.split('\n')[:-1]
    flipped.reverse()                               # flip the row order
    maxwidth = max(map(len, flipped))               # get max width, so we can pad when parsing shorter lines

    for line in flipped:
        row = flipped.index(line)
        crat.append([])                             # create row so we can append to it later
        for idx in range(maxwidth):
            if idx % 4 == 1:                        # only concern ourselves with indices that could contain letters
                if idx > len(line):                 # if the line is shorter than the max width, pad with null
                    crat[row].append(" ")
                elif line[idx].isalpha():
                    crat[row].append(line[idx])     # if letter, append letter
                else:
                    crat[row].append(" ")           # else, append null

    return crat


def build_instructions():
    byline = RAW_INSTRUCTIONS.split('\n')
    byword = [line.split(" ") for line in byline]
    instr = [[int(entry[1]), int(entry[3]), int(entry[5])] for entry in byword]

    return instr


def find_top_letter_in_stack(crat, stac):
    # returns list in format [row, column, letter]
    column = [letter[stac] for letter in crat]
    h = len(column)
    top = []

    count = h                                       # this absolutely sucks but i gave up for now
    for char in reversed(column):
        count -= 1
        if char.isalpha():
            top = [count, stac, char]
            break

    return top


def find_first_available_space_in_stack(crat, stac):
    # returns list in format [row, column]
    column = [letter[stac] for letter in crat]
    end = len(column)
    space = []

    for char in range(0, end):
        if column[char] == " ":
            space = [char, stac]
            break

    if not space:                               # seems like a shitty workaround, fix later?
        space = [end, stac]                     # returns the to-be-created space if it does not exist

    return space


if __name__ == '__main__':
    crate = build_crate()
    instructions = build_instructions()
    print(f"p1: {p1(crate, instructions)}, p2: {p2()}")
