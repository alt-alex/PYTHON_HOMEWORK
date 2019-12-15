#!/usr/bin/env python


def convert_ranges_to_ip_list(list):
    split_line = []
    rslt_line = []
    for l in list:
        if '-' not in l:
            rslt_line.append(l)
        else:
            if l.count('.') == 3:
                l_new = (l.split('.')[3]).split('-')
                l1 = l_new[0]
                l2 = l_new[1]
                three_oct = '.'.join(l.split('.')[:3])
                for i in range(int(l1), int(l2)+1):
                    split_line  = three_oct + '.' + str(i)
                    rslt_line.append(split_line)
            elif l.count('.') == 6:
                l1 = (l.split('.')[3]).split('-')[0]
                l2 = l.split('.')[6]
                for i in range(int(l1), int(l2)+1):
                    split_line  = three_oct + '.' + str(i)
                    rslt_line.append(split_line)
    return rslt_line


if __name__ == "__main__":
    print(convert_ranges_to_ip_list(list))
