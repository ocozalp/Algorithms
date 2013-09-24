def tree_bfs(head, target, comparator=lambda x, y: x.value == y):
    queue = [head]
    while len(queue) != 0:
        node = queue.pop(0)
        if comparator(node, target):
            return node
        queue.extend(node)

    return None


def graph_bfs(node, target, comparator=lambda x, y: x.value == y):
    queue = [node]
    visited_nodes = []

    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node not in visited_nodes:
            if comparator(current_node, target):
                return current_node
            queue.extend(current_node)

    return None
