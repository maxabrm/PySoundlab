from pydantic import BaseModel

class GraphModel(BaseModel):
    id: str
    name: str
    nodes: list
    connections: list
    