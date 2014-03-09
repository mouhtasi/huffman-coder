class Node(object):
    '''A class representing a node. The weight represents the frequency and the
    value represents the item.'''
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.left = None
        self.right = None

    def set_children(self, left_node, right_node):
        self.left = left_node
        self.right = right_node

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.weight == other.weight

    def __repr__(self):
        return "w[{0}] - v[{1}] -- l[{2}] - r[{3}]".format(self.weight,
                                            self.value, self.left, self.right)
