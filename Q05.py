"""
Program: Breadth-First Search Traversal
Description: This program implements the Breadth-First Search (BFS) traversal algorithm on an example graph.

How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 bfs_traversal.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python bfs_traversal.py" to run the program.
"""

from collections import deque

# Define an example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS traversal function
def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque()  # Create a queue for BFS

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Main function to initiate BFS traversal
def main():
    start_node = 'A'  # You can change the starting node here
    print("Breadth-First Search Traversal:")
    bfs(graph, start_node)

if __name__ == '__main__':
    main()
