#!/usr/bin/env python

def send_config_command(device='devices4.yaml', verbose=True):
    import netmiko
    import yaml

    command = input('enter command: ')

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
                result = my_con.send_config_set(command)
                if 'Invalid input detected' in result:
                    print('Команда "' + command + '" выполнилась с ошибкой "' +
                    "Invalid input detected at '^' marker\" на устройстве " +
                    device_params['ip'])
                else:
                    print(result)
            except ValueError as err:
                print(err)
        except netmiko.NetMikoAuthenticationException as err:
            print(err)
        except netmiko.NetMikoTimeoutException as err:
            print(err)
