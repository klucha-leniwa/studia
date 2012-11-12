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
