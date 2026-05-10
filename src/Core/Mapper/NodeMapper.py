from Core.Node.Node import Node, Poti
from Models.NodeModel import NodeModel, PotiModel
from typing import Callable, Dict, Optional

class NodeMapper:

    _nodeRegistry: Dict[str, Callable[[NodeModel], Node]] = {}

    @classmethod
    def registerNode(cls, nodeType: str):
        def decorator(func: Callable[[NodeModel], Node]):
            cls._nodeRegistry[nodeType] = func
            return func
        return decorator

    @classmethod
    def mapPoti(cls, potiModel: Optional[PotiModel]) -> Optional[Poti]:
        if potiModel is None:
            return None
        return Poti(potiModel.id, potiModel.inputPin, potiModel.resistance, potiModel.maxValue)

    @classmethod
    def createNode(cls, nodeModel: NodeModel) -> Node:
        nodeType = nodeModel.type

        if nodeType not in cls._nodeRegistry:
            raise ValueError(f"Unknown node type: {nodeType}")

        constructor = cls._nodeRegistry[nodeType]
        return constructor(nodeModel)