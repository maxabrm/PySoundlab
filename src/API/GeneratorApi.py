from fastapi import APIRouter
import Models.GraphModel as graph
import Models.NodeModel as nodes

router = APIRouter()

@router.post("/generateCode")
def generate_code(graph: graph.GraphModel):
    code = "// Generated code for Teensy\n\n"
    return f"Code für Teensy:\n{code}"

