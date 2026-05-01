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
        hasPoti = any(node.hasPoti() for node in graph.nodes)
        if hasPoti:
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
        
        self.code += "/// Initialize Connections\n\n"
         #initialize connections code
        self.code += f"{graph.getInitCode()}\n\n"


        #setup
        self.code += "void setup() {\n"
        for node in graph.nodes:
             #toDo: Generate Code
            self.code+=node.getNodeSetupCode()   
        self.code += "}\n\n"
        #main loop
        self.code += "void loop() {\n"

        for node in graph.nodes:
            if node.hasPoti():
                self.code+=node.Poti.getPotiLoopCode()
            loopCode = node.getNodeLoopCode()
            if loopCode:
                self.code += loopCode
        self.code += "}\n"
        return self.code


       

   