#!/usr/bin/env python


def srch_intf_v2(config_filename):
    intf = [line for line in config_filename
    if line.startswith('interface FastEthernet')
    or line.startswith(' switchport a')
    or line.startswith(' switchport trunk ')
    or line.startswith(' duplex')]
    return intf



def get_int_vlan_map2(filename):
    with open(filename) as cfg:
        cfg = cfg.readlines()

    list = srch_intf_v2(cfg)
    searched_line = ''.join(list).split(' duplex auto')
    dict_acs = {}
    dict_trnk = {}

    for line in searched_line:
        if 'trunk' in line:
            split_line = line.split()
            num_trunk = line.split()[-1].split(',')
            num_trunk = [int(i) for i in num_trunk]
            dict_trnk.update({split_line[1]: num_trunk})

        elif 'access' in line:
            split_line = line.split()
            dict_acs.update({split_line[1]: int(split_line[-1])})
        else:
            dict_acs.update({split_line[1]: 1})

    return  dict_acs, dict_trnk



print(get_int_vlan_map2('config_sw2.txt'))
