#!/usr/bin/env python

bad = {}
good = {}
commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
correct_commands = ['logging buffered 20010', 'ip http server']
commands = commands_with_errors + correct_commands


def send_config_command(command, device='devices4.yaml', verbose=True):
    import netmiko, time, yaml
    global output


    with open(device) as f:
        dev = yaml.safe_load(f)

    time.sleep(1)
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
                my_con.disconnect()
            except ValueError as err:
                print(err)
        except netmiko.NetMikoAuthenticationException as err:
            print(err)
        except netmiko.NetMikoTimeoutException as err:
            print(err)
    output = (good, bad)
    return output

if __name__ == "__main__":
    import pprint
    for l in commands:
        send_config_command(l)
    pprint.pprint(output)
