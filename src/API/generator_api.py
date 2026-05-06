from fastapi import APIRouter
import Models.graph_model as graph
import Models.node_model as nodes

router = APIRouter()

@router.post("/generateCode")
def generate_code(graph: graph.GraphModel):
    generator = generator.CodeGenerator(graph)
    code = generator.generate_code(graph)
    return f"Code für Teensy:\n{code}"

