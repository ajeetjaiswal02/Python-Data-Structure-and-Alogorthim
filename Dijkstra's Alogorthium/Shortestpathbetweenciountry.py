print("Dijkstra's algorithm allows us to find the shortest path between any two vertices of a graph.")
print("It differs from the minimum spanning tree because the shortest distance between two vertices might not include all the vertices of the graph.")

print("Shortest distance between 6 Diffrent Countries")
print("Soory for any speling Mistakes and Typos 😅")

from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

graph = Graph()
edges = [
    ('Mountain View', 'San frenscisco', 51),
    ('Mountain View', 'San Palao', 10375),
    ('Mountain View', 'Shangai', 9950),
    ('San frenscisco', 'Berlin', 9130),
    ('San frenscisco', 'Shangai', 9900),
    ('San frenscisco', 'Mountain View', 51),
    ('San Palao', 'Mountain View', 10375),
    ('San Palao', 'London', 9471),
    ('Shangai', 'Mountain View', 9950),  
    ('Shangai', 'London', 9217),
    ('Shangai', 'San frenscisco', 9900),
    ('London', 'Shangai', 9217),
    ('London', 'San palao', 9471),
    ('London', 'Berlin', 932),
    ('Berlin', 'San frenscisco', 9130),
    ('Berlin', 'London', 932)
]

for edge in edges:
    graph.add_edge(*edge)

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

print(dijsktra(graph, 'Mountain View', 'London'))