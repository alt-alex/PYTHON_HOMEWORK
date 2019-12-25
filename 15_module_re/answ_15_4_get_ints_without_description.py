#!/usr/bin/env python


def get_ints_without_description():
    with open('config_r1.txt') as cfg:
        file = cfg.read()


    import re

    list_intf = re.finditer('\n(interface \S+).*?!', file, re.DOTALL)

    rslt_list = []
    for line in list_intf:
        line = line[0]
        if 'descr' not in line:
            rslt = re.search(r'(interface \S+)', line)
            r = rslt.group()
            rslt_list.append(r)
    return rslt_list

if __name__ == '__main__':
    print(get_ints_without_description())
