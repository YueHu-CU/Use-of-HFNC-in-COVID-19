from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from itertools import repeat
nupurple = [78/256, 42/256, 132/256]
cublue = [108/256, 172/256, 228/256]
font = 20

#c_v = 31000; c_h = c_v / 5

MV_cap = c_v ; HFNC_cap = c_h 

t = 0
a_u = [0] * T; a_m = [0] * T; a_d = [0] * T
b_m = [0] * T; b_s = [0] * T 
Q_u = [0] * T; Q_m = [0] * T; Q_s = [0] * T; Q_d = [0] * T 
Z_u = [0] * T; Z_m = [0] * T; Z_d = [0] * T 
Y_m = [0] * T; Y_s = [0] * T

MV_Left = [] 
MV_Use = []

Death = [0] * T
Death_U = [0] * T
Death_M = [0] * T
Decom_M = [0] * T

while t < (T - 1):
    
    MV_cap = c_v - Z_u[t] - Z_m[t] - Z_d[t] - a_d[t] - a_u[t] - a_m[t]

    a_u[t] = min(Q_u[t], MV_cap)
    
    MV_cap = c_v - Z_u[t] - Z_m[t] - Z_d[t] - a_d[t] - a_u[t] - a_m[t]
    
    MV_Left.append(MV_cap)
    
    MV_Use.append(c_v - MV_cap)
    
    Q_u[t + 1] = Q_u[t] + (p_u * Lambda[t] + gamma_m * (Q_m[t] - a_m[t] - b_m[t]) + \
                     gamma_s * (Q_s[t] - b_s[t]) - a_u[t] - theta_u * (Q_u[t] - a_u[t])) * dt
    
    Z_u[t + 1] = Z_u[t] + (a_u[t] - mu_u * (Z_u[t] + a_u[t])) * dt
        
    Q_m[t + 1] = Q_m[t] + ((1 - p_u) * Lambda[t] - a_m[t] - b_m[t] - \
                     (theta_m + beta_m + gamma_m) * (Q_m[t] - a_m[t] - b_m[t])) * dt 
    
    Z_m[t + 1] = Z_m[t] + (a_m[t] - mu_m * (Z_m[t] + a_m[t])) * dt
        
    Y_m[t + 1] = Y_m[t] + (b_m[t] - nu_m * (Y_m[t] + b_m[t])) * dt 
        
    Q_d[t + 1] = Q_d[t] + (q_m * nu_m * (Y_m[t] + b_m[t]) - \
                      a_d[t] - theta_d * (Q_d[t] - a_d[t]) + \
                     q_s * nu_s * (Y_s[t] + b_s[t])) * dt 
        
    Z_d[t + 1] = Z_d[t] + (a_d[t] - mu_d * (Z_d[t] + a_d[t])) * dt 
        
    Q_s[t + 1] = Q_s[t] + ((1 - eta_u) * mu_u * (Z_u[t] + a_u[t]) + \
                     (1 - eta_m) * mu_m * (Z_m[t] + a_m[t]) + \
                     (1 - eta_d) * mu_d * (Z_d[t] + a_d[t]) - \
                     b_s[t] - (gamma_s + beta_s + theta_s) * (Q_s[t] - b_s[t])) * dt 
    
    Y_s[t + 1] = Y_s[t] + (b_s[t] - nu_s * (Y_s[t] + b_s[t])) * dt
        
    Death[t + 1] = Death[t] + (eta_u * mu_u * (Z_u[t] + a_u[t]) + \
                     theta_u * (Q_u[t] - a_u[t]) + \
                     eta_m * mu_m * (Z_m[t] + a_m[t]) + \
                     theta_m * (Q_m[t] - a_m[t] - b_m[t]) + \
                     eta_d * mu_d * (Z_d[t] + a_d[t]) + \
                     theta_d * (Q_d[t] - a_d[t]) + theta_s * (Q_s[t] - b_s[t]) + \
                     d_m * nu_m * (Y_m[t] + b_m[t]) + d_s * nu_s * (Y_s[t] + b_s[t])) * dt
    
    Death_U[t + 1] = Death_U[t] + (eta_u * mu_u * (Z_u[t] + a_u[t]) + \
                     theta_u * (Q_u[t] - a_u[t])) * dt 
    
    Death_M[t + 1] = Death_M[t] + (eta_m * mu_m * (Z_m[t] + a_m[t]) + \
                     theta_m * (Q_m[t] - a_m[t] - b_m[t]) + \
                     d_m * nu_m * (Y_m[t] + b_m[t])) * dt 
    
    Decom_M[t + 1] = Decom_M[t] + gamma_m * (Q_m[t] - a_m[t] - b_m[t]) * dt 
        
    t = t + 1


