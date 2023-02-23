from collections import namedtuple
from typing import List

Location = namedtuple('Location', ['y', 'x'])
puzzle_input = 'day8-puzzle-input.txt'

grid: List[List[int]] = []

with open(puzzle_input, 'r', encoding='utf-8') as f:
    for line in f:
        pure_line = line.strip()
        grid.append(list(map(int, pure_line)))


def main():
    visible_trees = 0
    trees_in_one_row = len(grid[0])
    for row in range(len(grid)):
        for col in range(trees_in_one_row):
            if row == 0 or row == len(grid) - 1:  # trees in the first and last row are all visible
                visible_trees += 1
            elif col == 0 or col == len(grid[0]) - 1:  # trees in the first and last column are all visible
                visible_trees += 1
            else:
                if is_visible_in_row(Location(row, col), grid):
                    visible_trees += 1
                elif is_visible_in_column(Location(row, col), grid):
                    visible_trees += 1
                else:
                    continue
    print(f'{visible_trees=}')


def is_visible_in_row(loc: Location, grid) -> bool:
    """Returns True if the tree in the location, `loc` in the `grid` is visible in its own
    row.
    Returns False otherwise.
    """
    row = grid[loc.y]
    this_tree_height = grid[loc.y][loc.x]
    trees_on_left = set(row[0 : loc.x])
    trees_on_right = set(row[loc.x + 1 :])
    return this_tree_height > max(trees_on_left, default=-1) or this_tree_height > max(trees_on_right, default=-1)


def is_visible_in_column(loc: Location, grid: List[List[int]]) -> bool:
    """Returns True if the tree in the location, `loc` in the `grid` is visible in its own
    column.
    Returns False otherwise.
    """
    this_tree_row, this_tree_col = loc.y, loc.x
    this_tree_height = grid[loc.y][loc.x]
    trees_above = set()
    trees_below = set()
    for row, trees in enumerate(grid):
        if row < this_tree_row:
            trees_above.add(trees[this_tree_col])
        elif row > this_tree_row:
            trees_below.add(trees[this_tree_col])
        else:
            continue
    return this_tree_height > max(trees_above, default=-1) or this_tree_height > max(trees_below, default=-1)


if __name__ == '__main__':
    main()
