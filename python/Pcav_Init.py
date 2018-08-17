class phase_cavity_sys:
	def __init__(self):
		"""Creating all the variables that are common to all phase cavities"""
		self.Prog_name = []
		self.Cav_Set = [] # Number of pairs of pcavs really two caviy makes up one system
		self.Cav_Num = [] # Number of cavities
		self.Cav_RF_Freq  = []  # Cavity RF frequency
		self.Cav_LO_Freq  = []  # Electronic LO freq
		self.Cav_IF_Freq  = []  # Dowmixed IF freq
		self.Cav_REF_Freq = []  # VCO frequency for pcav to munipulate
		self.Cav_PV_BeamQ_Rb = []
		self.Cav_PV_Q_Max    = []
		self.Cav_PV_BeamQ_setpoint = []
		self.Cav_PV_Watchdog = []
		self.Cav_PV_Beamf  = []
		self.Cav_PV_Humidity = []
		
				
		self.Calc_Fbck_Rate = []  # Feeback rate 
		self.Calc_Fbck_VCO_Gain =  []  # rad in VCO freq per pico second
		self.Calc_Fbck_Maxstep   = []
		self.Calc_Fbck_Q_Thres   = []
		self.Calc_Fbck_ADC_Thres = []
		self.Calc_PV_Time_Ctrl = [] # time control (?) (ps)
		self.Calc_PV_DAC_Scale = [] # DAC I/Q scale (V)
		self.Calc_PV_Phi_jump_max = [] # limit for RF resync (ps)
		self.Calc_PV_Phi_diff = [] # rms(cav1 - cav2)
		self.Calc_PV_out_diffs = []
		self.Calc_PV_Amp_max = []
		
		self.Calc_Wav_Length   = []
		self.Calc_Filter_Poles = []
		self.Calc_Filter_w     = []
		self.Calc_Filter_Type  = []
		self.Calc_Filter_Num   = []
		self.Calc_Filter_Den   = []

		self.Calc_Wav_Bckgrnd   = []
		self.Calc_Wav_Time_Step = []
		self.Calc_Wav_Time = []
		self.Calc_IF_Sin   = []
		self.Calc_IF_Cos   = []


		self.Ele_PV_Resync = []
		self.Ele_PV_Ctrl_Time_Q= [] # Pphase shifter #2 I & Q
		self.Ele_PV_Ctrl_Time_I= [] 

		self.EVR_Trig_Delay    = []
		self.EVR_Trig_Ena      = []
		self.EVR_Trig_Eventcode = []
		self.EVR_Trig_Eventcode_Ena = []
		self.EVR_PV_Trig_Ena       = []
		self.EVR_PV_Trig_Eventcode = []
		self.EVR_PV_Trig_Eventcode_Ena = []
		self.EVR_PV_Status     = []
		self.EVR_PV_Trig_Delay = []
		
		self.ADC_Chan       = []   # Number of ADC channels
		self.ADC_Points     = []   # ADC waveform points
		self.ADC_Clk        = []   # ADC clock sampling frequency
		self.ADC_PV_Waveform = []
		self.ADC_PV_Trig    = []
		self.ADC_PV_Arm     = []
		self.ADC_PV_Clk_Sel = []

		
		
		


