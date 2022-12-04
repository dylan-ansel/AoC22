with open('input.txt', 'r') as f:
    INPUT = f.read()


def p1():
    count = 0
    pairs = []
    for line in INPUT.split("\n"):
        firststr = line.split(",")[0].split("-")
        secondstr = line.split(",")[1].split("-")

        first = [int(item) for item in firststr]
        second = [int(item) for item in secondstr]

        if first[0] <= second[0] and first[1] >= second[1]:
            #print(f"{first}, {second}")
            count += 1
        elif second[0] <= first[0] and second[1] >= first[1]:
            #print(f"{first}, {second}")
            count += 1
    #print(pairs)
    return count


def p2():
    return ""


if __name__ == '__main__':
    print(p1(), p2())
