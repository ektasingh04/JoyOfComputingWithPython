from queue import Queue

def bfs(graph, start_node):
    visited = set()  # To keep track of visited nodes
    queue = Queue()  # Initialize a FIFO queue
    queue.put(start_node)  # Enqueue the start node
    visited.add(start_node)  # Mark the start node as visited

    print("BFS Traversal Order:")

    while not queue.empty():
        current_node = queue.get()  # Dequeue the front element
        print(current_node, end=" ")  # Process the current node

        # Traverse all the adjacent nodes
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put(neighbor)  # Enqueue the neighbor

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = {
        'A': ['B', 'C','E'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    bfs(graph, 'A')
