import nodes.nodes as nodes
class Graph:
    #variables
    nodes = []

    #methods
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)