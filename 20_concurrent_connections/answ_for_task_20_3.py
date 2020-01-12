#!/usr/bin/env python

def send_command_to_devices(DEV,
                            FILENAME,
                            COMMANDS,
                            LIMIT):
    import yaml
    from datetime import datetime
    from netmiko import ConnectHandler, NetMikoAuthenticationException
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import netmiko
    import re

    def con(dev_prmt, CMD):
        with netmiko.ConnectHandler(**dev_prmt) as tn:
            ENBL = tn.enable()
            r = re.search(r'.+?\r\n.+?\r\n(\S+?#)', ENBL)
            pre_result = tn.send_command(CMD)
            result = r.group(1) + CMD + '\n' + pre_result + '\n'
            return result


    with open(DEV) as f:
        dvs = yaml.safe_load(f)


    with ThreadPoolExecutor(max_workers=LIMIT) as executor:
        future_list = []
        with open(FILENAME, 'w') as f:
            hello_line = 'Create new file at ' + str(datetime.now()) + '\n\n'
            f.write(hello_line)
        for device in dvs:
            future = executor.submit(con, device, COMMANDS[device['ip']])
            future_list.append(future)
        with open(FILENAME, 'a') as f:
            for outp in as_completed(future_list):
                f.write(outp.result())

if __name__ == "__main__":
    commands = {'192.168.100.1': 'sh ip int br',
                '192.168.100.2': 'sh arp',
                '192.168.100.3': 'sh ip int br'}
    send_command_to_devices(DEV='devices.yaml', FILENAME='new_file.txt', COMMANDS=commands, LIMIT=3)

