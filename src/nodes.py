import node
from typing import Optional

class Input(node.Node):
    def __init__(self, id: str) -> None:
        super().__init__(id, "AudioInputI2S", None, None)

class Output(node.Node):
    def __init__(self, id: str, parameter: float) -> None:
        super().__init__(id, "AudioOutputI2S", None, None)

class Gain(node.Node):

    parameterTitle = "Gain"

    def __init__(self, id: str, parameter: float | None, Poti: node.Poti  | None) -> None:
        super().__init__(id, "AudioAmplifier", parameter, Poti)

class Filter(node.Node):

    parameterTitle = "Frequency"

    def __init__(self, id: str, parameter: float | None, Poti: node.Poti | None) -> None:
        super().__init__(id, "AudioFilterStateVariable", parameter, Poti)

    def getNodeInitCode(self):
        return f"{self.teensyAudioClass} {self.id};\n"

    def getNodeSetupCode(self):
        return f"{self.id}.frequency(0);\n"

    def getNodeLoopCode(self):
        if self.hasPoti():
            return f"{self.id}.frequency({self.parameter}*{self.Poti.id}.getValue()*Divider);\n"
    


class Delay(node.Node):

    parameterTitle = "Delay Time"

    def __init__(self, id: str, parameter: float | None, Poti: node.Poti | None) -> None:
        super().__init__(id, "AudioDelay", parameter, Poti)

    def getNodeInitCode(self):
        return super().getNodeInitCode()

    def getNodeSetupCode(self):
        return super().getNodeSetupCode()

    def getNodeLoopCode(self):
        return super().getNodeLoopCode()


class Reverb(node.Node):

    parameterTitle = "Reverb Time"

    def __init__(self, id: str, parameter: float | None, Poti: node.Poti | None) -> None:
        super().__init__(id, "AudioEffectFreeverb", parameter, Poti)  

    def getNodeInitCode(self):
        return super().getNodeInitCode()

    def getNodeSetupCode(self):
        return super().getNodeSetupCode()

    def getNodeLoopCode(self):
        return super().getNodeLoopCode()
    




