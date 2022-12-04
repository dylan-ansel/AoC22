with open('input.txt', 'r') as f:
    INPUT = f.read()


def p1():
    count = 0
    pairs = []
    for line in INPUT.split("\n"):
        first = [int(item) for item in line.split(",")[0].split("-")]
        second = [int(item) for item in line.split(",")[1].split("-")]
        if first[0] <= second[0] and first[1] >= second[1]:
            count += 1
        elif second[0] <= first[0] and second[1] >= first[1]:
            count += 1
    return count


def p2():
    return ""


if __name__ == '__main__':
    print(p1(), p2())
