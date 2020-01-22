#!/usr/bin/env python

class Topology():
    def __init__(self, T):
        list1 = {}
        self.t = T
        for l in self.t.items():
            if l[1] not in list1:
                list1[l[0]] = l[1]
        self.tplg = list1

    def __add__(self, other):
        new_topology = self.tplg.copy()
        new_topology.update(other.tplg)
        return  Topology(new_topology)
