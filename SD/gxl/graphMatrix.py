#!/usr/bin/env python


from graphMain import GraphMain
import helpers


class GraphMatrix(GraphMain):

    def load_matrix(self, file_path):

        matrix_file = open(file_path, 'r')
        matrix_file.seek(0)

        data = matrix_file.readlines()
        almost_parsed_data = {}

        i = 0
        for line in data:
            if 'id_list' not in line:
                line = line.strip()
                nodes = line.split(' ')
                self.nodes_map[i] = {}
                self.nodes_map[i]['id'] = nodes[0]
                almost_parsed_data[nodes[0]] = nodes[1:]
                i += 1
            else:
                line = line.strip()
                ids = line.split(' ')
                ids.remove('id_list')

        matrix_file.seek(0)

        parsed_data = {}
        for id in ids:
            parsed_data[id] = {}

        for node, row in almost_parsed_data.items():
            i = 0
            for id in ids:
                parsed_data[node][id] = row[i]
                i = i + 1

        i = 0
        for node, row in parsed_data.items():
            for pair in row.items():
                if '1' in pair and not ({'v1': pair[0], 'v2': node} in self.edges_map.values()):
                    self.edges_map[i] = {'v1': node, 'v2': pair[0]}
                    i = i +1

        self.is_directed = False

        return 'File loaded sucessfully!!'

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

        if self.matrix == {}:
            self.create_matrix()

        size = int(helpers.find_the_longest(self.matrix['id_list']) + 1)

        for key, nodes_names in self.matrix.items():
            if key == 'id_list':
                tmp = (size - len(key)) * ' '
                ugly_matrix_file.write(str(key) + ' ')
                pretty_matrix_file.write(str(key) + tmp)
                for node in nodes_names:
                    tmp = (size - len(str(node))) * ' '
                    ugly_matrix_file.write(str(node) + ' ')
                    pretty_matrix_file.write(str(node) + tmp)
                ugly_matrix_file.write('\n')
                pretty_matrix_file.write('\n')

        for key, nodes_list in self.matrix.items():
            if key is not 'id_list':
                tmp = (size - len(key)) * ' '
                ugly_matrix_file.write(str(key) + ' ')
                pretty_matrix_file.write(str(key) + tmp)
                for single_node in nodes_list:
                    tmp = (size - len(str(single_node))) * ' '
                    ugly_matrix_file.write(str(single_node) + ' ')
                    pretty_matrix_file.write(str(single_node) + tmp)
                ugly_matrix_file.write('\n')
                pretty_matrix_file.write('\n')

        return 'Matrix saved in files: matrix_pretty (nicely formatted) and matrix_ugly (not formatted)'
