a = input('Введите режим работы интерфейса (access/trunk): ')

b = input('Введите тип и номер интерфейса: ')

c = input('Введите номер влан(ов): ')




access_template = '''
    'interface {}',
     'switchport mode access', 'switchport access vlan {}',
     'switchport nonegotiate', 'spanning-tree portfast',
     'spanning-tree bpduguard enable'
     '''

print(access_template.format(b, c))



 trunk_template = '''
    'interface{}',
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
    '''

print(trunk_template(b,c))
