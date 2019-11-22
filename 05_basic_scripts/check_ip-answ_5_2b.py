#!/usr/bin/env python

from sys import argv

i = argv[1]

m = argv[2]

#ip = input('Ввидите IP-сети в формате: 0.0.0.0/0: ')

#i,m = ip.split('/')

a, b, c, d = [int(i.split('.')[0]), int(i.split('.')[1]), int(i.split('.')[2]), int(i.split('.')[3])]



ip_bin_prep = '{0:08b}{1:08b}{2:08b}{3:08b}'

ip_binary = ip_bin_prep.format(a,b,c,d)

ip_addr_net_bin = ip_binary[:int(m)] + '0'*(32 - int(m))

a1 = int(ip_addr_net_bin[:8], 2)
b1 = int(ip_addr_net_bin[8:16], 2)
c1 = int(ip_addr_net_bin[16:24], 2)
d1 = int(ip_addr_net_bin[24:], 2)



Network_template = '''
    Network:
    {0:<10}{1:<10}{2:<10}{3:<10}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''
print(Network_template.format(a1, b1, c1, d1))




mask_in_bin = ((int(m)) * '1') + ((32 - int(m)) * '0')

e = mask_in_bin[:8]
f = mask_in_bin[8:16]
g = mask_in_bin[16:24]
h = mask_in_bin[24:]


[e1, f1, g1, h1] = [int(e, 2), int(f, 2), int(g, 2), int(h, 2)]

template_mask = '''
    Mask:
    /{8}
    {0:<10}{1:<10}{2:<10}{3:<10}
    {4:08}  {5:08}  {6:08}  {7:08}
    '''

print(template_mask.format(e1, f1, g1, h1, int(e), int(f), int(g), int(h), int(m)))