Death_Decom = [x + y for x, y in zip(Death_M, Decom_M)]

Obj_Policy_1 = int(Death[-1])
Obj_Policy_1_U = int(Death_U[-1]) 
Obj_Policy_1_Non_U = int(Death_Decom[-1])

MV_Full_Policy_1 = round((MV_Left.count(0) / len(MV_Left)), 3)


###############################################################################
# Plot resources, cases and deaths over the horizon of the outbreak
#xtick = np.arange(0, T, 30 * T_div)
#xlabel = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
#
#ytick = np.arange(0, 3501, 500).tolist()
#ylabel = np.arange(0, 3.501, 0.5).tolist()
#
#Lambda_cumu = [0] * len(Lambda)
#for i in range(len(Lambda)):
#    Lambda_cumu[i] = sum(Lambda[0 : i]) * dt / 1
#
#fig, ax1 = plt.subplots(figsize = (10, 8))
#lin1 = ax1.plot(MV_Use, lw = 3, color = cublue, label = 'MV in use') 
#ax1.set_xticks(xtick)
#ax1.set_xticklabels(xlabel)
#ax1.tick_params(labelsize = font)
#ax1.set_ylabel('MV / HFNC in use', fontsize = font)
#
#ax2 = ax1.twinx() 
#lin3 = ax2.plot(Death, lw = 3, color = 'red', label = 'Cumulated deaths')
#ax2.set_ylim(-160, 3900)
#ax2.tick_params(labelsize = font, color = 'red', labelcolor = 'red')
#ax2.set_yticks(ytick)
#ax2.set_yticklabels(ylabel)
#ax2.set_ylabel('Cumulated deaths (K)', fontsize = font, color = 'red')
#
#ax3 = ax1.twinx() 
#lin4 = ax3.plot(Lambda_cumu, lw = 3, color = 'green', label = 'Cumulated cases')
#ax3.tick_params(labelsize = font, color = 'green', labelcolor = 'green', length = 70)
#ax3.set_ylabel('Cumulated cases (K)', fontsize = font, color = 'green')
#ax3.set_yticks(ytick)
#ax3.set_yticklabels(ylabel)
#
#plt.legend(loc = 'upper right', fontsize = 16)
#ax3.set_ylim(-160, 3900)
#
## added these three lines
#lin = lin1 + lin3 + lin4
#labs = [l.get_label() for l in lin]
#plt.legend(lin, labs, loc = 0, fontsize = 17)


###############################################################################
# Plot validation for restrospective MV demand
#Obs_data_death = pd.read_csv('Data/IHME_US_Cumu_Death_Retrospect.csv')
#Obs_death = []
#for i in range(Obs_data_death.shape[0]):
#    Obs_death.append(Obs_data_death.values.tolist()[i][0])
##    
#Obs_death = [x for item in Obs_death for x in repeat(item, T_div)]
#
#xtick = np.arange(0, T, 30 * T_div)
#xlabel = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
#
#ytick = np.arange(0, 170000, 20000).tolist()
#ylabel = np.arange(0, 17, 2).tolist()
#
#plt.figure(figsize = (10, 8))
#
#plt.plot(Death, lw = 3, color = 'red', label = 'Predicted')
#plt.plot(Obs_death, lw = 3, color = 'black', label = 'Observed')
#
#plt.xticks(xtick, xlabel, fontsize = font)
#plt.xlim(-100, len(Death) + 200)
#
#plt.ylabel('Cumulated deaths(K)', fontsize = font)
#plt.yticks(ytick, ylabel, fontsize = font)
#
#plt.legend(loc = 'lower right', fontsize = font)

