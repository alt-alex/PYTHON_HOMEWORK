#!/usr/bin/env python

with open('CAM_table.txt') as var_table:
    VT = var_table.readlines()[6:]
    result = {}
    for eachline in VT:
        vlan, mac, *other, intf = eachline.split()
        out_prm = vlan + '\t' + mac + '\t' + intf
        dict = {int(vlan): out_prm}
        result.update(dict)
for prm in sorted (result):
    print(result[prm])
