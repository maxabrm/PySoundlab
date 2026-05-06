from pydantic import BaseModel
import Models.node_model as node

class ConnectionModel(BaseModel):
    id: int
    node1: node.NodeModel
    node2: node.NodeModel

class GraphModel(BaseModel):
    nodes: list[node.NodeModel]
    connections: list[ConnectionModel]


