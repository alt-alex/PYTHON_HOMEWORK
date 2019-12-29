#!/usr/bin/env python

import sqlite3
import os

db_exists = os.path.exists('dhcp_snooping.db')
conn = sqlite3.connect('dhcp_snooping.db')

def create_db():
    with open('dhcp_snooping_schema.sql', 'r') as f:
        schema = f.read()

    if not db_exists:
        print('Creating schema...')
        conn.executescript(schema)
        print('Создаю базу данных...')
    else:
        print('База данных существует')


def find_dhcp():
    import glob
    import re
    list_dhcp = glob.glob('sw*dhcp*')

    dhcp_output = []
    for file in list_dhcp:
        with open(file) as f:
            devname = re.search(r'(\S*?)_', file)
            for line in f:
                if '/' in line:
                    r = re.search(r'(\S+) +?(\S+) +?\S+ +?\S+ +?(\d+) +?(\S+)', line)
                    row = [r.group(1), r.group(2), r.group(3), r.group(4), devname.group(1)]
                    dhcp_output.append(row)
    return  dhcp_output


def find_dev():
    dev_output = []
    import yaml
    with open('switches.yml') as f:
        file = yaml.safe_load(f)
        dictlist = []
        for l in file.values():
            for key, value in l.items():
                temp = [key,value]
                dictlist.append(temp)
    return dictlist


def add_data():
    for row in dhcp_output:
        try:
            with conn:
                print('Добавляю данные в таблицу dhcp...')
                query = '''insert into dhcp (mac, ip, vlan, interface, switch)
                           values (?, ?, ?, ?, ?)'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('Возникла ошибка: ', e)
    for row in dev_output:
        try:
            with conn:
                print('Добавляю данные в таблицу switches...')
                query = '''insert into switches (hostname, location)
                           values (?, ?)'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('Возникла ошибка: ', e)


if __name__ == '__main__':
    db_exists = os.path.exists('dhcp_snooping.db')
    conn = sqlite3.connect('dhcp_snooping.db')

    dhcp_output = find_dhcp()
    dev_output = find_dev()
    create_db()
    add_data()
