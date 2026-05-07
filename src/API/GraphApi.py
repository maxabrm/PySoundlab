from fastapi import APIRouter
import Models.GraphModel as graph
import Models.NodeModel as node

router = APIRouter()

@router.post("/validateGraph")
def validate_graph(graph: graph.GraphModel):
    return {"message": "Graph validated successfully"}

@router.post("/generateCode")
def generate_code(graph: graph.GraphModel):
    return {"message": "Code generated successfully"}


