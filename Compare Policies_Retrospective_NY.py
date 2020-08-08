from __future__ import division
import os
os.chdir('/Users/yhu22/Dropbox/My Work/Covid-19/GitHub')
import matplotlib.pyplot as plt
import numpy as np

# Death - all patients
P1_1 = []; P1_1_10 = []; 
Proposed_Post = []; Proposed_10_Post = []; Proposed_20_Post = []
Proposed_Pre = []; Proposed_10_Pre = []; Proposed_20_Pre = []

# Full MV utilization
P1_1_MV = []; P1_1_MV_10 = [];
Proposed_MV_Post = []; Proposed_10_MV_Post = []; Proposed_20_MV_Post = []
Proposed_MV_Pre = []; Proposed_10_MV_Pre = []; Proposed_20_MV_Pre = []

# Death - urgent patients
P1_1_U = []; P1_1_U_10 = [];
Proposed_U_Post = []; Proposed_10_U_Post = []; Proposed_20_U_Post = []
Proposed_U_Pre = []; Proposed_10_U_Pre = []; Proposed_20_U_Pre = []

# Death - non-urgent patients
P1_1_M = []; P1_1_M_10 = [];
Proposed_M_Post = []; Proposed_10_M_Post = []; Proposed_20_M_Post = []
Proposed_M_Pre = []; Proposed_10_M_Pre = []; Proposed_20_M_Pre = []

# Death - deteriorated patients
P1_1_D = []; P1_1_D_10 = [];
Proposed_D_Post = []; Proposed_10_D_Post = []; Proposed_20_D_Post = []
Proposed_D_Pre = []; Proposed_10_D_Pre = []; Proposed_20_D_Pre = []

# Death - stabilized patients 
P1_1_S = []; P1_1_S_10 = [];
Proposed_S_Post = []; Proposed_10_S_Post = []; Proposed_20_S_Post = []
Proposed_S_Pre = []; Proposed_10_S_Pre = []; Proposed_20_S_Pre = []

# Death and deterioration - non-urgent patients
P1_1_DD = []; P1_1_DD_10 = [];
Proposed_DD_Post = []; Proposed_10_DD_Post = []; Proposed_20_DD_Post = []
Proposed_DD_Pre = []; Proposed_10_DD_Pre = []; Proposed_20_DD_Pre = []


# MV capacity to enumerate on the national level
MV_capacity = [x * 3 for x in np.arange(1, 18, 1)] 

HFNC_to_MV_ratio = 8

