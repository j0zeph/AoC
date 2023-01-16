stacks = {
    1: ['D', 'T', 'R', 'B', 'J', 'L', 'W', 'G'],
    2: ['S', 'W', 'C'],
    3: ['R', 'Z', 'T', 'M'],
    4: ['D', 'T', 'C', 'H', 'S', 'P', 'V'],
    5: ['G', 'P', 'T', 'L', 'D', 'Z'],
    6: ['F', 'B', 'R', 'Z', 'J', 'Q', 'C', 'D'],
    7: ['S', 'B', 'D', 'J', 'M', 'F', 'T', 'R'],
    8: ['L', 'H', 'R', 'B', 'T', 'V', 'M'],
    9: ['Q', 'P', 'D', 'S', 'V'],
}

puzzle_input = 'day5-puzzle-input.txt'


def main():
    with open(puzzle_input, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line.startswith('move'):
                continue
            else:
                # extract the major parts of the instruction
                instructions = tuple(int(x) for x in line.split(' ') if x.isdigit())
                move_crates(stacks, instructions)

    print(get_top_most_crates(stacks))


def move_crates(stacks: dict, instructions: tuple) -> dict:
    """Returns a modified dictionary which is a result of moving crates from one
    stack to another, based on the instructions.
    The instruction (2, 1, 3) says to move 2 crates at once, while maintaining the
    order of crates, from stack 1 to stack 3
    """
    crate_num, src, dest = instructions
    temp = []

    for _ in range(crate_num):
        temp.append(stacks[src].pop())

    temp.reverse()
    stacks[dest].extend(temp)


def get_top_most_crates(stacks: dict) -> str:
    """Returns, as a string, the top-most crates of every stack"""
    top_most_crates = []
    for _, crates in stacks.items():
        # only report a crate if the stack is not empty
        if crates:
            top_most_crates.append(crates[-1])

    return ''.join(top_most_crates)


if __name__ == '__main__':
    main()
