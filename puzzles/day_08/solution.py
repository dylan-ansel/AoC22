import math

with open('input.txt', 'r') as f:
    INPUT = f.read()


def print_grids():
    """prints the input grid and the boolean grid side-by-side in a somewhat readable format"""
    if len(GRID) == len(BOOLGRID):
        for i, row in enumerate(GRID):
            print(f'{row}       {BOOLGRID[i]}')
    else:
        print("Grids are somehow not the same size.")


def get_column(colnum):
    column = [letter[colnum] for letter in GRID]

    return column


def get_row(rownum):
    row = GRID[rownum]

    return row


def p1():
    for i, row in enumerate(GRID):
        # DEBUG PRINTING
        # print("::::::::::::")
        for j, item in enumerate(row):
            is_tallest = [1, 1, 1, 1]
            for rowitem in get_row(i)[:j]:
                if rowitem >= item:
                    is_tallest[0] = 0
                    break
            for rowitem in get_row(i)[j+1:]:
                if rowitem >= item:
                    is_tallest[1] = 0
                    break
            for colitem in get_column(j)[:i]:
                if colitem >= item:
                    is_tallest[2] = 0
                    break
            for colitem in get_column(j)[i+1:]:
                if colitem >= item:
                    is_tallest[3] = 0
                    break
            # DEBUG PRINTING
            # print(f'item: {item}, sum: {is_tallest[2:5]}, row preceding: {get_column(i)[:j]}, row succeeding: {get_column(i)[j+1:]}')
            if sum(is_tallest) > 0:
                BOOLGRID[i][j] = 1

    summ = 0
    for row in BOOLGRID:
        summ += sum(row)

    return summ


def p2():
    products = []

    for i, row in enumerate(GRID):
        # DEBUG PRINTING
        # print("::::::::::::")
        for j, item in enumerate(row):
            scenic = [j, (W - j - 1), i, (H - i - 1)]
            for k, rowitem in enumerate(get_row(i)[:j]):        # look left
                if rowitem >= item:
                    scenic[0] = j-k
            for k, rowitem in enumerate(get_row(i)):            # look right
                # second condition because otherwise the post-slice indices would be unusable
                if rowitem >= item and k > j:
                    scenic[1] = k-j
                    break
            for k, colitem in enumerate(get_column(j)[:i]):     # look up
                if colitem >= item:
                    scenic[2] = i-k
            for k, colitem in enumerate(get_column(j)):         # look down
                if colitem >= item and k > i:
                    scenic[3] = k-i
                    break
            # DEBUG PRINTING
            # print(f'item: {item}, [{i},{j}] scenic: {scenic}, row preceding: {get_row(i)[:j]}, row succeeding: {get_row(i)[j+1:]}')
            products.append(math.prod(scenic))

    return max(products)


if __name__ == '__main__':
    GRID = [[int(char) for char in line] for line in INPUT.split('\n')]
    W, H = len(GRID[0]), len(GRID)  # assume rectangle
    BOOLGRID = [[0 for i in range(W)] for j in range(H)]

    # print_grids()
    print(f'p1: {p1()}, p2: {p2()}')
