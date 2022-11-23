# graph = {
#     'A': ['B', 'C', 'D'],
#     'B': ['E', 'F', 'G'],
#     'C': ['A', 'B'],
#     'D': ['C', 'E', 'F'],
#     'E': ['G', 'H', 'A'],
#     'F': ['B', 'C', 'D'],
#     'G': ['E', 'H'],
#     'H': ['J'],
#     'J': []
# }

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['E', 'F', 'G'],
    'D': ['F'],
    'E': ['C', 'H'],
    'F': ['H'],
    'G': ['D', 'J'],
    'H': ['J'],
    'J': []
}

def sort_fun(element):
    return element[0]

def calculate_depth(graph, start_node):
    paths = [(start_node,)]
    queue = [(start_node,)]

    while len(queue) > 0:
        current_path = queue.pop(0)
        for node in graph[current_path[-1]]:
            if node not in current_path:
                paths.append((*current_path, node))
                queue.append((*current_path, node))
    
    # for path in paths:
    #     print(path)
    return list(map(lambda x: ("Length: " + str(len(x) - 1), x), paths))

result = calculate_depth(graph, 'A')
for res in result:
    print(res)
print("Maximum depth of graph is: ", len(max(result)[1]) - 1)
