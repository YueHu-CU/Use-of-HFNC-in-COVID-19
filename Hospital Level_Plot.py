from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
font = 22

# Set width of bar
barWidth = 0.25
 
# Set height of bar
bars1 = Death_R_3
bars2 = Death_R_5
bars3 = Death_R_8

CI1 = [x1 - x2 for (x1, x2) in zip(Death_R_3_Upper, Death_R_3_Lower)]
CI2 = [x1 - x2 for (x1, x2) in zip(Death_R_5_Upper, Death_R_5_Lower)]
CI3 = [x1 - x2 for (x1, x2) in zip(Death_R_8_Upper, Death_R_8_Lower)]

# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
 
# Bar plot with intervals
plt.figure(figsize=(12, 8))

plt.bar(r1, bars1, yerr = CI1, color = '#7f6d5f', width = barWidth, 
        edgecolor = 'white', label = '3-to-1', align = 'center', alpha = 1,
       ecolor = 'black', capsize = 10)
plt.bar(r2, bars2, yerr = CI2, color = '#557f2d', width = barWidth, 
        edgecolor = 'white', label = '5-to-1', align = 'center', alpha = 1,
       ecolor = 'black', capsize = 10)
plt.bar(r3, bars3, yerr = CI3, color = '#2d7f5e', width = barWidth, 
        edgecolor = 'white', label = '8-to-1', align = 'center', alpha = 1,
       ecolor = 'black', capsize = 10)
 
plt.xlabel('Total mechanical ventilator capacity', fontsize = font)
plt.xticks([r + barWidth for r in range(len(bars1))], ['25', '50', '100', '150', '200', '250'], fontsize = font)

plt.yticks(fontsize = font)
plt.ylabel('Cumulative lives saved \n (vs No HFNC)', fontsize = font)

plt.legend(fontsize = font)

plt.show()

