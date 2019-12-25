#!/usr/bin/env python

import glob


def parse_sh_version(initial_file):
    import re
    with open(initial_file) as f:
        file = f.read()
        r = re.search(r'IOS.*Version (\S+),.*router uptime is (.*?)\n.*image file is "(\S+)"', file, re.DOTALL)
        ios = r.group(1)
        image = r.group(3)
        uptime = r.group(2)
        tpl = (ios, image, uptime)
    return tpl



def write_inventory_to_csv(data_filenames, csv_filename):
    import csv
    headers = ['hostname', 'ios', 'image', 'uptime']
    rslt = []
    rslt.append(headers)
    for line in data_filenames:
        with open(line) as f:
            r = parse_sh_version(line)
            rslt_tpl = [line[11:-4]]
            rslt_tpl = rslt_tpl + list(r)
            rslt.append(rslt_tpl)
    with open('routers_inventory.csv', 'w') as f:
        writer = csv.writer(f)
        for row in rslt:
            writer.writerow(row)


if __name__ == '__main__':
    sh_version_files = glob.glob('sh_vers*')
    write_inventory_to_csv(sh_version_files, 'routers_inventory.csv')
