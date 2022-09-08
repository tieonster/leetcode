# BFS using iteration and recursion

# Iterative
def breadthFirstPrint(graph, source):
    queue = deque([source])
    res = []
    while (len(queue)) > 0:
        current = queue.popleft() # Removes front element
        res.append(current)
        for neighbor in graph[current]:
            queue.push(neighbor)

    return res

graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []
}