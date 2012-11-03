#!/usr/bin/env python

import argparse
import sys
from graphMatrix import GraphMatrix
from graphMain import GraphMain

def main():

    parser = argparse.ArgumentParser('create graph object and make some operations')
    parser.add_argument('-i', '--input', action='store')
    parser.add_argument('-o', '--output', action='store')
    parser.add_argument('-f', '--file', action='store')
    parser.add_argument('-a', '--action', action='store', default='return_basics')
    args = parser.parse_args()


    if args.file is not None:

        if args.input == 'gxl' and args.output == None:
            xml_file = args.file
            try:
                from graphGXL import GraphGXL
            except ImportError:
                "Importing GraphGXL class failed, but don't panic"
            graph = GraphGXL()
            graph.load_file(xml_file)

            func = getattr(graph, args.action)
            func()
            msg = '\n'
            msg += 'File type %s successfully load to xml and graph object was created' % graph.type
            print msg

        elif args.input == 'matrix':
            matrix_file = args.file
            try:
                from graphMatrix import GraphMatrix
            except ImportError:
                "Importing GraphMatrix class failed, but don't panic"
            graph = GraphMatrix()
            graph.load_file(matrix_file)

            func = getattr(graph, args.action)
            func()
            msg = '\n'
            msg += 'Matrix file load successfully and graph object was created'
            print msg

        elif args.input == 'gxl' and args.output == 'matrix':
            xml_file = args.file
            try:
                from graphGXL import GraphGXL
                from graphMatrix import GraphMatrix
            except ImportError:
                "Importing GraphGXL and GraphMatrix classes failed, but don't panic"
            graph = GraphMatrix()
            graph.load_file(xml_file)

            func = getattr(graph, args.action)
            func()

        else:
            msg = '\n'
            msg += 'You have to pass type of input file \n'
            msg += '    For instance: -f file_name -i gxl \n'
            print msg
            sys.exit

    elif args.file == None and args.action =='return_basics':
        msg = "Runner creates graph object and perform given methods on it \n"
        msg += "Basic usage: \n"
        msg += "    -x | --xml 'file_name' - loads graph structure from xml/gxl file \n"
        msg += "    -a | --action 'action_name' - performs action on previously created graph \n"
        msg += "    -h | --help - prints this message \n"

        print msg

        sys.exit()


if __name__ == '__main__':
    main()