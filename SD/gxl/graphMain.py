#!/usr/bin/env python
import helpers
from random import choice
import sys


class GraphMain():

    def __init__(self, **kwargs):
        self.is_directed = ''
        self.type = ''
        self.nodes_map = {}
        self.edges_map = {}
        self.graph_info = ''
        self.neighbors = {}
        self.matrix = {}
        self.visited_list = {}
        self.is_integrated = ''
        if 'graph_to_compare' in kwargs.keys():
            self.graph_to_compare = kwargs.pop('graph_to_compare')

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

        if self.is_directed == False:

            for id in ids:
                self.visited_list[id] = {}
                self.visited_list[id]['visited'] = False
            helpers.mark_as_visited(self, id, self.neighbors[id])

            id = choice(ids)

            for pair in self.visited_list.values():
                if False in pair.values():
                    self.is_integrated = False
                else:
                    self.is_integrated = True

        else:
            for id in ids:
                self.visited_list[id] = {}
                self.visited_list[id]['visited'] = False
                self.visited_list[id]['visited_backwards'] = False

            id = choice(ids)

            helpers.mark_as_visited_in_directed(self, id, self.edges_map)

            for pair in self.visited_list.values():
                for val in pair.values():
                    if val == False:
                        self.is_integrated = False
                    else:
                        self.is_integrated = True

        if self.is_integrated:
            return 'Graph is integrated'
        else:
            return 'Graph not integrated'

    def graph_radius(self):

        self.check_integrity()

        if self.is_integrated:
            ids = helpers.extract_ids(self.nodes_map)
            start = choice(ids)
            end = choice(ids)
            sum = 0
            tmp = 0

            paths = {}
            for id in ids:
                paths[id] = {}
                for next_id in ids:
                    paths[id][next_id] = []
            if self.neighbors == {}:
                self.get_neighbors()

            for end in ids:
                for start in ids:
                    paths[start][end] = helpers.find_shortest_path(self, start, end)

            for start, paths_to_nodes in paths.items():
                for path in paths_to_nodes.values():
                    tmp += len(path)
                if sum == 0 or tmp <= sum:
                    if tmp == sum:
                        radius.append(start)
                        sum = tmp
                    elif tmp<sum:
                        sum = tmp
                        radius = []
                        radius.append(start)
                    elif sum == 0:
                        sum = tmp
                tmp = 0

            return "Graph's central vertex('es) is(are) %s" % radius

        else:
            return "Graph is not complete!"


if __name__ == '__main__':
    'GraphMain'