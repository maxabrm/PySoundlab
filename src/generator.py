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

         #initialize libraries -> Nei zeiten mal an die Nodes anpassen, damit nur die benötigten Libraries inkludiert werden
        self.code += "//Generated Code\n\n"
        if graph.hasPoti():
            self.code += "#include <ResponsiveAnalogRead.h>\n"  # Poti Werte auslesen
        self.code += "#include <Audio.h>\n" 
        self.code += "#include <Wire.h>\n"
        self.code += "#include <SPI.h>\n"   
        self.code += "#include <SD.h>\n"
        self.code += "#include <SerialFlash.h>\n\n"

        self.code += "const float Divider = 1.0/1023.0;\n\n" #Konstante für die Umrechnung der Poti Werte


        #initialize objects code
        for node in graph.nodes:
            self.code+=f"// Setup {node.getID()}\n"
            if node.hasPoti():
                self.code+=node.Poti.getPotiInitCode()
            self.code+=node.getNodeInitCode()

        #setup
        for node in graph.nodes:
             #toDo: Generate Code
            self.code+=node.getNodeSetupCode(node)   

        #main loop
        self.code += "void loop() {\n"

        for node in graph.nodes:
            if node.hasPoti():
                self.code+=node.Poti.getPotiLoopCode()
            self.code+=node.getNodeLoopCode(node) 
        self.code += "}\n"
        return self.code


       

   