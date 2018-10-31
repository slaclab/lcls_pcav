import epics as epics
import time as time
import numpy as np
import datetime as datetime
import math
import matplotlib.pyplot as plt
from scipy import signal

import Pcav_Init as sys_setup
import Cavity_Init as cavity_setup
import SPV_setup
import Pv_Setup as PV
import PV_fetch as PV_fetch



pre = 'SIOC:SYS0:ML00:AO'
IOC = 'UND:R02:IOC:16'
EVR = 'UND:R02:EVR:16'
BLD_IOC = 'UND:R02:IOC:10'
Prog_Name = 'BAT_mon.py'

Cavity_Set   = 2
Cavity_Num   = Cavity_Set * 2
ADC_Chan     = 4
ADC_Points   = 1024
Cav_Freq     = 2805e6
Cav_LO       = 2856e6
Cav_IF       = abs(Cav_Freq - Cav_LO)
ADC_CLK      = Cav_LO / 24
REF_VCO_Freq = 476e6
evr_chan = 15


Cav = range(Cavity_Set)
Cav_val = range(Cavity_Set)
PCav_Sys = sys_setup.phase_cavity_sys()
PCav_val = sys_setup.phase_cavity_sys()
for i in range(Cavity_Set):
    # print i
    Cav[i] = cavity_setup.cavity_init()
    Cav_val[i] = cavity_setup.cavity_init()
# Cav1 = cavity_setup.cavity_init()
# Cav2 = cavity_setup.cavity_init()

# Setting up the Phase cavity system PV name and parameters
Fbck_VCO_Gain  = 2 * math.pi * Cav_Freq * (1e-12)
Fbck_ADC_Thres = 500
Fbck_Q_Thres   = 10
Fbck_Max_Step  = 20
Fbck_Rate      = 1
PV.Pcav_PV_setup(PCav_Sys, IOC, EVR, pre)
PV.trigger_pv_setup(PCav_Sys, EVR, evr_chan)
PV.CAV_ADC_Var_setup(PCav_Sys, Cavity_Set, Cavity_Num, REF_VCO_Freq, ADC_CLK, Cav_IF, Cav_Freq, Cav_LO, ADC_Chan, ADC_Points)
PV.Script_name(PCav_Sys, Prog_Name)
# CAV_ADC_Var_setup(Cav_Sys, Cav_set, Cav_Num, Cav_REF_f, ADC_CLK, IF_f, RF_f, LO_f, ADC_Chan, ADC_Point)
PV.Fbck_Var_setup(PCav_Sys, Fbck_ADC_Thres, Fbck_Max_Step, Fbck_VCO_Gain, Fbck_Q_Thres, Fbck_Rate) #Fbck_Var_setup(Cav_Sys, ADC_Thres, Max_Step, VCO_Gain, Q_Thres, Rate)
PV.IF_Sin_Cos(PCav_Sys)
PV.Filter_Init(PCav_Sys)
PV.EVR_Delay(PCav_Sys)

# Setting up the individual cavity PV name and parameters
# print Cav[1].Ele_PV_Amp
for i in range(2):
    PV.Cavity_PV_setup(Cav[i], IOC, pre, BLD_IOC, i+1)
    PV.Electronic_Atten_calibration(Cav[i], i+1)

# caget values from the PVs
old_time = datetime.datetime.now()
new_time = old_time
good = 1
attngood = 1
triggood = 1
statgood = 1
mmsgood  = 1

new_time, good, attngood, triggood, statgood, mmsgood = PV_fetch.PV_collect(Cav, 2, Cav_val, new_time, good, attngood, triggood, statgood, mmsgood)
new_time, good, attngood, triggood, statgood, mmsgood = PV_fetch.PV_collect(PCav_Sys, 1, PCav_val, new_time, good, attngood, triggood, statgood, mmsgood)

# Fetching PV Values for individual cavity values
# for i in range(2):
#     for property, value in vars(Cav[i]).iteritems():
#         if 'PV' in property:
#             # print property, ": ", value
#             # print type(value)
#             value1 = epics.caget(value)
#             if value1 == None:
#                 value1 = np.nan
#                 good = 0
#                 # Check if any of the attn/amp/charge PV value is NaN
#                 if any(ptemp in property for ptemp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
#                     attngood = 0
#                     # print('Error with attn/amp/charge PV value')
#                 # Check if any of the EVR PV value is NaN
#                 elif any(ptemp in value for ptemp in ('EVR', 'evr')):
#                     triggood = 0
#                     # print('Error with EVR PV value')
#                 # Check if the MMS phase shifter is NaN
#                 elif 'Ele_PV_Phi_Ctrl' in property:
#                     mmsgood  = 0
#                     # print('Error with the MMS phase shifter')
#             # Check chassis status bit    
#             if any(ptemp in property for ptemp in ('Status', 'status')):
#                 statgood = 0
#                 # print('Error with AFE chassis status')     
#             setattr(Cav_val[i], property, value1)
#             print(str(value) + ' value is: ' + str(value1))
#     print '\n'

