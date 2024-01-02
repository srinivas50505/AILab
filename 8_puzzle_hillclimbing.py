import random
import copy

class EightPuzzle:
    def __init__(self, initial_state):
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.current_state = initial_state

    def print_state(self, state):
        for row in state:
            print(row)
        print()

    def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def generate_neighbors(self, state):
        i, j = self.find_blank(state)
        neighbors = []

        if i > 0:
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
            neighbors.append(new_state)

        if i < 2:
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
            neighbors.append(new_state)

        if j > 0:
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
            neighbors.append(new_state)

        if j < 2:
            new_state = copy.deepcopy(state)
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
            neighbors.append(new_state)

        return neighbors

    def hill_climbing(self):
        current_cost = self.calculate_cost(self.current_state)

        while True:
            neighbors = self.generate_neighbors(self.current_state)
            neighbors_cost = [self.calculate_cost(neighbor) for neighbor in neighbors]

            if min(neighbors_cost) >= current_cost:
                break

            best_neighbor = neighbors[neighbors_cost.index(min(neighbors_cost))]
            self.current_state = best_neighbor
            current_cost = min(neighbors_cost)

            self.print_state(self.current_state)
            print(f"Cost: {current_cost}")
            print("------")

        print("Goal state reached!")

    def calculate_cost(self, state):
        cost = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goal_state[i][j]:
                    cost += 1
        return cost

# Example usage
initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]  # Initial state with 0 representing the blank tile
puzzle = EightPuzzle(initial_state)
puzzle.print_state(initial_state)
puzzle.hill_climbing()
