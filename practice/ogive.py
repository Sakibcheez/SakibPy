import matplotlib.pyplot as plt
import numpy as np

# Data
classes = [10, 20, 30, 40, 50]
frequency = [2, 5, 7, 10, 6]

# Cumulative frequency
cumulative = np.cumsum(frequency)

# Plot Ogive
plt.plot(classes, cumulative, marker='o', linestyle='-', color='purple')
plt.title('Ogive (Cumulative Frequency)')
plt.xlabel('Class Interval Upper Bound')
plt.ylabel('Cumulative Frequency')
plt.grid(True)
plt.show()
