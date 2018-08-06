import Pcav_Init as sys_setup
import Cavity_Init as cavity_setup
import Pv_Setup as PV

pre = 'SIOC:SYS0:ML00:AO'
IOC = 'UND:R02:IOC:16'
EVR = 'UND:R02:EVR:16'

Cavity_Set   = 2
Cavity_Num   = Cavity_Set * 2
ADC_Points   = 1024
Cav_Freq     = 2805e6
Cav_LO       = 2856e6
REF_VCO_Freq = 476e6
evr_chan = 15

Cav = range(Cavity_Set)
PCav_Sys = sys_setup.phase_cavity_sys()
for i in range(Cavity_Set):
    Cav[i] = cavity_setup.cavity_init()
# Cav1 = cavity_setup.cavity_init()
# Cav2 = cavity_setup.cavity_init()

PV.Pcav_PV_setup(PCav_Sys, IOC, EVR, pre)
PV.trigger_pv_setup(PCav_Sys, EVR, evr_chan)
PV.Pcav_CAV_Var_setup(PCav_Sys)

for property, value in vars(PCav_Sys).iteritems():
    if "PV" not in property:
        # if value == "":
        print property, ": ", value
        # print('\n')

# for property, value in vars(Cav[0]).iteritems():
#     print property, ": ", value
    

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