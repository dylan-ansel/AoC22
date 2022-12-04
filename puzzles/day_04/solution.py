with open('input.txt', 'r') as f:
    INPUT = f.read()


def p1():
    count = 0
    assignments = parse(INPUT)

    for pair in assignments:
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            count += 1
        elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            count += 1

    return count


def p2():
    count = 0
    assignments = parse(INPUT)

    for pair in assignments:
        first = range(pair[0][0], pair[0][1] + 1)
        second = range(pair[1][0], pair[1][1] + 1)
        firstset = set(first)

        if len(firstset.intersection(second)) > 0: count += 1

    return count


def parse(raw):
    assignments = []
    for line in raw.split("\n"):
        first = [int(item) for item in line.split(",")[0].split("-")]
        second = [int(item) for item in line.split(",")[1].split("-")]
        assignments.append([first, second])

    return assignments


if __name__ == '__main__':
    print(f"p1: {p1()}, p2: {p2()}")
