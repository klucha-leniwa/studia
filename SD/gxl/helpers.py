#!/usr/bin/env python
import sys

def find_node_by_attribute(nodes, value, attribute='id'):
    for node, attributes_list in nodes.items():
        if attributes_list[attribute] == value:
            return nodes[node]

def extract_ids(nodes):
    ids = []
    for attrs in nodes.values():
        ids.append(attrs['id']);

    return ids

def find_the_longest(strings_list):

    the_longest = 0
    for string in strings_list:
        if the_longest < len(string):
            the_longest = len(string)

    return the_longest

def mark_as_visited(graph, node, node_neighbor_list):
    for neighbor in node_neighbor_list:
        if graph.visited_list[neighbor]['visited'] == False:
            graph.visited_list[neighbor]['visited'] = True
            mark_as_visited(graph, neighbor, graph.neighbors[neighbor])

def mark_as_visited_in_directed(graph, node, edges_list):

    for edge in edges_list.values():

        if edge['from'] == node:
            if graph.visited_list[node]['visited'] == False:
                graph.visited_list[node]['visited'] = True
            if graph.visited_list[edge['to']]['visited'] == False:
                graph.visited_list[edge['to']]['visited'] = True
                mark_as_visited_in_directed(graph, edge['to'], edges_list)

        elif edge['to'] == node:
            if graph.visited_list[node]['visited_backwards'] == False:
                graph.visited_list[node]['visited_backwards'] = True
            if graph.visited_list[edge['from']]['visited_backwards'] == False:
                graph.visited_list[edge['from']]['visited_backwards'] = True
                mark_as_visited_in_directed(graph, edge['from'], edges_list)

