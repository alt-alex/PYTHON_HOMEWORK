#!/usr/bin/env python

ip = input('Ввидите IP-сети в формате: 10.1.1.0/24: ')

i,m = ip.split('/')

a, b, c, d = [int(i.split('.')[0]), int(i.split('.')[1]), int(i.split('.')[2]), int(i.split('.')[3])]

template_IP = '''
    Network:
    {0:<10}{1:<10}{2:<10}{3:<10}
    {0:08b}  {1:08b}  {2:08b}  {3:08b}
    '''

mask_in_bin = ((int(m)) * '1') + ((32 - int(m)) * '0')

e = mask_in_bin[:8]
f = mask_in_bin[8:16]
g = mask_in_bin[16:24]
h = mask_in_bin[24:]

template_mask = '''
   subnet mask:
   {0:<10}{1:<10}{2:<10}{3:<10}
   {4:08}  {5:08}  {6:08}  {7:08}
   '''

print(template_IP.format(a, b, c, d))

print(template_mask.format(int(e, 2), int(f, 2), int(g, 2), int(h, 2), int(e), int(f), int(g), int(h), int(h)))

input ('press enter')
