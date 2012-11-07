#!/usr/bin/env python

from graphMain import GraphMain
from lxml import etree

class GraphGXL(GraphMain):


    def load_gxl(self, xml_file):
        """Load file from path given args"""
        xml_file = etree.parse(xml_file)
        self.parse_gxl(xml_file)

    def parse_gxl(self, xml_file):
        """Parse gxl file.
        Collect all edges and nodes with attributes and children"""

        self.type = xml_file.getroot().tag
        root = xml_file.getroot()
        self.nodes_map = {}
        self.edges_map = {}
        self.graph_info = {}

        info = root.find('graph')
        nodes = root.findall('graph/node')
        edges = root.findall('graph/edge')

        for k, v in info.attrib.items():
            self.graph_info[k] = v

        i=0
        for node in nodes:
            self.nodes_map[i] = node.attrib
            i = i+1

        i=0
        for edge in edges:
            self.edges_map[i] = edge.attrib
            i = i+1

        if self.graph_info.has_key('edgemode') and self.graph_info['edgemode'] == ' directed':
            self.is_directed = True


if __name__ == '__main__':
    'GraphGXL'