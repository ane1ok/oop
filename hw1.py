from collections import defaultdict

def makeConnected(n, connections):
    if len(connections) < n - 1:
        return -1

    # Create graph
    graph = defaultdict(list)
    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    # DFS to find connected components
    visited = set()
    components = 0
    for node in range(n):
        if node not in visited:
            dfs(node, visited, graph)
            components += 1

    # Count cables needed to connect components
    cables_needed = components - 1
    cables_available = len(connections)
    if cables_available < cables_needed:
        return -1

    # Return number of cables to extract and place
    return cables_needed


def dfs(node, visited, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, graph)
