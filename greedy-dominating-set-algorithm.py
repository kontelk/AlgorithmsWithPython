def greedy_dominating_set(graph):
    # Copy the graph to avoid mutating the original
    graph = {k: set(graph[k]) for k in graph}

    # Initially, all nodes are uncovered
    uncovered = set(graph)

    # Start with no nodes in the dominating set
    dom_set = set()

    # While there are still uncovered nodes...
    while uncovered:
        # Choose the node that covers the most uncovered nodes
        dom_node, _ = max(
            ((node, len(neighbors & uncovered))
             for node, neighbors in graph.items()),
            key=lambda x: x[1]
        )
        # Add it to the dominating set
        dom_set.add(dom_node)

        # It and its neighbors are now covered
        uncovered -= graph[dom_node] | {dom_node}

    return dom_set




graph = {
    'A': {'B', 'C'},
    'B': {'A', 'C', 'D'},
    'C': {'A', 'B', 'D'},
    'D': {'B', 'C'},
}

dom_set = greedy_dominating_set(graph)
print(dom_set)  # This will print some dominating set, e.g. {'B'}
