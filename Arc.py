class Arc:
    def __init__(self, from_, to, name, type_=None, weight=None):
        self.name = "arc" if name is None else name
        self.type_ = "undirected" if type_ is None else type_
        self.from_ = from_
        self.to = to
        self.weight = 0 if weight is None else weight
        self.connects = [from_, to]

    def set_distance_coords(self):
        self.weight = ((self.from_.x - self.to.x) ** 2 + (self.from_.y - self.to.y) ** 2) ** .5
