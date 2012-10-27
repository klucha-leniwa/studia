from lxml import etree

class GraphMaker():

    def load_file(self, xml_file):
        """Load file from path given args"""
        self.xml_file = etree.parse(xml_file)

    def check_type(self):
        """Check file type by root name.
        Run proper parsing method"""

        self.root = self.xml_file.getroot().tag
        parser = getattr(self, 'parse_%s' % self.root)
        parser()

    def parse_gxl(self):
        """Parse gxl file.
        Collect all edges and nodes with attributes and children"""

        root = self.xml_file.getroot()

        self.nodes_map = {}
        self.edges_map = {}
        self.graph_info = {}

        info = root.find('graph')
        nodes = root.findall('graph/node')
        edges = root.findall('graph/edge')

        for k, v in info.attrib.items():
            self.graph_info[k] = v

        i=0
        for node in nodes:
            self.nodes_map[i] = node.attrib
            i = i+1

        i=0
        for edge in edges:
            self.edges_map[i] = edge.attrib
            i = i+1


if __name__ == '__main__':
    'graphMaker'