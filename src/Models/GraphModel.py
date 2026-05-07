from pydantic import BaseModel
import Models.NodeModel as node

class ConnectionModel(BaseModel):
    id: int
    node1_id: str
    node2_id: str

class GraphModel(BaseModel):
    nodes: list[node.NodeModel]
    connections: list[ConnectionModel]


