#!/usr/bin/env python
with open('CAM_table.txt') as cfg:
    c = cfg.readlines()[6:]
    for line in c:
        a = line.split()[:2]
        b = line.split()[3]
        a.append(b)
        print(a)

