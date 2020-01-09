#!/usr/bin/env python

commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']


def send_commands(device, show=None, config=None):
    from answ_for_task_19_1 import send_show_command
    from answ_for_task_19_2 import send_config_command

    if show and config:
        print('Only one command!')
    elif show:
        send_show_command(device=device, command=show)
    elif config:
        send_config_command(device=device, command=config)


if __name__ == '__main__':
    print("Running: send_commands(device='devices.yaml', show='show ip int br')")
    send_commands(device='devices.yaml', show='show ip int br')
    print("Running: send_commands(device='devices.yaml', config=commands)")
    send_commands(device='devices.yaml', config=commands)
    print("Running: send_commands(device='devices.yaml', show='show ip int br', config=commands)")
    send_commands(device='devices.yaml', show='show ip int br', config=commands)
