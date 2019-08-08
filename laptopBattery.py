import pylab

lappiee = pylab.loadtxt('https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt', delimiter=',')
x_axis = lappiee[:, 0]
y_axis = lappiee[:, 1]
n=100
x_sum =0
y_sum =0
xy_product = 0
x_sq=0
for i in range (0,n):
    x_sum+=x_axis[i]
    y_sum+=y_axis[i]
    xy_product += x_axis[i]*y_axis[i]
    x_sq += x_axis[i]*x_axis[i]
x_mean = float((x_sum)/n)
y_mean = float((y_sum)/n)
slope = (n*xy_product - x_sum*y_sum)/(n*x_sq - x_sum*x_sum)
constant = y_mean - (x_mean*slope)
new=float(input())
ans = slope*new+constant 
print(ans)
