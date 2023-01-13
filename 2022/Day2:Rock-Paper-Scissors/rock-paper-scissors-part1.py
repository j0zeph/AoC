puzzle_input = 'day2-puzzle-input.txt'

# X=rock, Y=paper, Z=scissors, from my POV
# A=rock, B=paper, C=scissors, from opponent's POV
stats = {
    'X': {'score': 1, 'beats': 'C', 'beaten by': 'B', 'draws with': 'A'},
    'Y': {'score': 2, 'beats': 'A', 'beaten by': 'C', 'draws with': 'B'},
    'Z': {'score': 3, 'beats': 'B', 'beaten by': 'A', 'draws with': 'C'},
}

outcomes = {'win': 6, 'draw': 3, 'loss': 0}

my_score = 0

with open(puzzle_input, 'r', encoding='utf-8') as f:
    for round in f:
        their_shape, my_shape = round.strip().split()
        my_shape_score = stats[my_shape]['score']

        if stats[my_shape]['beats'] == their_shape:
            outcome = outcomes['win']
        elif stats[my_shape]['beaten by'] == their_shape:
            outcome = outcomes['loss']
        else:
            outcome = outcomes['draw']

        my_score += (my_shape_score + outcome)

print(my_score) # correct answer: 14264
