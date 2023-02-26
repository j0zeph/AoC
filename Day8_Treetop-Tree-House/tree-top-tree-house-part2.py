from typing import List, NamedTuple

Location = NamedTuple('Location', [('y', int), ('x', int)])
puzzle_input = 'day8-puzzle-input.txt'

grid: List[List[int]] = []

with open(puzzle_input, 'r', encoding='utf-8') as f:
    for line in f:
        pure_line = line.strip()
        grid.append(list(map(int, pure_line)))


def main():
    trees_in_one_row = len(grid[0])
    highest_score = 0

    for row in range(len(grid)):
        for col in range(trees_in_one_row):
            location = Location(row, col)
            vertical_score = scenic_score_above_and_below(location, grid)
            horizontal_score = scenic_score_left_and_right(location, grid)
            scenic_score = vertical_score * horizontal_score
            highest_score = scenic_score if scenic_score > highest_score else highest_score

    print(f'highest scenic score possible: {highest_score}')


def scenic_score_above_and_below(loc: Location, grid: List[List[int]]) -> int:
    """Returns how many trees are visible when looking above and below the tree in consideration."""
    our_tree_row, our_tree_col = loc.y, loc.x
    our_tree_height = grid[loc.y][loc.x]
    trees_above = []
    trees_below = []
    trees_seen_above = 0
    trees_seen_below = 0

    for row, trees in enumerate(grid):
        if row < our_tree_row:
            trees_above.append(trees[our_tree_col])
        elif row > our_tree_row:
            trees_below.append(trees[our_tree_col])
        else:
            continue

    if not len(trees_above):
        pass  # there are no trees above
    else:
        trees_above.reverse()  # start from the tree closest to our tree
        for tree_height in trees_above:
            if tree_height >= our_tree_height:  # we don't need to count anymore
                trees_seen_above += 1
                break
            else:
                trees_seen_above += 1

    if not len(trees_below):
        pass  # there are no trees below
    else:
        for tree_height in trees_below:
            if tree_height >= our_tree_height:
                trees_seen_below += 1
                break
            else:
                trees_seen_below += 1

    return trees_seen_above * trees_seen_below


def scenic_score_left_and_right(loc: Location, grid: List[List[int]]) -> int:
    """Returns how many trees are visible when looking to the left of the tree in consideration."""
    our_tree_row, our_tree_col = loc.y, loc.x
    our_tree_height = grid[loc.y][loc.x]
    trees_to_left = []
    trees_to_right = []
    trees_seen_to_the_left = 0
    trees_seen_to_the_right = 0

    for col, tree in enumerate(grid[our_tree_row]):
        if col < our_tree_col:
            trees_to_left.append(tree)
        if col > our_tree_col:
            trees_to_right.append(tree)
        else:
            continue

    if not len(trees_to_left):
        pass  # there are no trees to the left
    else:
        trees_to_left.reverse()  # start from the tree closest to our tree
        for tree_height in trees_to_left:
            if tree_height >= our_tree_height:
                trees_seen_to_the_left += 1
                break
            else:
                trees_seen_to_the_left += 1

    if not len(trees_to_right):
        pass  # there are no trees to the right
    else:
        for tree_height in trees_to_right:
            if tree_height >= our_tree_height:
                trees_seen_to_the_right += 1
                break
            else:
                trees_seen_to_the_right += 1

    return trees_seen_to_the_left * trees_seen_to_the_right


if __name__ == '__main__':
    main()
