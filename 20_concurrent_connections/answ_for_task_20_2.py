#!/usr/bin/env python

def con(dev_prmt, CMD):
    import netmiko
    with netmiko.ConnectHandler(**dev_prmt) as tn:
        tn.enable()
        result = tn.send_command(CMD)
        print("we get" + result  + ' from ' + dev_prmt['ip'])
        return result


def send_show_command_to_devices(DEV='devices.yaml',
                                 CMD='sh clock',
                                 FILENAME='new_file.yaml',
                                 LMT=3):
    from itertools import repeat
    import yaml, datetime
    from concurrent.futures import ThreadPoolExecutor

    with open(DEV) as f:
        dvs = yaml.safe_load(f)

    with ThreadPoolExecutor(max_workers=int(LMT)) as executor:
        hello_line = 'Create new file'
        with open(FILENAME, 'w') as f:
            yaml.dump(hello_line, f)
        start_time = datetime.datetime.now()
        result = executor.map(con, dvs, repeat(CMD))
        for d, outp in zip(dvs, result):
            line = (d['ip'], outp)
            with open(FILENAME, 'a') as f:
                yaml.dump(line, f)
        t = datetime.datetime.now() - start_time
        print('program execution time ' + str(t))

if __name__ == "__main__":
    send_show_command_to_devices()
