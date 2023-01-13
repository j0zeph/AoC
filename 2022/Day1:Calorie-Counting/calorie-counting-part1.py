"""
Puzzle input: Represents calories of food carried by elves.
Each elves' food is separated from another's by a blank line.

Goal: Find how many calories are being carried by the Elf with the most
Calories"""

highest_total = 0
current_total = 0

with open('puzzle-input.txt', 'r', encoding='utf-8') as f:
    while True:
        calorie = f.readline()
        if not calorie:
            break
        # reset current total before moving to the next set of numbers
        elif calorie == '\n':
            highest_total = max(highest_total, current_total)
            current_total = 0
        else:
            current_total += int(calorie)

print(highest_total)
