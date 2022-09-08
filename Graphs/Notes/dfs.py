# DFS algorithm using stack and recursion

graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []
}


# Iterative
def depthFirstPrint(graph, source):
    stack = [source]
    res = []

    while (len(stack) > 0):
        # Remove element from the stack
        current = stack.pop()
        res.append(current)

        # Push neighbouring elements to the stack
        for neighbor in graph[current]:
            stack.append(neighbor)

    return (res)


# Recursive
def depthFirstRecursive(graph, source):
    res = []

    def recurse (graph, source):
        res.append(source)
        for neighbor in graph[source]:
            depthFirstRecursive(graph, neighbor)

    recurse(graph, source)

    return res