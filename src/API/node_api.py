from fastapi import APIRouter
import Models.node_model as node
from Core.Mapper.node_mapper import NodeMapper   

router = APIRouter()
# eigentlich wird hier nur der Graph aktualisiert das ist nur zur Übung
@router.post("/addNode")
def add_node(node: node.NodeModel):
    NodeMapper.createNode(node)
    return {"message": "Node added successfully"}

