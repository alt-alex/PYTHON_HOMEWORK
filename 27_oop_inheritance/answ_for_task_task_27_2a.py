#!/usr/bin/env python

from netmiko.cisco import CiscoIosBase


class MyNetmiko(CiscoIosBase):
    def __init__(self, device_type, ip, username, password, secret):
        super().__init__(device_type = device_type, ip = ip, username = username, password = password, secret = secret)
        self.enable()
        self.send_command(secret + '\n')
    def _check_error_in_command(self, command):
        rslt = self.send_command(command)
        if 'Ambiguous command:' in rslt:
            print('You entered an Ambiguous command:', command)
        elif 'Invalid input detected' in rslt:
            print('You entered an Invalid command:', command)
        elif 'Incomplete command' in rslt:
            print('You entered an Incomplete command:', command)
        else:
            return rslt

