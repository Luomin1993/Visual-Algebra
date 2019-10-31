#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" load the file *.des and give the Graph instance result """

__author__ = 'hanss401'


import numpy as np;
import re;
import matplotlib.pyplot as plt;
import networkx as nx;

from relation_construct import *;

# -------- main func: read file and give Graph --------------
def read_file(FILE_PATH):
    # read the file;
    with open(FILE_PATH, 'r') as f:
        DES_LINES = f.read().split('\n')[0:-1];
    # init the GRAPH;
    GRAPH     = Graph(FILE_PATH.replace('.des',''), edges=[], nodes=[]);
    # loop: resolve each line of the *.des;
    for LINE_DES in DES_LINES:
        # get the sub-graph of this line;
        SUB_GRAPH = attr_auto_derive(LINE_DES);
        # combine the sub-graph into the GRAPH;
        # ----- loop: combine each edge into GRAPH;---------------------------
        for EDGE in SUB_GRAPH.edges:
            # if the EDGE is in the GRAPH:
            INDEX_OF_OBJ = _in_graph_(EDGE,GRAPH,JUDGE_ITEM='edge')
            if INDEX_OF_OBJ>=0:
                # but this EDGE has new attr;
                NEW_ATTRS = _new_attrs_to_graph_(EDGE,GRAPH,INDEX_OF_OBJ,JUDGE_ITEM='edge');
                if NEW_ATTRS>=0:
                    # add the new attrs into the corresponding object;
                    GRAPH.edges[INDEX_OF_OBJ] += NEW_ATTRS;
                # nothing to do: next line
                if NEW_ATTRS<0:
                    continue;    
            # if the EDGE is not in the GRAPH:
            if INDEX_OF_OBJ<0:
                # add the EDGE into the GRAPH:
                GRAPH.edges.append(EDGE);
        # ----- loop: combine each node into GRAPH;---------------------------
        for NODE in SUB_GRAPH.nodes:
            # if the NODE is in the GRAPH:
            INDEX_OF_OBJ = _in_graph_(NODE,GRAPH,JUDGE_ITEM='node')
            if INDEX_OF_OBJ>=0:
                # but this NODE has new attr;
                NEW_ATTRS = _new_attrs_to_graph_(NODE,GRAPH,INDEX_OF_OBJ,JUDGE_ITEM='node');
                if NEW_ATTRS>=0:
                    # add the new attrs into the corresponding object;
                    GRAPH.nodes[INDEX_OF_OBJ] += NEW_ATTRS;
                # nothing to do: next line
                if NEW_ATTRS<0:
                    continue;        
            # if the NODE is not in the GRAPH:
            if INDEX_OF_OBJ<0:
                # add the NODE into the GRAPH:
                GRAPH.nodes.append(NODE);        
    # return the result;        
    return GRAPH;        


# ------- sub func: judge if the edge/node is in the graph -----------
def _in_graph_(EDGE_OR_NODE,GRAPH,JUDGE_ITEM = None):
    if JUDGE_ITEM == 'edge':
        for INDEX_OF_OBJ in range(0,len(GRAPH.edges)):
            if GRAPH.edges[INDEX_OF_OBJ].name == EDGE_OR_NODE.name:
                return INDEX_OF_OBJ;

    if JUDGE_ITEM == 'node':
        for INDEX_OF_OBJ in range(0,len(GRAPH.nodes)):
            if GRAPH.nodes[INDEX_OF_OBJ].name == EDGE_OR_NODE.name:
                return INDEX_OF_OBJ;

    return -2;                                        


# ------- sub func: judge if the edge/node has new attr compared to the graph,find out-----------
def _new_attrs_to_graph_(EDGE_OR_NODE,GRAPH,INDEX_OF_OBJ,JUDGE_ITEM = None):
    if JUDGE_ITEM == 'edge':
        NEW_ATTRS = [];
        for ATTR in EDGE_OR_NODE.attr:
            if ATTR not in GRAPH.edges[INDEX_OF_OBJ].attr:
                NEW_ATTRS.append(ATTR);

    if JUDGE_ITEM == 'node':
        NEW_ATTRS = [];
        for ATTR in EDGE_OR_NODE.attr:
            if ATTR not in GRAPH.nodes[INDEX_OF_OBJ].attr:
                NEW_ATTRS.append(ATTR);

    return -2;                                        




# ----------- print the graph ---------------
def print_graph(GRAPH):
    print '---- Nodes ----'
    for NODE in GRAPH.nodes:
        print NODE.name;
        print NODE.attr;
    print '---- Edges ----'
    for EDGE in GRAPH.edges:
        print EDGE.name;
        print EDGE.attr;


# ----------- T E S T ---------------
if __name__ == '__main__':
   GRAPH = read_file('demo_thm.des');
   print_graph(GRAPH);