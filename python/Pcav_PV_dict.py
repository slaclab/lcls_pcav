def Pcav_PV_Init(IOC, EVR, SIOC):
    PVs = dict([
           ('Cav_PV_Humidity'      , IOC+':Humidity'),
           ('Calc_PV_Phi_jump_max' , SIOC+'747'),
           ('Calc_PV_Amp_max'      , SIOC+'745'),
           ('Cav_PV_Watchdog'      , SIOC+'751'),
           ('ADC_PV_Trig'          , EVR+':CTRL.DG0D'),
           ('Calc_PV_Time_Ctrl'    , SIOC+'744'),
           ('ADC_PV_Arm'           , IOC+':dig1:ARM'),
           ('Cav_PV_Beamf'         , 'EVNT:SYS0:1:LCLSBEAMRATE'),
           ('ADC_PV_Clk_Sel'       , IOC+':dig1:CLK'),
           ('EVR_PV_Trig_Ena'      , ''),
           ('EVR_PV_Status'        , EVR+':STATUS'),
           ('Cav_PV_BeamQ_Rb'      , 'IOC:IN20:BP01:QANN'),  #Yes, this is the same as the setpoint PV...  
           ('Calc_PV_Phi_diff'     , SIOC+'749'),
           ('Calc_PV_out_diffs'    , ''),
           ('Cav_PV_Q_Max'         , SIOC+'742'),
           ('Calc_PV_DAC_Scale'    , SIOC+'746'),
           ('EVR_PV_Trig_Eventcode' , ''),
           ('Cav_PV_BeamQ_setpoint' , 'IOC:IN20:BP01:QANN'),
           ('EVR_PV_Trig_Eventcode_Ena' , ''),
           ('EVR_PV_Trig_Delay'     , EVR+':CTRL.DG0D'),
           ('ADC_PV_Waveform'       , IOC+':dig1:WAV'),
           ('Ele_PV_Resync'         , IOC+':BTAM2:Resync'),
           ('Ele_PV_Ctrl_Time_Q'    , IOC+':PhaseShifter2:Q'),
           ('Ele_PV_Ctrl_Time_I'    , IOC+':PhaseShifter2:I')
           ])
    return PVs

def Pcav_Var_Init():
    Vars = dict([
        ('Prog_name'   ,  ''),
        ('ADC_Clk'     ,  ''),
        ('ADC_Chan'    ,  ''),
        ('ADC_Points'  ,  ''),

        ('Calc_Filter_w'    ,  ''),
        ('Calc_Wav_Time'    ,  ''),
        ('Calc_Filter_Type' ,  ''),
        ('Calc_Filter_Num'  ,  ''),
        ('Calc_Filter_Den'  ,  ''),
        ('Calc_Wav_Length'  ,  ''),
        ('Calc_Wav_Bckgrnd' ,  ''),
        ('Calc_Fbck_ADC_Thres' ,  ''),
        ('Calc_Fbck_Maxstep'  ,  ''),
        ('Calc_Fbck_VCO_Gain' ,  ''),
        ('Calc_IF_Cos'        ,  ''),
        ('Calc_Fbck_Q_Thres'  ,  ''),
        ('Calc_Filter_Poles'  ,  ''),
        ('Calc_Wav_Time_Step' ,  ''),
        ('Calc_IF_Sin'        ,  ''),
        ('Calc_Fbck_Rate'     ,  ''),        
        
        ('EVR_Trig_Ena'           ,  ''),
        ('EVR_Trig_Delay'         ,  ''),
        ('EVR_Trig_Eventcode_Ena' ,  ''),
        ('EVR_Trig_Eventcode'     ,  ''),        

        ('Cav_Set'       ,  ''),
        ('Cav_IF_Freq'   ,  ''),
        ('Cav_LO_Freq'   ,  ''),
        ('Cav_RF_Freq'   ,  ''),
        ('Cav_Num'       ,  ''),
        ('Cav_REF_Freq'  ,  '')
        ])
    return Vars