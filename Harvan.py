import numpy as np
import matplotlib.pyplot as plt


sampling_rate = 1000  
frequency = 5 
duration = 1.5 
t = np.linspace(0, duration, int(sampling_rate * duration))
wave = np.sin(2 * np.pi * frequency * t)

plt.plot(t, wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sound Wave Graph')
plt.grid(True)
plt.show()