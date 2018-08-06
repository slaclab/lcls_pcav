class cavity_init:
    def __init__(self):
        """ Creating variables that is only unique to each cavity """
        self.Ele_PV_Heater  = []
        self.Ele_PV_Temper  = []
        self.Ele_PV_Phi_Ctrl = [] # Variable static.pv.ctrl.dac in MATLAB (new stepper motor style phase shifter 4/2/2013)
        self.Ele_PV_Phi_Shift_ps = [] # Variable static.pv.out.phase_shift_ps
        self.Ele_PV_Phi_Shift_476_Deg = [] # Variable static.pv.out.phase_shifter
        self.Ele_PV_Ctrl_Time= [] # Pphase shifter #2 I & Q
        self.Ele_PV_Atten    = []
        self.Ele_PV_Amp      = []
        self.Ele_PV_Status   = []
        self.Ele_PV_Cav_Gain = []

        self.Ele_Attn_start = []
        self.Ele_Attn_end   = []
        self.Ele_Attn_val   = []
        self.Ele_Amp_gain   = []        
        self.Ele_Attn_Phi_Shift = []
        self.Ele_Attn_Gain = []
        self.Ele_bckg = []


        self.Cav_PV_bld_phase_rotation  = []
        self.Cav_PV_bld_charge_scale    = []
        self.Cav_PV_bld_cav_freq        = []
        self.Cav_PV_bld_prec_start      = []
        self.Cav_PV_Scale     = []
        self.Cav_PV_Offset    = []
        self.Cav_PV_Charge    = []
        self.Cav_PV_Time      = []
        self.Cav_PV_Freq      = []
        self.Cav_PV_MaxCounts = []
        self.CAV_PV_Q = []
                
        self.Calc_PV_Time_Std  = []
        self.Calc_PV_Time_Diff = []
        self.Calc_PV_Fbck_Gain = []
        self.Calc_PV_StartTime = []

        self.Calc_Window_Crude_Time = [] # Windowing for the caputred waveform record number in seconds after ADC triggered
        self.Calc_Window_Fit_Time   = [] 
        self.Calc_Window_Exact_Time = []