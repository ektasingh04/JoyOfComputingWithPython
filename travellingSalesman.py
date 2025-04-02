def tsp_dp(graph):
    """Solve TSP using Dynamic Programming with memoization."""
    n = len(graph)
    dp = [[-1] * (1 << n) for _ in range(n)]  # Initialize dp table with -1

    def visit(city, visited):
        """Recursive function to calculate minimum cost."""
        if visited == (1 << n) - 1:  # All cities visited
            return graph[city][0]  # Return to the starting city

        if dp[city][visited] != -1:  # If already computed
            return dp[city][visited]

        min_cost = float('inf')
        for next_city in range(n):
            if visited & (1 << next_city) == 0:  # If next_city not visited
                cost = graph[city][next_city] + visit(next_city, visited | (1 << next_city))
                min_cost = min(min_cost, cost)

        dp[city][visited] = min_cost
        return min_cost

    # Start from the first city and visit all
    return visit(0, 1 << 0)

# Example usage
if __name__ == "__main__":
    # Graph as an adjacency matrix
    graph = [
        [0, 20, 15, 10],
        [20, 0, 35, 25],
        [15, 35, 0, 30],
        [10, 25, 30, 0]
    ]
    min_cost = tsp_dp(graph)
    print("Minimum Cost:", min_cost)
