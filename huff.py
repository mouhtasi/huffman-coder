#!/usr/bin/python3

import sys
import heapq
from node import Node
import array

def frequency_dict(filename, peof):
    '''Return dict with frequency and items in file.'''
    freq = {}

    with open(filename, 'r') as file:
        for line in file:
            for item in line:
                if item in freq:
                    freq[item] += 1
                else:
                    freq[item] = 1

    freq = add_pseudo_eof(freq, peof)
    return freq

def dict_to_nodes(freq_dict):
    '''Return list of nodes created from frequency dict.'''
    freq = []

    for item, value in freq_dict.items():
        node = Node(value, item)
        freq.append(node)

    return freq

def add_pseudo_eof(freq_dict, peof):
    '''Return the frequency dict with the pseudo end-of-file char added.'''
    freq_dict[peof] = 1
    return freq_dict

def create_huff_tree(tree):
    '''Return a huffman tree heap.'''
    heapq.heapify(tree)

    while len(tree) > 1:
        node1 = heapq.heappop(tree)
        node2 = heapq.heappop(tree)

        child_left, child_right = node1, node2

        parent_node = Node(child_left.weight + child_right.weight,
                           child_left.value + child_right.value)
        parent_node.set_children(child_left, child_right)

        heapq.heappush(tree, parent_node)

    return tree

def get_leaves(node, leaves, prefix=''):
    if not node.left and not node.right: # leaf
        leaves[node.value] = prefix
    else:
        get_leaves(node.left, leaves, prefix + '0')
        get_leaves(node.right, leaves, prefix + '1')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python3 huff.py <filename>')
        sys.exit(2)
    elif len(sys.argv) > 1:
        filename = sys.argv[1]
        peof = '■'

        freq_dict = frequency_dict(filename, peof)
        freq_list = dict_to_nodes(freq_dict)
        tree = create_huff_tree(freq_list)
        leave = {}
        get_leaves(heapq.heappop(tree), leave)
        #print (sorted(list(leave.items())))
