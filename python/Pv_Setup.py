from Pcav_PV_dict import *
from Cavity_PV_dict import *
from scipy import signal
import numpy as np
import math
import matplotlib.pyplot as plt


def Cavity_PV_setup(Cav,IOC, SIOC, BLD_IOC, Set):
	CPV_dict = Cavity_PV_Init(IOC, SIOC, BLD_IOC, Set)
	for property, value in vars(Cav).iteritems():
		if property in CPV_dict:	
			# print property
			# if CPV_dict[property]
			# print type(CPV_dict[property])
			value = CPV_dict[property]
			setattr(Cav, property, value)
			# print property, ": ", value
			# print property, ": ", PV_dict[str(property)]

def Electronic_Atten_calibration(Cav, Set):
	atten_usable = Cav.Ele_Attn_end - Cav.Ele_Attn_start + 1 
	if Set == 1:
		atten_phi_val1 = [0]*atten_usable
		atten_phi_val2 = [0]*atten_usable
		atten_gain_val1 = [0.1877, 0.3236, 0.5663, 1.0000, 1.7702, 3.1294, 5.6230]
		atten_gain_val2 = [0.2387, 0.3714, 0.6063, 1.0000, 1.7079, 3.1206, 5.4714]
		Cav.Ele_Attn_Phi_Shift1[Cav.Ele_Attn_start-1:Cav.Ele_Attn_end] = atten_phi_val1
		Cav.Ele_Attn_Phi_Shift2[Cav.Ele_Attn_start-1:Cav.Ele_Attn_end] = atten_phi_val2
		Cav.Ele_Attn_Gain1[Cav.Ele_Attn_start-1:Cav.Ele_Attn_end] = atten_gain_val1
		Cav.Ele_Attn_Gain2[Cav.Ele_Attn_start-1:Cav.Ele_Attn_end] = atten_gain_val2		
	else: 
		atten_phi_val1 = [7.75, 4.6, 13.9, 0, 9.7, 4.8, 11]
		atten_phi_val2 = [6.35, 5.8, 13.3, 0, 6.7, 6.4, 11.3]
		atten_gain_val1 = [0.1939, 0.3305, 0.5767, 1.0000, 1.7723, 3.0995, 5.4857]
		atten_gain_val2 = [0.1835, 0.3218, 0.5624, 1.0000, 1.7624, 3.1579, 5.5128]		
		Cav.Ele_Attn_Phi_Shift1[Cav.Ele_Attn_start-1:Cav.Ele_Attn_end] = atten_phi_val1
		Cav.Ele_Attn_Phi_Shift2[Cav.Ele_Attn_start-1:Cav.Ele_Attn_end] = atten_phi_val2
		Cav.Ele_Attn_Gain1[Cav.Ele_Attn_start-1:Cav.Ele_Attn_end] = atten_gain_val1
		Cav.Ele_Attn_Gain2[Cav.Ele_Attn_start-1:Cav.Ele_Attn_end] = atten_gain_val2				
	# print atten_phi_val1
	# print Cav.Ele_Attn_Phi_Shift1
	# print atten_phi_val2
	# print Cav.Ele_Attn_Phi_Shift2
	# print atten_gain_val1
	# print Cav.Ele_Attn_Gain1
	# print atten_gain_val2
	# print Cav.Ele_Attn_Gain2

def Pcav_PV_setup(Cav_Sys, IOC, evr, SIOC):
	PV_dict = Pcav_PV_Init(IOC, evr, SIOC)
	Vars_dict = Pcav_Var_Init()
	for property, value in vars(Cav_Sys).iteritems():
		if "PV" in property:
			value = PV_dict[property]
			setattr(Cav_Sys, property, value)
			# print property, ": ", value
			# print property, ": ", PV_dict[str(property)]
		else:
			value = Vars_dict[property]
			setattr(Cav_Sys, property, value)

	Cav_Sys.Calc_PV_out_diffs = range(16)
	k = range(701, 717, 1)
	# print k
	# print len(Cav_Sys.Calc_PV_out_diffs)
	# print len(k)
	for i in range(16):
		Cav_Sys.Calc_PV_out_diffs[i] = SIOC + str(k[i])
		

def Filter_Init(Cav_Sys):
	Cav_Sys.Calc_Filter_w     = 0.12
	Cav_Sys.Calc_Filter_Poles = 3
	Cav_Sys.Calc_Filter_Type  = 'butter'
	Cav_Sys.Calc_Filter_Num, Cav_Sys.Calc_Filter_Den = signal.butter(Cav_Sys.Calc_Filter_Poles, Cav_Sys.Calc_Filter_w, 'low')

def EVR_Delay(Cav_Sys):
	Delay1 = np.array([140, 106030])
	Delay2 = np.array([150, 106020])
	Delay3 = np.array([43,  107578])
	Cav_Sys.EVR_Trig_Delay = np.array([Delay1, Delay2, Delay3])
	# print(Cav_Sys.EVR_Trig_Delay[:,0])

