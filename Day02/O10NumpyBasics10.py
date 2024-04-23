
import numpy as np

data = np.array([5, 10, 15, 18, 20])

# bin to set the intervals
bin = [0, 10, 20, 30]

graph = np.histogram(data, bin)
print(graph)

# the first array contains the frequency of counts of the data within each bin

# the second array contains the bin edges

# only one data point lies between 0 and 10 that is 5

# there are 2 data points between 10 and 20 (i.e 15 and 18)

# and 20 between 20 and 30

data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3])
print(f"data:{data}")

bin = [0, 5, 10]

graph = np.histogram(data, bin)
print(graph)

print("-" * 60)
from matplotlib import pyplot as plt

data = np.array([5, 10, 15, 18, 20])

bin = [0, 10, 20, 30]

graph = np.histogram(data, bin)

plt.hist(data,bin)
plt.show()
