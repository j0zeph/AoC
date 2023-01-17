from collections import deque

puzzle_input = 'day6-puzzle-input.txt'
PACKET_LENGTH = 4

def main():
    sliding_window = deque()
    with open(puzzle_input, 'r', encoding='utf-8') as f:
        while True:
            char = f.read(1)
            if not char:  # End of file
                break
            else:
                sliding_window.append(char)
                if len(sliding_window) == PACKET_LENGTH:
                    if chars_are_unique(sliding_window):
                        print(f.tell())  # chars processed
                        break
                    else:
                        sliding_window.popleft()
                else:
                    continue


def chars_are_unique(chars: deque) -> bool:
    return len(chars) == len(set(chars))


if __name__ == '__main__':
    main()
