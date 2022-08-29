import numpy as np
from matplotlib import pyplot as plt

MAXVOLTAGE = 3.3

with open ("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

volt = np.loadtxt("data.txt", dtype = int)
volt = volt/256 * MAXVOLTAGE
fig, ax = plt.subplots(figsize=(16, 10), dpi=300)

with open ("settings.txt", "r") as settings:
    dT = float(settings.readline())

tmp = np.arange(0, len(volt)*dT, dT)

xmax = np.argmax(tmp)*dT
qmax = volt.argmax()

str1 = "Charging time =" + str(qmax*dT) + "s" 
str2 = "Discharge time =" + (str((len(volt)-qmax)*dT)) + "s"

ax.set_title("Capacitor charge/discharge graph", fontsize = 17, wrap=True)
ax.set_xlabel("Time, s", fontsize = 15)
ax.set_ylabel("Voltage, V", fontsize = 15)

ax.plot(tmp, volt, color = 'r', label="V(t)", marker = 'o', markevery = 20)
ax.minorticks_on()

ax.grid(which='major', color = 'm', linewidth = 0.5)
ax.grid(which='minor', color = 'm', linestyle = '--')

ax.legend()
ax.set(xlim=(0, xmax + 1), ylim=(0, MAXVOLTAGE))

plt.text(0.3*len(tmp)*dT, 2, str1)
plt.text(0.3*len(tmp)*dT, 1.5, str2)

fig.savefig("graph.svg")
