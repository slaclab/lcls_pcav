function a1 = trigger_pv_setup_script(cavity_name, evr_name, evr_index)
	str_out          = 'CTRL.OUT0';
	str_eventcode    = 'CTRL.ENM';
	str_event_enable = 'CTRL.ENAB';
	% p = addprop(cavity_name, "pv_trig_enable{1}")
	disp('test')
	pv_trig_enable{1} = [evr_name ':TRIG0:EVENT' str_out]
	pv_trig_eventcode{1} = [evr_name ':TRIG0:EVENT' str_eventcode]
	pv_trig_eventcode_enable{1} = [evr_name ':TRIG0:EVENT' str_event_enable]

	for index = 2:evr_index
		pv_trig_enable{index} = [evr_name num2str(index-1) str_out];
		pv_trig_eventcode{index} = [evr_name num2str(index-1) str_eventcode];
		pv_trig_eventcode_enable{index} = [evr_name num2str(index-1) str_event_enable];
	end

end