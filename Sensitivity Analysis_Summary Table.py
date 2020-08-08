from __future__ import division
import numpy as np
import os
os.chdir('/Users/yhu22/Dropbox/My Work/Covid-19/GitHub')
import random

c_v = 60000
ratio_ven_to_mv = 1 / 5
c_h = c_v * ratio_ven_to_mv
duration = 272

Death_R = []
Days_R = [] 

random.seed(4) 

for j in range(100):
    
    execfile("Parameter_Random Sample.py") 

    if sum(Test) != 0:
        continue
    
    execfile("Policy_No_HFNC.py") 
            
    execfile("Policy_HFNC_Ext_MV_10.py") 

    Death_R.append(round(Obj_Policy_1 - Obj_Proposed_10_Post))
    Days_R.append(round((MV_Full_Policy_1 - MV_Full_Proposed_10_Post) * duration))

  
print min(Death_R), max(Death_R)

print min(Days_R), max(Days_R)

print np.sum([x > 0 for x in Days_R]) / len(Days_R)

print np.sum([x == 0 for x in Days_R]) / len(Days_R)

print np.sum([x < 0 for x in Days_R]) / len(Days_R)

