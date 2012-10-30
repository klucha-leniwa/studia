#!/usr/bin/env python
import helpers

class GraphMain():

    def __init__(self):
        self.is_directed = ''
        self.type = ''
        self.nodes_map = ''
        self.edges_map = ''
        self.graph_info = ''
        self.neighbors = ''

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

        if self.is_directed == True:
            for v in self.edges_map.values():
                child = helpers.find_node_by_attribute(self.nodes_map, v['to'])
                parent = helpers.find_node_by_attribute(self.nodes_map, v['from'])
                pairs.append([parent, child])

        return pairs

    def get_neighbors(self):

        self.neighbors = {}
        ids = helpers.extract_ids(self.nodes_map)
        pairs = self.family_tree()

        for id in ids:
            self.neighbors[id] = []

        for pair in pairs:
            self.neighbors[pair[0]['id']].append(pair[1]['id'])
            self.neighbors[pair[1]['id']].append(pair[0]['id'])

        print self.neighbors


if __name__ == '__main__':
    'GraphMain'