#!/usr/bin/python3

import sys
import os
from operator import itemgetter

def frequency_dict(filename):
    '''Read the file and create a dictionary with the read item and its
    frequency.'''
    freq = {}

    with open(filename, 'r') as file:
        for line in file:
            for item in line:
                if item in freq:
                    freq[item] += 1
                else:
                    freq[item] = 1

    return freq

def dict_to_tuples(freq_dict):
    '''Convert frequency dict to a list of tuples.'''
    freq = []

    for item, value in freq_dict.items():
        freq.append((item, value))

    return sorted(freq, key=itemgetter(1))

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python3 huff.py <filename>')
        sys.exit(2)
    elif len(sys.argv) > 1:
        filename = sys.argv[1]
        freq_dict = frequency_dict(filename)
        freq_list = dict_to_tuples(freq_dict)
