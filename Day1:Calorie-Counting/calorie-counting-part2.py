puzzle_input = 'day1-puzzle-input.txt'
total_calories_per_elf = []
current_total = 0

with open(puzzle_input, 'r', encoding='utf-8') as f:
    for calorie in f:
        if calorie == '\n': # blank line
            total_calories_per_elf.append(current_total)
            current_total = 0
        else:
            current_total += int(calorie)
    
    # scenario where there were numbers remaining, but there was no newline at 
    # the end of the file
    if current_total > 0:
        total_calories_per_elf.append(current_total)

# sort from biggest to smallest
sorted_calories = sorted(total_calories_per_elf, reverse=True)
top_three_calories = sorted_calories[0:3]
print(sum(top_three_calories)) # correct answer: 204837
