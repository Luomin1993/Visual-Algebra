#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" derive the attributes of the objects in graph automaticly """

__author__ = 'hanss401'


import numpy as np;
import re;
import matplotlib.pyplot as plt;
import networkx as nx;

from load_file import *;

class Relationship(object):
    	"""the basic class of Relationship

    	Parameters
        ----------
        name : string
            the name of the Relationship;
    
        attr : string
            one of the attributes:
               {'two','mul','map'};
    
        patten: re
            i.e.:r'*;*;*';

    	"""
    	def __init__(self, name, attr=None, patten):
    		super(Relationship, self).__init__();
    		self.name   =   name;
    		self.attr   =   atrt;
    		self.patten = patten;

# ------------ derive the relations --------------
def attr_auto_derive(LINE_DES):
	# init the sub-graph;
	SUB_GRAPH = Graph(name='sub-graph',edges=[],nodes=[]);
	# trans the STRING into LIST;
    OBJ_LIST = LINE_DES.split(';');
    # relationship: 'two':
    if len(OBJ_LIST) == 3:      
        # give attr of nodes:
        SUB_GRAPH.nodes.append( _attr_of_node_(OBJ_LIST[1]) );
        SUB_GRAPH.nodes.append( _attr_of_node_(OBJ_LIST[2]) );
        # give attr of edge:
        SUB_GRAPH.edges.append( _attr_of_edge_(OBJ_LIST[0],link_nodes=SUB_GRAPH.nodes) );
    # relationship: 'mul': (include the situation: map multi-objects to one)
    if len(OBJ_LIST) >  3:
        # give attr of nodes:
        for NODE_OBJ in OBJ_LIST[1:-1]:
            SUB_GRAPH.nodes.append( _attr_of_node_(NODE_OBJ) );
        # give attr of edge:    
        SUB_GRAPH.edges.append( _attr_of_edge_(OBJ_LIST[0],link_nodes=SUB_GRAPH.nodes) );         
    return SUB_GRAPH;



# ------------ sub-func: give attr of edge -------- 
#              then return the edge;
def _attr_of_edge_(STRING_EDGE,link_nodes=[]):
    # init the EDGE:
    EDGE = Edge(STRING_EDGE,[],link_nodes = link_nodes);
    # give the attr:
    if '(\\cdot' in STRING_EDGE:
        EDGE.attr.append('map');
        return EDGE;
    if 'DEF' == STRING_EDGE:
        EDGE.attr.append('def');
        return EDGE;
    if 'THM' == STRING_EDGE:
        EDGE.attr.append('thm');
        return EDGE;
    if 'EQ' == STRING_EDGE:
        EDGE.attr.append('eq');
        return EDGE;        
    EDGE.attr.append('normal');
    return EDGE;    

# ------------ sub-func: give attr of node -------- 
#              then return the node;
def _attr_of_node_(STRING_NODE):
    # init the NODE:
    NODE = Edge(STRING_NODE,[]);
    # give the attr:
    if STRING_NODE[0]=='$' and STRING_NODE[-1]=='$':
        NODE.attr.append('var');
    if '$' not in STRING_NODE:
        NODE.attr.append('deb');
    if '(\\cdot' in STRING_NODE:
        NODE.attr.append('map');        
    NODE.attr.append('normal');       
    return EDGE;


# ------------ complete the relations --------------
def attr_auto_complete(LINE_DES,GRAPH):
    pass;		

