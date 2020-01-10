#!/usr/bin/env python

def ping_ip_addresses(HOSTS=['192.168.1.1', '192.168.1.2'], MW=2):
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import datetime, subprocess

    def ping_func(host):
        reply = subprocess.run(['ping', '-c', '3', host], stdout=subprocess.DEVNULL)
        if reply.returncode == 0:
            rslt = host + ' Alive'
            print(rslt)
            return rslt
        else:
            rslt = host + ' Unreachable'
            print(rslt)
            return rslt


    start_time = datetime.datetime.now()
    with ThreadPoolExecutor(max_workers=MW) as executor:
        available_list = []
        rslt_list_r = []
        rslt_list_u = []
        for host in HOSTS:
            future = executor.submit(ping_func, host)
            available_list.append(future)
        for f in as_completed(available_list):
            if 'Un' not in f.result():
                rslt_list_r.append(f.result())
            else:
                rslt_list_u.append(f.result())
        result = (rslt_list_r, rslt_list_u)
        rslt_time = datetime.datetime.now() - start_time
        print(result, rslt_time)

if __name__ == '__main__':
    hosts = []
    for i in range(1, 10):
        host = '192.168.1.{}'.format(i)
        hosts.append(host)
    ping_ip_addresses(HOSTS=hosts)
