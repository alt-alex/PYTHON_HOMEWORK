#!/usr/bin/env python

commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands

def send_config_command(command, device='devices4.yaml', verbose=True):
    import netmiko
    import yaml
    global output, flag



    with open(device) as f:
        dev = yaml.safe_load(f)


    for device_params in dev:
        try:
            if verbose!=False:
                print('Connecting with {}...'.format(device_params['ip']))
            else:
                pass

            with netmiko.ConnectHandler(**device_params) as my_con:
                try:
                    my_con.enable()
                    result = my_con.send_config_set(command)
                    if 'Invalid input detected' in result:
                        print('Команда "' + command + '" выполнилась с ошибкой "' +
                        "Invalid input detected at '^' marker\" на устройстве " +
                        device_params['ip'])
                        flag = 'err'
                        bad[command] = result
                    elif '% Incomplete command.' in result:
                        print('Команда "' + command + '" выполнилась с ошибкой "' +
                        'Incomplete command" на устройстве ' +
                        device_params['ip'])
                        bad[command] = result
                    elif '% Ambiguous command' in result:
                        print('Команда "' + command + '" выполнилась с ошибкой "' +
                        'Ambiguous command" на устройстве ' +
                        device_params['ip'])
                        bad[command] = result
                    else:
                        print(result)
                        good[command] = result
                        flag = ''
                    my_con.disconnect()
                except ValueError as err:
                    print(err)
        except netmiko.NetMikoAuthenticationException as err:
            print(err)
        except netmiko.NetMikoTimeoutException as err:
            print(err)
    output = (good, bad)
    return output, flag



def f():
    import time
    global bad, good
    bad = {}
    good = {}
    for cmd in commands:
        send_config_command(cmd)
        if 'err' in flag:
            line = input('родолжать выполнять команды? [y]/n: ')
            if line == 'n':
                return output
        time.sleep(1)
    return output

if __name__ == '__main__':
    f()
