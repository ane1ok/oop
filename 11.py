from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# Test 1: Простой граф с одной связной компонентой
graph1 = {0: {1, 2}, 1: {0, 2}, 2: {0, 1, 3}, 3: {2}}
assert bfs(graph1, 0) == {0, 1, 2, 3}

# Test 2: Граф с несколькими связными компонентами
graph2 = {0: {1, 2}, 1: {0, 2}, 2: {0, 1}, 3: {4}, 4: {3}}
assert bfs(graph2, 0) == {0, 1, 2}

# Test 3: Граф с петлей на себя
graph3 = {0: {1, 2}, 1: {0, 2}, 2: {0, 1, 2}, 3: {2}}
assert bfs(graph3, 0) == {0, 1, 2, 3}

# Test 4: Пустой граф
graph4 = {}
assert bfs(graph4, 0) == set()
