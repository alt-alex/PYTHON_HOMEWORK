#!/usr/bin/env python

prerslt = []
with open('CAM_table.txt') as cam:
    for line in cam:
        if ' ' in line:
            if line[1].isdigit():
                vlan, mac, _, intf = line.split()
                prerslt.append([int(vlan), mac,intf])
                rslt = sorted(prerslt)
    for l in rslt:
        v, m, i = (l)
        editcam = '{}\t{}\t{}'.format(v, m, i)
        print(editcam)

