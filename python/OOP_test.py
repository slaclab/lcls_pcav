import Pcav_Init as sys_setup
import Cavity_Init as cavity_setup
import SPV_setup
import epics as epics
import time

import Pv_Setup as PV
import numpy as np
from scipy import signal
import math
import matplotlib.pyplot as plt


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
    # print i
    PV.Cavity_PV_setup(Cav[i], IOC, pre, BLD_IOC, i+1)
    PV.Electronic_Atten_calibration(Cav[i], i+1)

# blah = range(15)
# print blah
# for i in blah:
#     # print i
#     blah[i] = blah[i] + 1#     # print blah[i]

# print blah
# print Cav[1].Ele_Attn_start
# print Cav[1].Ele_Attn_end

# print blah[Cav[1].Ele_Attn_start]
# print blah[9:14]
# print blah[15]

# caget values from the PVs
for i in range(2):
    for property, value in vars(Cav[i]).iteritems():
        if 'PV' in property:
            # print property, ": ", value
            # print type(value)
            value1 = epics.caget(value)
            if value1 == None:
                value1 = np.nan
            setattr(Cav_val[i], property, value1)
            print(str(value) + ' value is: ' + str(value1))

    print '\n'

for property, value in vars(PCav_Sys).iteritems():
    if 'PV' in property:
        # print property
        # print property, ": ", value
        value_type = type(value)
        # print value_type
        if (value_type is list):
            value_len = len(value)
            temp = range(value_len)
            for x in range(value_len):
                # print(value[x])
                temp[x] = epics.caget(value[x])
                if temp[x] == None:
                    temp[x] = np.nan
                print(str(value[x]) + ' value is: ' + str(temp[x]))
                setattr(PCav_val, property, temp)
        else:
            value1 = epics.caget(value)
            if value1 == None:
                value1 = np.nan            
            setattr(PCav_val, property, value1)
            print(str(value) + ' value is: ' + str(value1))

print ('########################################################################')
print ('########################################################################')
# System and cavity value
for i in range(2):
    for property, value in vars(Cav_val[i]).iteritems():
        if 'PV' in property:
            # print property, ": ", value
            if np.isnan(value):
                if property in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max'):
                    attngood = 0
                good = 0
            else:
                good = 1
    print '\n'

for property, value in vars(PCav_val).iteritems():
    if 'PV' in property:
        # print property
        # print property, ": ", value
        # print np.isnan(value)
        # print np.any(np.isnan(value))
        if np.any(np.isnan(value)):
            if property in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max'):
                    attngood = 0
            good = 0
        else:
            good = 1

print good
print not(good)
if not(good):
    print "There is a NaN in the PV"
else:
    print "Everything is fine."

if not(attngood):
    print 'Error with amp, attn, and charge'
else:
    print 'Amp, attn, and charge is fine'





# Soft PV setup test
# SPV_setup.SPV_dib(Cav,PCav_Sys)



# trigger_pv_setup(pcav1, 'UND:R02:EVR:16', evr_chan)
# trigger_pv_setup(pcav2, 'UND:R02:EVR:17', evr_chan)



# print(pcav1.pv_trig_enable)

# for i in range(evr_chan-1):
# 	print(pcav1.pv_trig_enable[i])
# print('\n')

# for i in range(evr_chan-1):
# 	print(pcav1.pv_trig_eventcode[i])
# print('\n')

# for i in range(evr_chan-1):
# 	print(pcav1.pv_trig_event_enable[i])

# print(pcav1.Cav_Num)
# print('\n')

# for i in range(evr_chan-1):
# 	print(pcav2.pv_trig_enable[i])
# print('\n')

# for i in range(evr_chan-1):
# 	print(pcav2.pv_trig_eventcode[i])
# print('\n')

# for i in range(evr_chan-1):
# 	print(pcav2.pv_trig_event_enable[i])

# print(pcav2.Cav_Num)
# print('\n')