# encoding:utf-8
class Cluster:
    vec_set = []
    size = 0

    def __init__(self, centroid):
        self.centroid = centroid

    def add_vec(self, vec):
        self.vec_set.append(vec)
        self.size += 1
