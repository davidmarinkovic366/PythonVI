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
    ["I", "G"],
    ["J"],
    ["J"],
    [],
    ["J"],
    []
]

# caching data for fast access:
node_dict = {}
node_list : list[Node] = []

# creating all nodes:
for node_name in nodes_list:
    node = Node(node_name, [])
    node_dict[node_name] = node
    node_list.append(node)

# linking all nodes:
for i in range(0, len(nodes_links)):
    if len(nodes_links[i]) > 0:
        for name in nodes_links[i]:
            node_list[i].link_node(node_dict[name])

# just for check:
# for i in node_list:
    # print(i)

# list = gal.width_search(node_dict["A"], node_dict["J"])
gal.restart_nodes(node_list)
gal.depth_search(node_dict["A"], node_dict["G"])