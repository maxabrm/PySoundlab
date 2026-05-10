import Core.Node.Nodes as nodes
import Core.Node.Node as node
from typing import List

class Connection:
    id: int
    node1: node.Node
    node2: node.Node    

    def __init__(self, id: int, node1: node.Node, node2: node.Node) -> None:
        self.id = id
        self.node1 = node1
        self.node2 = node2
    
    def getConnectionCode(self) -> str:
        return f"AudioConnection patch_{self.id}({self.node1.id}, 0, {self.node2.id}, 0);\n"

class Graph:
    #variables
    nodes: List[node.Node] = []
    connections: List[Connection] = []

    #methods
    def __init__(self):
        self.nodes = []
        self.connections = []


    def addConnection(self, node1, node2):
        connection = Connection(len(self.connections)+1, node1, node2)
        self.connections.append(connection)

    def removeConnection(self, node1, node2):
        connection = next((conn for conn in self.connections if (conn.node1 == node1 and conn.node2 == node2) or (conn.node1 == node2 and conn.node2 == node1)), None)
        if connection:
            self.connections.remove(connection)

    def removeConnectionsOfNode(self, node):
        self.connections = [conn for conn in self.connections if node not in [conn.node1, conn.node2]]

    def addNode(self, node):
        self.nodes.append(node)

    def removeNode(self, node):
        self.nodes.remove(node)
        self.removeConnectionsOfNode(node)

    def removeNodeById(self, id):
        node_to_remove = next((node for node in self.nodes if node.id == id), None)
        if node_to_remove:
            self.removeNode(node_to_remove)

    def validateGraph(self) -> bool:
        for connection in self.connections:
            if connection.node1 not in self.nodes or connection.node2 not in self.nodes:
                return False
            if connection.node1 == connection.node2:
                return False
        if not any(isinstance(node, nodes.AudioOutput) for node in self.nodes):
            return False
        if not any(isinstance(node, nodes.AudioInput) for node in self.nodes):
            return False
        if any(isinstance(conn.node1, nodes.AudioOutput) for conn in self.connections):
            return False
        if any(isinstance(conn.node2, nodes.AudioInput) for conn in self.connections):
            return False
        return True

    def hasPoti(self, node) -> bool:
        if node.Poti is not None:
            return True
        else:
            return False
        
    def getInitCode(self):
        code = ""
        for i in range(len(self.nodes) - 1):  # Alle Nodes außer der letzten
            current_node = self.nodes[i]
            next_node = self.nodes[i + 1]
            code += f"AudioConnection patch_{i}({current_node.id}, 0, {next_node.id}, 0);\n"
        return code
    
    def sortByConnections(self):
        CountInConnections = {n: 0 for n in self.nodes}
        nextNodes= {n: None for n in self.nodes}

        for conn in self.connections:
            nextNodes[conn.node1] = conn.node2
            CountInConnections[conn.node2] += 1

        sorted_nodes = []
        iterationNode = next((n for n in self.nodes if CountInConnections[n] == 0), None)
        if iterationNode is None:
            return

        sorted_nodes.append(iterationNode)

        while nextNodes[iterationNode]:
            iterationNode = nextNodes[iterationNode]
            sorted_nodes.append(iterationNode)

        self.nodes = sorted_nodes


        