for i in MV_capacity:
    
    c_v = 100 * i 
    
    c_h = c_v / HFNC_to_MV_ratio
    
    execfile("Parameter.py") 
    
    execfile("Policy_No_HFNC.py") 
    
    execfile("Policy_No_HFNC_MV_10.py") 
        
    execfile("Policy_HFNC_Ext.py") 
        
    execfile("Policy_HFNC_Ext_MV_10.py") 
    
    execfile("Policy_HFNC_Ext_MV_20.py") 
    
    execfile("Policy_HFNC_Pre.py") 
        
    execfile("Policy_HFNC_Pre_MV_10.py") 
    
    execfile("Policy_HFNC_Pre_MV_20.py") 
    
    # Death - all patients
    P1_1.append((Obj_Policy_1)) 
    P1_1_10.append((Obj_Policy_1_10)) 
    Proposed_Post.append(Obj_Proposed_Post) 
    Proposed_10_Post.append(Obj_Proposed_10_Post) 
    Proposed_20_Post.append(Obj_Proposed_20_Post) 
    Proposed_Pre.append(Obj_Proposed_Pre) 
    Proposed_10_Pre.append(Obj_Proposed_10_Pre) 
    Proposed_20_Pre.append(Obj_Proposed_20_Pre) 
    
    # Full MV utilization
    P1_1_MV.append(MV_Full_Policy_1) 
    P1_1_MV_10.append(MV_Full_Policy_1_10) 
    Proposed_MV_Post.append(MV_Full_Proposed_Post) 
    Proposed_10_MV_Post.append(MV_Full_Proposed_10_Post) 
    Proposed_20_MV_Post.append(MV_Full_Proposed_20_Post) 
    Proposed_MV_Pre.append(MV_Full_Proposed_Pre) 
    Proposed_10_MV_Pre.append(MV_Full_Proposed_10_Pre) 
    Proposed_20_MV_Pre.append(MV_Full_Proposed_20_Pre) 
    
    # Death - urgent patients
    P1_1_U.append((Obj_Policy_1_U)) 
    P1_1_U_10.append((Obj_Policy_1_U_10)) 
    Proposed_U_Post.append(Obj_Proposed_U_Post) 
    Proposed_10_U_Post.append(Obj_Proposed_10_U_Post) 
    Proposed_20_U_Post.append(Obj_Proposed_20_U_Post) 
    Proposed_U_Pre.append(Obj_Proposed_U_Pre) 
    Proposed_10_U_Pre.append(Obj_Proposed_10_U_Pre) 
    Proposed_20_U_Pre.append(Obj_Proposed_20_U_Pre) 
    
    # Death and deterioration - non-urgent patients
    P1_1_DD.append((Obj_Policy_1_Non_U)) 
    P1_1_DD_10.append((Obj_Policy_1_Non_U_10)) 
    Proposed_DD_Post.append(Obj_Proposed_Non_U_Post) 
    Proposed_10_DD_Post.append(Obj_Proposed_10_Non_U_Post) 
    Proposed_20_DD_Post.append(Obj_Proposed_20_Non_U_Post) 
    Proposed_DD_Pre.append(Obj_Proposed_Non_U_Pre) 
    Proposed_10_DD_Pre.append(Obj_Proposed_10_Non_U_Pre) 
    Proposed_20_DD_Pre.append(Obj_Proposed_20_Non_U_Pre) 


###############################################################################
# Plot death - all patients
ytick = np.arange(0, 42000, 2000)
ylabel = [int(x / div) for x in ytick] 

xlabel = np.arange(0.5, 6.5, 0.5)
xtick = [x / 3 - 1 for x in np.arange(5, 51, 5)]

lb = 22000
ub = 42000

plt.figure(figsize=(10, 8))

plt.plot(P1_1, '-', color = 'black', lw = 3, label = 'No HFNC')
plt.plot(P1_1_10, '-', color = 'green', lw = 3, label = r'No HFNC + MV$_{10}$')

plt.plot(Proposed_Post, '-', color = 'red', lw = 3, label = r'HFNC$_{ext}$')
plt.plot(Proposed_Pre, '--', color = 'red', lw = 3, label = r'HFNC$_{non\mathrm{-}urg}$')

plt.plot(Proposed_10_Post, '-', color = 'orange', lw = 3, label = r'HFNC$_{ext}$ + MV$_{10}$')
plt.plot(Proposed_10_Pre, '--', color = 'orange', lw = 3, label = r'HFNC$_{non\mathrm{-}urg}$ + MV$_{10}$')

plt.xticks(xtick, xlabel, fontsize = font)
plt.xlabel('Number of MV (K)', fontsize = font)

plt.yticks(ytick, ylabel, fontsize = font)
plt.ylabel('All patients \n Cumulated deaths (K)', fontsize = font)

plt.ylim(lb, ub)

plt.title('%x-to-1 (MV-to-HFNC)'%HFNC_to_MV_ratio, fontsize = font)

plt.annotate('Estimated capacity', xy = (8.2578, lb), xytext = (8.2578 - 3.4, 38000), fontsize = font, 
            arrowprops = dict(arrowstyle = '-|>, head_length = 0.6, head_width = 0.3',
                              color = 'black', lw = 1),
            va = 'center', multialignment = 'left')
            
#plt.legend(loc = 'upper right', fontsize = font)

plt.show()


###############################################################################
# Plot death - all patients (alternative)
ytick = np.arange(0, 42000, 2000)
ylabel = [int(x / div) for x in ytick] 

xlabel = np.arange(0.5, 6.5, 0.5)
xtick = [x / 3 - 1 for x in np.arange(5, 51, 5)]

