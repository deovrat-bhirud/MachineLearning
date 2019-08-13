import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


url="https://raw.githubusercontent.com/akiwelekar/MLModels/master/aimarks2017.csv"
data = pd.read_csv(url)

x_axis =data["mse"]
y_axis =data["ese"]
x = np.array(x_axis)
y = np.array(y_axis)

def gradie(x,y):
    m = c = y_predic = 0
    epoch = 10000
    n = len(y)
    lr = 0.00001

    for i in range(epoch):
        y_predic = m * x + c
        dm = -(2/n)*sum(x*(y-y_predic))
        de = -(2/n)*sum(y-y_predic)
        m = m - lr * dm
        c = c - lr * de
        
        cost = (1/n) * sum([temp**2 for temp in (y-y_predic)])
        
        if(i==9999): print ("m= {},    c= {}, cost {}".format(m,c,cost))

def lsm():
  x=pd.Series(x_axis)
  y=pd.Series(y_axis)
  r= x.cov(y)/(y.std()*x.std())
  b_1= r*y.std()/x.std()
  b_0= y.mean()-(b_1*x.mean())
  print ("m= {},   c= {},".format(b_1,b_0))

gradie(x,y)
lsm()

# Output:-

# Gradient Descent Method.
# 
# Ordinary Least Square Method.
# 
