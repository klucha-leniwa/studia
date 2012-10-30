#!/usr/bin/env python

import argparse
import sys
from graphGXL import GraphGXL

def main():

    parser = argparse.ArgumentParser('create graph object and make some operations')
    parser.add_argument('-x', '--xml', action='store')
    parser.add_argument('-a', '--action', action='store', default='return_basics')
    args = parser.parse_args()

    if args.xml is not None:
        xml_file = args.xml
        graph = GraphGXL()
        graph.load_file(xml_file)

        func = getattr(graph, args.action)
        func()
        msg = '\n'
        msg += 'File type %s successfully load to xml and graph object was created' % graph.type
        print msg

    elif args.xml == None and args.action=='return_basics':
        msg = "Runner creates graph object and perform given methods on it \n"
        msg += "Basic usage: \n"
        msg += "    -x | --xml 'file_name' - loads graph structure from xml/gxl file \n"
        msg += "    -a | --action 'action_name' - performs action on previously created graph \n"
        msg += "    -h | --help - prints this message \n"

        print msg

        sys.exit()


if __name__ == '__main__':
    main()