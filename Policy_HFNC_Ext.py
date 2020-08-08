from __future__ import division

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
HFNC_Use = []

Death = [0] * T
Death_U = [0] * T
Death_M = [0] * T
Decom_M = [0] * T

while t < (T - 1):
    
    MV_cap = c_v - Z_u[t] - Z_m[t] - Z_d[t] - a_d[t] - a_u[t] - a_m[t]
    
    a_u[t] = min(Q_u[t], MV_cap)
    
    MV_cap = c_v - Z_u[t] - Z_m[t] - Z_d[t] - a_d[t] - a_u[t] - a_m[t]
    
    a_d[t] = min(Q_d[t], MV_cap)
    
    MV_cap = c_v - Z_u[t] - Z_m[t] - Z_d[t] - a_d[t] - a_u[t] - a_m[t]
    
    MV_Left.append(MV_cap)

    MV_Use.append(c_v - MV_cap)

    HFNC_cap = c_h - Y_m[t] - Y_s[t] - (Q_d[t] - a_d[t]) - b_m[t] - b_s[t]
    
    b_s[t] = min(((1 - eta_u) * mu_u * (Z_u[t] + a_u[t]) + \
                 (1 - eta_m) * mu_m * (Z_m[t] + a_m[t]) + \
                 (1 - eta_d) * mu_d * (Z_d[t] + a_d[t])), HFNC_cap)
    
    HFNC_cap = c_h - Y_m[t] - Y_s[t] - (Q_d[t] - a_d[t]) - b_m[t] - b_s[t]

    b_m[t] = min(Q_m[t] - a_m[t], HFNC_cap)
    
    HFNC_cap = c_h - Y_m[t] - Y_s[t] - (Q_d[t] - a_d[t]) - b_m[t] - b_s[t]
    
    HFNC_Use.append(c_h - HFNC_cap)

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

Obj_Proposed_Post = int(Death[-1])
Obj_Proposed_U_Post = int(Death_U[-1]) 
Obj_Proposed_Non_U_Post = int(Death_Decom[-1])

MV_Full_Proposed_Post = round((MV_Left.count(0) / len(MV_Left)), 3)

