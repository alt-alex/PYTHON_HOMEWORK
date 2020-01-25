#!/usr/bin/env python

from base_connect_class import BaseSSH

class CiscoSsh(BaseSSH, Exception):
    def __init__(self, device_type = None, ip = None, username = None, password = None, secret = None):
        if not username:
            username = input('username: ')
        if not  password:
            password = input('password: ')
        if not secret:
            secret = input('secret: ')
        super().__init__(device_type = device_type, ip = ip, username = username, password = password, secret = secret)
        self.ssh.enable()
        self.ssh.send_command(secret + '\n')

if __name__  == '__main__':
    device_params = {
        'device_type': 'cisco_ios',
        'ip': '192.168.100.1'
        }

    con = CiscoSsh(**device_params)
    print(con.send_show_command('sh privi'))
