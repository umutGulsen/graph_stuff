import numpy as np


class Node:
    def __init__(self, name=None, x=None, y=None, source=False):
        self.name = "node" if name is None else name
        self.label = -1
        self.x = 0 if x is None else x
        self.y = 0 if y is None else y
        self.neighbours = []
        self.index = -1
        self.degree_cent = 0
        self.source = source
        self.pop = int(np.random.random() * 10)
        self.parent = None
        self.children = []
