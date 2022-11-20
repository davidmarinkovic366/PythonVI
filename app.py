from Node import Node
import GraphAlgorithms as gal

# all nodes in graph:
nodes_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# links from one node to another:
nodes_links = [
    ["B", "C"],
    ["D", "E"],
    ["F", "G"],
    ["H"],
    ["G", "I"],
    ["J"],
    ["J"],
    [],
    ["J"],
    []
]

result = gal.create_graph(nodes_list, nodes_links)

node_dict = result[0]
node_list = result[1]

# check:
# for node in node_list:
#     print(node)

gal.restart_nodes(node_list)
gal.width_search(node_dict["A"], node_dict["J"])
# gal.restart_nodes(node_list)
# gal.depth_search(node_dict["A"], node_dict["J"])