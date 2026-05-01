#!/usr/bin/env python3
"""
PySoundLab - A Python project for sound processing and analysis.
"""

import sys
import node
import nodes
import graph
import generator

def main():
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

    gen = generator.CodeGenerator(g)
    print(gen.generate_code(g))

if __name__ == "__main__":
    main()