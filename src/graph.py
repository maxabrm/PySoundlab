import nodes.nodes as nodes
class Graph:
    #variables
    nodes = []

    #methods
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def hasPoti(self, node) -> bool:
        if node.Poti is not None:
            return True
        else:
            return False
        
    def getInitCode(self):
        code = ""
        for node in self.nodes:
            code+= f"AudioConnection patch{nodes.index(node)}()  + \n"  #toDo: Audio Conecctions 
        return code