# # Fetching PV value for the Phase Cavity system values
# for property, value in vars(PCav_Sys).iteritems():
#     if 'PV' in property:
#         value_type = type(value)
#         # print value_type
#         # Checks if the PV name is in a list like the EVR PVs.
#         if (value_type is list):
#             value_len = len(value)
#             temp = range(value_len)
#             for x in range(value_len):
#                 # print(value[x])
#                 temp[x] = epics.caget(value[x])
#                 if temp[x] == None:
#                     temp[x] = np.nan
#                     good = 0
#                     # Check if any of the attn/amp/charge PV value is NaN
#                     if any(ptemp in property for ptemp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
#                         attngood = 0
#                     # Check if any of the EVR PV value is NaN    
#                     elif any(ptemp in value[x] for ptemp in ('EVR','evr')):
#                         triggood = 0
#                     # Check if the MMS phase shifter is NaN                        
#                     elif 'Ele_PV_Phi_Ctrl' in property:
#                         mmsgood  = 0                    
#                 # Check chassis status bit    
#                 if (any(ptemp in property for ptemp in ('Status', 'status')) and (temp[x] != 0)):
#                     statgood = 0
#                     # print('Error with AFE chassis status')                            
#                 print(str(value[x]) + ' value is: ' + str(temp[x]))
#                 setattr(PCav_val, property, temp)
#         else:
#             value1 = epics.caget(value)
#             if value1 == None:
#                 value1 = np.nan            
#                 good = 0
#                 # Check if any of the attn/amp/charge PV value is NaN
#                 if any(ptemp in property for ptemp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
#                     attngood = 0
#                     # print('Error with attn/amp/charge PV value')
#                 # Check if any of the EVR PV value is NaN
#                 elif any(ptemp in value for ptemp in ('EVR', 'evr')):
#                     triggood = 0
#                     # print('Error with EVR PV value')
#                 # Check if the MMS phase shifter is NaN
#                 elif 'Ele_PV_Phi_Ctrl' in property:
#                     mmsgood  = 0
#                     # print('Error with the MMS phase shifter')
#             # Check chassis status bit    
#             if (any(ptemp in property for ptemp in ('Status', 'status')) and (value1 != 0)):
#                 statgood = 0
#                 # print('Error with AFE chassis status') 
#             setattr(PCav_val, property, value1)
#             print(str(value) + ' value is: ' + str(value1))
# new_time = datetime.datetime.now()

print ('########################################################################')
print ('########################################################################')
# Change print into Log in the future
# Error report for any NaN values
if not(good):
    print "There is a NaN in the PV"
else:
    print "No NaN values"
# Err report for amp/attn/charge NaN PV values
if not(attngood):
    print 'NaN Error with amp, attn, and charge'
else:
    print 'Amp, attn, and charge read is fine'
# Err report for stale PV data
if (not(new_time > old_time) and (PCav_val.Cav_PV_Beamf != 0)):
    print('Digitizer data is stale, timestamp is ' + str(new_time))
else:
    print('Timestamp is fine ' + str(new_time))
# Err report for phase shifter NaN PV values
if not(mmsgood):
    print('Read failure from phase shifter controls')
else:
    print('Phase shifter read is fine')
# Err report for chassis status err
if statgood:
    print('Error with AFE chassis status') 
else:
    print('AFE chassis status is fine')

print ('########################################################################')
print ('########################################################################')




# # System and cavity value
# for i in range(2):
#     for property, value in vars(Cav_val[i]).iteritems():
#         if 'PV' in property:
#             # print property, ": ", value
#             if any(temp in property for temp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
#                 print property, ": ", value
#                 print '\n'
#             # if np.isnan(value):
#             #     if any(temp in property for temp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
#             #         attngood = 0
#             #     good = 0
#             # else:
#             #     good = 1
#     print '\n'

# for property, value in vars(PCav_val).iteritems():
#     if 'PV' in property:
#         # print property
#         # print property, ": ", value
#         # print np.isnan(value)
#         # print np.any(np.isnan(value))
#         if any(temp in property for temp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
#             print property, ": ", value
#             print '\n'        
#         if np.any(np.isnan(value)):
#             if any(temp in property for temp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
#                     attngood = 0
#             good = 0
#         else:
#             good = 1
