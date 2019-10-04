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
ncs_agent = ncs_rca.NCS_RCA('192.168.152.96', 10101)

#Testing request for help

ncs_agent.help()
ncs_agent.time()

#load workspace a workspace

workspace_name = "C:/NCSData/Workspaces/Default.iws"

ncs_agent.workspace_load(workspace_name)

#TODO: insert connect command


#TODO: insert start command

