#!/usr/bin/env python

# 
# This file is a part of the Yapgvb software package, and is 
# licensed under the New BSD License.
# A `LICENSE' file should have been included with this source.
#
# Copyright (c) 2009 Lonnie Princehouse
#

# random_graph.py
# --------------------
# Generate a random graph and plot it in a variety of formats.

import yapgvb
#import extra packages
import numpy
import sqlobject
from sqlobject import SQLObject, PickleCol, StringCol, IntCol, FloatCol, BoolCol, TimestampCol, ForeignKey, RelatedJoin, MultipleJoin, SingleJoin



def generate_tree(nnodes = 3):
    
    import random
    graph = yapgvb.Digraph("my_graph")

    for i in xrange(nnodes):
        # Create a node named str(i)
        node = graph.add_node(str(i))

        # Assign a random shape and color
        node.shape = random.choice(yapgvb.shapes.values())
        node.color = random.choice(yapgvb.colors.values())

    # Get all of the nodes as a list 
    # (the graph.nodes attribute is an iterator)
    nodes = list(graph.nodes)

    edge = nodes[0] >> nodes[1]
    edge.label = "w1"
    
    edge = nodes[0] >> nodes[2]
    edge.label = "w2"
    
    #edge.color = random.choice(yapgvb.colors.values())
        

    return graph




if __name__ == '__main__':
    print "Generating a random directed graph..."
    graph = generate_tree()
    
    print "Using dot for graph layout..."
    graph.layout(yapgvb.engines.dot)
    
    demo_formats = [
        yapgvb.formats.jpg,
        yapgvb.formats.png,
        yapgvb.formats.ps,
        yapgvb.formats.svg,
    ]
    
    for format in demo_formats:
        filename = 'demo.%s' % format

        print "  Rendering %s ..." % filename

        graph.render(filename)