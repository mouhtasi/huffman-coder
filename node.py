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
        lt = False
        if self.weight < other.weight:
            lt = True
        elif self.value < other.value:
            lt = True
        return lt

    def __gt__(self, other):
        gt = False
        if self.weight > other.weight:
            gt = True
        elif self.value > other.value:
            gt = True
        return gt

    def __eq__(self, other):
        eq = False
        if self.weight == other.weight:
            eq = True
        elif self.value == other.value:
            eq = True
        return eq

    def __repr__(self):
        return "w[{0}] - v[{1}] -- l[{2}] - r[{3}]".format(self.weight,
                                            self.value, self.left, self.right)
