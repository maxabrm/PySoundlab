from Core.Node.Node import Node
from Models.NodeModel import NodeModel
from typing import Callable, Dict

#ToDo: Create Funktion für Graph und Connection

class NodeMapper:  

    _nodeRegistry: Dict[str, Callable[[NodeModel], Node]] = {}

    @classmethod
    def registerNode(cls, nodeType: str):
        def decorator(func: Callable[[NodeModel], Node]):
            cls._nodeRegistry[nodeType] = func
            return func
        return decorator

    @classmethod
    def createNode(cls, nodeModel: NodeModel) -> Node:
        nodeType = nodeModel.type

        if nodeType not in cls._nodeRegistry:
            raise ValueError(f"Unknown node type: {nodeType}")

        constructor = cls._nodeRegistry[nodeType]
        return constructor(nodeModel)