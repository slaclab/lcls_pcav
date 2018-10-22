classdef pcavity < dynamicprops
    properties
        num_cavities
        num_chans
        num_points
        num_waveform_length
        num_array_waveform
        pv_dig_trigger   % digitizer trigger delay PV
        pv_dig_arm       % digitizer trigger arm
        pv_digclockmode  % digitizer clock mode
        
        % cavity PV names
        pv_cavity_heater
        pv_cavity_temps

        % control PV names
        pv_ctrl_dac
        pv_ctrl_time
        pv_ctrl_atten
        pv_ctrl_amp
        
        % chassis status bits
        pv_status
        
        % beamline data PV names
        pv_bld_phase_rotation
        pv_bld_charge_scale
        pv_bld_cav_freq
        pv_bld_prec_start

        pv_trig_delay
    end
    methods
    function obj = trigger_pv_setup(self, evr_name, evr_index)
    	str_out          = 'CTRL.OUT0';
    	str_eventcode    = 'CTRL.ENM';
    	str_event_enable = 'CTRL.ENAB';
    	pv_trig_enable{1} = [evr_name ':TRIG0:EVENT' str_out]
    	pv_trig_eventcode{1} = [evr_name ':TRIG0:EVENT' str_eventcode]
    	pv_trig_eventcode_enable{1} = [evr_name ':TRIG0:EVENT' str_event_enable]

    	for index = 2:evr_index
    		pv_trig_enable{index} = [evr_name num2str(index-1) str_out];
    		pv_trig_eventcode{index} = [evr_name num2str(index-1) str_eventcode];
    		pv_trig_eventcode_enable{index} = [evr_name num2str(index-1) str_event_enable];
    	end
    end

end

end
