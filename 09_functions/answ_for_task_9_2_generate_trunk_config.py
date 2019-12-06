#!/usr/bin/env python

trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}



def generate_trunk_config(trunk_config, trunk_mode_template):
    rslt = []
    for intf in trunk_config:
        vlan = trunk_config[intf]
        for line in trunk_mode_template:
            if line.startswith('switchport trunk allowed vlan'):
                line_vlan = trunk_mode_template[2] + ' ' + ', '.join([str(elem) for elem in vlan])
                c = [intf, str(trunk_mode_template[0]), str(trunk_mode_template[1]), str(line_vlan)]
                rslt.extend(c)
    return rslt

print(generate_trunk_config(trunk_config, trunk_mode_template)
)
