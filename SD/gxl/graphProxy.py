from graphGXL import GraphGXL
from graphMatrix import GraphMatrix


class GraphProxy(GraphGXL, GraphMatrix):
    def hello(self):
        return 'hello'