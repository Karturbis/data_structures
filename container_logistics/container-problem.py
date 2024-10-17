import networkx as nx

def breadth_first_search(in_graph, node):
    queue: list = [node]
    node_attr = {n: {"visited": False, "parent": None, "depth": 0} for n in in_graph.nodes}
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

        return node_attr

def depth_first_search(in_graph, node):
    stack = [node]
    node_attr = {n: {"visited": False, "parent": None, "depth": 0, "discovery_time": 0, "end_time": 0} for n in in_graph.nodes}
    time = 0
    while stack:
        current_node = stack.pop(-1)
        time += 1
        for neighbour in in_graph.adj[current_node]:
            if node_attr[neighbour]["visited"]:
                continue
            stack.append(neighbour)
            na = node_attr[neighbour]
            na["visited"] = True
            na["parent"] = current_node
            na["depth"] = node_attr[current_node]["depth"] +1
            na["discovery_time"] = time
    
        return node_attr

if __name__ == "__main__":
    n = 10
    p = 3/n
    Graph = nx.gnp_random_graph(n, p)
