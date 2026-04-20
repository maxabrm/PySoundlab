import node
from typing import Optional

class Input(node.Node):
    def __init__(self, id: str, parameter: float) -> None:
        super().__init__(id, "AudioInputI2S", parameter, None)

class Output(node.Node):
    def __init__(self, id: str, parameter: float) -> None:
        super().__init__(id, "AudioOutputI2S", parameter, None)

class Gain(node.Node):
    def __init__(self, id: str, parameter: float, Poti: node.Poti | None) -> None:
        super().__init__(id, "AudioAmplifier", parameter, Poti)

class Filter(node.Node):
    def __init__(self, id: str, parameter: float, Poti: node.Poti) -> None:
        super().__init__(id, "AudioFilterStateVariable", parameter, Poti)

class Delay(node.Node):
    def __init__(self, id: str, parameter: float, Poti: node.Poti) -> None:
        super().__init__(id, "AudioDelay", parameter, Poti)


        