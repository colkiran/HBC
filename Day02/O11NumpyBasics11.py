
import numpy as np

day = [2, 4, 7]

petrol_prc = [95, 100, 105]

# .interp() function returns the one-dimensional piecewise linear interpolant to a function with given discrete data points (xp, fp)

day3_prc = np.interp(3, day, petrol_prc)
print(f"Price on Day 3: {day3_prc}")

day6_prc = np.interp(6, day, petrol_prc)
print(f"Price on Day 6: {day6_prc}")

print("-" * 60)

days = [2, 4, 7, 10]
petrol_prc = [95, 97, 100, 105]

inter_days = [1, 3, 5, 6, 8, 9]
inter_prc = np.interp(inter_days, days, petrol_prc)
print(inter_prc)

print("-" * 60)
from matplotlib import pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 3, 4, 5, 7, 8])

# generate evenly spaced values between min and max values
x_interp = np.linspace(x.min(), x.max(), 100)

y_interp = np.interp(x_interp, x, y)

plt.plot(x, y, 'bo')
plt.plot(x_interp, y_interp, 'r-')
plt.show()
