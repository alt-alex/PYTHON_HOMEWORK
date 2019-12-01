#!/usr/bin/env python

from sys import argv
input = argv[1]
output = argv[2]



ignore = ['duplex', 'alias', 'Current configuration']
a,b,c = ignore
with open(input) as cfg, open(output, 'w') as dest:
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
