message = 'Hello, Python Book!'
print(message)

import matplotlib.pyplot as plt
import numpy as num
t = np.arange(0.0, 2.0, 0.01)
s = np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)