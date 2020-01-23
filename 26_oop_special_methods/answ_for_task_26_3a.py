#!/usr/bin/env python

class IPAddress():
    def __init__(self, value):
        import re
        self.ip_address = value
        r = re.search(r'(\d+.\d+.\d+.\d)/(\d+)', value)
        if r:
            n = r.group(1).split('.')
            if 0  <= int(r.group(2)) <= 32 and 0 <= int(n[0]) <= 255  and 0 <= int(n[1]) <= 255  and 0 <= int(n[2]) <= 255 and 0 <= int(n[3]) <= 255:
                self.ip = r.group(1)
                self.mask = r.group(2)
            else:
                raise ValueError('Incorrect value of IPv4 address')
        else:
            raise ValueError('Incorrect form of IPv4 address')

    def __str__(self):
        return self.ip_address

    def __repr__(self):
        return f'IPv4 address {self.ip}'
