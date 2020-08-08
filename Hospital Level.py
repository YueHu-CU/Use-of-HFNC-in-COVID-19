from __future__ import division
import numpy as np
import os
os.chdir('/Users/yhu22/Dropbox/My Work/Covid-19/GitHub')
import scipy.stats
import random

def mean_confidence_interval(data, confidence = 0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

# Parameters to enumerate
MV_R = [25, 50, 100, 150, 200, 250]

Ratios = [3, 5, 8]

for k in Ratios:
    
    ratio_ven_to_mv = 1 / k
    Death_R = []
    Death_R_Lower = []
    Death_R_Upper = []
    
    for i in range(len(MV_R)):
        
        print "MV", MV_R[i], "Ratio", k
        
        c_v = MV_R[i] ; c_h = MV_R[i] * ratio_ven_to_mv
        
        Death_Inner = []
        random.seed(4) 
        
        for j in range(100):
            
            execfile("Parameter_Random Sample.py") 

            if sum(Test) != 0:
                continue
            
            execfile("Policy_No_HFNC.py") 
            
            execfile("Policy_HFNC_Ext_MV_10.py") 
    
            Death_Inner.append(round(Obj_Policy_1 - Obj_Proposed_10_Post))

        Death_R.append(mean_confidence_interval(Death_Inner, confidence = 0.95)[0])
        Death_R_Lower.append(mean_confidence_interval(Death_Inner, confidence = 0.95)[1])
        Death_R_Upper.append(mean_confidence_interval(Death_Inner, confidence = 0.95)[2])

    if hos_size == 100:
        Death_R[3] = 0; Death_R[4] = 0; Death_R[5] = 0
        Death_R_Lower[3] = 0; Death_R_Lower[4] = 0; Death_R_Lower[5] = 0
        Death_R_Upper[3] = 0; Death_R_Upper[4] = 0; Death_R_Upper[5] = 0
        
    if ratio_ven_to_mv == 1 / 3:
        Death_R_3 = Death_R
        Death_R_3_Lower = Death_R_Lower
        Death_R_3_Upper = Death_R_Upper
    elif ratio_ven_to_mv == 1 / 5:
        Death_R_5 = Death_R
        Death_R_5_Lower = Death_R_Lower
        Death_R_5_Upper = Death_R_Upper
    elif ratio_ven_to_mv == 1 / 8:
        Death_R_8 = Death_R
        Death_R_8_Lower = Death_R_Lower
        Death_R_8_Upper = Death_R_Upper
    
    