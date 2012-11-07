#!/usr/bin/env python

from graphMain import GraphMain
from graphGXL import GraphGXL
import helpers
import sys

class GraphMatrix(GraphMain, GraphGXL):

    def create_matrix(self):
        """Create matrix and save to file matrix.txt"""

        self.get_neighbors()
        self.matrix = {}
        nice_matrix = []

        matrix_file = open('matrix.txt', 'w')
        matrix_file_ugly = open('matrix_ugly.txt', 'w')
        ids = helpers.extract_ids(self.nodes_map)
        size = helpers.find_the_longest(ids) + 1

        row = ' '*(size)
        for id in ids:
            tmp = size - len(id)
            row += ' '*tmp + '%s' % str(id)

        nice_matrix.append(row)

        for id in ids:
            self.matrix[id] = []
            for node, neigbors in self.neighbors.items():
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
            for value in v:
                matrix_file_ugly.write(str(value) + ' ')
            matrix_file_ugly.write('\n')

    def load_matrix(self, file_path):
        matrix_file = open(file_path, 'r')
        matrix_file.seek(0)
        ids = []
        self.neighbors = {}

        data = matrix_file.readlines()[1:]
        almost_neighbors = {}
        for i in range(len(data)):
            data[i] = data[i].strip()
            data[i] = data[i].split(' ')
            almost_neighbors[data[i].pop(0)] = data[i]

        for k in almost_neighbors.keys():
            self.neighbors[k] = []

        ids = almost_neighbors.keys()
        for k, data in almost_neighbors.items():
            for i in range(len(ids)):
                self.neighbors[k].append((ids[i], data[i]))

