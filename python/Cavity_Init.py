class cavity_init:
    def __init__(self):
        """ Creating variables that is only unique to each cavity """
        self.Ele_PV_Heater  = []
        self.Ele_PV_Temper  = []
        self.Ele_PV_Phi_Ctrl = [] # Variable static.pv.ctrl.dac in MATLAB (new stepper motor style phase shifter 4/2/2013)
        self.Ele_PV_Phi_Shift_ps = [] # Variable static.pv.out.phase_shift_ps
        self.Ele_PV_Phi_Shift_476_Deg = [] # Variable static.pv.out.phase_shifter
        # self.Ele_PV_Ctrl_Time= [] # Pphase shifter #2 I & Q
        self.Ele_PV_Atten1   = []
        self.Ele_PV_Atten2   = []
        self.Ele_PV_Amp1     = []
        self.Ele_PV_Amp2     = []
        self.Ele_PV_Status1  = []
        self.Ele_PV_Status2  = []
        self.Ele_PV_Cav_Gain1 = []
        self.Ele_PV_Cav_Gain2 = []

        self.Ele_Attn_start = []
        self.Ele_Attn_end   = []
        self.Ele_Attn_val   = []
        self.Ele_Amp_gain1   = []
        self.Ele_Amp_gain2   = []
        self.Ele_Attn_Phi_Shift1 = []
        self.Ele_Attn_Phi_Shift2 = []
        self.Ele_Attn_Gain1 = []
        self.Ele_Attn_Gain2 = []
        self.Ele_bckg1 = []
        self.Ele_bckg2 = []


        self.Cav_PV_bld_phase_rotation  = []
        self.Cav_PV_bld_charge_scale    = []
        self.Cav_PV_bld_cav_freq        = []
        self.Cav_PV_bld_prec_start      = []
        self.Cav_PV_Scale1     = []
        self.Cav_PV_Scale2     = []
        self.Cav_PV_Offset1    = []
        self.Cav_PV_Offset2    = []
        self.Cav_PV_Charge1    = []
        self.Cav_PV_Charge2    = []
        self.Cav_PV_Time1      = []
        self.Cav_PV_Time2      = []
        self.Cav_PV_Freq1      = []
        self.Cav_PV_Freq2      = []
        self.Cav_PV_MaxCounts1 = []
        self.Cav_PV_MaxCounts2 = []
        self.Cav_PV_Q1 = []
        self.Cav_PV_Q2 = []
                
        self.Calc_PV_Time_Std1  = []
        self.Calc_PV_Time_Std2  = []
        self.Calc_PV_Time_Diff1 = []
        self.Calc_PV_Time_Diff2 = []
        self.Calc_PV_Fbck_Gain1 = []
        self.Calc_PV_Fbck_Gain2 = []
        self.Calc_PV_StartTime1 = []
        self.Calc_PV_StartTime2 = []

        self.Calc_Window_Crude_Time = [] # Windowing for the caputred waveform record number in seconds after ADC triggered
        self.Calc_Window_Fit_Time   = [] 
        self.Calc_Window_Exact_Time = []