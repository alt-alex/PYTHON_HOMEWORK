# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'




ANSWER IS:



output_templ = '''
    ...: Protocol:            {}
    ...: Prefix:              {}
    ...: AD/Metric:           {}
    ...: Next-Hop:            {}
    ...: Last update:         {}
    ...: Outbound Interface:  {}
    ...: '''


ospf_route = ospf_route.split()

a = ospf_route[0].replace('O', 'OSPF')

b = ospf_route[1]

c = ospf_route[2].strip('[]')

d = ospf_route[4].rstrip(',')

e = ospf_route[5].rstrip(',')

f = ospf_route[6]

print(output_templ.format(a,b,c,d,e,f))
