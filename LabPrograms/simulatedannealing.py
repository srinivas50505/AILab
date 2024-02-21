import math
import random

def cost_function(x):
    """
    Define the cost function. This can be any function you want to minimize.
    For demonstration, let's use a simple function.
    """
    return x ** 2

def simulated_annealing(cost_function, initial_solution, temperature, cooling_rate, min_temperature, max_iterations):
    """
    Simulated Annealing algorithm implementation.
    """
    current_solution = initial_solution
    best_solution = current_solution

    while temperature > min_temperature and max_iterations > 0:
        new_solution = current_solution + random.uniform(-1, 1)  # Corrected line
        current_cost = cost_function(current_solution)
        new_cost = cost_function(new_solution)

        if new_cost < current_cost:
            current_solution = new_solution

            if new_cost < cost_function(best_solution):
                best_solution = new_solution
        else:
            delta_cost = new_cost - current_cost
            probability = math.exp(-delta_cost / temperature)

            if random.random() < probability:
                current_solution = new_solution

        temperature *= cooling_rate
        max_iterations -= 1

    return best_solution

# Example usage
initial_solution = 10  # Initial solution
temperature = 100  # Initial temperature
cooling_rate = 0.95  # Cooling rate
min_temperature = 0.01  # Minimum temperature
max_iterations = 1000  # Maximum number of iterations

best_solution = simulated_annealing(cost_function, initial_solution, temperature, cooling_rate, min_temperature, max_iterations)

print("Best solution found:", best_solution)
print("Cost of best solution:", cost_function(best_solution))
