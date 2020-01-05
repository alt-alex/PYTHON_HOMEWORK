#!/usr/bin/env python

def get_data(vlan = None, num = None, *args):
    import sqlite3
    con = sqlite3.connect('dhcp_snooping.db')
    if vlan == None and num == None:
        for row in con.execute('select * from dhcp'):
            print(row)
    elif vlan == None or num == None or  args:
        print('Cкрипт поддерживает только два или ноль аргументов.')
    else:
        for row in con.execute("select * from dhcp where {} = '{}'".format(vlan, num)):
            print(row)

if __name__ == '__main__':
    a = input('введите данные №1: ')
    b = input('введите данные №2: ')
    if a  and b:
        get_data(a, b)
    else:
        get_data()
