import Core.Node.Nodes as nodes
import Core.Graph.Graph as graph

class CodeGenerator:


    code: str
    audioGraph: graph.Graph

    def __init__(self, audioGraph: graph.Graph) -> None:
        self.code = ""
        self.audioGraph = audioGraph

    def generate_code(self, audioGraph: graph.Graph):
        self.audioGraph = audioGraph
        self.code = ""

         #initialize libraries -> Bei zeiten mal an die Nodes anpassen, damit nur die benötigten Libraries inkludiert werden
        self.code += "//Generated Code\n\n"
        hasPoti = any(node.hasPoti() for node in self.audioGraph.nodes)
        if hasPoti:
            self.code += "#include <ResponsiveAnalogRead.h>\n"  # Poti Werte auslesen
        self.code += "#include <Audio.h>\n" 
        self.code += "#include <Wire.h>\n"
        self.code += "#include <SPI.h>\n"   
        self.code += "#include <SD.h>\n"
        self.code += "#include <SerialFlash.h>\n\n"

        self.code += "const float Divider = 1.0/1023.0;\n\n" #Konstante für die Umrechnung der Poti Werte


        #initialize objects code
        for node in self.audioGraph.nodes:
            self.code+=f"// Setup {node.getID()}\n"
            if node.hasPoti():
                self.code+=node.Poti.getPotiInitCode()
            self.code+=node.getNodeInitCode()
        
        self.code += "/// Initialize Connections\n\n"
         #initialize connections code
        for connection in self.audioGraph.connections:
            self.code+=connection.getConnectionCode()


        #setup
        self.code += "void setup() {\n"
        for node in self.audioGraph.nodes:
             #toDo: Generate Code
            self.code+=node.getNodeSetupCode()   
        self.code += "}\n\n"
        #main loop
        self.code += "void loop() {\n"

        for node in self.audioGraph.nodes:
            if node.hasPoti():
                self.code+=node.Poti.getPotiLoopCode()
            loopCode = node.getNodeLoopCode()
            if loopCode:
                self.code += loopCode
        self.code += "}\n"
        return self.code


       

   