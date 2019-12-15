#!/usr/bin/env python

R = ['8.8.8.8', '192.168.1.1', '192.168.1.34']

U = ['10.1.1.1-3', '192.168.41.128-192.168.41.132', '192.168.1.2', '192.168.1.35']

def print_ip_table(R, U):
    import tabulate
    d = {'Reachable': R, 'Unreachable': U}
    columns = ['Reachable', 'Unreachable']
    return tabulate.tabulate(d, headers = columns)

if __name__ == '__main__':
    print(print_ip_table(R, U))
