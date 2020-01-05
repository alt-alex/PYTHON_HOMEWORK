#!/usr/bin/env python

def send_show_command(device='devices.yaml', command='show clock'):
    import netmiko
    import yaml


    with open(device) as f:
        dev = yaml.safe_load(f)


    for device_params in dev:
        my_con = netmiko.ConnectHandler(**device_params)
        my_con.enable()
        result = my_con.send_command(command)
        print(result)



if __name__ == "__main__":
    send_show_command()
