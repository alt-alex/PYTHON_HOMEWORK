#!/usr/bin/env python

def send_command_to_devices(DEV,
                            FILENAME,
                            LIMIT,
                            SHOW=None,
                            CONFIG=None):

    import yaml
    from datetime import datetime
    from netmiko import ConnectHandler, NetMikoAuthenticationException
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import netmiko
    import re

    with open(DEV) as f:
        dvs = yaml.safe_load(f)


    def send_show(dev_prmt, CMD):
        with netmiko.ConnectHandler(**dev_prmt) as tn:
            ENBL = tn.enable()
            r = re.search(r'.+?\r\n.+?\r\n(\S+?#)', ENBL)
            pre_result = tn.send_command(CMD)
            result = r.group(1) + CMD + '\n' + pre_result + '\n'
            return result



    def send_conf(dev_prmt, CMD):
        with netmiko.ConnectHandler(**dev_prmt) as tn:
            ENBL = tn.enable()
            r = re.search(r'.+?\r\n.+?\r\n(\S+?#)', ENBL)
            pre_result = tn.send_config_set(CMD)
            result = r.group(1) + CMD + '\n' + pre_result + '\n'
            return result




    with ThreadPoolExecutor(max_workers=LIMIT) as executor:
        future_list = []
        with open(FILENAME, 'w') as f:
            hello_line = 'Create new file at ' + str(datetime.now()) + '\n\n'
            f.write(hello_line)
        for device in dvs:
            if SHOW:
                COMMANDS = SHOW
                future = executor.submit(send_show, device, COMMANDS)
                future_list.append(future)
            elif CONFIG:
                COMMANDS = CONFIG
                future = executor.submit(send_conf, device, CONFIG)
                future_list.append(future)
            else:
                pass
        with open(FILENAME, 'a') as f:
            for outp in as_completed(future_list):
                f.write(outp.result())


if __name__ == '__main__':
    send_command_to_devices(DEV='devices.yaml', FILENAME='new_file.txt', SHOW='show users', LIMIT=3)
