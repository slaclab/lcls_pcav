import SPV_Comment_dict as SCD
import numpy as np
import epics

def setup(PV, DESC, EGU, PREC, SCRIPT):
    val    = [DESC, EGU, PREC, SCRIPT]
    fields = ['.DESC', '.EGU', '.PREC']
    
    print PV
    temp = PV.split(':')
    tempPV = 'SIOC'
    temp1 = temp[len(temp)-1]
    scriptPV = 'S'

    for i in range(1, len(temp1), 1):
        # print temp1[i]
        scriptPV = scriptPV + temp1[i]
  
    temp[len(temp)-1] =  scriptPV
        
    for i in range(1, len(temp), 1):
        tempPV = tempPV + ':' + temp[i] 
        # print tempPV
    
    for i in range(len(val)):
        if i < len(val)-1:
            print PV+fields[i] + ' ' + str(val[i])
            # epics.caput(PV+fields[i], str(val[i]))
        else:
            print tempPV + ' ' + str(val[i])
            # epics.capug(tempPV, str(val[i]))

def SPV_dib(Cav, Cav_Sys):
    for i in range(Cav_Sys.Cav_Set+1):
        # print i
        if i == 2:
            for property, value in vars(Cav_Sys).iteritems():
                if property in SPV_dict:
                    temp = SPV_dict[property]
                    if np.size(value) > 1:
                        print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                        print np.size(value)
                        print property                     
                        for x in range(np.size(value)):
                            # print value[x]
                            setup(value[x], temp[0], temp[1], temp[2], Cav_Sys.Prog_name)
                        print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                    else:
                        print property
                        setup(value, temp[0], temp[1], temp[2], Cav_Sys.Prog_name)
        else:
            for property, value in vars(Cav[i]).iteritems():
                SPV_dict = SCD.SPV_Comment_dict(i+1)
                if property in SPV_dict:
                    if np.size(value) > 1:
                        print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                        print np.size(value)
                        print property                     
                        for x in range(np.size(value)):
                            # print value[x]
                            setup(value[x], temp[0], temp[1], temp[2], Cav_Sys.Prog_name)
                        print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                    else:
                        temp = SPV_dict[property]
                        print property
                        setup(value, temp[0], temp[1], temp[2], Cav_Sys.Prog_name)
                