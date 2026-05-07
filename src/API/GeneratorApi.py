from fastapi import APIRouter
import Models.graph_model as graph
import Models.node_model as nodes

router = APIRouter()

@router.post("/generateCode")
def generate_code(graph: graph.GraphModel):
    code = "// Generated code for Teensy\n\n"
    return f"Code für Teensy:\n{code}"

