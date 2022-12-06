with open('input.txt', 'r') as f:
    INPUT = f.read()


def p1():
    # 4 unique characters
    answer = detect_marker(INPUT, 4)

    return answer


def p2():
    #14 unique characters
    answer = detect_marker(INPUT, 14)

    return answer


def detect_marker(message, number):
    answer = 0
    for i in range(len(message)):
        running = message[i:i + number]
        running_unique = []
        for char in running:
            if running.count(char) == 1:
                running_unique.append(True)                 # is unique? True
            else:
                running_unique.append(False)                # is unique? False
        if False not in running_unique:                     # is any character NOT unique?
            answer = message.index(running) + number
            break

    return answer


if __name__ == '__main__':
    print(f"p1: {p1()}, p2: {p2()}")
