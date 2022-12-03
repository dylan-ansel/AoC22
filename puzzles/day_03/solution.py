with open('puzzles\\day_03\\input.txt', 'r') as f:
    INPUT = f.read()

hardcodelol = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def p1():
    total = 0
    for rucksack in INPUT.split('\n'):
        first_half = rucksack[:len(rucksack)//2]
        second_half = rucksack[len(rucksack)//2:]

        #print(f"{first_half} {second_half}")
        for char in first_half:
            if char in second_half:
                #print(f"Char: {char}, Value: {hardcodelol.index(char) + 1}\n")
                total += hardcodelol.index(char) + 1
                break
    return total

print(f"The sum of priorities is {p1()}.")