def IF_Sin_Cos(Cav_Sys):
	Cav_Sys.Calc_Wav_Time = np.arange(0, Cav_Sys.ADC_Points/Cav_Sys.ADC_Clk, 1/Cav_Sys.ADC_Clk)
	Cav_Sys.Calc_IF_Sin = np.sin(2*np.pi*Cav_Sys.Cav_IF_Freq*Cav_Sys.Calc_Wav_Time)
	Cav_Sys.Calc_IF_Cos = np.cos(2*np.pi*Cav_Sys.Cav_IF_Freq*Cav_Sys.Calc_Wav_Time)
	# plt.plot(Cav_Sys.Calc_Wav_Time, Cav_Sys.Calc_IF_Sin)
	# plt.plot(Cav_Sys.Calc_Wav_Time, Cav_Sys.Calc_IF_Cos)
	# plt.show()

def Script_name(Cav_Sys, Prog_name):
	Cav_Sys.Prog_name = Prog_name
	

def CAV_ADC_Var_setup(Cav_Sys, Cav_set, Cav_Num, Cav_REF_f, ADC_CLK, IF_f, RF_f, LO_f, ADC_Chan, ADC_Point):
	Cav_Sys.ADC_Clk = ADC_CLK
	Cav_Sys.Cav_IF_Freq = IF_f
	Cav_Sys.Cav_RF_Freq = RF_f
	Cav_Sys.Cav_LO_Freq = LO_f
	Cav_Sys.Cav_Set = Cav_set
	Cav_Sys.ADC_Chan = ADC_Chan
	Cav_Sys.ADC_Points = ADC_Point
	Cav_Sys.Cav_Num = Cav_Num
	Cav_Sys.Cav_REF_Freq = Cav_REF_f

def Fbck_Var_setup(Cav_Sys, ADC_Thres, Max_Step, VCO_Gain, Q_Thres, Rate):
	Cav_Sys.Calc_Fbck_ADC_Thres = ADC_Thres
	Cav_Sys.Calc_Fbck_Maxstep   = Max_Step
	Cav_Sys.Calc_Fbck_VCO_Gain  = VCO_Gain
	Cav_Sys.Calc_Fbck_Q_Thres   = Q_Thres
	Cav_Sys.Calc_Fbck_Rate      = Rate



def trigger_pv_setup(Cav_Sys, evr='', evr_index=1):
	"""creating the trigger PV variables"""
	Str_Out          = 'CTRL.OUT0'
	Str_Eventcode    = 'CTRL.ENM'
	Str_Event_Enable = 'CTRL.ENAB'
	
	Cav_Sys.EVR_PV_Trig_Ena = range(evr_index)
	Cav_Sys.EVR_PV_Trig_Eventcode = range(evr_index)
	Cav_Sys.EVR_PV_Trig_Eventcode_Ena = range(evr_index)
	Cav_Sys.EVR_Trig_Ena = np.zeros(evr_index)
	Cav_Sys.EVR_Trig_Eventcode_Ena = np.zeros(evr_index)
	Cav_Sys.EVR_Trig_Eventcode     = np.zeros(evr_index)
	# print(np.size(Cav_Sys.EVR_Trig_Ena))
	# print(np.size(Cav_Sys.EVR_Trig_Eventcode_Ena))
	# print(np.size(Cav_Sys.EVR_Trig_Eventcode))
	# Cav_Sys.PV_EVR_Stat = evr + ':STATUS'
	# Cav_Sys.PV_ADC_Trig = evr + ':CTRL.DG0D'

	for i in range(evr_index):
		if i == 0:
			Cav_Sys.EVR_PV_Trig_Ena[i] = evr + ':TRIG0:EVENT' + Str_Out
			Cav_Sys.EVR_PV_Trig_Eventcode[i] = evr + ':TRIG0:EVENT' + Str_Eventcode
			Cav_Sys.EVR_PV_Trig_Eventcode_Ena[i] = evr + ':TRIG0:EVENT' + Str_Event_Enable
		else:
			Cav_Sys.EVR_PV_Trig_Ena[i] = evr + ':EVENT' + str(i) + Str_Out
			Cav_Sys.EVR_PV_Trig_Eventcode[i] = evr + ':EVENT' + str(i) + Str_Eventcode
			Cav_Sys.EVR_PV_Trig_Eventcode_Ena[i] = evr + ':EVENT' + str(i) + Str_Event_Enable
		# print(Cav_Sys.EVR_PV_Trig_Ena[i])
		# print(Cav_Sys.EVR_PV_Trig_Eventcode[i])
		# print(Cav_Sys.EVR_PV_Trig_Eventcode_Ena[i])

	# print(len(Cav_Sys.EVR_PV_Trig_Ena))
	# print(len(Cav_Sys.EVR_PV_Trig_Eventcode))
	# print(len(Cav_Sys.EVR_PV_Trig_Eventcode_Ena))
	

def PV_maker(first='', second='', third='', fourth=''):
	"""Makes a PV string with 4 values concated"""
	pass
