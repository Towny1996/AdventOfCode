class PartTwo:
    input, maze_size, moves = [], [], 0
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    visited, obstacles = set(), set()
    looped_paths = 0

    def __init__(self, input: []):
      self.input = input

    def DoWork(self):
        guards_position = []
        self.maze_size = [len(self.input[0].strip()) - 1, len(self.input) - 1]

        for y, line in enumerate(self.input):
            for x, char in enumerate(line):
                if char == '#':
                    self.obstacles.add((x, y))
                if char == '^':
                    guards_position = [x, y]

        self.visited = self.MoveGuardsPositionForInitialPath(set(), guards_position, 0)

        for new_blocker in self.visited:
            new_blockers = self.obstacles.copy()
            new_blockers.add(new_blocker)

            if self.MoveGuardPositionWithBlocker(set(), guards_position, new_blockers, 0):
                self.looped_paths += 1

        return self.looped_paths - 1

    def MoveGuardsPositionForInitialPath(self, visited: set, guards_position: [], direction: int):
        guards_new_x = (guards_position[0] + self.directions[direction][0])
        guards_new_y = (guards_position[1] + self.directions[direction][1])

        if (guards_new_x, guards_new_y) in self.obstacles:
            direction = 0 if direction == 3 else direction + 1
            return self.MoveGuardsPositionForInitialPath(visited, guards_position, direction)

        if (guards_new_x, guards_new_y) not in visited:
            self.moves += 1
            visited.add((guards_new_x, guards_new_y))

        if (guards_new_x == self.maze_size[0] or guards_new_y == self.maze_size[1]) or (guards_new_x == -1 or guards_new_y == -1):
            return visited

        return self.MoveGuardsPositionForInitialPath(visited, [guards_new_x, guards_new_y], direction)

    def MoveGuardPositionWithBlocker(self, visited: set, guards_position: [], obstacles: set, direction: int):
        guards_new_x = (guards_position[0] + self.directions[direction][0])
        guards_new_y = (guards_position[1] + self.directions[direction][1])

        if (guards_new_x, guards_new_y) in obstacles:
            direction = 0 if direction == 3 else direction + 1
            return self.MoveGuardPositionWithBlocker(visited, guards_position, obstacles, direction)

        if (direction, guards_new_x, guards_new_y) not in visited:
            visited.add((direction, guards_new_x, guards_new_y))
        else:
            return True

        if (guards_new_x == self.maze_size[0] or guards_new_y == self.maze_size[1]) or (guards_new_x == -1 or guards_new_y == -1):
            return False

        return self.MoveGuardPositionWithBlocker(visited, [guards_new_x, guards_new_y], obstacles, direction)