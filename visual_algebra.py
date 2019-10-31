#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" main function """

__author__ = 'hanss401'


import numpy as np;
import re;
import matplotlib.pyplot as plt;
import networkx as nx;

from load_file import *;
from plot_functions import *;

# ----------- the main function --------------
def visual_algebra(FILE_PATH):
    GRAPH = read_file(FILE_PATH);
    plotter = Plotter('FAKE_NAME',graph=GRAPH);
    draw_edges(GRAPH);
    draw_nodes(GRAPH);
    plt.show();

