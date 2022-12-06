with open('input.txt', 'r') as f:
    INPUT = f.read()

RAW_CRATE = INPUT.split('\n\n')[0]
RAW_INSTRUCTIONS = INPUT.split('\n\n')[1]


def p1(crat, inst):
    for i in range(len(inst)):
        move_count = inst[i][0]
        move_from = inst[i][1] - 1             # get ahead of any off-by-one errors here
        move_to = inst[i][2] - 1               # and here

        for movement in range(move_count):
            letter = \
                find_top_n_letters_in_stack(crat, move_from, 1)[0][2]
            previous_home = \
                find_top_n_letters_in_stack(crat, move_from, 1)[0][:-1]
            new_home = \
                find_first_available_space_in_stack(crat, move_to)

            crat = ensure_adequate_space(crat, new_home, 1)

            crat[new_home[0]][new_home[1]] = letter
            crat[previous_home[0]][previous_home[1]] = " "

    message = get_message(crat)

    return message


def p2(crat, inst):
    for i in range(len(inst)):
        move_count = inst[i][0]
        move_from = inst[i][1] - 1             # get ahead of any off-by-one errors here
        move_to = inst[i][2] - 1               # and here

        previous = \
            find_top_n_letters_in_stack(crat, move_from, move_count)

        for idx in range(move_count - 1, -1, -1):           # this sucks
            letter = previous[idx][2]
            old_home = previous[idx][0:2]
            new_home = \
                find_first_available_space_in_stack(crat, move_to)

            # DEBUG PRINTING
            # print_crate(crat)
            # print(f"move {letter} from {old_home} to {new_home}")

            crat = ensure_adequate_space(crat, new_home, move_count)

            crat[new_home[0]][new_home[1]] = letter
            crat[old_home[0]][old_home[1]] = " "

        # DEBUG PRINTING
        # print_crate(crat)

    message = get_message(crat)

    return message


def build_crate():
    # we're using spaces instead of null because they're easier to debug in a monospaced environment. deal.
    crat = []                                       # init crate
    flipped = RAW_CRATE.split('\n')[:-1]
    flipped.reverse()                               # flip the row order
    maxwidth = max(map(len, flipped))               # get max width, so we can pad when parsing shorter lines

    for line in flipped:
        row = flipped.index(line)
        crat.append([])                             # create row so we can append to it later
        for idx in range(maxwidth):
            if idx % 4 == 1:                        # only concern ourselves with indices that could return letters
                if idx > len(line):                 # if the line is shorter than the max width, pad with space
                    crat[row].append(" ")
                elif line[idx].isalpha():
                    crat[row].append(line[idx])     # if letter, append letter
                else:
                    crat[row].append(" ")           # else, append with space

    return crat


def build_instructions():
    byline = RAW_INSTRUCTIONS.split('\n')
    byword = [line.split(" ") for line in byline]
    instr = [[int(entry[1]), int(entry[3]), int(entry[5])] for entry in byword]

    return instr


def find_top_n_letters_in_stack(crat, stac, n):
    # returns 2d list in format [[row, column, letter]]
    column = get_column(crat, stac)
    top_letters = []
    top = get_stack_height(crat, stac) - 1
    bottom = top - n

    for idx in range(top, bottom, - 1):
        top_letters.append([idx, stac, column[idx]])

    return top_letters


def find_first_available_space_in_stack(crat, stac):
    # returns list in format [row, column]
    column = get_column(crat, stac)
    end = get_stack_height(crat, stac)
    space = []

    for char in range(0, end):
        if column[char] == " ":
            space = [char, stac]
            break

    if not space:                               # seems like a shitty workaround, fix later?
        space = [end, stac]                     # returns the to-be-created space if it does not exist

    return space


def get_message(crat):
    message = ""
    transposed = transpose_crate(crat)
    for row in transposed:
        topmost = ""
        for item in row:
            if item.isalpha():
                topmost = item
        message += topmost

    return message


def get_column(crat, colnum):
    column = [letter[colnum] for letter in crat]

    return column


def get_row(crat, rownum):
    # dunno if i'll use this, but why not?
    row = crat[rownum]

    return row


def get_stack_height(crat, colnum):
    # because len(stac) would include the spaces
    height = 0
    column = get_column(crat, colnum)
    for item in column:
        if item.isalpha(): height += 1

    return height


def transpose_crate(crat):
    transposed = [list(i) for i in zip(*crat)]

    return transposed


def ensure_adequate_space(crat, new_home, move_count):
    width = len(get_row(crat, 0))
    expected_height = new_home[0] + move_count
    current_height = len(crat)

    if expected_height > current_height:
        for count in range(move_count):
            crat.append([" " for i in range(width)])

    return crat


def print_crate(crat):
    length = len(crat)
    crattext = ""

    for idx in range(length - 1, -1, -1):                # seriously enough with this shit
        rowtext = ""
        for item in crat[idx]:
            if item.isalpha():
                rowtext += f"[{item}] "
            else:
                rowtext += f" *  "
        crattext += f"{rowtext}\n"

    print(crattext)


if __name__ == '__main__':
    INSTRUCTIONS = build_instructions()

    CRATE = build_crate()
    print(f"p1: {p1(CRATE, INSTRUCTIONS)}")

    CRATE = build_crate()                       # CRATE is being overwritten after p1() runs somehow ?????
    print(f"p2: {p2(CRATE, INSTRUCTIONS)}")     # so i have to do this dumb shit
