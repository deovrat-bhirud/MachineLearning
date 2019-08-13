import numpy as np
import pandas as pd

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
        
        if(i==9999): print ("slope = {},    constant = {},   cost = {}".format(m,c,cost))

def lsm():
  x=pd.Series(x_axis)
  y=pd.Series(y_axis)
  r= x.cov(y)/(y.std()*x.std())
  b_1= r*y.std()/x.std()
  b_0= y.mean()-(b_1*x.mean())
  print ("slope = {},   constant = {},".format(b_1,b_0))

lsm()
gradie(x,y)


# Output:-

# Ordinary Least Square Method.
# slope = 1.6321516393442619,   y-intercept = 30.6663524590164, 

# Gradient Descent Method.
# slope = 4.408581734132559,    constant = 0.935694742066278,   cost = 96.0183282956435

# For accurate answer you must increase the umber of iteration or Increase the learning rate.
# For example if the number of iteration is 10000 And learning rate is 0.009 then Output is
# slope = 1.6321521129102268,    constant = 30.666347387962162,   cost = 18.797289187067147
