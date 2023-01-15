def main():
    puzzle_input = 'day4-puzzle-input.txt'
    overlapping_pairs = 0

    with open(puzzle_input, 'r', encoding='utf-8') as f:
        for line in f:
            l_range, r_range = line.strip().split(',')
            l_sections = get_sections_from_range(l_range)
            r_sections = get_sections_from_range(r_range)

            if sections_overlap(l_sections, r_sections):
                overlapping_pairs += 1

    print(overlapping_pairs)


def get_sections_from_range(elf_range: str) -> set:
    """Returns a set of sections, given the elf's range.
    Given '4-7' as an input, the function returns {4, 5, 6, 7}
    """
    left_num, right_num = [int(x) for x in elf_range.split('-')]
    return set(range(left_num, right_num + 1))


def sections_overlap(section1: set, section2: set) -> bool:
    """Returns True if section1 and section2 overlap.False otherwise."""
    return len(section1.intersection(section2)) > 0


if __name__ == '__main__':
    main()
