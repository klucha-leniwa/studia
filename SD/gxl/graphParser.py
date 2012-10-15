#!/usr/bin/env python

import sys
from lxml import etree


class GraphParser():
    """Load and parse file.
    Return format acceptable by networkx module"""
    def __init__(self):
        self.load_file()

    def parse_gxl(self, xml_file):
        """Parse gxl file.
        Collect all edges and nodes with attributes and children"""

        root = xml_file.getroot()

        self.nodes_map = {}
        self.edges_map = {}

        nodes = root.findall('graph/node')
        edges = root.findall('graph/edge')

        i=0
        for node in nodes:
            self.nodes_map[i] = node.attrib
            i = i+1

        i=0
        for edge in edges:
            self.edges_map[i] = edge.attrib
            i = i+1

    def check_type(self, xml_file):
        """Check file type by root name.
        Run proper parsing method"""

        root = xml_file.getroot().tag
        parser = getattr(self, 'parse_%s' % root)
        parser(xml_file)

    def load_file(self):
        """Load file from path given in first sys.argv"""

        try:
            filename = sys.argv[1]
        except IndexError:
            print '\n\
            No path to file given. Enter path as argument when running a program\
            \n'
            sys.exit()

        xml_file = etree.parse(filename)
        self.check_type(xml_file)


if __name__ == '__main__':
    'GraphParser'