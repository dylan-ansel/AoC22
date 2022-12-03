with open('puzzles\\day_03\\input.txt', 'r') as f:
    INPUT = f.read()

HARDCODELOL = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
GROUP_SIZE = 3

def p1():
    total = 0
    for rucksack in INPUT.split('\n'):
        first_half = rucksack[:len(rucksack)//2]
        second_half = rucksack[len(rucksack)//2:]
        for char in first_half:
            if char in second_half:
                total += HARDCODELOL.index(char) + 1
                break
    return total

def p2():
    total = 0
    rucksack_list = []
    
    for rucksack in INPUT.split('\n'):
        rucksack_list.append(rucksack)

    for sack_number in range(0, len(rucksack_list), GROUP_SIZE):
        for char in rucksack_list[sack_number]:
            if char in rucksack_list[sack_number + 1] and char in rucksack_list[sack_number + 2]:
                total += HARDCODELOL.index(char) + 1
                break
                    
    return total

print(f"The sum of priorities is {p1()}.")
print(f"The sum of lore that I don't feel like rereading is {p2()}.")