from fastapi import APIRouter
import Core.Graph.graph as graph
import Core.Node.node as node
import Core.Node.nodes as nodes

router = APIRouter()

@router.post("/addNode")
def add_node(node: node.Node):
    graph.addNode(node)
    return {"message": "Node added successfully"}

@router.post("/addConnection")
def add_connection(connection: graph.Connection):
    graph.addConnection(connection)
    return {"message": "Connection added successfully"}

@router.post("/createGraph")
def create_graph():
    new_graph = graph.Graph()
    return {"message": "Graph created successfully"}
        


