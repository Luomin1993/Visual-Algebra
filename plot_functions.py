#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" plotting functions """

__author__ = 'hanss401'

# Constant: define the distance equals same_pos:
SAME_DIS = 0.3;
MOVE_DIS = 0.5;


import numpy as np;
import re;
import matplotlib.pyplot as plt;
import networkx as nx;

from load_file import *;

"""
S;$M$;$R$-Mod
$\sub$;$Q$;$M$
divide;$M$;$Q$
IS;$ASS_R$;$\{P\}$
DEF;$Q$;$P$-Primary Submod;
           ||
           ||
          \  /
           \/
========= GRAPH ===========
---- Nodes ----
$M$
['var', 'normal']
$R$-Mod
['normal']
$Q$
['var', 'normal']
$ASS_R$
['var', 'normal']
$\{P\}$
['var', 'normal']
$P$-Primary Submod
['normal']
---- Edges ----
IS
['normal']
$\sub$
['normal']
divide
['normal']
DEF
['def']
"""


class Plotter(object):
    """keep the global info of plotting"""
    def __init__(self, name, graph=None):
        super(Plotter, self).__init__()
        self.name  =  name;
        self.graph = GRAPH;
        
# --------- plot main --------------------
def plot_out(GRAPH,SAVE_PATH):
    NXG = nx.DiGraph();
    # list the 'var' nodes;
    VAR_NODES = [];
    for NODE in GRAPH.nodes:
        if ('var' in NODE.attr) and ('map' not in NODE.attr):
            VAR_NODES.append(NODE.name);
    # list the 'deb' nodes;
    DEB_NODES = [];
    for NODE in GRAPH.nodes:
        if 'deb' in NODE.attr:
            DEB_NODES.append(NODE.name);        
    # list the 'map' nodes;
    MAP_NODES = [];
    for NODE in GRAPH.nodes:
        if 'map' in NODE.attr:
            MAP_NODES.append(NODE.name);   
    # add two-obj edges into the NXG;
    for EDGE in GRAPH.edges:
        if len(EDGE.nodes) == 2:
            NXG.add_edge( EDGE.nodes[0], EDGE.nodes[1]);
    # layout the nodes(within two-obj edges);
    POSITIONS = nx.spring_layout(NXG);
    # draw nodes:
    if VAR_NODES != []:
        nx.draw_networkx_nodes(NXG, POSITIONS, 
                               nodelist = VAR_NODES,
                                 node_size = 1000,
                                 node_color = 'b',
                                 node_shape = 'o');
    if DEB_NODES != []:
        nx.draw_networkx_nodes(NXG, POSITIONS, 
                               nodelist = DEB_NODES,
                                 node_size = 1200,
                                 node_color = 'b',
                                 node_shape = 'o');
    if MAP_NODES != []:
        nx.draw_networkx_nodes(NXG, POSITIONS, 
                               nodelist = MAP_NODES,
                                 node_size = 1000,
                                 node_color = 'b',
                                 node_shape = 'o');
    # draw edges with 2-nodes:
    nx.draw_networkx_edges(NXG, POSITIONS, 
                              style = 'dashed', 
                              arrowsize = 13.2, 
                              edge_cmap = plt.cm.Blues, 
                              width = 2, 
                              arrows = False);
    # draw edges:
    for EDGE in GRAPH.edges:
        LINKED_POSITIONS = _get_nodes_positions_(EDGE,POSITIONS);
        # draw edge over mul-nodes:
        if len(LINKED_POSITIONS)>2:
            # not 'map':
            if 'map' not in EDGE.attr:
                # compute the average-position;
                AVE_POSITION = _compute_ave_pos_(LINKED_POSITIONS);
                # draw line to each linked node;
                for POSITION in LINKED_POSITIONS:
                    plt.plot(np.array(POSITION),np.array(AVE_POSITION),style='-.',color='green');
            # is 'map':
            if 'map' in EDGE.attr:
                # compute the average-position;
                AVE_POSITION = _compute_ave_pos_(LINKED_POSITIONS[0:-1]);
                # draw line to each linked node;
                for POSITION in LINKED_POSITIONS[0:-1]:
                    plt.plot(np.array(POSITION),np.array(AVE_POSITION),style='-.',color='green');
                # draw a quiver;
                plt.plot(np.array(AVE_POSITION),np.array(LINKED_POSITIONS[-1]),style='--',color='blue');

    # add the labels:            
    OCCUPIED_POSITIONS = [];
    for EDGE in GRAPH.edges:
        # for 'two'-type edge:
        if len(EDGE.link_nodes)==2:
            # compute the label-pos:
            LINKED_POSITIONS = _get_nodes_positions_(EDGE,POSITIONS);
            LABEL_POS        =   _compute_ave_pos_(LINKED_POSITIONS);
            # check if it's occupied;
            while _is_occupied_(LABEL_POS,OCCUPIED_POSITIONS):
                # move to the nearest pos:
                LABEL_POS[1] -= MOVE_DIS;
            # write the text;    
            plt.text(LABEL_POS[0],LABEL_POS[1],EDGE.name,fontsize=font_size);   
            # record the position occupied:
            OCCUPIED_POSITIONS.append(LABEL_POS);
        # for 'mul'-type edge:
        if len(EDGE.link_nodes)>2 and 'map' not in EDGE.attr:
            # compute the label-pos:
            LINKED_POSITIONS = _get_nodes_positions_(EDGE,POSITIONS);
            LABEL_POS        =   _compute_ave_pos_(LINKED_POSITIONS);
            # check if it's occupied;
            while _is_occupied_(LABEL_POS,OCCUPIED_POSITIONS):
                # move to the nearest pos:
                LABEL_POS[1] -= MOVE_DIS;
            # write the text;    
            plt.text(LABEL_POS[0],LABEL_POS[1],EDGE.name,fontsize=font_size);   
            # record the position occupied:
            OCCUPIED_POSITIONS.append(LABEL_POS);
        # for 'map'-type edge:
        if len(EDGE.link_nodes)>2 and 'map' in EDGE.attr:
            # compute the label-pos:
            LINKED_POSITIONS = _get_nodes_positions_(EDGE,POSITIONS);
            LABEL_POS        =   _compute_ave_pos_(LINKED_POSITIONS[-1]);
            # check if it's occupied;
            while _is_occupied_(LABEL_POS,OCCUPIED_POSITIONS):
                # move to the nearest pos:
                LABEL_POS[1] -= MOVE_DIS;
            # write the text;    
            plt.text(LABEL_POS[0],LABEL_POS[1],EDGE.name,fontsize=font_size);   
            # record the position occupied:
            OCCUPIED_POSITIONS.append(LABEL_POS);
        
    # save and close;
    plt.savefig(SAVE_PATH);
    plt.close('all');


