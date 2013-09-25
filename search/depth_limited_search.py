def tree_dls(head, target, limit, comparator=lambda x, y: x.value == y):
    queue = [(head, 0)]
    while len(queue) != 0:
        node, node_level = queue.pop()
        if node_level <= limit:
            if comparator(node, target):
                return node

            if node_level < limit:
                queue.extend([(child, node_level + 1) for child in node])

    return None


def graph_dls(node, target, limit, comparator=lambda x, y: x.value == y):
    queue = [(node, 0)]
    visited_nodes = []

    while len(queue) != 0:
        current_node, current_node_level = queue.pop()

        if current_node_level <= limit and current_node not in visited_nodes:
                if comparator(current_node, target):
                    return current_node

                if current_node_level < limit:
                    queue.extend([(child, current_node_level + 1) for child in current_node])

                visited_nodes.append(current_node)

    return None