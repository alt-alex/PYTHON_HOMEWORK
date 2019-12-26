#!/usr/bin/env python

def generate_topology_from_cdp(list_of_files, save_to_filename = None):

    import yaml

    from answ_task_17_2_parse_sh_cdp_neighbors import parse_sh_cdp_neighbors

    dict_rslt = {}

    for file in list_of_files:
        r = parse_sh_cdp_neighbors(file)
        dict_rslt.update(r)

    if save_to_filename:
        with open(save_to_filename, 'w') as f:
            yaml.dump(dict_rslt, f)
    return dict_rslt

if __name__ == '__main__':
    import glob
    sh_version_files = glob.glob('sh_cdp*')
    print(generate_topology_from_cdp(sh_version_files, 'topology.yaml'))
