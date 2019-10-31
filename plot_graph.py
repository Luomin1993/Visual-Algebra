# -*- coding: utf-8 -*-
import numpy as np;
import re;
import matplotlib.pyplot as plt;
import networkx as nx;

"""
The Main Plot Function:
    ---- Read the Describe File: *.des;
    ---- Pre-define the Plot Rules;
    ---- Check If There is Any More Rules Reasoning;
    ---- Visualize the Graph;
"""


#-------- Add Labels Like add_edge() -----------
def add_label(NODE_1,
	          NODE_2,
	          pos,
	          LABEL_NAME,
	          font_size=10,
              font_color='k',
              font_family='sans-serif',
              font_weight='normal',
              alpha=1.0,
              bbox=None,
              ax=None,
              rotate=True,
              **kwds):
    #if ax is None:
    #    ax = plt.gca()
    # set optional alignment
    horizontalalignment = kwds.get('horizontalalignment', 'center')
    verticalalignment = kwds.get('verticalalignment', 'center')        
    (x1, y1) = pos[NODE_1];
    (x2, y2) = pos[NODE_2];
    (x, y)   = (x1 * 0.5 + x2 * (1.0 - 0.5),
                y1 * 0.5 + y2 * (1.0 - 0.5));
    plt.text(x,y,LABEL_NAME,fontsize=font_size);
    """
    text_info = ax.text(x, y,
                LABEL_NAME,
                size=font_size,
                color=font_color,
                family=font_family,
                weight=font_weight,
                alpha=alpha,
                horizontalalignment=horizontalalignment,
                verticalalignment=verticalalignment,
                rotation=0.0,
                transform=ax.transData,
                bbox=bbox,
                zorder=1,
                clip_on=True,
                );
    return text_info;
    """


def plot_demo():
    G = nx.DiGraph();
    attributes = [];
    PATH    = './demo_fig.pdf';
    # Def Nodes;
    POINT_0 = '$\phi$';
    POINT_1 = '$M$';
    POINT_2 = '$R$';
    POINT_3 = '$S$';
    NODES_1 = [POINT_1,POINT_2];
    NODES_2 = [POINT_0,POINT_3];
    # Def Edges;
    G.add_edge(POINT_0,POINT_2, label = 'fish');
    G.add_edge(POINT_1,POINT_2, label = 'toor');
    G.add_edge(POINT_1,POINT_3, label = 'tute');
    G.add_edge(POINT_2,POINT_3, label = '=');
    # Draw Nodes;
    pos = nx.spring_layout(G);
    nx.draw_networkx_nodes(G, pos, nodelist = NODES_1,node_size = 1000,node_color = 'b',node_shape = 'o');
    nx.draw_networkx_nodes(G, pos, nodelist = NODES_2,node_size = 1200,node_color = 'r',node_shape = '^');
    # Draw Edges;
    nx.draw_networkx_edges(G, pos, style = 'dashed', arrowsize = 13.2, edge_cmap = plt.cm.Blues, width = 2, arrows = False);
    # Show Node Labels;
    nx.draw_networkx_labels(G, pos, font_size=14, font_family='sans-serif');
    # Show Edge Labels;
    add_label(POINT_0,POINT_2,pos,'$L_{02}$',font_size=7);
    add_label(POINT_1,POINT_2,pos,'$L_{12}$',font_size=7);
    add_label(POINT_1,POINT_3,pos,'$L_{13}$',font_size=7);
    add_label(POINT_2,POINT_3,pos,'$L_{23}$',font_size=7);
    # ----------- test the positions -------------
    """
    labels = dict(((u, v), d) for u, v, d in G.edges(data=True))
    label_pos = 0.5;
    for (n1, n2), label in labels.items():
        (x1, y1) = pos[n1]
        (x2, y2) = pos[n2]
        (x, y) = (x1 * label_pos + x2 * (1.0 - label_pos),
                  y1 * label_pos + y2 * (1.0 - label_pos))
        print '-----------------------'
        print (x1, y1);
        print (x2, y2);
        print (x, y);
    """
    # Draw Labels;
    #nx.draw_spring(G,with_labels = True);
    #text_items = nx.draw_networkx_edge_labels(G, pos, font_size = 10, alpha = 0.8, rotate = False);
    # Save Fig;
    plt.axis('on');
    plt.xlim((-2,2))
    plt.ylim((-2,2))
    plt.savefig(PATH);
    plt.close('all');
    # ----------- show the position infomation ----------
    """
    for (n1, n2), text_info in text_items.items():
    	 # print (n1, n2);
    	 # Pos of nodes;
    	 print pos[n1];
    	 print pos[n2];
    	 # Pos of edge text;
    	 print text_info;
    """	 

"""
[ 0.22071186 -0.21337444] POINT_1     no
[-0.38015121  0.26853255] POINT_2     no
Text(-0.0797197,0.0275791,u'toor')    yes
[-0.72373247 -1.        ] POINT_0     no
[-0.38015121  0.26853255] POINT_2     no
Text(-0.551942,-0.365734,u'fish')     yes
[-0.38015121  0.26853255] POINT_2     no
[0.88317181 0.94484188]   POINT_3     no
Text(0.25151,0.606687,u'=')           yes
[ 0.22071186 -0.21337444] POINT_1     no
[0.88317181 0.94484188]   POINT_3     no
Text(0.551942,0.365734,u'tute')       yes
"""

# =====================   FUNCTIONS   ============================

"""
  ********** Describing File **********
IS;$M$:$R$-Mod
$\sub$;$Q$;$M$
divide;$M$;$Q$
IS;$ASS_R$;$\{P\}$
DEF;$Q$;$P$-Primary Submod;

"""















if __name__ == '__main__':
    plot_demo();