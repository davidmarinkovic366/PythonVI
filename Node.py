class Node:
    def __init__(self, val: str, linked_nodes: list):
        self.val: str = val
        self.linked_nodes: list = linked_nodes
        self.prev_node: Node = None

    def link_node(self, node):
        if not node in self.linked_nodes:
            self.linked_nodes.append(node)

    def unlink_node(self, node):
        if node in self.linked_nodes:
            self.linked_nodes.remove(node)

    def __str__(self):
        data = f"Node({self.val}): ["
        if len(self.linked_nodes) > 0:
            for node in self.linked_nodes:
                data += f"{node.val}, "
            data = data[0:len(data)-2]
        data += "]"
        return data
    