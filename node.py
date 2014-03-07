class Node(object):
    '''A class representing a node. The weight represents the frequency and the
    value represents the item.'''
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def set_children(self, left_node, right_node):
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value
