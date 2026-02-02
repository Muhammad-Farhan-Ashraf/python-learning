import numpy as np
import matplotlib.pyplot as plt
"""Generate Random Sale data"""
days=30
dates=np.arange(1,days+1)
sales=np.random.randint(0,1000, size=days)
"""Analyze the data"""
mean=np.mean(sales)
median=np.median(sales)
sd=np.std(sales)
maximum=np.max(sales)
minimum=np.min(sales)
"""Print the analyzed result"""
print("Sales Statistics")
print(f"Mean: {mean}")
print(f"Median Value, {median}")
print(f"standard deviation,{ sd}")
print(f"Maximum Value, {maximum}")
print(f"Minimum Value, {minimum}")
"""Plot the Figure"""
plt.figure()
plt.plot(dates,sales, color="g")
plt.title("Sales over days")
plt.xlabel("DAYS")
plt.ylabel("SALES")
plt.show()