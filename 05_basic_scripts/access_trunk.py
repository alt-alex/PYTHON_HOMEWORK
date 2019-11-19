#!/usr/bin/env python

a = input('Введите режим работы интерфейса (access/trunk): ')

b = input('Введите тип и номер интерфейса: ')

c = input('Введите номер влан(ов): ')

access_template = '''
     interface {}
     switchport mode access
     switchport access vlan {}
     switchport nonegotiate
     spanning-tree portfast
     spanning-tree bpduguard enable
     '''

trunk_template = '''
    interface {}
    switchport trunk encapsulation dot1q
    switchport mode trunk
    switchport trunk allowed vlan {}
    '''


access_trunk = {'access': access_template , 'trunk': trunk_template}


print(access_trunk[a].format(b, c))
