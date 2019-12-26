#!/usr/bin/env python

def parse_sh_cdp_neighbors(name_of_file):
    import re

    with open(name_of_file) as f:
        file = f.readlines()

    for line in file:
        if '>' in line:
            l = line

    r = re.search(r'(\S+)>', l)
    name_dev = r.group(1)


    dict = {}
    for line in file:
        if '/' in line:
            r = re.search(r'(\S+) +?(\S+ \S+) +?\S+ .*?I +?\S+ +(\S+ \S+)', line)
            neighb = r.group(1)
            loc = r.group(2)
            rmt_int = r.group(3)
            dict[loc] = {neighb: rmt_int}

    rslt_dict = {}
    rslt_dict[name_dev] = dict
    return rslt_dict

if __name__ == '__main__':
    print(parse_sh_cdp_neighbors('sh_cdp_n_sw1.txt'))

