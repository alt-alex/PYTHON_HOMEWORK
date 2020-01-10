#!/usr/bin env python

import yaml

from itertools import repeat
from concurrent.futures import ThreadPoolExecutor


with open('devices.yaml') as f:
    dev = yaml.safe_load(f)

def con(d_p, CMD):
    import netmiko
    with netmiko.ConnectHandler(**dev_prmts) as tn:
        tn.enable()
        result = tn.send_command(CMD)
        print("we get" + result)
        return result


for dev_prmts in dev:
    con(dev_prmts, 'sh clock')



with ThreadPoolExecutor(max_workers=3) as executor:
    result = executor.map(con, dev, repeat('sh clock'))
    for d, outp in zip(dev, result):
        line = (d['ip'], outp)
        with open('new_file.yaml', 'a') as f:
            yaml.dump(line, f)

