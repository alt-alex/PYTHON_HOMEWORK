#!/usr/bin/env python


def convert_ios_nat_to_asa():
    import re
    rslt = []
    with open('cisco_nat_config.txt') as cfg, open('result.txt', 'w') as dest:
        file = cfg.readlines()
        for line in file:
            r = re.search(r'.*(ins\S+) so\S+ (\S+) (\S+) (\S+) (\S+) .*/\d+ (\d+)', line)
            if r:
                new_line = 'object network LOCAL_' + r.group(4) + '\n host ' + r.group(4) + '\n nat (' + r.group(1) + ',outside) ' + r.group(2) + ' interface service ' + r.group(3) + ' ' + r.group(5) + ' ' + r.group(6) + '\n'
            dest.write(new_line)

if __name__ == '__main__':
     convert_ios_nat_to_asa()
