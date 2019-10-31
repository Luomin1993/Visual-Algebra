#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" plotting functions """

__author__ = 'hanss401'


import numpy as np;
import re;
import matplotlib.pyplot as plt;
import networkx as nx;

from load_file import *;

class Plotter(object):
	"""keep the global info of plotting"""
	def __init__(self, name, graph=None):
		super(Plotter, self).__init__()
		self.name  =  name;
		self.graph = GRAPH;
		

# --------- draw the edges set -----------
def draw_edges(PLOTTER):
    pass;


# --------- draw the nodes set -----------
def draw_nodes(PLOTTER):
    pass;
