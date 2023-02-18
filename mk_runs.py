#! /usr/bin/env python
#
#   script generator for project="2021-S1-US-3"
#
#   lmtinfo.py grep US-3 Science Map | awk '{print $2}' | sort


import os
import sys

# in prep of the new lmtoy module
try:
    lmtoy = os.environ['LMTOY']
    sys.path.append(lmtoy)
    from lmtoy import runs
except:
    print("No LMTOY with runs.py")
    sys.exit(0)

project="2023-S1-MX-47"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["11863-3703"] =  [ 105120, 105121, 105122,                                         # feb 9
                      105354, 105355, 105356,                                         # feb 10
                      105474, 105475, 105476,                                        # feb 14
                      105773, 105774, 105775, 105777, 105778, 105779,
                      105781, 105782, 105783, 105785, 105786, 105787,
                      105790, 105791, 105792,]                                        # feb 15
on["8593-12705"] =  [ 106091, 106092, 106093, 106095, 106096, 106097,
                      106099, 106100, 106101, 106105, 106106, 106107,
                      106109, 106110, 106111, 106113, 106114, 106115,
                      106117, 106118, 106119, 106122, 106123, 106124,]                # feb 18

on["8998-12705"] =  [ 106026, 106027, 106028, 106030, 106031, 106032,
                      106034, 106035, 106036, 106040, 106041, 106042,
                      106044, 106045, 106046, 106048, 106049, 106050,
                      106052, 106053, 106054, 106055,]                                # feb 18


on["9487-9102"] = [ 104790, 104791, 104792, 104794, 104795, 104796, 104798, 104799,
                    104800, 104803, 104804, 104805, 104807, 104808, 104809, 104811,
                    104812, 104813, 104828, 104829, 104830, 104832, 104833,           # feb 6
                    104944, 104945, 104946,                                           # feb 8
                    105236, 105237, 105238,]                                          # feb 10

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["11863-3703"] = "xlines=110.6,0.3"
pars1["8593-12705"] = "xlines=110.2,0.3"
pars1["8998-12705"] = "xlines=107.4,0.3"     # double peak ?
pars1["9487-9102"]  = "xlines=110.7,0.3"


#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["11863-3703"] = "srdp=1 admit=0"
pars2["8593-12705"] = ""
pars2["8998-12705"] = ""
pars2["9487-9102"]  = "srdp=1 admit=0"

runs.mk_runs(project, on, pars1, pars2)
