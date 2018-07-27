def trigger_pv_setup(cavity, evr_name, evr_index):
	"creating the trigger PV variables"
	str_out          = 'CTRL.OUT0'
	str_eventcode    = 'CTRL.ENM'
	str_event_enable = 'CTRL.ENAB'
	
	cavity.pv_trig_enable = range(evr_index-1)
	cavity.pv_trig_eventcode = range(evr_index-1)
	cavity.pv_trig_event_enable = range(evr_index-1)

	for i in range(evr_index-1):
		if i == 0:
			cavity.pv_trig_enable[i] = evr_name + 'TRIG0:EVENT' + str_out
			cavity.pv_trig_eventcode[i] = evr_name + 'TRIG0:EVENT' + str_eventcode
			cavity.pv_trig_event_enable[i] = evr_name + 'TRIG0:EVENT' + str_event_enable
		else:
			cavity.pv_trig_enable[i] = evr_name + ':EVENT' + str(i) + str_out
			cavity.pv_trig_eventcode[i] = evr_name + 'EVENT' + str(i) + str_eventcode
			cavity.pv_trig_event_enable[i] = evr_name + 'EVENT' + str(i) + str_event_enable
		# print(cavity.pv_trig_enable[i])

