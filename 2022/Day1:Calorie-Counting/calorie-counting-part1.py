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
