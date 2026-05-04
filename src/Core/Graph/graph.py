import Core.Node.nodes as nodes

class Graph:
    #variables
    nodes = []

    #methods
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

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