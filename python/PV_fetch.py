import epics as epics
import time as time
import datetime as datetime
import numpy as np

def PV_collect(Cav_class, class_type, Cav_val, new_time, good, attngood, triggood, statgood, mmsgood):   
    if (class_type != 1):
        # Fetching PV Values for individual cavity values
        for i in range(2):
            for property, value in vars(Cav_class[i]).iteritems():
                if 'PV' in property:
                    # print property, ": ", value
                    # print type(value)
                    value1 = epics.caget(value)
                    if value1 == None:
                        value1 = np.nan
                        good = 0
                        # Check if any of the attn/amp/charge PV value is NaN
                        if any(ptemp in property for ptemp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
                            attngood = 0
                            # print('Error with attn/amp/charge PV value')
                        # Check if any of the EVR PV value is NaN
                        elif any(ptemp in value for ptemp in ('EVR', 'evr')):
                            triggood = 0
                            # print('Error with EVR PV value')
                        # Check if the MMS phase shifter is NaN
                        elif 'Ele_PV_Phi_Ctrl' in property:
                            mmsgood  = 0
                            # print('Error with the MMS phase shifter')
                    # Check chassis status bit    
                    if any(ptemp in property for ptemp in ('Status', 'status')):
                        statgood = 0
                        # print('Error with AFE chassis status')     
                    setattr(Cav_val[i], property, value1)
                    print(str(value) + ' value is: ' + str(value1))
        new_time = datetime.datetime.now()                                
    else:
        # Fetching PV value for the Phase Cavity system values
        for property, value in vars(Cav_class).iteritems():
            if 'PV' in property:
                value_type = type(value)
                # print value_type
                # Checks if the PV name is in a list like the EVR PVs.
                if (value_type is list):
                    value_len = len(value)
                    temp = range(value_len)
                    for x in range(value_len):
                        # print(value[x])
                        temp[x] = epics.caget(value[x])
                        if temp[x] == None:
                            temp[x] = np.nan
                            good = 0
                            # Check if any of the attn/amp/charge PV value is NaN
                            if any(ptemp in property for ptemp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
                                attngood = 0
                            # Check if any of the EVR PV value is NaN    
                            elif any(ptemp in value[x] for ptemp in ('EVR','evr')):
                                triggood = 0
                            # Check if the MMS phase shifter is NaN                        
                            elif 'Ele_PV_Phi_Ctrl' in property:
                                mmsgood  = 0                    
                        # Check chassis status bit    
                        if (any(ptemp in property for ptemp in ('Status', 'status')) and (temp[x] != 0)):
                            statgood = 0
                            # print('Error with AFE chassis status')                            
                        print(str(value[x]) + ' value is: ' + str(temp[x]))
                        setattr(Cav_val, property, temp)
                else:
                    value1 = epics.caget(value)
                    if value1 == None:
                        value1 = np.nan            
                        good = 0
                        # Check if any of the attn/amp/charge PV value is NaN
                        if any(ptemp in property for ptemp in ('Atten','Amp','Cav_PV_BeamQ_Rb','Cav_PV_Q_Max')):
                            attngood = 0
                            # print('Error with attn/amp/charge PV value')
                        # Check if any of the EVR PV value is NaN
                        elif any(ptemp in value for ptemp in ('EVR', 'evr')):
                            triggood = 0
                            # print('Error with EVR PV value')
                        # Check if the MMS phase shifter is NaN
                        elif 'Ele_PV_Phi_Ctrl' in property:
                            mmsgood  = 0
                            # print('Error with the MMS phase shifter')
                    # Check chassis status bit    
                    if (any(ptemp in property for ptemp in ('Status', 'status')) and (value1 != 0)):
                        statgood = 0
                        # print('Error with AFE chassis status') 
                    setattr(Cav_val, property, value1)
                    print(str(value) + ' value is: ' + str(value1))
        new_time = datetime.datetime.now()
            
    return new_time, good, attngood, triggood, statgood, mmsgood