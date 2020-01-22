#!/usr/bin/env python

class IPAddress(Exception):
    def __init__(self, value):
        r = re.search(r'(\d+.\d+.\d+.\d)/(\d+)', value)
        if r:
            n = r.group(1).split('.')
            if 8 <= int(r.group(2)) <= 32 and 0 <= int(n[0]) <= 32 <= 32 and 0 <= int(n[1]) <= 32 <= 32 and 0 <= int(n[2]) <= 32 <= 32 and 0 <= int(n[3]) <= 32:
                self.ip = r.group(1)
                self.mask = r.group(2)
            else:
                raise ValueError('Incorrect IPv4 address')
        else:
            raise ValueError('Incorrect address')
