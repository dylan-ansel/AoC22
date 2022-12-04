with open('input.txt', 'r') as f:
    INPUT = f.read()


def p1():
    count = 0
    pairs = []
    for line in INPUT.split("\n"):
        first = line.split(",")[0].split("-")
        second = line.split(",")[1].split("-")
        if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
            print(f"{first}, {second}")
            count += 1
        elif int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1]):
            print(f"{first}, {second}")
            count += 1
    #print(pairs)
    return count

    # TODO figure out why i had to cast all this shit


def p2():
    return ""


if __name__ == '__main__':
    print(p1(), p2())
