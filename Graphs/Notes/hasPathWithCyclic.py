# Write a function that takes in an array of edges for an undirected graph
# and two nodes (nodeA, nodeB). The function should return a boolean indicating whether
# or not there exists a path between nodeA and nodeB.

# Need to add a visited array

def undirectedPath(edges, nodeA, nodeB):

    # Function to construct graph from edges
    def buildGraph(edges):
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

    # Recursive function that takes into account visited nodes and prevents infinite loop
    def hasPath(graph, src, dest, visited):
        if src == dest:
            return True

        if src in visited:
            return False

        visited.add(src)
            
        for neighbor in graph[src]:
            if hasPath(graph, neighbor, dest, visited) == True:
                return True

        return False


    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set([]))


    
edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"]
    ["o", "n"]
]