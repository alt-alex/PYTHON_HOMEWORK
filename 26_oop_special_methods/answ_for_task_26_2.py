#!/usr/bin/env python

class CiscoTelnet():
    def __init__(self, ip, username, password, secret):
        username = username.encode('utf-8') + b'\n'
        password = password.encode('utf-8') + b'\n'
        secret = secret.encode('utf-8') + b'\n'
        import telnetlib
        self.tl = telnetlib.Telnet(ip)
        print('connection - ok')
        self.tl.read_until(b'Username')
        self.tl.write(username)
        self.tl.read_until(b'Password')
        self.tl.write(password)
        print('login and password - ok')
        self.tl.read_until(b'>')
        self.tl.write(b'enable\n')
        self.tl.read_until(b'Password')
        self.tl.write(secret)
        self.tl.read_until(b'#')
        print('enable mode - ok')
        self.tl.write(b'terminal length 0\n')
        self.tl.read_until(b'#')
        print('clipaging - off')

    def __enter__(self):
        print('Manager of  context is available')
        return self

    def _write_line(self, command):
        command = command.encode('utf-8') + b'\n'
        self.tl.write(command)

    def send_show_command(self, command):
        command = command.encode('utf-8') + b'\n'
        self.tl.write(command)
        rslt = self.tl.read_until(b'#')
        print(rslt.decode('utf-8'))

    def __exit__(self, exc_type, exc_value, traceback):
        self.tl.close()
