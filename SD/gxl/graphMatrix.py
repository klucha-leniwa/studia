#!/usr/bin/env python

from graphMain import GraphMain
from graphGXL import GraphGXL
import helpers
import sys


class GraphMatrix(GraphMain, GraphGXL):

    def load_matrix(self, file_path):
        matrix_file = open(file_path, 'r')
        matrix_file.seek(0)
        self.neighbors = {}

        data = matrix_file.readlines()
        almost_neighbors = {}
        for i in range(len(data)):
            data[i] = data[i].strip()
            data[i] = data[i].split(' ')
            almost_neighbors[data[i].pop(0)] = data[i]

        for k in almost_neighbors.keys():
            self.neighbors[k] = []

        ids = almost_neighbors.keys()

        for i in range(len(ids)):
            j = 0
            for k in almost_neighbors[ids[i]]:
                if k == '1':
                    self.neighbors[ids[i]].append(ids[j])
                j = j+1

        print self.neighbors

        sys.exit()
        for k, data in almost_neighbors.items():
            for i in range(len(ids)):
                self.nodes_map[i] = {'id': ids[i]}

        i = 0
        for k, v in self.neighbors.items():
            self.edges_map[i] = []
            for node in v:
                if '1' in node:
                    self.edges_map[i] = {'v1': k, 'v2' : node[0]}
            i = i+1

    def create_matrix(self):
        """Create matrix"""

        ids = helpers.extract_ids(self.nodes_map)
        if self.neighbors == {}:
            self.get_neighbors()

        for id in ids:
            self.matrix[id] = []
        for k, v in self.neighbors.items():
            for id in ids:
                if id in v:
                    self.matrix[k].append(1)
                else:
                    self.matrix[k].append(0)

        self.matrix['id_list'] = ids

        return self.matrix

    def save_matrix(self):

        pretty_matrix_file = open('matrix_pretty.txt', 'w')
        ugly_matrix_file = open('matrix_ugly.txt', 'w')
        pretty_matrix = []
        ugly_matrix = []


        if self.matrix == {}:
            self.create_matrix()

        size = helpers.find_the_longest(self.matrix['ids']) + 1