# --------- sub-func:give the positions of the linked nodes of the edge ----------
def _get_nodes_positions_(EDGE,POSITIONS):
    LINKED_POSITIONS = [];
    for NODE in EDGE.link_nodes:
        (POS_X,POS_Y) = POSITIONS[NODE];
        LINKED_POSITIONS.append( (POS_X,POS_Y) );
    return LINKED_POSITIONS;    

# --------- sub-func:compute average position ----------
def _compute_ave_pos_(LINKED_POSITIONS):
    AVE_POSITION = (0.0,0.0);
    for POSITION in LINKED_POSITIONS:
        AVE_POSITION[0] += POSITION[0];
        AVE_POSITION[1] += POSITION[1];
    AVE_POSITION[0] = AVE_POSITION[0]/len(LINKED_POSITIONS);
    AVE_POSITION[1] = AVE_POSITION[1]/len(LINKED_POSITIONS);
    return AVE_POSITION;

# --------- sub-func:compute if the two positions is the same ----------
def _same_pos_(POSITION_A,POSITION_B):
    DISTANCE = np.sqrt((POSITION_A[0]-POSITION_B[0])**2 + (POSITION_A[1]-POSITION_B[1])**2);
    if DISTANCE < SAME_DIS:
        return True;
    return False;    

# --------- draw the edges set -----------
def draw_edges(PLOTTER):
    pass;


# --------- draw the nodes set -----------
def draw_nodes(PLOTTER):
    pass;


"""
    =============    ===============================
    character        color
    =============    ===============================
    ``'b'``          blue 蓝
    ``'g'``          green 绿
    ``'r'``          red 红
    ``'c'``          cyan 蓝绿
    ``'m'``          magenta 洋红
    ``'y'``          yellow 黄
    ``'k'``          black 黑
    ``'w'``          white 白
    =============    ===============================

"""


# ---------- T E S T -----------
if __name__ == '__main__':
    GRAPH = read_file('demo_thm.des');
    plot_out(GRAPH,'demo_thm.pdf');