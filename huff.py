#!/usr/bin/python3

import sys
import os

def get_frequency_dict(filename):
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

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python3 huff.py <filename>')
        sys.exit(2)
    elif len(sys.argv) > 1:
        filename = sys.argv[1]
        freq = get_frequency_dict(filename)
