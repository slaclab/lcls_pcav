def SPV_Comment_dict(Set):
    if Set == 1:
        Set_dic = dict([
            ('Phi_Shift_476', 'Phase control NEH'),
            ('Phi_Shift_ps' , 'Phase shift FEH'),
            ('Cav_1'        , 'Cav 1 '),
            ('Cav_2'        , 'Cav 2 ')
        ])
    else:
        Set_dic = dict([
            ('Phi_Shift_476', 'Phase control NEH'),
            ('Phi_Shift_ps' , 'Phase shift FEH'),
            ('Cav_1'        , 'Cav 3 '),
            ('Cav_2'        , 'Cav 4 ')            
        ])

    Comment_val = dict([
        ('Cav_PV_Q_Max'             , ['Full signal charge'     ,'pC',       2]),
        ('Calc_PV_Time_Ctrl'        , ['Time control'           ,'ps',       3]),
        ('Calc_PV_Amp_max'          , ['Amplifier charge threshold', 'pC',   1]),
        ('Calc_PV_DAC_Scale'        , ['DAC scale'              ,'V',        2]),
        ('Calc_PV_Phi_jump_max'     , ['Phase jump tolerance'   ,'ps',       2]),
        ('Ele_PV_Phi_Shift_476_Deg' , [Set_dic['Phi_Shift_476'] ,'rad476',   3]),
        ('Ele_PV_Phi_Shift_ps'      , [Set_dic['Phi_Shift_ps']  ,'ps',       3]),
        ('Calc_PV_Phi_diff'         , ['(Cav1 - Cav2) noise'    ,'ps',       4]),
        ('Calc_PV_out_diffs'        , ['Difference signals'     ,'ps',       3]),
        ('Cav_PV_Scale1'            , [Set_dic['Cav_1']+'scale (in)' ,'arb',  2]),
        ('Cav_PV_Scale2'            , [Set_dic['Cav_2']+'scale (in)' ,'arb',  2]),
        ('Cav_PV_Offset1'           , [Set_dic['Cav_1']+'phase offset (in)' ,'arb',  2]),
        ('Cav_PV_Offset2'           , [Set_dic['Cav_2']+'phase offset (in)' ,'arb',  2]),
        ('Ele_PV_Cav_Gain1'         , [Set_dic['Cav_1']+'attenuator (in)'   , '1:15', 0]),
        ('Ele_PV_Cav_Gain2'         , [Set_dic['Cav_2']+'attenuator (in)'   , '1:15', 0]),
        ('Calc_PV_Fbck_Gain1'       , [Set_dic['Cav_1']+'feedback gain (in)', 'arb' , 4]),
        ('Calc_PV_Fbck_Gain2'       , [Set_dic['Cav_2']+'feedback gain (in)', 'arb' , 4]),
        ('Calc_PV_StartTime1'       , [Set_dic['Cav_1']+'start time (in)', 'ps'  , 3]),
        ('Calc_PV_StartTime2'       , [Set_dic['Cav_2']+'start time (in)', 'ps'  , 3]),
        ('Cav_PV_Charge1'           , [Set_dic['Cav_1']+'charge  (out)'  , 'pC'  , 2]),
        ('Cav_PV_Charge2'           , [Set_dic['Cav_2']+'charge  (out)'  , 'pC'  , 2]),
        ('Cav_PV_Time1'             , [Set_dic['Cav_1']+'time  (out)'    , 'ps'  , 3]),
        ('Cav_PV_Time2'             , [Set_dic['Cav_2']+'time  (out)'    , 'ps'  , 3]),
        ('Cav_PV_Freq1'             , [Set_dic['Cav_1']+'frequency-2805 (out)'  , 'MHz' , 4]),
        ('Cav_PV_Freq2'             , [Set_dic['Cav_2']+'frequency-2805 (out)'  , 'MHz' , 4]),
        ('Cav_PV_MaxCounts1'        , [Set_dic['Cav_1']+'max dig counts (out)'  , 'cts' , 0]),
        ('Cav_PV_MaxCounts2'        , [Set_dic['Cav_2']+'max dig counts (out)'  , 'cts' , 0]),
        ('Cav_PV_MaxCounts2'        , [Set_dic['Cav_2']+'max dig counts (out)'  , 'cts' , 0]),
        ('Calc_PV_Time_Std1'        , [Set_dic['Cav_1']+'std deviation (out)'   , 'ps'  , 3]),
        ('Calc_PV_Time_Std2'        , [Set_dic['Cav_2']+'std deviation (out)'   , 'ps'  , 3]),
        ('Calc_PV_Time_Diff1'       , [Set_dic['Cav_1']+'diff to Cav 1 (out)'   , 'ps'  , 3]),
        ('Calc_PV_Time_Diff2'       , [Set_dic['Cav_2']+'diff to Cav 1 (out)'   , 'ps'  , 3]),
        ('Q1'                       , [Set_dic['Cav_1']+'Q (out)'               , 'arb' , 1]),
        ('Q2'                       , [Set_dic['Cav_2']+'Q (out)'               , 'arb' , 1])        
    ])
    return Comment_val