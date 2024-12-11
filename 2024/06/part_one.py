class PartOne:
    input, obstacles, maze_size, moves = [], [], [], 0
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    visited = []

    def __init__(self, input: []):
      self.input = input

    def DoWork(self):
        guards_position = []
        self.maze_size = [len(self.input[0].strip()) - 1, len(self.input) - 1]

        for y, line in enumerate(self.input):
            for x, char in enumerate(line):
                if char == '#':
                    self.obstacles.append([x, y])
                if char == '^':
                    guards_position = [x, y]

        return self.MoveGuardsPosition(guards_position, 0)

    def MoveGuardsPosition(self, guards_position: [], direction: int):
        guards_new_x = (guards_position[0] + self.directions[direction][0])
        guards_new_y = (guards_position[1] + self.directions[direction][1])

        if any(obstacle == [guards_new_x, guards_new_y] for obstacle in self.obstacles):
            direction = 0 if direction == 3 else direction + 1
            return self.MoveGuardsPosition(guards_position, direction)

        if not any(visited == [guards_new_x, guards_new_y] for visited in self.visited):
            self.moves += 1
            self.visited.append([guards_new_x, guards_new_y])

        if (guards_new_x == self.maze_size[0] or guards_new_y == self.maze_size[1]) or (guards_new_x == -1 or guards_new_y == -1):
            return self.moves

        return self.MoveGuardsPosition([guards_new_x, guards_new_y], direction)