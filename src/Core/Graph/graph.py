import Core.Node.nodes as nodes
import Core.Node.node as node
from pydantic import BaseModel
from typing import List, Optional

class Connection(BaseModel):
    node1: node.Node
    node2: node.Node    

    def __init__(self, node1: node.Node, node2: node.Node) -> None:
        self.node1 = node1
        self.node2 = node2
    
    def getConnectionCode(self) -> str:
        return f"AudioConnection patch_{self.audioGraph.connections.index(self)}({self.node1.id}, 0, {self.node2.id}, 0);\n"

class Graph(BaseModel):
    #variables
    nodes: List[node.Node] = []
    connections: List[Connection] = []

    #methods
    def __init__(self):
        self.nodes = []
        self.connections = []


    def addConnection(self, node1, node2):
        connection = Connection(node1, node2)
        self.connections.append(connection)

    def removeConnection(self, node1, node2):
        connection = Connection(node1, node2)
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
            self.removeConnectionsOfNode(node_to_remove)

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