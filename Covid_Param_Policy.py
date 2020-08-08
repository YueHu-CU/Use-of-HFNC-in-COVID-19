#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 22:33:59 2020

@author: yh2987
"""

from __future__ import division
from gurobipy import *
import os
os.chdir('/Users/yhu22/Dropbox/My Work/Covid-19/080620')
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import copy 
import math
from scipy.optimize import curve_fit
import pandas as pd
from itertools import repeat

nupurple = [78/256, 42/256, 132/256]
nupurple2 = [204/256, 196/256, 223/256]
nupurple3 = [182/256, 172/256, 209/256]
cublue = [108/256, 172/256, 228/256]
cublue2 = [185/256, 217/256, 235/256]
font = 22

mil = 1e06; infty = 1e08; div = 1000


#### arrival rate - U Wash
MV_los = 10
 

###############################################################################
#### National level
#### IHME (Retrospect study)
#UWash_data_death = pd.read_csv('Data/IHME_US_Death_Retrospect.csv')
#All_ven = []
#for i in range(UWash_data_death.shape[0]):
#    All_ven.append(UWash_data_death.values.tolist()[i][0])
#fitted_factor = 2.15
#Lambda = [x * fitted_factor for x in All_ven]
#current_death = 152930.653



#### IHME (Full Time Period)
UWash_data_inc_death = pd.read_csv('Data/IHME_US_Death.csv')
All_ven = []
for i in range(UWash_data_inc_death.shape[0]):
    All_ven.append(UWash_data_inc_death.values.tolist()[i][0])
fitted_factor = 2.15
Lambda = [x * fitted_factor for x in All_ven]    
current_death = 152930.653



#### COVID-19 Simulator 
####https://viz.covid19forecasthub.org
####https://github.com/reichlab/covid19-forecast-hub/blob/master/data-processed/Covid19Sim-Simulator/metadata-Covid19Sim-Simulator.txt
#Sim_data_inc_death = pd.read_csv('Data/Sim_US_Death.csv')
#All_ven = []
#for i in range(Sim_data_inc_death.shape[0]):
#    All_ven.append(Sim_data_inc_death.values.tolist()[i][0])
#fitted_factor = 2.15
#Lambda = [x * fitted_factor for x in All_ven]
#current_death = 152930.653



#### UCLA - SuEIR 
####https://viz.covid19forecasthub.org
####https://github.com/reichlab/covid19-forecast-hub/blob/master/data-processed/UCLA-SuEIR/metadata-UCLA-SuEIR.txt
#Sim_data_inc_death = pd.read_csv('Data/UCLA_US_Death.csv')
#All_ven = []
#for i in range(Sim_data_inc_death.shape[0]):
#    All_ven.append(Sim_data_inc_death.values.tolist()[i][0])
#fitted_factor = 2.15
#Lambda = [x * fitted_factor for x in All_ven]
#current_death = 152930.653





################################################################################
##### New York State
### Retrospect
#UWash_data_death = pd.read_csv('Data/IHME_NY_Death_Retrospect.csv')
#All_ven = []
#for i in range(UWash_data_death.shape[0]):
#    All_ven.append(UWash_data_death.values.tolist()[i][0])
#fitted_factor = 1.59
#Lambda = [x * fitted_factor for x in All_ven]
#current_death = 32819.87755





################################################################################
#### City level
### Detroit - Michigan - Wayne - 890 MV
#UWash_data_inc_death = pd.read_csv('Data/IHME_Michigan_Death.csv')
##UWash_data_inc_death = pd.read_csv('Data/IHME_Michigan_Death_Retrospect.csv')
#
#All_ven = []
#for i in range(UWash_data_inc_death.shape[0]):
#    All_ven.append(UWash_data_inc_death.values.tolist()[i][0])
#fitted_factor = 1.8
#Lambda = [x * fitted_factor for x in All_ven]    
#
#factor4 = 1584 / 6506
#Lambda = [x * factor4 for x in Lambda]
#
#
#mv_cap = 1584 / 6506 * 890
#current_death = 1584



#### NYC - NY - 2772 MV
#UWash_data_inc_death = pd.read_csv('Data/IHME_NY_Death.csv')
##UWash_data_inc_death = pd.read_csv('Data/IHME_NY_Death_Retrospect.csv')
#
#All_ven = []
#for i in range(UWash_data_inc_death.shape[0]):
#    All_ven.append(UWash_data_inc_death.values.tolist()[i][0])
#fitted_factor = 1.59
#Lambda = [x * fitted_factor for x in All_ven]    
#
#factor4 = 23563 / 32756  
#Lambda = [x * factor4 for x in Lambda]
#
#
#mv_cap = 23563 / 32756 * 2772
#current_death = 23563 




##### New Orleans - Lousiana - Orleans - 559 MV
#
#UWash_data_inc_death = pd.read_csv('Data/IHME_Louisiana_Death.csv')
##UWash_data_inc_death = pd.read_csv('Data/IHME_Louisiana_Death_Retrospect.csv')
#
#All_ven = []
#for i in range(UWash_data_inc_death.shape[0]):
#    All_ven.append(UWash_data_inc_death.values.tolist()[i][0])
#fitted_factor = 2
#Lambda = [x * fitted_factor for x in All_ven]    
#
#factor4 = 561 / 4146 
#Lambda = [x * factor4 for x in Lambda]
#
#
#mv_cap = 561 / 4146 * 559
#current_death = 561 




##### Miami - Florida - 1995 MV
#
#UWash_data_inc_death = pd.read_csv('Data/IHME_Florida_Death.csv')
##UWash_data_inc_death = pd.read_csv('Data/IHME_Florida_Death_Retrospect.csv')
#
#All_ven = []
#for i in range(UWash_data_inc_death.shape[0]):
#    All_ven.append(UWash_data_inc_death.values.tolist()[i][0])
#fitted_factor = 2.4
#Lambda = [x * fitted_factor for x in All_ven]    
#
#
#factor4 = 1784 / 7747
#Lambda = [x * factor4 for x in Lambda]
#
#
#mv_cap = 1784 / 7747 * 1995
#current_death = 1784 




#### Arizona - Arizona -  814 MV

#UWash_data_inc_death = pd.read_csv('Data/IHME_Arizona_Death.csv')
##UWash_data_inc_death = pd.read_csv('Data/IHME_Arizona_Death_Retrospect.csv')
#
#All_ven = []
#for i in range(UWash_data_inc_death.shape[0]):
#    All_ven.append(UWash_data_inc_death.values.tolist()[i][0])
#fitted_factor = 2.4
#Lambda = [x * fitted_factor for x in All_ven]    
#
#
#factor4 = 2307 / 4081
#Lambda = [x * factor4 for x in Lambda]
#
#
#mv_cap = 2307 / 4081 * 814
#current_death = 2307



#plt.figure(figsize=(10, 8))
#plt.plot(Lambda, '-', color = 'black', lw = 3, label = "Arrival rate")
#plt.plot(All_ven, '-', color = 'red', lw = 3, label = "Incidient death")
#plt.ylabel('Count', fontsize = font)
#plt.xticks(np.arange(0, len(Lambda), 30), labelplace, fontsize = font)
#plt.yticks(fontsize = font)
#plt.legend(loc = 'upper right', fontsize = font)




T_div = 24; dt = 1 / T_div
Lambda = [x for item in Lambda for x in repeat(item, T_div)]
T = len(Lambda)





#################################################################################
###### Hospital level
## Scale peak all-bed demand to peak hospital inpatient demand
#hos_size = 100
#
#ratio_ven_to_all_bed = 0.398
#ratio_region_to_nation = hos_size * ratio_ven_to_all_bed / max(All_ven) 
#
#Lambda = [x * ratio_region_to_nation for x in Lambda]



###### Hospital level
##Scale peak all-bed demand to peak hospital inpatient demand
#hos_size = 250
#max_all_bed = 33293.50618
#
##ratio_death_to_all_bed = 0.027
##ratio_region_to_nation = hos_size * ratio_death_to_all_bed / max(All_ven) 
#
#
##ratio_region_to_nation = hos_size / max(All_ven) / ratio_death_to_all_bed
#ratio_region_to_nation = hos_size / max_all_bed
#
#
#
#Lambda = [x * ratio_region_to_nation for x in Lambda]









##############################################################################
# Plot arrival rate
labelplace = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']

#ytick = 

plt.figure(figsize=(10, 8))
plt.plot(Lambda, '-', color = 'black', lw = 3)
plt.ylabel('MV demand', fontsize = font)
plt.xticks(np.arange(0, T, 30 * T_div), labelplace, fontsize = font)
plt.yticks(fontsize = font)
#plt.title('UCLA-SuEIR', fontsize = font)
















###############################################################################
#### parameters


### proportion of urgent patients
p_u = 0.33
# range 0.16 - 0.5


### time in state before transition to next state
## not HFNC/MV
# moderate
#1 / (gamma_m + theta_m + beta_m)
#los_m = [] range 15 - 25 hours
los_m = 20 / 24
# urgent
#1 / theta_u
#theta_u = 1 / [] range 0.5 - 2 hours
theta_u = 1 / (1 / 24)
# stabilized 
#1 / (gamma_s + theta_s + beta_s)
#los_s = [] range 8 - 16 hours
los_s = 12 / 24
## HFNC
# moderate
#1 / nu_m
#nu_m = 1 / [] range 24 - 72 hours
nu_m = 1 / (48 / 24)
# stabilized
#1 / nu_s 
#nu_s = 1 / [] range 10 - 26 hours
nu_s = 1 / (18 / 24)
# deteriorated
#1 / theta_d
#theta_d = 1 / [] range 10 - 20 hours
theta_d = 1 / (15 / 24)
## MV
# moderate
#1 / mu_m
#mu_m = 1 / [] range 72 - 168 hours
mu_m = 1 / (120 / 24)
# urgent
#1 / mu_u
#mu_u = 1 / [] range 192 - 288 hours
mu_u = 1 / (240 / 24)
# deteriorated range: 10 - 14 days, 240 - 336 hours
#1 / mu_d
#mu_d = 1 / [] range 240 - 336 hours
mu_d = 1 / (288 / 24)



### probability of death
## on regular O2, not HFNC/MV
# moderate
#theta_m / (gamma_m + theta_m + beta_m) 
#theta_m = [] / los_m range 0.02 - 0.08
theta_m = 0.05 / los_m
#    theta_m = 0.3 / los_m
# urgent
1
# stabilized
#theta_s / (gamma_s + theta_s + beta_s) 
#theta_s = [] / los_s range 0.06 - 0.14
theta_s = 0.1 / los_s
## HFNC
# moderate
#d_m
#d_m = [] range 0.02 - 0.06 
d_m = 0.04
# stabilized
#d_s
#d_s = [] range 0.04 - 0.12
d_s = 0.08 
# deteriorated 
1 
## MV
# moderate
#eta_m
#eta_m = [] range 0.1 - 0.2 CHANGED
eta_m = 0.15
# urgent 
#eta_u
#eta_u = [] range 0.45 - 0.55 
eta_u = 0.5
# deteiorated
#eta_d
#eta_d = [] range 0.55 - 0.65
eta_d = 0.6



### probabiliyt of deterioration
## on regular O2, not HFNC/MV
# moderate
#gamma_m / (gamma_m + theta_m + beta_m)
#gamma_m = [] / los_m range 0.55 - 0.75 CHANGED
gamma_m = 0.65 / los_m
#    gamma_m = 0.8 / los_m
# stabilized
#gamma_s / (gamma_s + theta_s + beta_s)
#gamma_s = [] / los_s  range 0.1 - 0.2
gamma_s = 0.15 / los_s
#    gamma_s = 0 / los_s
## HFNC
# moderate 
#q_m
#q_m = [] range 0.35 - 0.55 CHANGED
q_m = 0.45
#    q_m = 0.7
# stabilized
#q_s
#q_s = [] range 0.05 - 0.1 
q_s = 0.075
#    q_s = 0


#### retrieve beta_m and beta_s
beta_m = 1 / los_m - gamma_m - theta_m
beta_s = 1 / los_s - gamma_s - theta_s








###############################################################################

Test = []
Test.append(q_m < 0 or q_m > 1)
Test.append(d_m < 0 or d_m > 1)
Test.append(q_s < 0 or q_s > 1)
Test.append(d_s < 0 or d_s > 1)
Test.append(eta_m < 0 or eta_m > 1)
Test.append(eta_u < 0 or eta_u > 1)
Test.append(eta_d < 0 or eta_d > 1)
Test.append(q_m + d_m > 1)
Test.append(q_s + d_s > 1)




#if sum(Test) == 0:
#    print('No error')
#else:
#    print('Error with parameters')
#
#print('')











