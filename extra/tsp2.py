from itertools import permutations

def calculate_cost(graph, tour):
    """Calculate the total cost of a given tour."""
    cost = 0
    for i in range(len(tour) - 1):
        cost += graph[tour[i]][tour[i + 1]]
    # Add the cost of returning to the starting city
    cost += graph[tour[-1]][tour[0]]
    return cost

def tsp_brute_force(graph):
    """Solve TSP using brute force."""
    n = len(graph)
    cities = range(n)
    min_cost = float('inf')
    best_tour = None

    for tour in permutations(cities):
        cost = calculate_cost(graph, tour)
        if cost < min_cost:
            min_cost = cost
            best_tour = tour

    return best_tour, min_cost

# Example usage
if __name__ == "__main__":
    # Graph as an adjacency matrix
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    best_tour, min_cost = tsp_brute_force(graph)
    print("Best Tour:", best_tour)
    print("Minimum Cost:", min_cost)
