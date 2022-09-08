# Find distance between two nodes in a graph

# Uses BFS
def nodeDistance(edges, nodeA, nodeB):

    def getGraph(edges):
        graph = {}

        for edge in edges:
            [a, b] = edge
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        return graph

    graph = getGraph(edges)

    queue = deque([nodeA])
    visited = set([]) # Add visited array to keep track of nodes that have been visited

    while len(queue) > 0:
        count = 0
        current = queue.popleft()

        if current ==  nodeB:
            return count

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.push((neighbor, count+1)) # Add 1 if neighbor has been visited
                visited.add(neighbor)


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]
