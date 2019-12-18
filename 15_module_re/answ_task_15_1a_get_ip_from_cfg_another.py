#!/usr/bin/env python

def get_ip_from_cfg(config):

    import re
    dict = {}
    with open(config) as cfg:
        rgex = ('(?P<intf>interface \S+)''| ip ad\S+ (?P<ip>\S+) (?P<mask>\S+)')
        rslt = re.finditer(rgex, cfg.read())
        for r in rslt:
            if r.lastgroup == 'intf':
                intf = r.group('intf')
            else:
                ip = r.group('ip')
                mask = r.group('mask')
                dict[intf] = (ip, mask)

    return dict



if __name__ == '__main__':
    print(get_ip_from_cfg('config_r1.txt'))
