from Pcav_init import *
from Pv_Setup *

pcav1 = phase_cavity()


# pcav1.pv_trig_enable = 'test0'
# pcav1.pv_trig_enable1 = 'test1'

# print(pcav1.pv_trig_enable0)

evr_chan = 15
trigger_pv_setup(pcav1, 'UND:R02:EVR:16', evr_chan)


for i in range(evr_chan-1):
	print(pcav1.pv_trig_enable[i])

print('\n')

for i in range(evr_chan-1):
	print(pcav1.pv_trig_eventcode[i])

print('\n')

for i in range(evr_chan-1):
	print(pcav1.pv_trig_event_enable[i])
