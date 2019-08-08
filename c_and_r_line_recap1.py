import math
x_scores = [15 , 12 , 8  , 8 ,  7 ,  7 ,  7 ,  6   , 5  , 3]
y_scores = [10  ,25 , 17  ,11 , 13 , 17 , 20 , 13 , 9  , 15]
n=10
x_sum =0
y_sum =0
for i in range (0,n):
    x_sum=x_sum+x_scores[i]
    y_sum=y_sum+y_scores[i]
x_mean = float((x_sum)/n)
y_mean = float((y_sum)/n)
devi_squy=0
devi_squx=0
devi_product=0
for i in range (0,n):
  devi_squx += (x_scores[i]-x_mean)**2
  devi_squy += (y_scores[i]-y_mean)**2
  devi_product += (x_scores[i]-x_mean)*(y_scores[i]-y_mean)
  
ans = float(devi_product)/math.sqrt(devi_squx*devi_squy)
print (ans)  
