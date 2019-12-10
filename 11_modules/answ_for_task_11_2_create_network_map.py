def create_network_map(*args):
   rslt_cfg = ''
   for i in args:
      with open(i) as cfg:
          cfg_file = cfg.read()
          rslt_cfg = rslt_cfg + cfg_file
   return rslt_cfg


r = create_network_map('sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt', 'sh_cdp_n_sw1.txt')

newline = []

for line in  r.split('\n'):
    if 'Eth' in line or '>' in line:
        newline.append(line)



value_key = []
dict = {}
for l in newline:

        if '>' in l:
            d_k = l[:2]
        else:
            l = l.split()
            rslt_local = l[1] + l[2]
            rslt_outer = l[-2] + l[-1]
            dict.update({(d_k, rslt_local): (l[0], rslt_outer)})


