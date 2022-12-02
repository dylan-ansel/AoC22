elfcalories = []

with open("puzzles\\day_01\\input.txt") as f:
    runningtotal = 0
    for g in f:
        if g == "\n":
            elfcalories.append(runningtotal)
            runningtotal = 0
        else:
            runningtotal += int(g)
  
print(f"Elf number {elfcalories.index(max(elfcalories)) + 1} is carrying {max(elfcalories)} total calories.")

#part 2
topthreecaloriecount = 0
sortedelves = sorted(elfcalories, reverse=True)

for i in range(len(sortedelves)):
    if i < 3:
        topthreecaloriecount += sortedelves[i]

print(f"The sum of the top three fatasses is {topthreecaloriecount}.")