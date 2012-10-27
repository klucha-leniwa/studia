import argparse
import sys
from graphMethods import GraphMethods

def main():

    parser = argparse.ArgumentParser('create graph object and make some operations')
    parser.add_argument('-f', '--file', action='store')
    parser.add_argument('-a', '--action', action='store', default='return_basics')
    args = parser.parse_args()

    graph = GraphMethods()

    if args.file is not None:
        xml_file = args.file
        graph.load_file(xml_file)
        graph.check_type()

        if args.action is not 'return_basics':
            action = args.action
            func = getattr(graph, action)
            func()

        else:
            func = getattr(graph, args.action)
            func()
            msg = '\n'
            msg += 'File type %s successfully load to xml and graph object was created' % graph.root
            print msg

main()


if __name__ == '__main__':
    main()