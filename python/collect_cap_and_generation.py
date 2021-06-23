import os
import pypsa
import pandas as pd
import numpy as np

basedir = '/gws/pw/j05/cop26_hackathons/oxford/Group_folders/group_5/data/schlott_material'
#model = 'ICHEC'
#model = 'CNRM'
model = 'MPI'
modeldir = os.path.join(basedir, model)
cap_share_all = None
gen_share_all = None
gen_share_per_node_all = None
for period in os.listdir(modeldir):
        print("collect data of model {} for period {}".format(model, period))
        network_d = os.path.join(modeldir,period)
        network = pypsa.Network(network_d)
        
        ### capacity/generation shares
        cap_share = network.generators.p_nom_opt.groupby(network.generators.carrier).sum() # per carrier
        gen_share = network.generators_t.p.groupby(network.generators.carrier, axis=1).sum().sum() # per carrier
        gen_share_per_node = network.generators_t.p.groupby([network.generators.bus, network.generators.carrier], axis=1).sum().sum() # per carrier and bus
        if cap_share_all is None:
                cap_share_all = pd.DataFrame(index=cap_share.index)
                gen_share_all = pd.DataFrame(index=gen_share.index)
                gen_share_per_node_all = pd.DataFrame(index=gen_share_per_node.index)
        cap_share_all[period] = cap_share
        gen_share_all[period] = gen_share
        gen_share_per_node_all[period] = gen_share_per_node

cap_share_all.to_csv("cap_share_all_periods_model_{}.csv".format(model))
gen_share_all.to_csv("gen_share_all_periods_model_{}.csv".format(model))
gen_share_per_node_all.to_csv("gen_share_per_node_all_periods_model_{}.csv".format(model))

    
