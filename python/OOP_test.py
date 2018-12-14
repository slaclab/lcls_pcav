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
    Cav[i] = cavity_setup.cavity_init()
    Cav_val[i] = cavity_setup.cavity_init()

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


while True:
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

    print ('########################################################################')
    print ('########################################################################')
    # Change print into Log in the future
    print(new_time)

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
    
    # Error report for any NaN values
    if not(good):
        print "There is a NaN in the PV"
    else:
        print "No NaN values"

    print('########################################################################')
    print('########################################################################')
    if not(good):
        continue
    time.sleep(1.5)
    print('    ROFL:ROFL:LOL:ROFL:ROFL')
    print('            ___^___ _      ')
    print('    L    __/      [] \     ') 
    print('   LOL===__           \    ')
    print('    L      \___ ___ ___]   ')
    print('               I   I       ')
    print('            ----------/    ')

# Set correct Amp/Attn setting
    if attngood:
        charge_ratio = 1e3 * (PCav_val.Cav_PV_BeamQ_Rb / PCav_val.Cav_PV_Q_Max)
        # print charge_ratio
        for i in range(2):
            blah0 = np.multiply(charge_ratio, Cav[i].Ele_Attn_Gain1)
            blah1 = np.multiply(charge_ratio, Cav[i].Ele_Attn_Gain2)
            attn_ind = np.nonzero(blah0 >= 1)[0][0]
            # print attn_ind
            if not attn_ind:
                attn_ind = 14
            amp_thres = (1e3 * PCav_val.Cav_PV_BeamQ_Rb) < PCav_val.Calc_PV_Amp_max
            if any(temp != amp_thres for temp in (Cav_val[i].Ele_PV_Amp1, Cav_val[i].Ele_PV_Amp2)):
                print('Switching high gain amplifier to ' + str(amp_thres))
                print('epics.caput(' + str(Cav[i].Ele_PV_Amp1) + ', ' + str(amp_thres) + ')')
                print('epics.caput(' + str(Cav[i].Ele_PV_Amp2) + ', ' + str(amp_thres) + ')')

            else:
                print PCav_val.Cav_PV_BeamQ_Rb
                print (1e3 * PCav_val.Cav_PV_BeamQ_Rb)
                print np.multiply(1e3, PCav_val.Cav_PV_BeamQ_Rb)
                print PCav_val.Calc_PV_Amp_max
                print amp_thres
                print Cav_val[i].Ele_PV_Amp1
                print Cav_val[i].Ele_PV_Amp2
                print('Testing caput print out')
                print('Switching high gain amplifier to ' + str(amp_thres))
                print('epics.caput(' + str(Cav[i].Ele_PV_Amp1) + ', ' + str(amp_thres) + ')')
                print('epics.caput(' + str(Cav[i].Ele_PV_Amp2) + ', ' + str(amp_thres) + ')')
                # Happy day



        
        # attn_val = 




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