lb = 22000
ub = 42000

plt.figure(figsize=(10, 8))

plt.plot(P1_1, '-', color = 'black', lw = 3)
plt.plot(P1_1_10, '-', color = 'green', lw = 3)

plt.plot(Proposed_Post, '-', color = 'red', lw = 3)
plt.plot(Proposed_Pre, '--', color = 'red', lw = 3)

plt.plot(Proposed_10_Post, '-', color = 'orange', lw = 3)
plt.plot(Proposed_10_Pre, '--', color = 'orange', lw = 3)

plt.xticks(xtick, xlabel, fontsize = font)
plt.xlabel('Number of MV (K)', fontsize = font)

plt.yticks(ytick, ylabel, fontsize = font)
plt.ylabel('All patients \n Cumulated deaths (K)', fontsize = font)

plt.ylim(lb, ub)

plt.title('%x-to-1 (MV-to-HFNC)'%HFNC_to_MV_ratio, fontsize = font)

plt.annotate('Estimated capacity', xy = (8.2578, lb), xytext = (8.2578 - 3.4, 38000), fontsize = font, 
            arrowprops = dict(arrowstyle = '-|>, head_length = 0.6, head_width = 0.3',
                              color = 'black', lw = 1),
            va = 'center', multialignment = 'left')
            
plt.scatter([8.2578], [current_death], color = 'blue', marker = 'x', s = 250,
            lw = 3, label = 'Current observation')

plt.legend(loc = 'upper right', fontsize = font)

plt.show()


###############################################################################
# Plot death - urgent patients
ytick = np.arange(0, 42000, 4000)
ylabel = [int(x / div) for x in ytick] 

xlabel = np.arange(0.5, 6.5, 0.5)
xtick = [x / 3 - 1 for x in np.arange(5, 51, 5)]

lb = 8000
ub = 40000

plt.figure(figsize=(10, 8))

plt.plot(P1_1_U, '-', color = 'black', lw = 3, label = 'No HFNC')
plt.plot(P1_1_U_10, '-', color = 'green', lw = 3, label = r'No HFNC + MV$_{10}$')

plt.plot(Proposed_U_Post, '-', color = 'red', lw = 3, label = r'HFNC$_{ext}$')
plt.plot(Proposed_U_Pre, '--', color = 'red', lw = 3, label = r'HFNC$_{non\mathrm{-}urg}$')

plt.plot(Proposed_10_U_Post, '-', color = 'orange', lw = 3, label = r'HFNC$_{ext}$ + MV$_{10}$')
plt.plot(Proposed_10_U_Pre, '--', color = 'orange', lw = 3, label = r'HFNC$_{non\mathrm{-}urg}$ + MV$_{10}$')

plt.xticks(xtick, xlabel, fontsize = font)
plt.xlabel('Number of MV (K)', fontsize = font)

plt.yticks(ytick, ylabel, fontsize = font)
plt.ylabel('Urgent patients \n Cumulated deaths (K)', fontsize = font)

plt.ylim(lb, ub)

plt.title('%x-to-1 (MV-to-HFNC)'%HFNC_to_MV_ratio, fontsize = font)

plt.annotate('Estimated capacity', xy = (8.2578, lb), xytext = (8.2578 - 3.4, 36000), fontsize = font, 
            arrowprops = dict(arrowstyle = '-|>, head_length = 0.6, head_width = 0.3',
                           color = 'black', lw = 1),
            va = 'center', multialignment = 'left')
            
#plt.legend(loc = 'upper right', fontsize = font)

plt.show()


###############################################################################
# Plot death and deterioration - non-urgent patients
ytick = np.arange(0, 42000, 4000)
ylabel = [int(x / div) for x in ytick] 

xlabel = np.arange(0.5, 6.5, 0.5)
xtick = [x / 3 - 1 for x in np.arange(5, 51, 5)]

lb = 0
ub = 30000

plt.figure(figsize=(10, 8))

