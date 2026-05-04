#!/usr/bin/env python3
"""
PySoundLab - A Python project for sound processing and analysis.
"""

import sys
import Core.Node.node as node
import Core.Node.nodes as nodes
import Core.Graph.graph as graph
import Core.CodeGen.generator as generator
import API.graph_api as graph_api
import API.generator_api as generator_api
import API.node_api as node_api
from fastapi import FastAPI

def main():


    app = FastAPI()
    app.include_router(graph_api.router, prefix="/graph")
    app.include_router(generator_api.router, prefix="/generator")
    app.include_router(node_api.router, prefix="/node")

  # Schneller Test  
    print("// Welcome to PySoundLab!")
    print("// Python version:", sys.version)

    GoldPoti = node.Poti("poti1", "A0", 10000.0, 1023.0)

    InputNode = nodes.AudioInput("input1")
    filterNode = nodes.Filter("filter1", 1000.0, GoldPoti)
    OutputNode = nodes.AudioOutput("output1")

    g = graph.Graph()
    g.addNode(InputNode)
    g.addNode(filterNode)
    g.addNode(OutputNode)
    g.addConnection(InputNode, filterNode)
    g.addConnection(filterNode, OutputNode)

    gen = generator.CodeGenerator(g)
    print(gen.generate_code(g))

if __name__ == "__main__":
    main()