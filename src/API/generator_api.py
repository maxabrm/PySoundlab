from fastapi import APIRouter
import Core.Graph.graph as graph
import Core.Node.nodes as nodes

router = APIRouter()

@router.post("/generateCode")
def generate_code(graph: graph.Graph):
    generator = generator.CodeGenerator(graph)
    code = generator.generate_code(graph)
    return f"Code für Teensy:\n{code}"

