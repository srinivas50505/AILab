import math
import random

def simulated_annealing(initial_state, cost_function, temperature, cooling_rate, iterations):
    current_state = initial_state
    best_state = current_state
    current_cost = cost_function(current_state)
    best_cost = current_cost

    for i in range(iterations):
        temperature *= cooling_rate

        neighbor_state = generate_neighbor(current_state)
        neighbor_cost = cost_function(neighbor_state)

        if neighbor_cost < current_cost or random.random() < math.exp((current_cost - neighbor_cost) / temperature):
            current_state = neighbor_state
            current_cost = neighbor_cost

        if current_cost < best_cost:
            best_state = current_state
            best_cost = current_cost

    return best_state, best_cost

def distance(city1, city2):
    # Euclidean distance between two cities
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(route):
    # Calculate the total distance of a route
    total = 0
    for i in range(len(route) - 1):
        total += distance(route[i], route[i + 1])
    return total

def generate_neighbor(route):
    # Generate a neighboring route by swapping two cities
    neighbor = route.copy()
    i, j = random.sample(range(len(route)), 2)
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

# Example usage for TSP:
cities = [(0, 0), (1, 2), (3, 1), (5, 2), (2, 4)]

initial_state = random.sample(cities, len(cities))
initial_temperature = 100.0
cooling_rate = 0.95
iterations = 1000

best_route, best_distance = simulated_annealing(initial_state, total_distance, initial_temperature, cooling_rate, iterations)

print("Best Route:", best_route)
print("Best Distance:", best_distance)
