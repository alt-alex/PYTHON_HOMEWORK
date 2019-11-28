#!/usr/bin/env python

with open('config_sw1.txt') as cfg:

    for line in cfg:
        if line[:1] == '!':
            continue
        else:
            print(line.rstrip())

