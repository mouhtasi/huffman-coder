#!/usr/bin/python3

import sys
import heapq
from node import Node

def frequency_dict(filename):
    '''Return dict with frequency and items in file.'''
    freq = {}

    with open(filename, 'r') as file:
        for line in file:
            for item in line:
                if item in freq:
                    freq[item] += 1
                else:
                    freq[item] = 1

    return freq

def dict_to_nodes(freq_dict):
    '''Return list of nodes created from frequency dict.'''
    freq = []

    for item, value in freq_dict.items():
        node = Node(value, item)
        freq.append(node)

    return freq

def sort_nodes(node1, node2):
    '''Return a tuple with the lesser node first and the greater second.'''
    if node1 < node2:
        t = (node1, node2)
    else:
        t = (node2, node1)
    return t

def create_huff_tree(tree):
    '''Return a huffman tree heap.'''
    heapq.heapify(tree)

    while len(tree) > 1:
        node1 = heapq.heappop(tree)
        node2 = heapq.heappop(tree)

        smaller_node, greater_node = sort_nodes(node1, node2)
        child_left, child_right = smaller_node, greater_node

        parent_node = Node(child_left.weight + child_right.weight,
                           child_left.value + child_right.value)
        parent_node.set_children(child_left, child_right)

        heapq.heappush(tree, parent_node)

    return tree


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python3 huff.py <filename>')
        sys.exit(2)
    elif len(sys.argv) > 1:
        filename = sys.argv[1]
        freq_dict = frequency_dict(filename)
        freq_list = dict_to_nodes(freq_dict)
        tree = create_huff_tree(freq_list)
