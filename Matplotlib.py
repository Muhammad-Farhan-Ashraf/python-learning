import numpy as np
import matplotlib.pyplot as plt
#Scatter plot
x_data=np.random.random(50)*(100)
y_data=np.random.random(50)*(100)
plt.scatter(x_data,y_data, marker="*", c="pink" )
plt.show()
#line graph
years=[2010 + x for x in range (16)]
weights=[60,61,54,65,64,50,65,56,76,56,56,43,56,45,53,70]
plt.plot(years,weights)
plt.xlabel("Years")
plt.ylabel("Weights")
plt.show()
# Bar graph
plt.bar(years,weights, color="green")
plt.show()
score=np.random.normal(20,1.5,1000)
plt.hist(score)
plt.show()
#Pie chart
subject=["Economics", " Computer science", "Mathematics", " History", "Political Science"]
students=[20,25,31,15,34]
plt.pie(students,labels= subject)
plt.show()