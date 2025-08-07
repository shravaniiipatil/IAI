def dfs(graph, start, goal):
    stack = [start]
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                print("Goal found:", node)
                break
            neighbors = graph.get(node, [])
            for neighbor in reversed(neighbors):  
                if neighbor not in visited:
                    stack.append(neighbor)

    print("DFS Traversal:", visited)
#user ip
graph = {}
nodes = int(input("Enter number of nodes: "))
for _ in range(nodes):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors
start = input("Enter start node: ")
goal = input("Enter goal node: ")

dfs(graph, start, goal)