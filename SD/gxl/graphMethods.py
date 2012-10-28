#!/usr/bin/env python

from graphMaker import GraphMaker
import helpers


class GraphMethods(GraphMaker):

    def return_basics(self):

        for node in self.nodes_map.keys():
            print 'node: ' + str(node)
            for attr in self.nodes_map[node].items():
                print attr

        for edge in self.edges_map.keys():
            print 'edge: ' + str(edge)
            for attr in self.edges_map[edge].items():
                print  attr

    def family_tree(self):

        pairs = []

        if self.is_directed == True and self.root == 'gxl':
            for k, v in self.edges_map.items():
                child = helpers.find_node_by_attribute(self.nodes_map, v['to'])
                parent = helpers.find_node_by_attribute(self.nodes_map, v['from'])
                pairs.append([parent, child])

        return pairs

    def create_matrix(self):

        pairs = self.family_tree()
        ids = helpers.extract_ids(self.nodes_map)