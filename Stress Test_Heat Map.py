from __future__ import division
from matplotlib import colors
import seaborn as sns
font = 20

execfile("Parameter.py")

c_v = 100; c_h = 20

q_m_R = [0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35]

los_d_R = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

mu_d_R = [1 / 10, 1 / 11, 1 / 12, 1 / 13, 1 / 14, 1 / 15, 1 / 16, 1 / 17,
          1 / 18, 1 / 19, 1 / 20]

duration = 272

Death_R = np.empty([len(q_m_R), len(mu_d_R)])
Uti_R = np.empty([len(q_m_R), len(mu_d_R)])
Uti_Day_R = np.empty([len(q_m_R), len(mu_d_R)])

for ii in range(len(q_m_R)):
    for jj in range(len(mu_d_R)):
        q_m = q_m_R[ii]
        mu_d = mu_d_R[jj]
        
        execfile("Policy_No_HFNC.py") 
        
        execfile("Policy_HFNC_Ext_MV_10.py") 
        
        Death_R[ii, jj] = int(Obj_Policy_1 - Obj_Proposed_10_Post)
        
        Uti_R[ii, jj] = round((MV_Full_Policy_1 - MV_Full_Proposed_10_Post) * 100, 1)
        
        Uti_Day_R[ii, jj] = round((MV_Full_Policy_1 - MV_Full_Proposed_10_Post) * duration, 1)
        

###############################################################################
# Plot cumulative lives saved
G = sns.light_palette("green")
R = sns.light_palette("darkred")

cmap = colors.ListedColormap([R[2], G[0], G[1], G[2], G[3], G[4], G[5]])
bounds=[-100, 0, 100, 200, 300, 400, 500, 600]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots(figsize=(16,8))
im = ax.imshow(Death_R, cmap=cmap, norm=norm) 

# show all ticks
ax.set_xticks(np.arange(len(los_d_R)))
ax.set_yticks(np.arange(len(q_m_R)))

# label ticks with the respective list entries
ax.set_xticklabels([x - 5 for x in los_d_R], fontsize = font)
ax.set_yticklabels(q_m_R, fontsize = font)
ax.set_xlabel('Excess MV duration of decompensated patients (days)', fontsize = font, labelpad = 15)
ax.set_ylabel('Probability of decompensation', fontsize = font, labelpad = 15)

## Loop over data dimensions and create text annotations 
#for i in range(len(q_m_R)):
#    for j in range(len(mu_d_R)):
#        ax.text(j, i, int(Death_R[i, j]), ha="center", va="top", 
#                color="black", fontsize = font)
##ax.set_title('Cumulative lives saved', fontsize = 16)

cb = ax.figure.colorbar(im, extend='both')
cb.ax.tick_params(labelsize = font)
cb.set_label(label = 'Cumulative lives saved', size = font)
cb.ax.set_yticklabels(bounds)

fig.tight_layout()

plt.show()


###############################################################################
# Plot cumulative lives saved
G = sns.light_palette("green")
R = sns.light_palette("darkred")
Mid = sns.diverging_palette(10, 220, sep = 80, n = 7)

cmap = colors.ListedColormap([R[3], R[2], R[1], G[2], G[3], G[4]])
bounds = [-60, -40, -20, 0, 20, 40, 60]
norm = colors.BoundaryNorm(bounds, cmap.N)

cmap2 = colors.ListedColormap([G[4], G[3], G[2], R[1], R[2], R[3]])
bounds2 = [-60, -40, -20, 0, 20, 40, 60]
norm2 = colors.BoundaryNorm(bounds2, cmap2.N)

fig, ax = plt.subplots(figsize = (16, 8))
im2 = ax.imshow(Uti_Day_R, cmap = cmap2, norm = norm2) 
im = ax.imshow(Uti_Day_R, cmap = cmap, norm = norm) 

# show all ticks
ax.set_xticks(np.arange(len(los_d_R)))
ax.set_yticks(np.arange(len(q_m_R)))

# label ticks with the respective list entries
ax.set_xticklabels([x - 5 for x in los_d_R], fontsize = font)
ax.set_yticklabels(q_m_R, fontsize = font)
ax.set_xlabel('Excess MV duration of decompensated patients (days)', fontsize = font, labelpad = 15)
ax.set_ylabel('Probability of decompensation', fontsize = font, labelpad = 15)

## Loop over data dimensions and create text annotations 
#for i in range(len(q_m_R)):
#    for j in range(len(mu_d_R)):
#        if round(Uti_Day_R[i, j], 1) < 0:
#            ax.text(j, i, round(Uti_Day_R[i, j], 1), ha="center", va="top", 
#                color="black", fontsize = font)
#        elif round(Uti_Day_R[i, j], 1) >= 0:
#            ax.text(j, i, round(Uti_Day_R[i, j], 1), ha="center", va="top", 
#                color="black", fontsize = font)
##ax.set_title('Reduction in MV full-utilization period (%)', fontsize = 16)

cb = ax.figure.colorbar(im2, norm = plt.Normalize(bounds2[0], bounds2[-1]),
                        orientation = 'vertical', extend='both')
cb.ax.tick_params(labelsize = font)
cb.set_label(label = 'Change in days with no available MV', size = font)
cb.set_ticks(bounds2)
cb.ax.set_yticklabels(bounds2)

fig.tight_layout()

plt.show()

