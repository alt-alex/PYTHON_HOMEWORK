#!/usr/bin/env python

def create_network_map(*args):
    rslt_cfg = ''
    newline = []
    value_key = []
    dict = {}

    for i in args:
       with open(i) as cfg:
           cfg_file = cfg.read()
           rslt_cfg = rslt_cfg + cfg_file



    for line in  rslt_cfg.split('\n'):
        if '>' in line or 'Eth' in line:
            newline.append(line)


    for l in newline:

            if '>' in l:
                d_k = l[:2]
            else:
                l = l.split()
                rslt_local = l[1] + l[2]
                rslt_outer = l[-2] + l[-1]
                dict.update({(d_k, rslt_local): (l[0], rslt_outer)})


    dict_rslt = {}
    for lines in dict.items():
       if lines[1] not in dict_rslt.keys():
            dict_rslt.update({lines[0]: lines[1]})
    dict_rslt



    return dict_rslt
if __name__ == '__main__':

    print(create_network_map('sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt', 'sh_cdp_n_sw1.txt'))
