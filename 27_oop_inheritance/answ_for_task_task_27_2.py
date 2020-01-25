#!/usr/bin/env python

from netmiko.cisco import CiscoIosBase

class MyNetmiko(CiscoIosBase):
    def __init__(self, device_type, ip, username, password, secret):
        super().__init__(device_type = device_type, ip = ip, username = username, password = password, secret = secret)
        self.enable()
        self.send_command(secret + '\n')

