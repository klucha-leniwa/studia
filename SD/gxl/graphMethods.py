from graphMaker import GraphMaker
import networkx as nx


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

    def create_simple_graph_object(self):

        self.Graph = nx.Graph()

        for k, v in self.nodes_map.items():
            self.Graph.add_node(k, v)