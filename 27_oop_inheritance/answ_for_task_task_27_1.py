#!/usr/bin/env python
from base_connect_class import BaseSSH

class CiscoSsh(BaseSSH):
    def __init__(self, device_type, ip, username, password, secret):
        super().__init__(device_type = device_type, ip = ip, username = username, password = password, secret = secret)
        self.ssh.enable()
        self.ssh.send_command(secret + '\n')
