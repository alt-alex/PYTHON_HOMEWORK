#!/usr/bin/env python

def transform_topology(some_file):

    import yaml
    with open(some_file) as f:
        templates = yaml.safe_load(f)


    list_dev = []
    for l in templates.keys():
        list_dev.append(l)


    dict = {}
    for l in list_dev:
        list_key = list(templates[l].keys())
        for line in list_key:
            tpl1 = (l, line)
            tpl2 = (list(templates[l][line].keys())[0], list(templates[l][line].values())[0])
            dict[tpl1] = tpl2


    new_list = []
    for line in list(dict.keys()):
        line = line[0]
        new_list.append(line)
    new_list


    rslt_dict = {}
    for l in dict.items():
        if l[1] not in list(rslt_dict.keys()):
            rslt_dict[l[0]] = l[1]

    return rslt_dict


if __name__ == '__main__':
    print(transform_topology('topology.yaml'))
