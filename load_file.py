#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" load the file *.des and give the Graph instance result """

__author__ = 'hanss401'


import numpy as np;
import re;
import matplotlib.pyplot as plt;
import networkx as nx;


# -------- main func: read file and give Graph --------------
def read_file(FILE_PATH):
    # read the file;
    with open(FILE_PATH, 'r') as f:
        DES_LINES = f.read().split('\n')[0:-1];
    # init the GRAPH;
    GRAPH     = Graph(FILE_PATH.replace('.des',''), edges_set=[], nodes_set=[]);
    # loop: resolve each line of the *.des;
    for LINE_DES in DES_LINES:
        # get the sub-graph of this line;
        SUB_GRAPH = attr_auto_derive(LINE_DES);
        # combine the sub-graph into the GRAPH;
        # ----- loop: combine each edge into GRAPH;---------------------------
        for EDGE in SUB_GRAPH.edges:
            # if the EDGE is in the GRAPH:
            INDEX_OF_OBJ = _in_graph_(EDGE,GRAPH,JUDGE_ITEM='edge')
            if INDEX_OF_OBJ:
                # but this EDGE has new attr;
                NEW_ATTRS = _new_attrs_to_graph_(EDGE_OR_NODE,GRAPH,INDEX_OF_OBJ,JUDGE_ITEM='edge');
                if not (NEW_ATTRS == False):
                    # add the new attrs into the corresponding object;
                    GRAPH.edges[INDEX_OF_OBJ] += NEW_ATTRS;
            # if the EDGE is not in the GRAPH:
            else:
                # add the EDGE into the GRAPH:
                GRAPH.edges.append(EDGE);
        # ----- loop: combine each node into GRAPH;---------------------------
        for NODE in SUB_GRAPH.nodes:
            # if the NODE is in the GRAPH:
            INDEX_OF_OBJ = _in_graph_(NODE,GRAPH,JUDGE_ITEM='node')
            if INDEX_OF_OBJ:
                # but this NODE has new attr;
                NEW_ATTRS = _new_attrs_to_graph_(EDGE_OR_NODE,GRAPH,INDEX_OF_OBJ,JUDGE_ITEM='node');
                if not (NEW_ATTRS == False):
                    # add the new attrs into the corresponding object;
                    GRAPH.nodes[INDEX_OF_OBJ] += NEW_ATTRS;
            # if the NODE is not in the GRAPH:
            else:
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

    return False;                                        


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

    return False;                                        



class Edge(object):
        """the basic class of Edge

        Parameters
        ----------
        name : string
            the name of the Edge;
    
        attr : list of {string}
            each of which is one of the attributes:
               {'def','thm','eq','map'};

        attr : list of {string}
            linked nodes, i.e.:
               {'$\phi$','S_a',...};       
    
        style: string, optional
            the style of the edge drawed;

        color: string, optional
            the color of the edge drawed;    
        """
        def __init__(self, name, attr, style=None, color=None, link_nodes=[]):
            super(Edge, self).__init__();
            self.name       =       name;
            self.attr       =       atrt; 
            self.style      =      style;
            self.color      =      color;
            self.link_nodes = link_nodes;

            
class Node(object):
        """the basic class of Node

        Parameters
        ----------
        name : string
            the name of the Node;
    
        attr : list of {string}
            each of which is one of the attributes:
               {'var','prop','deb','link','map'};
    
        style: string, optional
            the style of the node drawed;

        color: string, optional
            the color of the node drawed;    
        """
        def __init__(self, name, attr, style=None, color=None):
            super(Node, self).__init__();
            self.name  =  name;
            self.attr  =  atrt;
            self.style = style;
            self.color = color;
            

class Graph(object):
        """the basic class of Graph

        Parameters
        ----------
        name : string
            the name of the Graph;

        edges_set : list, {edges};
            the name of the Graph;
    
        nodes_set : list, {nodes};
            one of the attributes:
        """
        def __init__(self, edges=None, nodes=None):
            super(Graph, self).__init__();
            self.edges = edges;
            self.nodes = nodes;
            

                                