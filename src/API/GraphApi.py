from fastapi import APIRouter
import Models.GraphModel as graph
import Models.NodeModel as node

router = APIRouter()

@router.post("/addNode")
def add_node(node: node.NodeModel):
    return {"message": "Node added successfully"}

@router.post("/addConnection")
def add_connection(node_model1: node.NodeModel, node_model2: node.NodeModel):
    return {"message": "Connection added successfully"}

@router.post("/createGraph")
def create_graph():
    return {"message": "Graph created successfully"}
        


