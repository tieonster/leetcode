# Get the number of independent graphs from a graph


# Create dfs function called explore
# Function will run dfs through tree, and if reaches the end, return back true
def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    return True

# Main function to count number of independent graphs
def connectedComponentsCount(graph):
    visited = set([])

    count = 0

    for node, list in graph.items():
        # if explore returns true, means algo has finished traversing one tree, increment count by 1
        if explore(graph, node, visited) == True:
            count += 1

    return count



graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []
}