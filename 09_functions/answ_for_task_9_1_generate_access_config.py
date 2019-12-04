#!/usr/bin/env python

access_config = {
    'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17
    }


access_mode_template = [
    'switchport mode access', 'switchport access vlan',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]



def generate_access_config(intf_vlan_mapping, access_template):
    '''
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access
    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    '''
    rslt = []
    for line in access_config:
        intf = line
        a_t = access_template.copy()
        a_t.insert(0, intf)
        new_oct = a_t[2] + ' ' + str(access_config[intf])
        a_t.pop(2)
        a_t.insert(2, new_oct)
        rslt.append((', '.join(a_t)))
    return rslt





print(generate_access_config(access_config, access_mode_template))

