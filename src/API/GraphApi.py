from fastapi import APIRouter
import Models.GraphModel as graph
from Core.Mapper.GraphMapper import GraphMapper
import Models.NodeModel as node
from Core.CodeGen.Generator import CodeGenerator

router = APIRouter()

@router.post("/validateGraph")
def validate_graph(graph: graph.GraphModel):
    mapped_graph = GraphMapper.map_graph_model_to_graph(graph)
    is_valid = mapped_graph.validateGraph()
    return {"valid": is_valid}

@router.post("/generateCode")
def generate_code(graph: graph.GraphModel):
    mapped_graph = GraphMapper.map_graph_model_to_graph(graph)
    code_generator = CodeGenerator(mapped_graph)
    code = code_generator.generate_code(mapped_graph)
    return {"code": code}


