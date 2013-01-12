#!/usr/bin/env python

import argparse
import sys
from graphProxy import GraphProxy
from graphComparer import GraphComparer

def main():

    parser = argparse.ArgumentParser('create graph object and make some operations')
    parser.add_argument('-i', '--input', action='store')
    parser.add_argument('-f', '--file', action='store')
    parser.add_argument('-a', '--action', action='store', default='return_basics')
    parser.add_argument('-f2', '--file2', action='store')
    args = parser.parse_args()


    if args.file is not None:

        if args.input == None:
            msg = '\n'
            msg += 'You have to pass type of input file \n'
            msg += '    For instance: -f file_name -i gxl \n'
            print msg
            sys.exit()

        if args.action == 'check_iso' and args.file2 is None:
            msg = '\n'
            msg += 'If You want to check integrity please pass two input files \n'
            msg += '\t For instance: -f graph_one_file_name -f2 graph_two_file_name \n'
            msg += 'Please remeber that both files must be same type (gxl or matrix) \n'
            print msg
            sys.exit()

        if args.action == 'check_iso' and args.file2 is not None:        

            graph_one = GraphProxy()
            loader = getattr(graph_one, 'load_%s' % args.input)
            loader(args.file)

            graph_two = GraphProxy()
            loader = getattr(graph_two, 'load_%s' % args.input)
            loader(args.file2)

            graph = GraphComparer(graph_one, graph_two)

        if args.action != 'check_iso':
            graph = GraphProxy()

            loader = getattr(graph, 'load_%s' % args.input)
            loader(args.file)

        func = getattr(graph, args.action)
        returned_data = func()
        msg = '\n'
        msg += 'File successfully loaded!'
        msg += '\nResult of function: \n \t' + str(returned_data)
        msg += '\n'
        print msg


    elif args.file == None and args.action =='return_basics':
        msg = "Runner creates graph object and perform given methods on it \n"
        msg += "Basic usage: \n"
        msg += "    -i | --input 'file_type' - type of input file for example: gxl \n"
        msg += "    -a | --action 'action_name' - action you want to perform on graph for examle: get_neighbors \n"
        msg += "    -f | --file 'file_name' - path to file \n"
        msg += "    -h | --help - prints this message \n"

        print msg

        sys.exit()


if __name__ == '__main__':
    main()