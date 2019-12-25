#!/usr/bin/env python

def generate_description_from_cdp():

    import re

    with open('sh_cdp_n_sw1.txt') as cfg:
        file = cfg.readlines()

    grp = {}
    regex = (r'(\S+) +(\S+ \S+).* (\S+ \S+)')
    for line in file:
        if '/' in line:
            r = re.search(regex, line)
            grp[r.group(2)] = 'description Connected to ' + r.group(1) + ' port ' + r.group(3)
    return grp

if __name__ == '__main__':
    print(generate_description_from_cdp())
