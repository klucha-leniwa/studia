#!/usr/bin/env python


def find_node_by_attribute(nodes, value, attribute='id'):
    for node, attributes_list in nodes.items():
        if attributes_list[attribute] == value:
            return nodes[node]

def extract_ids(nodes):
    ids = []
    for attrs in nodes.values():
        ids.append(attrs['id']);

    return ids