def bfs(node, target, comparator=lambda x, y: x == y):
    queue = [node]
    visited_nodes = []

    while len(queue) != 0:
        current_node = queue.pop(0)
        if current_node not in visited_nodes:
            if comparator(current_node.value, target):
                return current_node
            queue.extend(current_node)
            visited_nodes.append(current_node)

    return None


def dfs(node, target, comparator=lambda x, y: x == y):
    queue = [node]
    visited_nodes = []

    while len(queue) != 0:
        current_node = queue.pop()
        if current_node not in visited_nodes:
            if comparator(current_node.value, target):
                return current_node
            queue.extend(current_node)
            visited_nodes.append(current_node)

    return None


def dls(node, target, limit, comparator=lambda x, y: x == y):
    queue = [(node, 0)]
    visited_nodes = []
    max_level = 0

    while len(queue) != 0:
        current_node, current_node_level = queue.pop()
        max_level = max(max_level, current_node_level)

        if current_node_level <= limit and current_node not in visited_nodes:
                if comparator(current_node.value, target):
                    return current_node, current_node_level

                if current_node_level < limit:
                    queue.extend([(child, current_node_level + 1) for child in current_node])

                visited_nodes.append(current_node)

    return None, max_level


def iterative_deepening_search(node, target, comparator=lambda x, y: x == y):
    level = 0
    found_level = 0

    while level == found_level:
        level += 1
        result, found_level = dls(node, target, level, comparator)
        if result is not None:
            return result


    return None