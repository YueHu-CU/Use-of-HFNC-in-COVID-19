from __future__ import division
import os
os.chdir('/Users/yhu22/Dropbox/My Work/Covid-19/GitHub')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from itertools import repeat
import random
font = 22; div = 1000

###############################################################################
###### NATIONAL LEVEL
### IHME (full time period)
Data_inc_death = pd.read_csv('Data/IHME_US_Death.csv')
All_ven = []
for i in range(Data_inc_death.shape[0]):
    All_ven.append(Data_inc_death.values.tolist()[i][0])
fitted_factor = 2.15
Lambda = [x * fitted_factor for x in All_ven]    
current_death = 152930.653


#### IHME (retrospect study)
#Data_inc_death = pd.read_csv('Data/IHME_US_Death_Retrospect.csv')
#All_ven = []
#for i in range(Data_inc_death.shape[0]):
#    All_ven.append(Data_inc_death.values.tolist()[i][0])
#fitted_factor = 2.15
#Lambda = [x * fitted_factor for x in All_ven]
#current_death = 152930.653


#### COVID-19 Simulator 
#Data_inc_death = pd.read_csv('Data/Sim_US_Death.csv')
#All_ven = []
#for i in range(Data_inc_death.shape[0]):
#    All_ven.append(Data_inc_death.values.tolist()[i][0])
#fitted_factor = 2.15
#Lambda = [x * fitted_factor for x in All_ven]
#current_death = 152930.653


#### UCLA - SuEIR 
#Data_inc_death = pd.read_csv('Data/UCLA_US_Death.csv')
#All_ven = []
#for i in range(Data_inc_death.shape[0]):
#    All_ven.append(Data_inc_death.values.tolist()[i][0])
#fitted_factor = 2.15
#Lambda = [x * fitted_factor for x in All_ven]
#current_death = 152930.653


###############################################################################
#### New York State (Retrospect study)
#Data_inc_death = pd.read_csv('Data/IHME_NY_Death_Retrospect.csv')
#All_ven = []
#for i in range(Data_inc_death.shape[0]):
#    All_ven.append(Data_inc_death.values.tolist()[i][0])
#fitted_factor = 1.59
#Lambda = [x * fitted_factor for x in All_ven]
#current_death = 32819.87755


###############################################################################
####### CITY LEVEL
#### Wayne - Detroit - Michigan (890 MV)
#Data_inc_death = pd.read_csv('Data/IHME_Michigan_Death.csv')
#All_ven = []
#for i in range(Data_inc_death.shape[0]):
#    All_ven.append(Data_inc_death.values.tolist()[i][0])
#fitted_factor = 1.8
#Lambda = [x * fitted_factor for x in All_ven]    
#city_to_state_death_ratio = 1584 / 6506
#Lambda = [x * city_to_state_death_ratio for x in Lambda]
#current_death = 1584


#### NYC - NY (2772 MV)
#Data_inc_death = pd.read_csv('Data/IHME_NY_Death.csv')
#All_ven = []
#for i in range(Data_inc_death.shape[0]):
#    All_ven.append(Data_inc_death.values.tolist()[i][0])
#fitted_factor = 1.59
#Lambda = [x * fitted_factor for x in All_ven]    
#city_to_state_death_ratio = 23563 / 32756  
#Lambda = [x * city_to_state_death_ratio for x in Lambda]
#current_death = 23563 


#### Orleans - New Orleans - Lousiana (559 MV)
#Data_inc_death = pd.read_csv('Data/IHME_Louisiana_Death.csv')
#All_ven = []
#for i in range(Data_inc_death.shape[0]):
#    All_ven.append(Data_inc_death.values.tolist()[i][0])
#fitted_factor = 2
#Lambda = [x * fitted_factor for x in All_ven]    
#city_to_state_death_ratio = 561 / 4146 
#Lambda = [x * city_to_state_death_ratio for x in Lambda]
#current_death = 561 


#### Miami - Florida (1995 MV)
#Data_inc_death = pd.read_csv('Data/IHME_Florida_Death.csv')
#All_ven = []
#for i in range(Data_inc_death.shape[0]):
#    All_ven.append(Data_inc_death.values.tolist()[i][0])
#fitted_factor = 2.4
#Lambda = [x * fitted_factor for x in All_ven]    
#city_to_state_death_ratio = 1784 / 7747
#Lambda = [x * city_to_state_death_ratio for x in Lambda]
#current_death = 1784 


