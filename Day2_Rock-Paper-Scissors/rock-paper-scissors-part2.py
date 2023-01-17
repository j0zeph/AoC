puzzle_input = 'day2-puzzle-input.txt'

# R=rock, P=paper, S=scissors, from my POV
my_stats = {
    'R': {'score': 1},
    'P': {'score': 2},
    'S': {'score': 3},
}

# A=rock, B=paper, C=scissors, from opponent's POV
their_stats = {
    'A': {'score': 1, 'beats': 'S', 'beaten by': 'P', 'draws with': 'R'},
    'B': {'score': 2, 'beats': 'R', 'beaten by': 'S', 'draws with': 'P'},
    'C': {'score': 3, 'beats': 'P', 'beaten by': 'R', 'draws with': 'S'},
}

outcomes = {
    'X': {'name': 'loss', 'score': 0},
    'Y': {'name': 'draw', 'score': 3},
    'Z': {'name': 'win', 'score': 6},
}

my_score = 0

with open(puzzle_input, 'r', encoding='utf-8') as f:
    for round in f:
        their_shape, my_outcome = round.strip().split()

        if outcomes[my_outcome]['name'] == 'win':
            my_shape = their_stats[their_shape]['beaten by']
        elif outcomes[my_outcome]['name'] == 'loss':
            my_shape = their_stats[their_shape]['beats']
        else:
            my_shape = their_stats[their_shape]['draws with']

        my_score += my_stats[my_shape]['score'] + outcomes[my_outcome]['score']

print(my_score) # correct answer: 12382

