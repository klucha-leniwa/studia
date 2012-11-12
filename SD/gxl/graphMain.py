#!/usr/bin/env python
import helpers
from random import choice

class GraphMain():

    def __init__(self):
        self.is_directed = ''
        self.type = ''
        self.nodes_map = {}
        self.edges_map = {}
        self.graph_info = ''
        self.neighbors = {}
        self.matrix = {}
        self.visited_list = {}
        self.is_integrated = ''

    def return_basics(self):

        for node in self.nodes_map.keys():
            print 'node: ' + str(node)
            for attr in self.nodes_map[node].items():
                print attr

        for edge in self.edges_map.keys():
            print 'edge: ' + str(edge)
            for attr in self.edges_map[edge].items():
                print attr

        return self.nodes_map, self.edges_map

    def family_tree(self):

        pairs = []

        if self.is_directed == True:
            for v in self.edges_map.values():
                child = helpers.find_node_by_attribute(self.nodes_map, v['to'])
                parent = helpers.find_node_by_attribute(self.nodes_map, v['from'])
                pairs.append([parent, child])

        else:
            for edge in self.edges_map.values():
                pairs.append([{'id':edge['v1']}, {'id':edge['v2']}])

        return pairs

    def get_neighbors(self):

        ids = helpers.extract_ids(self.nodes_map)
        pairs = self.family_tree()

        for id in ids:
            self.neighbors[id] = []

        for pair in pairs:
            self.neighbors[pair[0]['id']].append(pair[1]['id'])
            self.neighbors[pair[1]['id']].append(pair[0]['id'])

        return self.neighbors

    def check_integrity(self):

        if self.neighbors == {}:
            self.get_neighbors()
        ids = helpers.extract_ids(self.nodes_map)
        for id in ids:
            self.visited_list[id] = {}
            self.visited_list[id]['visited'] = False

        id = choice(ids)

        helpers.mark_as_visited(self, id, self.neighbors[id])

        for pair in self.visited_list.values():
            if False in pair.values():
                self.is_integrated = False
            else:
                self.is_integrated = True

        if self.is_integrated:
            return 'Graph is integrated'
        else:
            return 'Graph not integrated'


if __name__ == '__main__':
    'GraphMain'