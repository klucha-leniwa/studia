import helpers
import networkx as nx

class GraphComparer():
	def __init__(self, graph_one, graph_two):
		self.graph_one = graph_one
		self.graph_two = graph_two

	def check_iso(self):
		if len(self.graph_one.nodes_map) != len(self.graph_two.nodes_map):
			return 'Graphs are not isomorphic - numbers of nodes are not equal'
		if len(self.graph_one.edges_map) != len(self.graph_two.edges_map):
			return 'Graphs are not isomorphic - numbers of edges are not equal'
		neighbors_list_one = self.graph_one.get_neighbors()
		neighbors_list_two = self.graph_two.get_neighbors()

		G1 = nx.Graph()
		G2 = nx.Graph()

		for nodes in self.graph_one.nodes_map.values():
			for k, v in nodes.items():
				G1.add_node(v, id=v) 

		for nodes in self.graph_two.nodes_map.values():
			for k, v in nodes.items():
				G2.add_node(v, id=v)

		for edges in self.graph_one.edges_map.values():
			G1.add_edge(edges['v1'], edges['v2'])


		for edges in self.graph_two.edges_map.values():
			G2.add_edge(edges['v1'], edges['v2'])

		result =  nx.is_isomorphic(G1, G2)

		if result:
			return 'Congrats! Graphs are isomorphic!'
		else:
			return 'Too bad... Graphs are not isomorphic...'