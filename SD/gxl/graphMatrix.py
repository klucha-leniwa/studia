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
        """Create matrix and save to file matrix.txt"""

        ids = helpers.extract_ids(self.nodes_map)
        size = helpers.find_the_longest(ids) + 1

        for id in ids:
            self.matrix[id] = []
            for neigbors in self.neighbors.values():
                if id in neigbors:
                    self.matrix[id].append(1)
                else:
                    self.matrix[id].append(0)

        print self.matrix
        sys.exit()

        for k, v in self.matrix.items():
            tmp = size - len(k)
            row = ' '*tmp + '%s' % str(k)
            for value in v:
                tmp = size - len(str(value))
                row += ' ' *tmp + '%s' % str(value)
            nice_matrix.append(row)

        for k, v in self.matrix.items():
            self.matrix[k] = []
            for value in v:
                self.matrix[k].append(str(value) + ' ')

        return self.matrix

    def save_matrix(self):
        self.get_neighbors()
        self.matrix = {}
        nice_matrix = []

        matrix_file = open('matrix_1.txt', 'w')
        matrix_file_ugly = open('matrix_ugly_1.txt', 'w')
        ids = helpers.extract_ids(self.nodes_map)
        size = helpers.find_the_longest(ids) + 1

        row = ' '*(size)
        for id in ids:
            tmp = size - len(id)
            row += ' '*tmp + '%s' % str(id)

        nice_matrix.append(row)

        for id in ids:
            self.matrix[id] = []
            for neigbors in self.neighbors.values():
                if id in neigbors:
                    self.matrix[id].append(1)
                else:
                    self.matrix[id].append(0)

        for k, v in self.matrix.items():
            tmp = size - len(k)
            row = ' '*tmp + '%s' % str(k)
            for value in v:
                tmp = size - len(str(value))
                row += ' ' *tmp + '%s' % str(value)
            nice_matrix.append(row)

        for row in nice_matrix:
            matrix_file.write(row + '\n')
        for k, v in self.matrix.items():
            matrix_file_ugly.write(k + ' ')
            self.matrix[k] = []
            for value in v:
                matrix_file_ugly.write(str(value) + ' ')
                self.matrix[k].append(str(value) + ' ')
            matrix_file_ugly.write('\n')

        return self.matrix

    def parse_matrix(self):

        self.create_matrix()

        for i in range(len(self.matrix.keys())):
            self.nodes_map[i] = {'id' : self.matrix.keys()[i]}

        return self.nodes_map
