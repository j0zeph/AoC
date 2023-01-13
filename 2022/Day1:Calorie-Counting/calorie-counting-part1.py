"""
Puzzle input: Represents calories of food carried by elves.
Each elves' food is separated from another's by a blank line.

Goal: Find how many calories are being carried by the Elf with the most
Calories"""

puzzle_input = 'day1-puzzle-input.txt'
highest_total = 0
current_total = 0

with open(puzzle_input, 'r', encoding='utf-8') as f:
    for calorie in f:
        if not calorie: # end of file
            break
        elif calorie == '\n': # blank line
            highest_total = max(highest_total, current_total)
            current_total = 0 # reset before the next batch of calories
        else:
            current_total += int(calorie)

print(highest_total) # correct answer: 68442
