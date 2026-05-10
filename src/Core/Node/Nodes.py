import Core.Node.Node as node
from typing import Optional

#ToDo Nodes ausarbeiten

class AudioInput(node.Node):
    def __init__(self, id: str) -> None:
        super().__init__(id, "AudioInputI2S", None, None, None)

class AudioOutput(node.Node):
    def __init__(self, id: str) -> None:
        super().__init__(id, "AudioOutputI2S", None, None, None)

class Gain(node.Node):

    def __init__(self, id: str, parameter: Optional[float], Poti: Optional[node.Poti]) -> None:
        super().__init__(id, "AudioEffectWaveshaper ", parameter, "Gain", Poti)
      
    def getNodeInitCode(self):
        return f"{self.teensyAudioClass} {self.id};\n"

    def getNodeSetupCode(self):
        return f"{self.id}.;\n"

    def getNodeLoopCode(self):
            return f"" # Wavehaper function fehlt noch


class Filter(node.Node):

    def __init__(self, id: str, parameter: Optional[float], Poti: Optional[node.Poti]) -> None:
        super().__init__(id, "AudioFilterStateVariable", parameter, "Frequency", Poti)

    def getNodeInitCode(self):
        return f"{self.teensyAudioClass} {self.id};\n"

    def getNodeSetupCode(self):
        return f"{self.id}.frequency(0);\n"

    def getNodeLoopCode(self):
        if self.hasPoti():
            return f"{self.id}.frequency({self.parameter}*({self.Poti.id}.getValue()*{self.Poti.id}_divider));\n"
        else:
            return f"{self.id}.frequency({self.parameter});\n"
    


class Delay(node.Node):

    def __init__(self, id: str, parameter: Optional[float], Poti: Optional[node.Poti]) -> None:
        super().__init__(id, "AudioDelay", parameter, "Delay Time", Poti)

    def getNodeInitCode(self):
        return super().getNodeInitCode()

    def getNodeSetupCode(self):
        return super().getNodeSetupCode()

    def getNodeLoopCode(self):
        return super().getNodeLoopCode()


class Reverb(node.Node):

    def __init__(self, id: str, parameter: Optional[float], Poti: Optional[node.Poti]) -> None:
        super().__init__(id, "AudioEffectFreeverb", parameter, "Reverb Time", Poti)

    def getNodeInitCode(self):
        return f"{self.teensyAudioClass} {self.id};\n"

    def getNodeSetupCode(self):
       return f"{self.id}.roomsize({0});\n"

    def getNodeLoopCode(self):
        if self.hasPoti():
            return f"{self.id}.roomsize({self.parameter}*({self.Poti.id}.getValue()*{self.Poti.id}_divider));\n"
        else:
            return f"{self.id}.roomsize({self.parameter});\n"
    




