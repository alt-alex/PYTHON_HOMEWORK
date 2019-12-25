#!/usr/bin/env python

def parse_sh_ip_int_br():
    import re
    with open('sh_ip_int_br.txt') as cfg:
        file = cfg.readlines()
        rslt = []
        for l in file:
            r = re.search(r'(\S+) +(\S+) .*(u\S+|d\S+) .*(u\S+|d\S+)', l)
            if r:
                rslt.append(r.groups())
    return rslt


if __name__ == '__main__':
    print(parse_sh_ip_int_br())
