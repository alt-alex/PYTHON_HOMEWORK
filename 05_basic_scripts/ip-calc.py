#!/usr/bin/env python3

ip = input('Ввидите IP-сети в формате: 0.0.0.0/0: ')

i,m = ip.split('/')

a, b, c, d = [int(i.split('.')[0]), int(i.split('.')[1]), int(i.split('.')[2]), int(i.split('.')[3])]



ip_bin_prep = '{0:08b}{1:08b}{2:08b}{3:08b}'

print ('\n\n\nIP address: ', i)





ip_binary = ip_bin_prep.format(a,b,c,d)

print ('IP address in binary: ', ip_binary)




ip_addr_net_bin = ip_binary[:int(m)] + '0'*(32 - int(m))

a1 = ip_addr_net_bin[:8]
b1 = ip_addr_net_bin[8:16]
c1 = ip_addr_net_bin[16:24]
d1 = ip_addr_net_bin[24:]

ip_subnet = str(int(a1, 2)) + '.' + str(int(b1, 2)) + '.' + str(int(c1, 2)) + '.' + str(int(d1, 2))

print('Network Address: ', ip_subnet)




ip_addr_brd_bin = ip_binary[:int(m)] + '1'*(32 - int(m))

a2 = ip_addr_brd_bin[:8]
b2 = ip_addr_brd_bin[8:16]
c2 = ip_addr_brd_bin[16:24]
d2 = ip_addr_brd_bin[24:]

ip_addr_brd_bin = str(int(a2, 2)) + '.' + str(int(b2, 2)) + '.' + str(int(c2, 2)) + '.' + str(int(d2, 2))

print('Broadcast Address: ', ip_addr_brd_bin)




first_valid_ip = str(int(a1, 2)) + '.' + str(int(b1, 2)) + '.' + str(int(c1, 2)) + '.' + str(int(d1, 2) + 1)

last_valit_ip  = str(int(a2, 2)) + '.' + str(int(b2, 2)) + '.' + str(int(c2, 2)) + '.' + str(int(d2, 2) - 1)


print('Usable Host Range: ', first_valid_ip, ' - ', last_valit_ip)




usable_hosts = 2 ** (32 - int(m)) - 2

print('Number of usable hosts: ', usable_hosts)




mask_in_bin = ((int(m)) * '1') + ((32 - int(m)) * '0')

e = mask_in_bin[:8]
f = mask_in_bin[8:16]
g = mask_in_bin[16:24]
h = mask_in_bin[24:]

template_mask_in_dec = '''Subnet mask: {0}.{1}.{2}.{3}'''
print(template_mask_in_dec.format(int(e, 2), int(f, 2), int(g, 2), int(h, 2)))


template_mask_in_bin = '''Subnet mask in binary: {0:08}{1:08}{2:08}{3:08}'''
print(template_mask_in_bin.format(int(e), int(f), int(g), int(h)))

wildcard_mask = '''{0:08}{1:08}{2:08}{3:08}'''
print('Wildcard_mask: ', wildcard_mask.format(int(e), int(f), int(g), int(h))[::-1])




input ('\n\npress enter')
