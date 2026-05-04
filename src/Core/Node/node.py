
from typing import Optional
from pydantic import BaseModel

class Poti(BaseModel):
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
        code = f"{self.id}_divider = 1.0/{self.maxValue};\n"
        code += f"ResponsiveAnalogRead {self.id}({self.inputPin}, true);\n"
        return code
    
    def getPotiLoopCode(self) -> str:
        code = f"{self.id}.update();\n"
        return code

class Node(BaseModel): 

    id: str
    teensyAudioClass: str
    parameter: float
    parameterTitle: str
    Poti: Optional['Poti']


    def __init__(self, id: str, teensyAudioClass: str, parameter: float, parameterTitle: str, Poti: Optional['Poti']) -> None:
        self.id = id
        self.teensyAudioClass = teensyAudioClass
        self.parameter = parameter
        self.parameterTitle = parameterTitle
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
        return f"{self.teensyAudioClass} {self.id};\n"
    
    def getNodeSetupCode(self) -> str:
        ##toDo: Implement TeenysAudio Code
        return f"{self.id}.begin();\n"

    def getNodeLoopCode(self) -> str:   
        ##toDo: Implement TeenysAudio Code
        return f"{self.id}.update();\n"

    def setParameter(self, parameter: float):
        self.parameter = parameter