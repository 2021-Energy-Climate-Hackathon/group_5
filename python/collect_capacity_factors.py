import os
import pypsa
import pandas as pd
import numpy as np

basedir = '/gws/pw/j05/cop26_hackathons/oxford/Group_folders/group_5/data/schlott_material'
models = ['ICHEC','CNRM','MPI']

for model in models:
    modeldir = os.path.join(basedir, model)
    
    # Dataframes for capacity factor of input data
    df_cap_fact = None
    df_cap_per_carrier = None
    df_cap_per_carrier_and_node = None
    # Dataframe for output data
    for period in os.listdir(modeldir):
        print("collect data of model {} for period {}".format(model, period))
        network_d = os.path.join(modeldir,period)
        network = pypsa.Network(network_d)
        
        n_timesteps = len(network.snapshots)
        n_generators_per_carrier = pd.Series({carrier: len(network.generators.index[network.generators.carrier==carrier])
                                              for carrier in ['onwind', 'offwind', 'solar', 'ror']})
        
        # input data
        # capacity factor
        print("collect mean, max, min of capacity per generator node")
        avg_capacity_factor = network.generators_t.p_max_pu.mean() # per generator node
        if df_cap_fact is None:
            df_cap_fact = pd.DataFrame(index=avg_capacity_factor.index)
        
        df_cap_fact[period, 'ave'] = avg_capacity_factor
        df_cap_fact[period, 'max'] = network.generators_t.p_max_pu.max()
        df_cap_fact[period, 'min'] = network.generators_t.p_max_pu.min()
        
        avg_capacity_factor_per_carrier = (network.generators_t.p_max_pu.groupby(network.generators.carrier, axis=1).sum().sum()/
                                           (n_timesteps*n_generators_per_carrier)) # per carrier
        if df_cap_per_carrier is None:
            df_cap_per_carrier = pd.DataFrame(index=avg_capacity_factor_per_carrier.index)
        
        df_cap_per_carrier[period] = avg_capacity_factor_per_carrier
        
        avg_capacity_factor_per_carrier_and_node = network.generators_t.p_max_pu.groupby([network.generators.bus, network.generators.carrier], 
                                                                                 axis=1).sum().sum()/n_timesteps 
        
        if df_cap_per_carrier_and_node is None:
            df_cap_per_carrier_and_node = pd.DataFrame(index=avg_capacity_factor_per_carrier_and_node.index)
        df_cap_per_carrier_and_node[period] = avg_capacity_factor_per_carrier_and_node
        
    
    print("save dataframe to csv files")
    df_cap_fact.to_csv("../data/cap_factor_input_all_periods_{}.csv".format(model))
    df_cap_per_carrier.to_csv("../data/cap_factor_input_per_carrier_all_periods_{}.csv".format(model))
    df_cap_per_carrier_and_node.to_csv("../data/cap_factor_input_per_carrier_and_node_all_periods_{}.csv".format(model))
        
        
        
        

    