plt.plot(P1_1_DD, '-', color = 'black', lw = 3, label = 'MV Urgent')
plt.plot(P1_1_DD_10, '-', color = 'green', lw = 3, label = 'MV Urgent')

plt.plot(Proposed_DD_Post, '-', color = 'red', lw = 3, label = 'Proposed Policy (Post)')
plt.plot(Proposed_DD_Pre, '--', color = 'red', lw = 3, label = 'Proposed Policy (Pre)')

plt.plot(Proposed_10_DD_Post, '-', color = 'orange', lw = 3, label = 'Proposed policy + 10% (Post)')
plt.plot(Proposed_10_DD_Pre, '--', color = 'orange', lw = 3, label = 'Proposed policy + 10% (Pre)')

plt.xticks(xtick, xlabel, fontsize = font)
plt.xlabel('Number of MV (K)', fontsize = font)

plt.yticks(ytick, ylabel, fontsize = font)
plt.ylabel('Non-urgent patients \n Cumulated deaths and deterioration (K)', fontsize = font)

plt.ylim(lb, ub)

plt.title('%x-to-1 (MV-to-HFNC)'%HFNC_to_MV_ratio, fontsize = font)

plt.annotate('Estimated capacity', xy = (8.2578, 0), xytext = (8.2578 - 3.4, 28000), fontsize = font, 
            arrowprops = dict(arrowstyle = '-|>, head_length = 0.6, head_width = 0.3',
                           color = 'black', lw = 1),
            va = 'center', multialignment = 'left')
            
#plt.legend(loc='upper right', fontsize = 16)

plt.show()


###############################################################################
# Plot full MV utilization (days)
duration = 181

P1_1_MV_days = [x * duration for x in P1_1_MV]
P1_1_MV_days_10 = [x * duration for x in P1_1_MV_10]
Proposed_MV_Post_days = [x * duration for x in Proposed_MV_Post]
Proposed_MV_Pre_days = [x * duration for x in Proposed_MV_Pre]
Proposed_10_MV_Post_days = [x * duration for x in Proposed_10_MV_Post]
Proposed_10_MV_Pre_days = [x * duration for x in Proposed_10_MV_Pre]

ytick_MV = np.arange(0, 141, 20) 
ylabel_MV = np.arange(0, 141, 20) 

xlabel = np.arange(0.5, 6.5, 0.5)
xtick = [x / 3 - 1 for x in np.arange(5, 51, 5)]

plt.figure(figsize=(10, 8))

plt.plot(P1_1_MV_days, '-', color = 'black', lw = 3, label = 'No HFNC')
plt.plot(P1_1_MV_days_10, '-', color = 'green', lw = 3, label = r'No HFNC + MV$_{10}$')

plt.plot(Proposed_MV_Post_days, '-', color = 'red', lw = 3, label = r'HFNC$_{ext}$')
plt.plot(Proposed_MV_Pre_days, '--', color = 'red', lw = 3, label = r'HFNC$_{non\mathrm{-}urg}$')

plt.plot(Proposed_10_MV_Post_days, '-', color = 'orange', lw = 3, label = r'HFNC$_{ext}$ + MV$_{10}$')
plt.plot(Proposed_10_MV_Pre_days, '--', color = 'orange', lw = 3, label = r'HFNC$_{non\mathrm{-}urg}$ + MV$_{10}$')

plt.xticks(xtick, xlabel, fontsize = font)
plt.xlabel('Number of MV (K)', fontsize = font)

plt.yticks(ytick_MV, ylabel_MV, fontsize = font)
plt.ylabel('Days with no available MV', fontsize = font)

plt.title('%x-to-1 (MV-to-HFNC)'%HFNC_to_MV_ratio, fontsize = font)

plt.annotate('Estimated capacity', xy = (8.2578, 0), xytext = (8.2578 - 3.4, 120), fontsize = font, 
            arrowprops = dict(arrowstyle = '-|>, head_length = 0.6, head_width = 0.3',
                           color = 'black', lw = 1),
            va = 'center', multialignment = 'left')
            
#plt.legend(loc = 'upper right', fontsize = font)

plt.show()

