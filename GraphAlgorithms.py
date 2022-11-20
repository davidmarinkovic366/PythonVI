from Node import Node

# create a graph from list of node names and node links
def create_graph(nodes_list: list[str], nodes_links: list[list[str]]) -> tuple[dict[str:Node], list[Node]]:
    
    # caching data for fast access:
    node_dict : dict[str:Node] = {}
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
    
    return (node_dict, node_list)

# create a graph with links in both directions:
def create_bidirectional_linked_graph(nodes_list: list[str], nodes_links: list[list[str]]) -> tuple[dict[str:Node], list[Node]]:
     # caching data for fast access:
    node_dict : dict[str:Node] = {}
    node_list : list[Node] = []

    # creating all nodes:
    for node_name in nodes_list:
        node = Node(node_name, [])
        node_dict[node_name] = node
        node_list.append(node)

    for i in range(0, len(nodes_list)):
        if len(nodes_links[i]) > 0:
            for name in nodes_links[i]:
                node_list[i].link_node(node_dict[name])
                node_dict[name].link_node(node_list[i])

    return (node_dict, node_list)

# remove all prevous nodes from all nodes:
def restart_nodes(node_list: list[Node]):
    for node in node_list:
        node.prev_node = None

# pise...
def depth_search(start_node: Node, end_node: Node) -> list[Node] or None:
    
    tmp_start_node : Node = start_node
    node_arr : list[Node] = [tmp_start_node]
    processed_nodes : list[Node] = []
    found : bool = False

    while len(node_arr) > 0 and not found:
        if len(node_arr) == 0:
            break
        current_node : Node = node_arr.pop(0)
        if not current_node == end_node:
            for potential_node in current_node.linked_nodes:
                if not potential_node in processed_nodes:
                    node_arr.append(potential_node)
                    potential_node.prev_node = current_node
            processed_nodes.append(current_node)    
        else: 
            found = True
    
    if not found:
        print(f"No path between node [{start_node.val}] and node [{end_node.val}]")
    else:
        path_arr : list[Node] = []
        tmp_node = end_node
        while not tmp_node == start_node:
            path_arr.append(tmp_node)
            tmp_node = tmp_node.prev_node
        path_arr.append(tmp_node)

        print_str = ""
        for tnode in path_arr:
            print_str += f"{tnode.val} - "
        print_str = print_str[0:len(print_str) - 3]
        print_str = print_str[::-1]
        print(print_str)

        return path_arr
        
def width_search(start_node: Node, end_node: Node) -> list[Node] or None:

    tmp_start_node : Node = start_node
    node_arr : list[Node] = [tmp_start_node]
    processed_nodes : list[Node] = []
    found : bool = False

    while not len(node_arr) == 0 and not found:
        current_node : Node = node_arr.pop(0)
        if not current_node == end_node:
            for next_node in current_node.linked_nodes:
                if not next_node in processed_nodes and not next_node in node_arr:
                    node_arr.append(next_node)
                    next_node.prev_node = current_node
            processed_nodes.append(current_node)
        else:
            found = True

    if not found:
        print(f"No path between node [{start_node.val}] and node [{end_node.val}]")
    else:
        path_list : list[Node] = []
        tmp_node : Node = end_node
        path_str = f"{tmp_node.val} - "
        while not tmp_node == start_node:
            path_list.append(tmp_node)
            tmp_node = tmp_node.prev_node
            path_str += f"{tmp_node.val} - "
        
        path_str = path_str[0:len(path_str) - 3]
        path_str = path_str[::-1]
        print(path_str)

        return path_list



