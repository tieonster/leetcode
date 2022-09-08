# Determines if you can reach one node from another node

# DFS Solution (Recursion)
def hasPath(graph, src, dest):
    if src == dest:
        return True

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dest) == True:
            return True

    return False

graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []
}

# BFS Solution (Iterative)
def hasPath(graph, src, dest):
    queue = deque([src])

    while(len(queue) > 0):
        current = queue.popleft()
        if current == dest: 
            return True
        
        for neighbor in graph[current]:
            queue.push(neighbor)

    return False