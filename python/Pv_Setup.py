from Pcav_PV_dict import *


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

	Cav_Sys.Calc_PV_out_diffs = range(15)
	k = range(701, 716, 1)
	# print len(Cav_Sys.Calc_PV_out_diffs)
	# print len(k)
	for i in range(15):
		Cav_Sys.Calc_PV_out_diffs[i] = SIOC + str(k[i])		

def Pcav_CAV_Var_setup(Cav_Sys):
	pass


def trigger_pv_setup(Cav_Sys, evr='', evr_index=1):
	"""creating the trigger PV variables"""
	Str_Out          = 'CTRL.OUT0'
	Str_Eventcode    = 'CTRL.ENM'
	Str_Event_Enable = 'CTRL.ENAB'
	
	Cav_Sys.EVR_PV_Trig_Ena = range(evr_index-1)
	Cav_Sys.EVR_PV_Trig_Eventcode = range(evr_index-1)
	Cav_Sys.EVR_PV_Trig_Eventcode_Ena = range(evr_index-1)
	# Cav_Sys.PV_EVR_Stat = evr + ':STATUS'
	# Cav_Sys.PV_ADC_Trig = evr + ':CTRL.DG0D'

	for i in range(evr_index-1):
		if i == 0:
			Cav_Sys.EVR_PV_Trig_Ena[i] = evr + 'TRIG0:EVENT' + Str_Out
			Cav_Sys.EVR_PV_Trig_Eventcode[i] = evr + 'TRIG0:EVENT' + Str_Eventcode
			Cav_Sys.EVR_PV_Trig_Eventcode_Ena[i] = evr + 'TRIG0:EVENT' + Str_Event_Enable
		else:
			Cav_Sys.EVR_PV_Trig_Ena[i] = evr + ':EVENT' + str(i) + Str_Out
			Cav_Sys.EVR_PV_Trig_Eventcode[i] = evr + 'EVENT' + str(i) + Str_Eventcode
			Cav_Sys.EVR_PV_Trig_Eventcode_Ena[i] = evr + 'EVENT' + str(i) + Str_Event_Enable
		# print(cavity.pv_trig_enable[i])
	

def PV_maker(first='', second='', third='', fourth=''):
	"""Makes a PV string with 4 values concated"""
	pass
