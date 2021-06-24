import os
import pypsa
import pandas as pd
import numpy as np
import pickle as pkl

basedir = '/gws/pw/j05/cop26_hackathons/oxford/Group_folders/group_5/data/schlott_material'
models = ['ICHEC','CNRM','MPI']

for model in models:
    modeldir = os.path.join(basedir, model)
    network_per_period = {}
    # Dataframe for output data
    for period in os.listdir(modeldir):
        print("collect data of model {} for period {}".format(model, period))
        network_d = os.path.join(modeldir,period)
        network = pypsa.Network(network_d)
        network_per_period[period] = network
        
    with open('networks_per_period_{}.pkl'.format(model), 'wb') as handle:
        pkl.dump(network_per_period, handle)
        
    