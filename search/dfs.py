def tree_dfs(head, target, comparator=lambda x, y: x.value == y):
    queue = [head]
    while len(queue) != 0:
        node = queue.pop()
        if comparator(node, target):
            return node
        queue.extend(node)

    return None


def graph_dfs(node, target, comparator=lambda x, y: x.value == y):
    queue = [node]
    visited_nodes = []

    while len(queue) != 0:
        current_node = queue.pop()
        if current_node not in visited_nodes:
            if comparator(current_node, target):
                return current_node
            queue.extend(current_node)
            visited_nodes.append(current_node)

    return None
