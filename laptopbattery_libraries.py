import numpy as np
import pandas as pd 
import pylab
from matplotlib import pyplot

X,Y = np.loadtxt('https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt', delimiter=',',unpack=True)
x=pd.Series(X)
y=pd.Series(Y)
r= x.cov(y)/(y.std()*x.std())
b_1= r*y.std()/x.std()
b_0= y.mean()-(b_1*x.mean())

pyplot.scatter(x, y)
pyplot.title('Lappiee Battery Chart')
pyplot.xlabel('Charge')
pyplot.ylabel('Screen On Time')
pyplot.grid()
pyplot.show()

# After analyzing the graph it is found that charging laptop for x period of time, Fred gets 2x screen on time
# Maximim Screen On time of laptop is 8 hours 

new=float(input())
ans=round(b_1*new+b_0,2)
print(ans)
