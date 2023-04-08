from collections import deque
from typing import Deque, Optional, Dict, Union, List
import pprint

COMMAND = '$'
TARGET_SIZE = 100000
PUZZLE_FILE = 'day7-puzzle-input.txt'

class File:
    """Represents a file"""

    def __init__(self, size: int = 0, name: Optional[str] = None) -> None:
        self.size = size
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'File({self.name}, {self.size})'


class Dir:
    """Represents a directory"""

    def __init__(self, size: int = 0, name: Optional[str] = None, parent: Optional['Dir'] = None) -> None:
        self.size = size
        self.name = name
        self.parent = parent

    def __hash__(self) -> int:
        # take into account similarly named directories with different parents
        return hash(str(self.name) + str(self.parent)) 

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'Dir({self.name}, .. {self.parent}, {self.size})'


def main():
    with open(PUZZLE_FILE, 'r', encoding='utf-8') as f:
        layout: Deque[str] = deque(line.strip() for line in f.readlines())  # the commands from the puzzle input   

    # create root directory
    root = Dir(name='/')
    dir_structure = build_dir_structure(layout=layout, root_dir=root)
    pprint.pprint(dir_structure)
    print('sizes: ')
    dir_sizes = get_all_dir_sizes(dir_structure, root_dir=root)
    pprint.pprint(dir_sizes)

    sums_of_target_dirs = 0

    for _, size in dir_sizes.items():
        if size <= TARGET_SIZE:
            sums_of_target_dirs += size

    print(sums_of_target_dirs)


def build_dir_structure(layout: Deque[str], root_dir: 'Dir') -> Dict['Dir', List]:
    """Builds a graph of the directory structure"""

    dir_graph: Dict['Dir', List[Union['Dir', 'File']]] = dict()
    dir_graph[root_dir] = list()
    current_node = root_dir

    # build the graph of files and directories
    while layout:
        item = layout.popleft()
        if item.startswith(COMMAND) and 'cd' in item:  # cd command
            _, _, directory = item.split()
            if directory == '..':  # move to the parent directory
                current_node = current_node.parent
                continue
            else:
                dir = Dir(name=directory, parent=current_node)
                # create the directory, except if it is the root
                if (not dir.name == '/') and (dir_graph.get(dir, '') == ''):
                    dir_graph[dir] = list()
                    current_node = dir
                continue

        elif item.startswith(COMMAND) and "ls" in item:  # ls command
            item = layout.popleft()

            # keep adding the files in the ls list, until the next command is encountered, or until there is no more
            while not item.startswith('$'):
                if item[0].isdigit():  # add file info to the current node
                    size, name = item.split()
                    dir_graph[current_node].append(File(name=name, size=int(size)))
                else:  # add folder info to the current node
                    _, name = item.split()
                    dir_graph[current_node].append(Dir(name=name, parent=current_node))

                if len(layout):  # get the next items in the ls list, as long as there are items left to get
                    item = layout.popleft()
                else:
                    break

            # put back the extra item that was used to exit the loop, unless that was the very last item
            if len(layout):
                layout.appendleft(item)

    return dir_graph


def get_all_dir_sizes(dir_layout: Dict['Dir', List[Union['Dir', 'File']]], root_dir: Dir):
    """Returns a list of directories in the directory layout, and their sizes"""

    dir_sizes = {root_dir.name: root_dir.size}

    for item in dir_layout[root_dir]:
        if isinstance(item, File):
            dir_sizes[root_dir.name] += item.size  # count up the size of the current root
        else:
            sub_dir_size = get_all_dir_sizes(dir_layout, item)  # find the size of this subdirectory
            dir_sizes[root_dir.name] += sub_dir_size[item.name]  # add this subdirectory's size to the size of the root
            dir_sizes.update(sub_dir_size)

    return dir_sizes


if __name__ == '__main__':
    main()
