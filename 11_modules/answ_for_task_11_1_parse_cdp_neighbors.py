#!/usr/bin/env python



with open('sh_cdp_n_sw1.txt') as cfg:
    cdp_file = cfg.read()


def parse_cdp_neighbors(cdp_file):

    with open('sh_cdp_n_sw1.txt') as cfg:
        cdp_file = cfg.read()

    newline = []
    for line in  cdp_file.split('\n'):
        if 'Eth' in line:
            newline.append(line)

    dict = {}

    for l in newline:
        l = l.split()
        rslt_local = l[1] + l[2]
        rslt_outer = l[-2] + l[-1]
        dict.update({('sw1', rslt_local): (l[0], rslt_outer)})
    return dict


if __name__ == '__main__':

    print(parse_cdp_neighbors(cdp_file))
