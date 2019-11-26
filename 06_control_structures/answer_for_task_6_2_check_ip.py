#!/usr/bin/env python

ip = input('Entrer ip: ')


a,b,c,d = ip.split('.')


if 0 < int(a) < 224:
    print ('unicast')
elif 223 < int(a) < 240:
    print ('multicast')
elif  int(a) == int(b) == int(c) == int(d) == 255:
    print('broadcast')
elif  int(a) == int(b) == int(c) == int(d) == 0:
    print('unassigned')
else:
    print('unused')
