#!/usr/bin/env python

class Topology():
    def __init__(self, T):
        self.t = T
        list1 = {}
        for l in self.t.items():
            if l[1] not in list1:
                list1[l[0]] = l[1]
                self.newlst = list1

    def delete_link(self, x, y):
        list2 = {}
        if x in self.t and y in self.t:
            for l in self.t.items():
                if x not in l and y not in l:
                    list2[l[0]] = l[1]
            return list2
        else:
            print('no such device')
