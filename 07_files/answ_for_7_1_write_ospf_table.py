#!/usr/bin/env python

output_templ = '''
    Protocol:            {}
    Prefix:              {}
    AD/Metric:           {}
    Next-Hop:            {}
    Last update:         {}
    Outbound Interface:  {}
    '''

with open('ospf.txt', 'r') as ospf:
    ospf_route = ospf.readlines()


for list in ospf_route:
    list = list.split()
    a = list[0].replace('O', 'OSPF')
    b = list[1]
    c = list[2].strip('[]')
    d = list[4].rstrip(',')
    e = list[5].rstrip(',')
    f = list[6]
    print(output_templ.format(a,b,c,d,e,f))
