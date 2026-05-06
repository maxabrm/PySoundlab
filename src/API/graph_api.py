from fastapi import APIRouter
import Models.graph_model as graph
import Models.node_model as node

router = APIRouter()

@router.post("/addNode")
def add_node(node: node.NodeModel):
    return {"message": "Node added successfully"}

@router.post("/addConnection")
def add_connection(connection: graph.Connection):
    return {"message": "Connection added successfully"}

@router.post("/createGraph")
def create_graph():
    return {"message": "Graph created successfully"}
        


