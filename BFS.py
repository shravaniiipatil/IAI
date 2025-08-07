def bfs(graph, start, goal):
    queue = [start]
    visited = []
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)

            if node == goal:
                print("Goal found:", node)
                break

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    print("BFS Traversal:", visited)
# Input
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter start node: ")
goal = input("Enter goal node: ")

# Run BFS
bfs(graph, start, goal)