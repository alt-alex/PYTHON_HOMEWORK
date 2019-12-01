#!/usr/bin/env python


ignore = ['duplex', 'alias', 'Current configuration']
a,b,c = ignore


with open('config_sw1.txt') as cfg, open('config_sw1_cleared.txt', 'w') as dest:
        for line in cfg:
            if line[:1] == '!':
                continue
            elif a in line:
                continue
            elif b in line:
                continue
            elif c in line:
                continue
            else:
#                print(line)
                dest.write(line)
