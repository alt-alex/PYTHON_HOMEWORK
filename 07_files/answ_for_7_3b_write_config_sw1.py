#!/usr/bin/env python

entvl = input('enter VLAN:   ')
with open('CAM_table.txt') as cam:
    for line in cam:
        if ' ' in line:
            if line[1].isdigit():
                vlan, mac, _, intf = line.split()
                if entvl == vlan:
                    print(vlan, mac,intf)

