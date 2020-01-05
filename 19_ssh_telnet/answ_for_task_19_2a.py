#!/usr/bin/env python

commands = [
'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]

def send_config_command(device='devices.yaml', command='show clock', verbose=True):
    import netmiko
    import yaml


    with open(device) as f:
        dev = yaml.safe_load(f)


    for device_params in dev:
        try:
            if verbose!=False:
                print('Connecting with {}...'.format(device_params['ip']))
            else:
                pass

            my_con = netmiko.ConnectHandler(**device_params)
            try:
                my_con.enable()
                result = my_con.send_config_set(commands)
                print(result)
            except ValueError as err:
                print(err)
        except netmiko.NetMikoAuthenticationException as err:
            print(err)
        except netmiko.NetMikoTimeoutException as err:
            print(err)

if __name__ == "__main__":
    send_config_command(command=commands)
