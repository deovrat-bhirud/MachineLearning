x_scores = [15 , 12 , 8  , 8 ,  7 ,  7 ,  7 ,  6   , 5  , 3]
y_scores = [10  ,25 , 17  ,11 , 13 , 17 , 20 , 13 , 9  , 15]
n=10
x_sum =0
y_sum =0
xy_product = 0
x_sq=0
for i in range (0,n):
    x_sum+=x_scores[i]
    y_sum+=y_scores[i]
    xy_product += x_scores[i]*y_scores[i]
    x_sq += x_scores[i]*x_scores[i]
ans = (n*xy_product - x_sum*y_sum)/(n*x_sq - x_sum*x_sum)
print('%.3f'%ans)
