from fastapi import APIRouter
import Models.graph_model as graph
import Models.node_model as node  

router = APIRouter()

@router.post("/addPoti")
def add_poti(node: node.NodeModel, poti: node.PotiModel):
    node.addPoti(poti)
    return {"message": "Poti added successfully"}

@router.post("/addNode")
def add_node(node: node.NodeModel):
    return {"message": "Node added successfully"}

