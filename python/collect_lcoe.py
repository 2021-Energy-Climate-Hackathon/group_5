import os
import pypsa
import pandas as pd
import numpy as np


basedir = '/gws/pw/j05/cop26_hackathons/oxford/Group_folders/group_5/data/schlott_material'
for model in ['ICHEC','CNRM','MPI']:
    modeldir = os.path.join(basedir, model)
    lcoe_all = None
    lcoe_per_carrier_all = None
    lcoe_per_carrier_and_node_all = None
    for period in os.listdir(modeldir):
        print("collect data of model {} for period {}".format(model, period))
        network_d = os.path.join(modeldir,period)
        network = pypsa.Network(network_d)

        ### levelized cost of electricity
        investments = network.generators.p_nom_opt * network.generators.capital_cost
        operation = network.generators_t.p.sum() * network.generators.marginal_cost

        generation_per_carrier = network.generators_t.p.groupby(network.generators.carrier,axis=1).sum()
        operation_per_carrier = operation.groupby(network.generators.carrier).sum()
        investments_per_carrier = investments.groupby(network.generators.carrier).sum()

        generation_per_carrier_and_node = network.generators_t.p.groupby([network.generators.bus, network.generators.carrier],axis=1).sum()
        operation_per_carrier_and_node = operation.groupby([network.generators.bus, network.generators.carrier]).sum()
        investments_per_carrier_and_node = investments.groupby([network.generators.bus, network.generators.carrier]).sum()

        lcoe = (investments.sum() + operation.sum()) / network.loads_t.p_set.sum().sum() # for whole system
        lcoe_per_carrier = (investments_per_carrier.sum() + operation_per_carrier.sum()) / generation_per_carrier.sum() # per carrier
        lcoe_per_carrier_and_node = ((investments_per_carrier_and_node.sum() + operation_per_carrier_and_node.sum()) / 
                            generation_per_carrier_and_node.sum()) # per carrier and bus

        if lcoe_all is None:
            lcoe_all = pd.DataFrame(index=['lcoe'])
            lcoe_per_carrier_all = pd.DataFrame(index=lcoe_per_carrier.index)
            lcoe_per_carrier_and_node_all = pd.DataFrame(index=lcoe_per_carrier_and_node.index)

        lcoe_all[period] = lcoe
        lcoe_per_carrier_all[period] = lcoe_per_carrier
        lcoe_per_carrier_and_node_all[period] = lcoe_per_carrier_and_node
    
    lcoe_all.to_csv("lcoe_all_periods_model_{}.csv".format(model))
    lcoe_per_carrier_all.to_csv("lceo_per_carrier_all_periods_model_{}.csv".format(model))
    lcoe_per_carrier_and_node_all.to_csv("lceo_per_carrier_per_node_all_periods_model_{}.csv".format(model))
