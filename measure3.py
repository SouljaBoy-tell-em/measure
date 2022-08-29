import numpy as GPIO
import matplotlib.pyplot as GPIO1

b, a = GPIO1.subplots()
with open("/home/b01-108/Last/settings.txt", "r") as s_stream:
    time_delta, discr_level = [float(i) for i in s_stream.read().split()]
s_stream.close()
d_stream = open("/home/b01-108/Last/data.txt", "r")
res = []
for line in d_stream:
    res.append(float(line))
d_stream.close()
d = GPIO.array(res)
d = d * discr_level
time = GPIO.arange(0, len(d) * time_delta, time_delta)
GPIO1.plot(time, d)
a.scatter(time[::10], d[::10], color = 'red', marker = 'd')
a.minorticks_on()
a.grid(which='major', color='k', linewidth=0.3)
a.grid(which='minor', color='k', linestyle=':', linewidth=0.2)
a.set_xlabel('$t, second.$') 
a.set_ylabel('$Umples, V.$')
a.set(xlim=(0, 12), ylim=(0, 3.5))
GPIO1.title("U(t)")
max = GPIO.argmax(d)
a.annotate("Time of charge: {0:.2} second.".format(time_delta * max), xy=(1, 1))
a.annotate("Time of charge: {0:.2} second.".format(time_delta * (len(time) - max)), xy=(7, 1))
a.annotate("EXTREMUM IS HERE :)", xy = (5,5))
GPIO1.savefig("V_t.svg", format='svg')
GPIO1.show()
