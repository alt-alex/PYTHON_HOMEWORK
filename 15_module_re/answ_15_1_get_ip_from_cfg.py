#!/usr/bin/env python

def get_ip_from_cfg(config):
    import re
    rslt = []
    with open(config) as cfg:
        for line in cfg:
            regex = re.search(r' ip address (\S+) (\S+)', line)
            if regex:
                ip_mask = (regex.group(1), regex.group(2))
                rslt.append(ip_mask)
        return rslt

if __name__ == '__main__':
    print(get_ip_from_cfg('config_r1.txt'))
