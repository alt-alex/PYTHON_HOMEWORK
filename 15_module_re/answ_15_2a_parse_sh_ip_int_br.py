#!/usr/bin/env python

def parse_sh_ip_int_br():
    headers = ['interface', 'address', 'status', 'protocol']
    import re
    with open('sh_ip_int_br.txt') as cfg:
        file = cfg.readlines()
        list_dict = []
        rslt = {}
        for l in file:
            r = re.search(r'(\S+) +(\S+) .*(u\S+|d\S+) .*(u\S+|d\S+)', l)
            if r:
                for i in range(5):
                    rslt[headers[(i-1)]] = r.group(i)
                a = rslt.copy()
                list_dict.append(a)
    return list_dict

if __name__ == '__main__':
    print(parse_sh_ip_int_br())
