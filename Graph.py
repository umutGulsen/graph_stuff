import matplotlib.pyplot as plt
import numpy as np
import time


class Graph:
    def __init__(self, nodes, arcs, tree=False, sub=False):
        self.nodes = nodes
        self.nodenames = [n.name for n in self.nodes]
        self.index_nodes()
        self.arcs = arcs
        self.adj_list = {}
        self.create_adj_list()
        self.label = -1
        self.node_dict = {}
        self.fill_node_dict()
        self.adj_matrix = []
        if sub:
            self.reset_arcs()

        self.create_adj_matrix()
        self.tree = tree
        self.source_node = None


    def detect_source_node(self):
        for n in self.nodes:
            if n.source:
                self.source_node = n
                print(f"The source node is {n.name}.")
                return

    def index_nodes(self):
        for i, n in enumerate(self.nodes):
            n.index = i

    def draw_graph(self):
        figure = plt.figure(num=None, figsize=(8, 6), dpi=80)
        for node in self.nodes:
            plt.scatter(node.x, node.y, s=500, c="gray")
            plt.annotate(node.name, (node.x, node.y))
        for arc in self.arcs:
            if arc.type_ != "directed":
                plt.plot([arc.from_.x, arc.to.x], [arc.from_.y, arc.to.y], c="blue")
            else:
                plt.arrow(arc.from_.x, arc.from_.y, arc.to.x-arc.from_.x, arc.to.y-arc.from_.y,
                          head_width=.15, head_starts_at_zero=False, length_includes_head=True)
        plt.axis("off")
        plt.show()

    def set_dist(self):
        for arc in self.arcs:
            arc.set_distance_coords()

    def create_adj_list(self):
        for n in self.nodes:
            n.neighbours = []
            for a in self.arcs:
                if a.from_ == n:
                    n.neighbours.append(a.to)
                elif a.to == n and a.type_ == "undirected":
                    n.neighbours.append(a.from_)
            if len(n.neighbours) > 0:
                self.adj_list[n] = n.neighbours

    def label_dfs(self):
        label = 0
        visited = []
        path = []
        not_visited = self.nodes.copy()
        at = not_visited[0]
        visited.append(at)
        not_visited.remove(at)

        #print(f"Start at {at.name}")
        path.append(at)
        while len(not_visited) > 0:
            at.label = label
            choices = []
            for n in at.neighbours:
                if n not in visited:
                    choices.append(n)
            if len(choices) != 0:
                at = choices[0]
                at.label = label
                visited.append(at)
                not_visited.remove(at)
                #print(f"Went to {at.name}")
                path.append(at)
            else:
                path.remove(at)
                if len(path) > 0:
                    at = path[-1]
                    #print(f"Back to {at.name}")
                else:
                    #print(f"Looking for more components...")
                    label += 1
                    if len(not_visited)>0:
                        at = not_visited[0]
                        #print(f"Start anew from {at.name}")
                        visited.append(at)
                        not_visited.remove(at)
                        at.label=label
                    else:
                        return 0
        print("Finished Labeling")

    def shortest_path_bfs(self, start, end, draw):
        print(f"Looking for shortest path between {start.name} and {end.name}...")
        if start.name == end.name:
            print("Start and end node are the same")
            return [True, 0]
        current = start
        queue = [start]
        visited = []
        found = False
        parent_dict = {}
        while len(queue) > 0:
            print(f"Currently in {current.name}")
            queue.remove(current)
            visited.append(current)
            for n in self.adj_list[current]:
                if n not in visited and n not in queue:
                    queue.append(n)
                    parent_dict[n.name] = current.name
                if n == end:
                    found = True
            current = queue[0]
            if found:
                print("Found the target")
                break
        if found:
            step = 0
            next_node = end.name
            path = []
            while next_node != start.name:
                path.append(next_node)
                step += 1
                next_node = parent_dict[next_node]
            path.append(start.name)
            print(f"Found {end.name} in {step} steps.")
            print(f"Path: {[path[len(path)-1-i] for i in range(len(path))]}")

            if draw:
                figure = plt.figure(num=None, figsize=(8, 6), dpi=80)
                for node in self.nodes:
                    plt.scatter(node.x, node.y, s=500, c="gray")
                    plt.annotate(node.name, (node.x, node.y))
                for arc in self.arcs:
                    if arc.from_.name in path and arc.to.name in path:
                        plt.plot([arc.from_.x, arc.to.x], [arc.from_.y, arc.to.y], c="red")
                    else:
                        plt.plot([arc.from_.x, arc.to.x], [arc.from_.y, arc.to.y], c="blue")
                plt.axis("off")
                plt.show()
        else:  # not found
            step = None
            print(f"No path found.")
        return [found, step]

    def fill_node_dict(self):
        for n in self.nodes:
            self.node_dict[n.name] = n

    def create_adj_matrix(self):
        self.adj_matrix = [[0 for nj in self.nodes] for ni in self.nodes]
        for arc in self.arcs:
            self.adj_matrix[arc.from_.index][arc.to.index] = 1
            if arc.type_ == "undirected":
                self.adj_matrix[arc.to.index][arc.from_.index] = 1

    def reset_arcs(self):
        for a in self.arcs:
            a.from_ = self.node_dict[a.from_.name]
            a.to = self.node_dict[a.to.name]

    def check_adjacency_via_matrix(self, f, t):
        if self.adj_matrix[f][t]:
            print(f"{self.nodes[f].name} and {self.nodes[t].name} are connected.")
            return True
        else:
            print(f"{self.nodes[f].name} and {self.nodes[t].name} are not connected.")
            return False

    def assign_degree_centrality(self, draw=False):
        for n in self.nodes:
            n.degree_cent = len(self.adj_list[n])
        if draw:
            figure = plt.figure(num=None, figsize=(8, 6), dpi=80)
            for node in self.nodes:
                plt.scatter(node.x, node.y, s=500, c="gray", alpha=.8)
                plt.annotate(f"{node.name} {round(node.degree_cent, 2)}", (node.x, node.y))
            for arc in self.arcs:
                plt.plot([arc.from_.x, arc.to.x], [arc.from_.y, arc.to.y], c="blue")

            plt.axis("off")
            plt.show()

    def assign_closeness_centrality(self, draw):
        label_count = [0 for n in self.nodes]
        for n in self.nodes:
            label_count[n.label] += 1

        for ni in self.nodes:
            distances = []
            for nj in self.nodes:
                if ni.index != nj.index and ni.label == nj.label:  # not equal and connected
                    f, s = self.shortest_path_bfs(ni, nj, draw=False)
                    if f:
                        distances.append(s)
            ni.closeness_cent = (label_count[ni.label]-1) / sum(distances)

        if draw:
            figure = plt.figure(num=None, figsize=(8, 6), dpi=80)
            for node in self.nodes:
                plt.scatter(node.x, node.y, s=np.max([50,300 + 800*node.closeness_cent]), c="gray", alpha=.8)
                plt.annotate(f"{node.name} {round(node.closeness_cent,2)}", (node.x, node.y))
            for arc in self.arcs:
                plt.plot([arc.from_.x, arc.to.x], [arc.from_.y, arc.to.y], c="blue")
            plt.axis("off")
            plt.show()

    def leaf_sum(self, draw=False):
        sum = 0
        path = [self.source_node]
        while len(path) > 0:
            at = path[0]
            path.remove(at)
            for neighbor in self.adj_list[at]:
                if neighbor in self.adj_list.keys():
                    path.append(neighbor)
                    #print(f"Found {neighbor.name}")
                else:
                    #print("ended", neighbor.name)
                    sum += neighbor.pop
        print(sum)
        if draw:
            figure = plt.figure(num=None, figsize=(8, 6), dpi=80)
            for node in self.nodes:
                plt.scatter(node.x, node.y, s=500, c="gray")
                plt.annotate(f"{node.name} {round(node.pop,2)}", (node.x, node.y))
            for arc in self.arcs:
                if not self.tree:
                    plt.plot([arc.from_.x, arc.to.x], [arc.from_.y, arc.to.y], c="blue")
                else:
                    plt.arrow(arc.from_.x, arc.from_.y, arc.to.x - arc.from_.x, arc.to.y - arc.from_.y,
                              head_width=.15, head_starts_at_zero=False, length_includes_head=True)
            plt.axis("off")
            plt.show()

    def height(self, node):
        if node in self.adj_list.keys():
            return 1+np.max([self.height(neig) for neig in self.adj_list[node]])
        else:
            return 0

    def tree_height(self):
        print(f"Height of the tree is {self.height(self.source_node)}.")

    def associate_children(self, source):
        if source in self.adj_list.keys():
            for child in self.adj_list[source]:
                if child != source.parent:
                    child.parent = source
                    source.children.append(child)
                    self.associate_children(child)

    def root_tree(self, source):
        self.source_node = source
        self.associate_children(source)
        for arc in self.arcs:
            arc.type_ = "directed"
            if arc.from_ in arc.to.children:
                old_from = arc.from_
                old_to = arc.to
                arc.from_ = old_to
                arc.to = old_from
        for n in self.nodes:
            n.neighbours=[]
        self.adj_list={}
        self.create_adj_list()
        self.draw_graph()

    def find_center(self):

        sub_nodes=[]
        sub_arcs=[]
        for n in self.nodes:
            if n.degree_cent > 1:
                sub_nodes.append(n)
        for a in self.arcs:
            if a.from_ in sub_nodes and a.to in sub_nodes:
                sub_arcs.append(a)
        if len(sub_nodes) > 2:
            sub_graph = Graph(sub_nodes, sub_arcs, tree=True, sub=True)
            #time.sleep(1)
            sub_graph.assign_degree_centrality(draw=True)
            sub_graph.find_center()
        else:
            print(f"Center found: {[node.name for node in sub_nodes] }")