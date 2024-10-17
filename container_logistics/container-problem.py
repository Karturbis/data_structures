import networkx as nx

def strip_unvisited(graph_dict: dict):
    """return the Graph, without all unvisited nodes"""
    return {n: graph_dict[n] for n in graph_dict if graph_dict[n]["visited"]}

def breadth_first_search(in_graph, node, include_unvisited=False):
    """Returns the path to @node in @in_graph as a dict"""
    queue: list = [node]
    node_attr = {
        n: {"visited": False, "parent": None, "depth": 0} for n in in_graph.nodes
    }
    while queue:
        current_node = queue.pop(0)
        for neighbour in in_graph.adj[current_node]:
            if node_attr[neighbour]["visited"]:
                continue
            queue.append(neighbour)
            na = node_attr[neighbour]
            na["visited"] = True
            na["parent"] = current_node
            na["depth"] = node_attr[current_node]["depth"] + 1

        if not include_unvisited:
            node_attr = strip_unvisited(node_attr)
        return node_attr

def depth_first_search(in_graph, node, include_unvisited=False):
    stack = [node]
    node_attr = {
        n: {
            "visited": False,
            "parent": None,
            "depth": 0,
        }
        for n in in_graph.nodes
    }
    while stack:
        current_node = stack.pop(-1)
        for neighbour in in_graph.adj[current_node]:
            if node_attr[neighbour]["visited"]:
                continue
            stack.append(neighbour)
            na = node_attr[neighbour]
            na["visited"] = True
            na["parent"] = current_node
            na["depth"] = node_attr[current_node]["depth"] + 1
    
    

    if not include_unvisited:
        node_attr = strip_unvisited(node_attr)
    return node_attr


if __name__ == "__main__":
    n = 10
    p = 3 / n
    Graph = nx.gnp_random_graph(n, p)
    print(breadth_first_search(Graph, 2))
