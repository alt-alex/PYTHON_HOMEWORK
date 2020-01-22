#!/usr/bin/env python

class Topology():
    def __init__(self, T):
        list1 = {}
        self.t = T
        for l in self.t.items():
            if l[1] not in list1:
                list1[l[0]] = l[1]
        self.tplg = list1
