
class Poti:
    id: str
    inputPin: str
    resistance: float
    maxValue: float


    def __init__(self, id: str, inputPin: str, resistance: float, maxValue: float) -> None:
        self.id = id
        self.inputPin = inputPin
        self.resistance = resistance
        self.maxValue = maxValue

    def getPotiInitCode(self) -> str:
        ##toDo: Implement TeenysAudio Code
        return f"AudioControlSGTL5000 {self.id}({self.inputPin}, {self.resistance}, {self.maxValue});\n"

class Node: 

    id: str
    teensyAudioClass: str
    parameter: float
    Poti: Poti


    def __init__(self, id: str, teensyAudioClass: str, parameter: float, Poti: Poti | None) -> None:
        self.id = id
        self.teensyAudioClass = teensyAudioClass
        self.parameter = parameter
        self.Poti = Poti

        
    def getNodeInitCode(self) -> str:
        ##toDo: Implement TeenysAudio Code
        return f"{self.teensyAudioClass} {self.id}({self.parameter});\n"
    
    def getNodeSetupCode(self) -> str:
        ##toDo: Implement TeenysAudio Code
        return f"{self.id}.begin();\n"

    def getNodeLoopCode(self) -> str:   
        ##toDo: Implement TeenysAudio Code
        return f"{self.id}.update();\n"
