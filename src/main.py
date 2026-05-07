#!/usr/bin/env python3
"""
PySoundLab - A Python project for sound processing and analysis.
"""

import sys
import Core.Mapper.NodeMappings
import Core.Node.Node as node
import Core.Node.Nodes as nodes
import Core.Graph.Graph as graph
import Core.CodeGen.Generator as generator
import API.GraphApi as graph_api

from fastapi import FastAPI

def main():


    app = FastAPI()
    app.include_router(graph_api.router, prefix="/graph")

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