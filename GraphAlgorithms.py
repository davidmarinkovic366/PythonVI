from Node import Node

# remove all prevous nodes from all nodes:
def restart_nodes(node_list: list[Node]):
    for node in node_list:
        node.prev_node = None

# pise...
def width_search(start_node: Node, end_node: Node) -> list[Node] or None:
    
    tmp_start_node : Node = start_node
    node_arr : list[Node] = [tmp_start_node]
    processed_nodes : list[Node] = []
    found : bool = False

    while len(node_arr) > 0 and not found:
        if len(node_arr) == 0:
            break
        current_node : Node = node_arr[0]
        if not current_node == end_node:
            for potential_node in current_node.linked_nodes:
                if not potential_node in processed_nodes:
                    node_arr.append(potential_node)
                    potential_node.prev_node = current_node
            processed_nodes.append(current_node)    
            node_arr.remove(current_node) 
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
        print(print_str)

        return path_arr
        
def depth_search(start_node: Node, end_node: Node) -> list[Node] or None:

    tmp_start_node : Node = start_node
    node_stack : list[Node] = [tmp_start_node]
    processed_nodes : list[Node] = []
    found : bool = False

    while not len(node_stack) == 0 and not found:
        current_node : Node = node_stack.pop(0)
        if not current_node == end_node:
            for next_node in current_node.linked_nodes:
                if not next_node in processed_nodes:
                    node_stack.append(next_node)
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
        print(path_str)

        return path_list