#### Pheonix - Arizona (814 MV)
#Data_inc_death = pd.read_csv('Data/IHME_Arizona_Death.csv')
#All_ven = []
#for i in range(Data_inc_death.shape[0]):
#    All_ven.append(Data_inc_death.values.tolist()[i][0])
#fitted_factor = 2.4
#Lambda = [x * fitted_factor for x in All_ven]    
#city_to_state_death_ratio = 2307 / 4081
#Lambda = [x * city_to_state_death_ratio for x in Lambda]
#current_death = 2307


###############################################################################
####### HOSPITAL LEVEL
# Scale peak all-bed demand to peak hospital inpatient demand
hos_size = 1000
max_all_bed = 33293.50618
ratio_region_to_nation = hos_size / max_all_bed
Lambda = [x * ratio_region_to_nation for x in Lambda]


###############################################################################
T_div = 24; dt = 1 / T_div
Lambda = [x for item in Lambda for x in repeat(item, T_div)]
T = len(Lambda)


###############################################################################
# Plot arrival rate
#labelplace = ['Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
#plt.figure(figsize=(10, 8))
#plt.plot(Lambda, '-', color = 'black', lw = 3)
#plt.ylabel('MV demand', fontsize = font)
#plt.xticks(np.arange(0, T, 30 * T_div), labelplace, fontsize = font)
#plt.yticks(fontsize = font)


###############################################################################
###### Parameters
### proportion of urgent patients
p_u = 0.33
p_u = random.uniform(0.16, 0.5)

### time in state before transition to next state
## not HFNC/MV
# moderate
los_m = 20 / 24
los_m = random.uniform(15 / 24, 25 / 24)

# urgent
theta_u = 1 / (1 / 24)
theta_u = random.uniform(1 / (0.5 / 24), 1 / (2 / 24)) 

# stabilized 
los_s = 12 / 24
los_s = random.uniform(8 / 24, 16 / 24)

## HFNC
# moderate
nu_m = 1 / (48 / 24)
nu_m = random.uniform(1 / (24 / 24), 1 / (72 / 24))

# stabilized
nu_s = 1 / (18 / 24)
nu_s = random.uniform(1 / (10 / 24), 1 / (26 / 24))

# deteriorated
theta_d = 1 / (15 / 24)
theta_d = random.uniform(1 / (10 / 24), 1 / (20 / 24))

## MV
# moderate
mu_m = 1 / (120 / 24)
mu_m = random.uniform(1 / (72 / 24), 1 / (168 / 24))

# urgent
mu_u = 1 / (240 / 24)
mu_u = random.uniform(1 / (192 / 24), 1 / (288 / 24))

# deteriorated range: 10 - 14 days, 240 - 336 hours
mu_d = 1 / (288 / 24)
mu_d = random.uniform(1 / (240 / 24), 1 / (336 / 24))

### probability of death
## on regular O2, not HFNC/MV
# moderate
theta_m = 0.05 / los_m
theta_m = random.uniform(0.02 / los_m, 0.08 / los_m)

# stabilized
theta_s = 0.1 / los_s
theta_s = random.uniform(0.06 / los_s, 0.14 / los_s)

## HFNC
# moderate
d_m = 0.04
d_m = random.uniform(0.02, 0.06)

# stabilized
d_s = 0.08 
d_s = random.uniform(0.04, 0.12)

## MV
# moderate
eta_m = 0.15
eta_m = random.uniform(0.1, 0.2)

# urgent 
eta_u = 0.5
eta_u = random.uniform(0.45, 0.55)

# deteiorated
eta_d = 0.6
eta_d = random.uniform(0.55, 0.65)

### probabiliyt of deterioration
## on regular O2, not HFNC/MV
# moderate
gamma_m = 0.65 / los_m
gamma_m = random.uniform(0.55 / los_m, 0.75 / los_m)

# stabilized
gamma_s = 0.15 / los_s
gamma_s = random.uniform(0.1 / los_s, 0.2 / los_s)

## HFNC
# moderate 
q_m = 0.45
q_m = random.uniform(0.35, 0.55)

# stabilized
q_s = 0.075
q_s = random.uniform(0.05, 0.1)

### retrieve beta_m and beta_s
beta_m = 1 / los_m - gamma_m - theta_m
beta_s = 1 / los_s - gamma_s - theta_s


###############################################################################
#### Sanity check
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

