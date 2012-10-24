#!/usr/bin/env python

import networkx as nx
import pygraphviz as pgv
from graphParser import GraphParser


class GraphCreator():
    """Draw graph using networkx module"""

    def __init__(self, *args, **kwargs):
        self.parsed_data = GraphParser()
        self.nodes_map = self.parsed_data.nodes_map
        self.edges_map = self.parsed_data.edges_map
        self.graph_info = self.parsed_data.graph_info
        self.create()

    def create(self):
        """Create graph from nodes and edges"""
        graph = nx.Graph()

        if self.graph_info.has_key('edgemode') and self.graph_info['edgemode'] == ' directed':
            graph = nx.DiGraph()

        for k, v in self.nodes_map.items():
            graph.add_node(k, v)

        for k, v in self.edges_map.items():
            child = self.find_node_by_attr(graph, v['to'])[0]
            parent = self.find_node_by_attr(graph, v['from'])[0]
            graph.add_edge(child, parent, self.get_edge_attr(k))

        self.draw(graph)

    def draw(self, graph):
        nx.write_dot(graph,'file.dot')
        G=pgv.AGraph('file.dot')
        G.layout()
        G.draw('file.png', format='png',prog='dot')

    def find_node_by_attr(self, graph, attr_val, attr='id'):
        """Find node by attribute value"""
        node = [key for key, value in nx.get_node_attributes(graph, attr).iteritems() if value == attr_val]
        return node

    def get_edge_attr(self, edge):
        """Substract from edge info about attributes"""
        attrs = {}
        for k, v in self.edges_map[edge].items():
            if k != 'to' and k != 'from':
                attrs[k] = v
        return attrs


GraphCreator()