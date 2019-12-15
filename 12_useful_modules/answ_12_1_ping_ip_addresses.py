#!/usr/bin/env python

import subprocess

def host_line(x):
    hostline = []
    for i in range(1, x):
        l = '192.168.1.' + str(i)
        hostline.append(l)
    return hostline



def ping_ip_addresses(l):
    reach_hst = []
    unreach_hst = []
    for host in l:
        rslt = subprocess.run(['fping', '-c', '1', '-t', '500', '-s', host], stderr=subprocess.PIPE)
        if rslt.returncode == 0:
            reach_hst.append(host)
        else:
            unreach_hst.append(host)
    output = (reach_hst, unreach_hst)
    return output



if __name__ == '__main__':

	l = host_line(51)
	print(ping_ip_addresses(l))
