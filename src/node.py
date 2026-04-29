
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
        return f"ResponsiveAnalogRead {self.id}({self.inputPin}, true);\n"
    
    def getPotiLoopCode(self) -> str:
        return f"{self.id}.update();\n"

class Node: 

    id: str
    teensyAudioClass: str
    parameter: float
    Poti: Poti | None


    def __init__(self, id: str, teensyAudioClass: str, parameter: float, Poti: Poti | None) -> None:
        self.id = id
        self.teensyAudioClass = teensyAudioClass
        self.parameter = parameter
        self.Poti = Poti

    def hasPoti(self) -> bool:
        if self.Poti is not None:
            return True
        else:
            return False

    def getID(self) -> str:
        return self.id
        
    def getNodeInitCode(self) -> str:
        ##toDo: Implement TeenysAudio Code
        return f"{self.teensyAudioClass} {self.id}({self.parameter});\n"
    
    def getNodeSetupCode(self) -> str:
        ##toDo: Implement TeenysAudio Code
        return f"{self.id}.begin();\n"

    def getNodeLoopCode(self) -> str:   
        ##toDo: Implement TeenysAudio Code
        return f"{self.id}.update();\n"
