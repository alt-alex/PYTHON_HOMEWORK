#!/usr/bin/env python

def get_ip_from_cfg(config):

    import re
    dict = {}
    with open(config) as cfg:
        rgex = ('(?P<intf>interface \S+)''| ip ad\S+ (?P<ip>\S+) (?P<mask>\S+)')
        for line in cfg:
            rslt = re.match(rgex, line)
            if rslt:
                if rslt.group('intf'):
                    intf = rslt.group('intf')
                    ip = mask = ''
                    dict[intf] = {}
                else:
                    ip = rslt.group('ip')
                    mask = rslt.group('mask')
                dict[intf] = (ip, mask)

    rslt_dict = {}
    for l in dict.items():
        if ('', '') not in l:
            rslt_dict[l[0]] = l[1]
    return  rslt_dict

if __name__ == '__main__':
    print(get_ip_from_cfg('config_r1.txt'))
