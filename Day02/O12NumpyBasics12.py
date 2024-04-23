
import numpy as np

# get the current date and time
date_time = np.datetime64('now')
print(f"Current Date Time :{date_time}")

print("-" * 60)
# todays date
today = np.datetime64('today', 'D')
print(f"current Date :{today}")

print("-" * 60)
year = np.datetime64('2024', 'Y')
print(f"Year :{year}")

month = np.datetime64('2024-04', "M")
print(f"Month :{month}")

day = np.datetime64('2024-04-23', "D")
print(f"Day :{day}")

print("-" * 60)

# coverting numpy date time to python datetime
from datetime import datetime
dt64 = np.datetime64('now')

# convert to python datetime
dt = dt64.astype(datetime)
print(f"date :{dt}")

# from python datetime to datetime64
dt = datetime(2024, 4, 23, 18, 34, 25)
print(f"Date :{dt}")

dt64 = np.datetime64(dt)
print(dt64)

print("-" * 60)

# create a range of dates using datetime64
dates = np.arange('2024-04-13', '2024-04-23', dtype='datetime64[D]')
print(f"dates :{dates}")

print("-" * 60)
date1 = np.datetime64('2023-04-15')
date2 = np.datetime64('2024-04-23')

print(f"Difference between dates :{date2 - date1}")
print(f"Business Days :{np.busday_count(date1, date2)}")

print("-" * 60)
from matplotlib import pyplot as plt

car = np.array(['hyundai', 'maruti', 'kia', 'vw', 'skoda', 'mahindra', 'tata'])
print(f"cars :{car}")

catWt = np.array([2.5, 2.9, 3.0, 3.8, 4, 4.1, 4.25])
print(f"car weight :{catWt}")

# plt.plot(car, catWt)
# plt.show()

carClr = [6, 7, 8, 9, 10, 11, 12]
carSize = [20, 40, 60, 80, 100, 120, 140]

# plt.scatter(car, catWt, carClr, carSize)
# plt.show()

plt.bar(car, catWt)
plt.show()
