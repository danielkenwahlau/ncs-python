'''
Testing NCS Remote Control Agent

Copyright IFEN GmbH, 2012

@author: uwsc
'''

import time
import ncs_rca

# create object and connect to NCS remote control agent
# on target computer (here 'localhost' as an example)
# agent must already be running on target computer
ncs_agent = ncs_rca.NCS_RCA('localhost', 10101)

# load existing scenario file
ncs_agent.scenario_load('Test1')

# start simulation
ncs_agent.simulation_run()

# commands are executed as they come, if they must be executed  
# at a later time, the script has to delay sending them 
time.sleep(6)

# get the powerlevel for all satellites
results = ncs_agent.simulation_info_powerlevel()
print(results[0])

# change powerlevel for specific satellite
result = ncs_agent.simulation_param_powerlevel_set('EIRP-GPS-027-L5','-60.0')
print(result)

# commands are executed as they come, if they must be executed  
# at a later time, the script has to delay sending them 
time.sleep(6)

# get powerlevel for specific satellite
result = ncs_agent.simulation_param_powerlevel_get('EIRP-GPS-027-L5')
print(result)

# stop simulation
ncs_agent.simulation_stop()


    
