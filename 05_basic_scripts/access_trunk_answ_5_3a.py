#!/usr/bin/env python

a = input('Введите режим работы интерфейса (access/trunk): ')


a_vlan = 'Введите номер VLAN: '

t_vlan = 'Введите разрешенные VLANы: '

a_t = {'access': a_vlan , 'trunk': t_vlan}

d = input(a_t[a] )


access_template = '''
     switchport mode access
     switchport access vlan {}
     switchport nonegotiate
     spanning-tree portfast
     spanning-tree bpduguard enable
     '''


trunk_template = '''
    switchport trunk encapsulation dot1q
    switchport mode trunk
    switchport trunk allowed vlan {}
    '''
access_trunk = {'access': access_template , 'trunk': trunk_template}
print(access_trunk[a].format(d))
