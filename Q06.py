"""
Program: Depth-First Search Traversal
Description: This program implements the Depth-First Search (DFS) traversal algorithm on an example graph.

How to Run:
- On Ubuntu/Linux: Open the terminal and navigate to the directory containing this file. Use the command "python3 dfs_traversal.py" to run the program.
- On Windows: Open a command prompt and navigate to the directory containing this file. Use the command "python dfs_traversal.py" to run the program.
"""

# Define an example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS traversal function
def dfs(graph, start, visited):
    if start not in visited:
        print(start, end=' ')
        visited.add(start)
        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

# Main function to initiate DFS traversal
def main():
    start_node = 'A'  # You can change the starting node here
    print("Depth-First Search Traversal:")
    visited = set()
    dfs(graph, start_node, visited)

if __name__ == '__main__':
    main()
