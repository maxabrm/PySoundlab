class CodeGenerator:

#variables
    code = ""
    graph = None

#methods
    def __init__(self, graph):
        self.code = ""

    def generate_code(self, graph):
        self.graph = graph
        self.code = ""

        #initialize instances code
        for node in graph.nodes:
            #toDo: Generate Code
            self.code+=node.getNodeInitCode(node) 

        #setup
        for node in graph.nodes:
             #toDo: Generate Code
            self.code+=node.getNodeSetupCode(node)   

        #main loop
        self.code += "void loop() {\n"

        for node in graph.nodes:
            self.code+=node.getNodeLoopCode(node) 
        self.code += "}\n"
        return self.code


       

   