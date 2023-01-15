lower_case_priority = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

upper_case_priority = {
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
}

puzzle_input = 'day3-puzzle-input.txt'
total_priorities = 0

# stores every elf group
elf_group = []

with open(puzzle_input, 'r', encoding='utf-8') as f:
    for line in f:
        bag = line.strip()
        elf_group.append(bag)
        if not len(elf_group) == 3:
            continue
        else:
            # use the first bag in the elf group as a starting point for intersection
            common_item = set(elf_group[0])
            for bag in elf_group:
                common_item = common_item.intersection(set(bag))
            # turn common item into a string before its priority is accumulated
            common_item = ''.join(list(common_item))
            if common_item.isupper():
                total_priorities += upper_case_priority[common_item]
            else:
                total_priorities += lower_case_priority[common_item]
            elf_group.clear()

print(total_priorities) # correct answer: 2363
