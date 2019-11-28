#!/usr/bin/env python

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]



trunk = {
        '0/1': ['add', '10', '20', '30', '40'],
        '0/2': ['only', '11', '30', '100', '200', '300'],
        '0/4': ['del', '17']
    }


for intf, vlan in trunk.items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if vlan[0] == 'add':
                print(' switchport trunk allowed vlan add', ','.join(vlan[1:]))
            elif vlan[0] == 'del':
                print(' switchport trunk allowed', ','.join(vlan[1:]))
            else:
                print(' switchport trunk allowed vlan remove', ','.join(vlan[1:]))
        else:
            print(' {}'.format(command))

