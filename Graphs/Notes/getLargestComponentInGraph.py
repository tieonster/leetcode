# Given a graph, find the largest component in graph

# Helper DFS function
def exploreSize(graph, current, visited):
    if current in visited:
        return 0

    visited.add(current)

    # Set size to 1 at first call, and increment size later on for every visited neighbor
    size = 1

    for neighbor in graph[current]:
        size += exploreSize(graph, neighbor, visited)

    return size


# Main function (Traversal function)
def getLargestComponentGraph(graph):
    visited = set([])
    longest = 0 # Create a longest variable

    for node, list in graph.items():
        size = exploreSize(graph, node, visited)
        if size > longest:
            longest = size

    return longest


largestComponent = {
    "0": ["8", "1", "5"],
    "1": ["0"],
    "5": ["0", "8"],
    "8": ["0", "5"],
    "2": ["3", "4"],
    "3": ["2", "4"],
    "4": ["3", "2"]
}